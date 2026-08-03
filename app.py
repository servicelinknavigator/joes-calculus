import os
import re
import logging
import base64
from uuid import uuid4
from datetime import timedelta

import markdown as md_lib
import requests as http
from flask import Flask, render_template, request, redirect, url_for, session, jsonify, abort
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
    return sb_get("exercises", {"chapter_id": f"eq.{chapter_id}", "select": "*", "order": "order_index"})


def set_progress(user_id, chapter_id, status):
    existing = sb_get("progress", {"user_id": f"eq.{user_id}", "chapter_id": f"eq.{chapter_id}", "select": "id"})
    if existing:
        sb_patch(f"progress?id=eq.{existing[0]['id']}", {"status": status, "updated_at": "now()"})
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
                                progress=progress, theory_html="", placeholder=True)

    if progress.get(chapter["id"]) in (None, "not_started"):
        set_progress(session["user_id"], chapter["id"], "in_progress")
        progress[chapter["id"]] = "in_progress"

    exercises = get_exercises(chapter["id"])
    for ex in exercises:
        ex["question_html"] = md(ex["question"])
        ex["full_solution_html"] = md(ex["full_solution"])

    return render_template(
        "chapter.html",
        chapter=chapter,
        exercises=exercises,
        modules=modules,
        progress=progress,
        theory_html=md(chapter["theory_content"]),
        summary_html=md(chapter.get("summary") or ""),
        placeholder=False,
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


_ALLOWED_IMAGE_TYPES = {"image/jpeg": "jpg", "image/png": "png", "image/webp": "webp", "image/heic": "heic"}


@app.route("/exercise/<int:exercise_id>/upload", methods=["POST"])
def exercise_upload(exercise_id):
    guard = require_login()
    if guard:
        return jsonify({"error": "not_logged_in"}), 401

    file = request.files.get("image")
    if not file or not file.filename:
        return jsonify({"error": "Geen bestand ontvangen"}), 400

    mime_type = file.mimetype
    if mime_type not in _ALLOWED_IMAGE_TYPES:
        return jsonify({"error": "Alleen foto's (jpg, png, webp, heic) worden ondersteund"}), 400

    image_bytes = file.read()
    if not image_bytes:
        return jsonify({"error": "Leeg bestand"}), 400

    rows = sb_get("exercises", {"id": f"eq.{exercise_id}", "select": "id,question,full_solution"})
    if not rows:
        abort(404)
    exercise = rows[0]

    verdict, feedback = review_solution_image(exercise["question"], exercise["full_solution"], image_bytes, mime_type)

    ext = _ALLOWED_IMAGE_TYPES[mime_type]
    storage_path = f"{session['user_id']}/{exercise_id}/{uuid4().hex}.{ext}"
    upload_resp = http.post(
        f"{SUPABASE_URL}/storage/v1/object/{STORAGE_BUCKET}/{storage_path}",
        headers={**SB_SVC, "Content-Type": mime_type},
        data=image_bytes, timeout=20,
    )
    image_path = storage_path if upload_resp.status_code in (200, 201) else None
    if image_path is None:
        app.logger.warning("Storage upload mislukt: %s %s", upload_resp.status_code, upload_resp.text[:200])

    sb_post("exercise_submissions", {
        "user_id": session["user_id"],
        "exercise_id": exercise_id,
        "image_path": image_path,
        "ai_verdict": verdict,
        "ai_feedback": feedback,
    }, prefer="return=minimal")

    sb_post("exercise_attempts", {
        "user_id": session["user_id"],
        "exercise_id": exercise_id,
        "submitted_answer": "(foto-upload)",
        "is_correct": verdict == "correct",
    }, prefer="return=minimal")

    return jsonify({"verdict": verdict, "feedback": feedback})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
