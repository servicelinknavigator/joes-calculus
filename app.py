import os
import re
import json
import logging
import base64
from uuid import uuid4
from datetime import timedelta, datetime, timezone

import markdown as md_lib
import requests as http
from flask import Flask, render_template, request, redirect, url_for, session, jsonify, abort, Response
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv(override=True)

app = Flask(__name__)
app.logger.setLevel(logging.INFO)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-secret-change-me")
app.permanent_session_lifetime = timedelta(days=30)
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10MB, ruim genoeg voor een foto

SUPABASE_URL         = os.environ.get("SUPABASE_URL", "")
SUPABASE_ANON_KEY     = os.environ.get("SUPABASE_ANON_KEY", "")
SUPABASE_SERVICE_KEY  = os.environ.get("SUPABASE_SERVICE_KEY", "")
ADMIN_EMAIL           = os.environ.get("ADMIN_EMAIL", "contact@slnsolutions.nl").lower()
ANTHROPIC_API_KEY     = os.environ.get("ANTHROPIC_API_KEY", "")
STORAGE_BUCKET        = "solution-uploads"

SB_SVC = {"Authorization": f"Bearer {SUPABASE_SERVICE_KEY}", "apikey": SUPABASE_SERVICE_KEY}
_anthropic_client = Anthropic(api_key=ANTHROPIC_API_KEY) if ANTHROPIC_API_KEY else None


# ── Supabase REST helpers (backend gebruikt altijd de service key; autorisatie
#    gebeurt hier in Python op basis van de Flask-sessie, niet via Supabase RLS
#    per gebruiker: bewust simpel gehouden voor deze kleine, persoonlijke app) ──

def sb_get(path, params=None):
    r = http.get(f"{SUPABASE_URL}/rest/v1/{path}", headers=SB_SVC, params=params, timeout=10)
    r.raise_for_status()
    return r.json()


def sb_post(path, payload, prefer="return=representation"):
    headers = {**SB_SVC, "Content-Type": "application/json", "Prefer": prefer}
    r = http.post(f"{SUPABASE_URL}/rest/v1/{path}", headers=headers, json=payload, timeout=10)
    r.raise_for_status()
    return r.json() if r.content else None


def sb_patch(path, payload, prefer="return=minimal"):
    headers = {**SB_SVC, "Content-Type": "application/json", "Prefer": prefer}
    r = http.patch(f"{SUPABASE_URL}/rest/v1/{path}", headers=headers, json=payload, timeout=10)
    r.raise_for_status()
    return r.json() if r.content else None


def md(text):
    return md_lib.markdown(text or "", extensions=["extra"])


def now_iso():
    return datetime.now(timezone.utc).isoformat()


# ── AI-nakijken van geüploade foto's ─────────────────────────────────────────

_VERDICT_RE = re.compile(r"VERDICT:\s*(correct|incorrect|unclear)", re.IGNORECASE)
_FEEDBACK_RE = re.compile(r"FEEDBACK:\s*(.*)", re.IGNORECASE | re.DOTALL)


def review_solution_image(question, full_solution, image_bytes, mime_type):
    if not _anthropic_client:
        return "unclear", "De AI-nakijkfunctie is nog niet geconfigureerd (ANTHROPIC_API_KEY ontbreekt op de server)."

    b64 = base64.b64encode(image_bytes).decode("utf-8")
    prompt = f"""Je bent een geduldige wiskundedocent die een foto van een met de hand geschreven uitwerking nakijkt.

Opgave:
{question}

Correcte uitwerking (referentie voor jou, dit is niet per se de enige juiste aanpak):
{full_solution}

Beoordeel de uitwerking op de foto: is de redenering en het eindantwoord correct? Kleine notatiefouten mogen genegeerd worden als de wiskunde klopt. Antwoord in het Nederlands, exact in dit formaat, zonder extra tekst ervoor:
VERDICT: correct of incorrect of unclear
FEEDBACK: korte, vriendelijke uitleg (maximaal 4 zinnen) over wat goed ging en, als er iets misging, wat er precies misging en waarom."""

    message = _anthropic_client.messages.create(
        model="claude-sonnet-5",
        max_tokens=500,
        messages=[{
            "role": "user",
            "content": [
                {"type": "image", "source": {"type": "base64", "media_type": mime_type, "data": b64}},
                {"type": "text", "text": prompt},
            ],
        }],
    )
    text = "".join(block.text for block in message.content if block.type == "text")

    verdict_match = _VERDICT_RE.search(text)
    feedback_match = _FEEDBACK_RE.search(text)
    verdict = verdict_match.group(1).lower() if verdict_match else "unclear"
    feedback = feedback_match.group(1).strip() if feedback_match else text.strip()
    return verdict, feedback


# ── AI-generatie van nieuwe oefenopgaven en toetsen ─────────────────────────

_GEN_QUESTION_RE = re.compile(r"VRAAG:\s*(.*?)\nHINT1:", re.DOTALL)
_GEN_HINT1_RE = re.compile(r"HINT1:\s*(.*?)\nHINT2:", re.DOTALL)
_GEN_HINT2_RE = re.compile(r"HINT2:\s*(.*?)\nUITWERKING:", re.DOTALL)
_GEN_SOLUTION_RE = re.compile(r"UITWERKING:\s*(.*)", re.DOTALL)


def generate_exercise_variant(chapter_title, source):
    """Genereert een nieuwe opgave in dezelfde stijl/moeilijkheidsgraad als `source`,
    voor de 'oneindig oefenen'-knop. Geeft None terug als generatie niet lukt."""
    if not _anthropic_client:
        return None

    prompt = f"""Je bent een wiskundedocent die oefenopgaven voor een calculus-app maakt.

Onderwerp: hoofdstuk "{chapter_title}".

Hier is een voorbeeldopgave met uitwerking, als stijl- en niveauvoorbeeld:

VOORBEELD OPGAVE: {source['question']}
VOORBEELD UITWERKING: {source['full_solution']}

Maak een NIEUWE opgave over exact hetzelfde onderwerp en dezelfde techniek, met vergelijkbare moeilijkheidsgraad, maar met andere functies/getallen (geen kopie). Schrijf in het Nederlands met LaTeX-notatie tussen dollartekens ($...$), in dezelfde stijl als het voorbeeld. Geef ook twee progressieve hints (de eerste subtiel, de tweede concreter) en een volledig uitgewerkte oplossing met genummerde stappen, net als het voorbeeld.

Antwoord EXACT in dit formaat, zonder andere tekst ervoor of erna:
VRAAG: <opgavetekst>
HINT1: <eerste hint>
HINT2: <tweede hint>
UITWERKING: <volledige uitwerking>"""

    message = _anthropic_client.messages.create(
        model="claude-sonnet-5",
        max_tokens=1200,
        messages=[{"role": "user", "content": prompt}],
    )
    text = "".join(block.text for block in message.content if block.type == "text")

    q = _GEN_QUESTION_RE.search(text)
    h1 = _GEN_HINT1_RE.search(text)
    h2 = _GEN_HINT2_RE.search(text)
    sol = _GEN_SOLUTION_RE.search(text)
    if not (q and sol):
        app.logger.warning("Kon gegenereerde opgave niet parsen: %s", text[:300])
        return None

    hints = [h.group(1).strip() for h in (h1, h2) if h and h.group(1).strip()]
    return {"question": q.group(1).strip(), "hints": hints, "full_solution": sol.group(1).strip()}


def generate_test_questions(chapter_title, source_exercises):
    """Genereert één nieuwe toetsvraag per meegegeven bron-opgave (dus per subcategorie)."""
    if not _anthropic_client or not source_exercises:
        return []

    examples = "\n\n".join(
        f"Subcategorie {i+1} voorbeeld: {ex['question']}\nUitwerking: {ex['full_solution']}"
        for i, ex in enumerate(source_exercises)
    )
    n = len(source_exercises)
    prompt = f"""Je bent een wiskundedocent die een toets samenstelt voor hoofdstuk "{chapter_title}".

Hieronder staan voorbeeldopgaven, één per subcategorie van dit hoofdstuk:

{examples}

Maak een toets met precies {n} nieuwe opgaven, één per subcategorie hierboven (zelfde onderwerp/techniek, andere functies/getallen dan het voorbeeld, vergelijkbare moeilijkheidsgraad). Schrijf in het Nederlands met LaTeX-notatie tussen dollartekens ($...$). Geef ook een volledig uitgewerkte oplossing per opgave, met genummerde stappen.

Antwoord uitsluitend met geldige JSON, een array van precies {n} objecten, niets anders (geen markdown-codeblok, geen uitleg):
[{{"question": "...", "full_solution": "..."}}, ...]"""

    message = _anthropic_client.messages.create(
        model="claude-sonnet-5",
        max_tokens=3500,
        messages=[{"role": "user", "content": prompt}],
    )
    text = "".join(block.text for block in message.content if block.type == "text").strip()
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip())

    try:
        data = json.loads(text)
        return [{"question": q["question"], "full_solution": q["full_solution"]} for q in data]
    except Exception:
        app.logger.warning("Kon testvragen niet parsen: %s", text[:300])
        return []


# ── Foto-uploads (gedeeld tussen opgaven en toetsvragen) ────────────────────

_ALLOWED_IMAGE_TYPES = {"image/jpeg": "jpg", "image/png": "png", "image/webp": "webp", "image/heic": "heic"}


def _validate_upload():
    file = request.files.get("image")
    if not file or not file.filename:
        return None, None, (jsonify({"error": "Geen bestand ontvangen"}), 400)
    mime_type = file.mimetype
    if mime_type not in _ALLOWED_IMAGE_TYPES:
        return None, None, (jsonify({"error": "Alleen foto's (jpg, png, webp, heic) worden ondersteund"}), 400)
    image_bytes = file.read()
    if not image_bytes:
        return None, None, (jsonify({"error": "Leeg bestand"}), 400)
    return image_bytes, mime_type, None


def _store_image(user_id, subfolder, image_bytes, mime_type):
    ext = _ALLOWED_IMAGE_TYPES[mime_type]
    storage_path = f"{user_id}/{subfolder}/{uuid4().hex}.{ext}"
    resp = http.post(
        f"{SUPABASE_URL}/storage/v1/object/{STORAGE_BUCKET}/{storage_path}",
        headers={**SB_SVC, "Content-Type": mime_type},
        data=image_bytes, timeout=20,
    )
    if resp.status_code not in (200, 201):
        app.logger.warning("Storage upload mislukt: %s %s", resp.status_code, resp.text[:200])
        return None
    return storage_path


def _serve_submission_image(table, submission_id):
    rows = sb_get(table, {"id": f"eq.{submission_id}", "select": "user_id,image_path"})
    if not rows or not rows[0]["image_path"]:
        abort(404)
    sub = rows[0]
    if sub["user_id"] != session["user_id"] and session.get("role") != "admin":
        abort(403)
    resp = http.get(f"{SUPABASE_URL}/storage/v1/object/{STORAGE_BUCKET}/{sub['image_path']}", headers=SB_SVC, timeout=15)
    if resp.status_code != 200:
        abort(404)
    ext = sub["image_path"].rsplit(".", 1)[-1].lower()
    mime = {"jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png",
            "webp": "image/webp", "heic": "image/heic"}.get(ext, "application/octet-stream")
    return Response(resp.content, mimetype=mime)


# ── Auth ─────────────────────────────────────────────────────────────────────

def require_login():
    if "user_id" not in session:
        return redirect(url_for("login", next=request.path))
    return None


@app.context_processor
def inject_user():
    return {
        "current_user": {
            "email": session.get("email"),
            "name": session.get("name"),
            "role": session.get("role"),
        } if "user_id" in session else None
    }


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html", error=None)

    email = (request.form.get("email") or "").strip().lower()
    password = request.form.get("password") or ""

    if not email or not password:
        return render_template("login.html", error="Vul e-mailadres en wachtwoord in.")

    resp = http.post(
        f"{SUPABASE_URL}/auth/v1/token?grant_type=password",
        headers={"apikey": SUPABASE_ANON_KEY, "Content-Type": "application/json"},
        json={"email": email, "password": password},
        timeout=10,
    )
    if resp.status_code != 200:
        app.logger.info("Login mislukt voor %s: %s", email, resp.status_code)
        return render_template("login.html", error="Onjuist e-mailadres of wachtwoord.")

    auth_data = resp.json()
    user_id = auth_data["user"]["id"]

    profiles = sb_get("profiles", {"id": f"eq.{user_id}", "select": "id,email,name,role"})
    profile = profiles[0] if profiles else {"id": user_id, "email": email, "name": None, "role": "student"}

    session.permanent = True
    session["user_id"] = profile["id"]
    session["email"] = profile["email"]
    session["name"] = profile.get("name")
    session["role"] = profile.get("role", "student")

    next_url = request.args.get("next") or url_for("dashboard")
    return redirect(next_url)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# ── Content helpers ──────────────────────────────────────────────────────────

def get_modules_with_chapters():
    modules = sb_get("modules", {"select": "id,order_index,title", "order": "order_index"})
    chapters = sb_get("chapters", {
        "select": "id,module_id,chapter_number,title,is_placeholder",
        "order": "chapter_number",
    })
    for m in modules:
        m["chapters"] = [c for c in chapters if c["module_id"] == m["id"]]
    return modules


def get_progress_map(user_id):
    rows = sb_get("progress", {"user_id": f"eq.{user_id}", "select": "chapter_id,status"})
    return {r["chapter_id"]: r["status"] for r in rows}


def annotate_module_progress(modules, progress):
    """Voegt completed_count/total_count/pct toe aan elke module, voor de voortgangsbalken."""
    for m in modules:
        real_chapters = [c for c in m["chapters"] if not c["is_placeholder"]]
        completed = sum(1 for c in real_chapters if progress.get(c["id"]) == "completed")
        total = len(real_chapters)
        m["completed_count"] = completed
        m["total_count"] = total
        m["pct"] = round(100 * completed / total) if total else 0
        for c in m["chapters"]:
            st = progress.get(c["id"], "not_started")
            c["status"] = st
            c["status_pct"] = {"not_started": 0, "in_progress": 50, "completed": 100}.get(st, 0)
    return modules


def get_chapter_by_number(chapter_number):
    rows = sb_get("chapters", {"chapter_number": f"eq.{chapter_number}", "select": "*"})
    return rows[0] if rows else None


def get_exercises(chapter_id):
    """Geeft per opgave-slot (order_index) alleen de meest recente versie terug,
    zodat een AI-gegenereerde variant de vorige vervangt in de weergave."""
    rows = sb_get("exercises", {
        "chapter_id": f"eq.{chapter_id}", "select": "*", "order": "order_index.asc,id.desc",
    })
    latest_per_slot = {}
    for r in rows:
        if r["order_index"] not in latest_per_slot:
            latest_per_slot[r["order_index"]] = r
    return [latest_per_slot[k] for k in sorted(latest_per_slot.keys())]


def get_source_exercise(exercise_id):
    """Vindt de originele (niet-AI-gegenereerde) opgave van hetzelfde slot, als
    stijlvoorbeeld voor een volgende generatie."""
    rows = sb_get("exercises", {"id": f"eq.{exercise_id}", "select": "*"})
    if not rows:
        return None
    ex = rows[0]
    if not ex["is_ai_generated"]:
        return ex
    if ex.get("source_exercise_id"):
        src = sb_get("exercises", {"id": f"eq.{ex['source_exercise_id']}", "select": "*"})
        if src:
            return src[0]
    return ex


def get_latest_results(user_id, exercise_ids):
    """Geeft per exercise_id het laatst opgeslagen resultaat (True/False), voor het
    onthouden van de goed/fout-knoppen zodra je een hoofdstuk opnieuw bezoekt."""
    if not exercise_ids:
        return {}
    ids = ",".join(str(i) for i in exercise_ids)
    rows = sb_get("exercise_attempts", {
        "user_id": f"eq.{user_id}",
        "exercise_id": f"in.({ids})",
        "select": "exercise_id,is_correct,created_at",
        "order": "created_at.desc",
    })
    latest = {}
    for r in rows:
        if r["exercise_id"] not in latest and r["is_correct"] is not None:
            latest[r["exercise_id"]] = r["is_correct"]
    return latest


def get_submissions_map(user_id, exercise_ids):
    """Alle foto-uploads per opgave, nieuwste eerst, voor de permanente uploadgeschiedenis."""
    if not exercise_ids:
        return {}
    ids = ",".join(str(i) for i in exercise_ids)
    rows = sb_get("exercise_submissions", {
        "user_id": f"eq.{user_id}",
        "exercise_id": f"in.({ids})",
        "select": "id,exercise_id,ai_verdict,ai_feedback,image_path,created_at",
        "order": "created_at.desc",
    })
    m = {}
    for r in rows:
        m.setdefault(r["exercise_id"], []).append(r)
    return m


def get_test_submissions_map(user_id, question_ids):
    if not question_ids:
        return {}
    ids = ",".join(str(i) for i in question_ids)
    rows = sb_get("test_submissions", {
        "user_id": f"eq.{user_id}",
        "test_question_id": f"in.({ids})",
        "select": "id,test_question_id,ai_verdict,ai_feedback,image_path,created_at",
        "order": "created_at.desc",
    })
    m = {}
    for r in rows:
        m.setdefault(r["test_question_id"], []).append(r)
    return m


def get_tests_for_chapter(user_id, chapter_id):
    return sb_get("tests", {
        "user_id": f"eq.{user_id}",
        "chapter_id": f"eq.{chapter_id}",
        "select": "id,status,score,total,created_at,completed_at",
        "order": "created_at.desc",
    })


def get_owned_test(test_id):
    rows = sb_get("tests", {"id": f"eq.{test_id}", "select": "*"})
    if not rows:
        return None
    t = rows[0]
    if t["user_id"] != session["user_id"] and session.get("role") != "admin":
        return None
    return t


def set_progress(user_id, chapter_id, status):
    existing = sb_get("progress", {"user_id": f"eq.{user_id}", "chapter_id": f"eq.{chapter_id}", "select": "id"})
    if existing:
        sb_patch(f"progress?id=eq.{existing[0]['id']}", {"status": status, "updated_at": now_iso()})
    else:
        sb_post("progress", {"user_id": user_id, "chapter_id": chapter_id, "status": status}, prefer="return=minimal")


# ── Routes ───────────────────────────────────────────────────────────────────

@app.route("/")
def dashboard():
    guard = require_login()
    if guard:
        return guard
    modules = get_modules_with_chapters()
    progress = get_progress_map(session["user_id"])
    annotate_module_progress(modules, progress)
    return render_template("dashboard.html", modules=modules, progress=progress)


@app.route("/chapter/<int:chapter_number>")
def chapter_view(chapter_number):
    guard = require_login()
    if guard:
        return guard

    chapter = get_chapter_by_number(chapter_number)
    if not chapter:
        abort(404)

    modules = get_modules_with_chapters()
    progress = get_progress_map(session["user_id"])
    annotate_module_progress(modules, progress)

    if chapter["is_placeholder"]:
        return render_template("chapter.html", chapter=chapter, exercises=[], modules=modules,
                                progress=progress, theory_html="", placeholder=True, tests=[])

    if progress.get(chapter["id"]) in (None, "not_started"):
        set_progress(session["user_id"], chapter["id"], "in_progress")
        progress[chapter["id"]] = "in_progress"

    exercises = get_exercises(chapter["id"])
    exercise_ids = [ex["id"] for ex in exercises]
    latest_results = get_latest_results(session["user_id"], exercise_ids)
    submissions_map = get_submissions_map(session["user_id"], exercise_ids)
    for ex in exercises:
        ex["question_html"] = md(ex["question"])
        ex["full_solution_html"] = md(ex["full_solution"])
        ex["last_result"] = latest_results.get(ex["id"])
        ex["submissions"] = submissions_map.get(ex["id"], [])

    tests = get_tests_for_chapter(session["user_id"], chapter["id"])

    return render_template(
        "chapter.html",
        chapter=chapter,
        exercises=exercises,
        modules=modules,
        progress=progress,
        theory_html=md(chapter["theory_content"]),
        summary_html=md(chapter.get("summary") or ""),
        placeholder=False,
        tests=tests,
    )


@app.route("/chapter/<int:chapter_number>/complete", methods=["POST"])
def chapter_complete(chapter_number):
    guard = require_login()
    if guard:
        return guard
    chapter = get_chapter_by_number(chapter_number)
    if not chapter:
        abort(404)
    set_progress(session["user_id"], chapter["id"], "completed")
    return redirect(url_for("chapter_view", chapter_number=chapter_number))


@app.route("/exercise/<int:exercise_id>/self_report", methods=["POST"])
def exercise_self_report(exercise_id):
    guard = require_login()
    if guard:
        return jsonify({"error": "not_logged_in"}), 401

    is_correct = bool((request.json or {}).get("correct"))
    sb_post("exercise_attempts", {
        "user_id": session["user_id"],
        "exercise_id": exercise_id,
        "submitted_answer": "(zelf beoordeeld)",
        "is_correct": is_correct,
    }, prefer="return=minimal")
    return jsonify({"ok": True})


@app.route("/exercise/<int:exercise_id>/upload", methods=["POST"])
def exercise_upload(exercise_id):
    guard = require_login()
    if guard:
        return jsonify({"error": "not_logged_in"}), 401

    image_bytes, mime_type, err = _validate_upload()
    if err:
        return err

    rows = sb_get("exercises", {"id": f"eq.{exercise_id}", "select": "id,question,full_solution"})
    if not rows:
        abort(404)
    exercise = rows[0]

    verdict, feedback = review_solution_image(exercise["question"], exercise["full_solution"], image_bytes, mime_type)
    image_path = _store_image(session["user_id"], f"exercise/{exercise_id}", image_bytes, mime_type)

    sub_row = sb_post("exercise_submissions", {
        "user_id": session["user_id"],
        "exercise_id": exercise_id,
        "image_path": image_path,
        "ai_verdict": verdict,
        "ai_feedback": feedback,
    })

    sb_post("exercise_attempts", {
        "user_id": session["user_id"],
        "exercise_id": exercise_id,
        "submitted_answer": "(foto-upload)",
        "is_correct": verdict == "correct",
    }, prefer="return=minimal")

    return jsonify({
        "verdict": verdict,
        "feedback": feedback,
        "submission_id": sub_row[0]["id"] if sub_row else None,
    })


@app.route("/exercise/<int:exercise_id>/generate-variant", methods=["POST"])
def exercise_generate_variant(exercise_id):
    guard = require_login()
    if guard:
        return jsonify({"error": "not_logged_in"}), 401

    rows = sb_get("exercises", {"id": f"eq.{exercise_id}", "select": "*"})
    if not rows:
        abort(404)
    current = rows[0]
    source = get_source_exercise(exercise_id) or current

    chapter_rows = sb_get("chapters", {"id": f"eq.{current['chapter_id']}", "select": "chapter_number,title"})
    if not chapter_rows:
        abort(404)
    chapter_title = chapter_rows[0]["title"]

    variant = generate_exercise_variant(chapter_title, source)
    if not variant:
        return jsonify({"error": "Kon geen nieuwe opgave genereren, probeer het later opnieuw."}), 502

    new_rows = sb_post("exercises", {
        "chapter_id": current["chapter_id"],
        "order_index": current["order_index"],
        "difficulty": source.get("difficulty", 1),
        "question": variant["question"],
        "hints": variant["hints"],
        "full_solution": variant["full_solution"],
        "answer_type": "open",
        "is_ai_generated": True,
        "source_exercise_id": source["id"],
    })

    return jsonify({
        "ok": True,
        "chapter_number": chapter_rows[0]["chapter_number"],
    })


@app.route("/uploads/exercise/<int:submission_id>")
def uploaded_image_exercise(submission_id):
    guard = require_login()
    if guard:
        return guard
    return _serve_submission_image("exercise_submissions", submission_id)


@app.route("/uploads/test/<int:submission_id>")
def uploaded_image_test(submission_id):
    guard = require_login()
    if guard:
        return guard
    return _serve_submission_image("test_submissions", submission_id)


# ── Toetsen ──────────────────────────────────────────────────────────────────

@app.route("/chapter/<int:chapter_number>/test/new", methods=["POST"])
def test_new(chapter_number):
    guard = require_login()
    if guard:
        return guard

    chapter = get_chapter_by_number(chapter_number)
    if not chapter or chapter["is_placeholder"]:
        abort(404)

    source_exercises = get_exercises(chapter["id"])
    sources = [get_source_exercise(ex["id"]) or ex for ex in source_exercises]

    questions = generate_test_questions(chapter["title"], sources)
    if not questions:
        questions = [{"question": ex["question"], "full_solution": ex["full_solution"]} for ex in source_exercises]

    test_rows = sb_post("tests", {
        "chapter_id": chapter["id"],
        "user_id": session["user_id"],
        "total": len(questions),
    })
    test_id = test_rows[0]["id"]

    for i, q in enumerate(questions, start=1):
        sb_post("test_questions", {
            "test_id": test_id,
            "order_index": i,
            "question": q["question"],
            "full_solution": q["full_solution"],
        }, prefer="return=minimal")

    return redirect(url_for("test_view", test_id=test_id))


@app.route("/test/<int:test_id>")
def test_view(test_id):
    guard = require_login()
    if guard:
        return guard

    test = get_owned_test(test_id)
    if not test:
        abort(404)

    questions = sb_get("test_questions", {"test_id": f"eq.{test_id}", "select": "*", "order": "order_index"})
    q_ids = [q["id"] for q in questions]
    submissions_map = get_test_submissions_map(session["user_id"], q_ids)
    for q in questions:
        q["question_html"] = md(q["question"])
        q["full_solution_html"] = md(q["full_solution"])
        q["submissions"] = submissions_map.get(q["id"], [])

    chapter_rows = sb_get("chapters", {"id": f"eq.{test['chapter_id']}", "select": "chapter_number,title"})
    chapter = chapter_rows[0] if chapter_rows else {}

    modules = get_modules_with_chapters()
    progress = get_progress_map(session["user_id"])
    annotate_module_progress(modules, progress)

    return render_template(
        "test.html", test=test, questions=questions, chapter=chapter,
        modules=modules, progress=progress,
    )


@app.route("/test/<int:test_id>/question/<int:question_id>/self_report", methods=["POST"])
def test_question_self_report(test_id, question_id):
    guard = require_login()
    if guard:
        return jsonify({"error": "not_logged_in"}), 401
    test = get_owned_test(test_id)
    if not test:
        abort(404)

    is_correct = bool((request.json or {}).get("correct"))
    sb_patch(f"test_questions?id=eq.{question_id}", {"verdict": "correct" if is_correct else "incorrect"})
    return jsonify({"ok": True})


@app.route("/test/<int:test_id>/question/<int:question_id>/upload", methods=["POST"])
def test_question_upload(test_id, question_id):
    guard = require_login()
    if guard:
        return jsonify({"error": "not_logged_in"}), 401
    test = get_owned_test(test_id)
    if not test:
        abort(404)

    image_bytes, mime_type, err = _validate_upload()
    if err:
        return err

    q_rows = sb_get("test_questions", {"id": f"eq.{question_id}", "select": "question,full_solution"})
    if not q_rows:
        abort(404)
    question = q_rows[0]

    verdict, feedback = review_solution_image(question["question"], question["full_solution"], image_bytes, mime_type)
    image_path = _store_image(session["user_id"], f"test/{question_id}", image_bytes, mime_type)

    sub_row = sb_post("test_submissions", {
        "user_id": session["user_id"],
        "test_question_id": question_id,
        "image_path": image_path,
        "ai_verdict": verdict,
        "ai_feedback": feedback,
    })

    sb_patch(f"test_questions?id=eq.{question_id}", {"verdict": verdict, "ai_feedback": feedback})

    return jsonify({
        "verdict": verdict,
        "feedback": feedback,
        "submission_id": sub_row[0]["id"] if sub_row else None,
    })


@app.route("/test/<int:test_id>/complete", methods=["POST"])
def test_complete(test_id):
    guard = require_login()
    if guard:
        return guard
    test = get_owned_test(test_id)
    if not test:
        abort(404)

    questions = sb_get("test_questions", {"test_id": f"eq.{test_id}", "select": "verdict"})
    score = sum(1 for q in questions if q["verdict"] == "correct")
    sb_patch(f"tests?id=eq.{test_id}", {
        "status": "completed",
        "score": score,
        "total": len(questions),
        "completed_at": now_iso(),
    })
    return redirect(url_for("test_view", test_id=test_id))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
