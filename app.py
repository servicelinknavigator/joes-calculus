import os
import re
import logging
from datetime import timedelta

import markdown as md_lib
import requests as http
from flask import Flask, render_template, request, redirect, url_for, session, jsonify, abort
from dotenv import load_dotenv
from sympy import simplify
from sympy.parsing.sympy_parser import (
    parse_expr, standard_transformations,
    implicit_multiplication_application, convert_xor,
)

load_dotenv(override=True)

app = Flask(__name__)
app.logger.setLevel(logging.INFO)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-secret-change-me")
app.permanent_session_lifetime = timedelta(days=30)

SUPABASE_URL         = os.environ.get("SUPABASE_URL", "")
SUPABASE_ANON_KEY     = os.environ.get("SUPABASE_ANON_KEY", "")
SUPABASE_SERVICE_KEY  = os.environ.get("SUPABASE_SERVICE_KEY", "")
ADMIN_EMAIL           = os.environ.get("ADMIN_EMAIL", "contact@slnsolutions.nl").lower()

SB_SVC = {"Authorization": f"Bearer {SUPABASE_SERVICE_KEY}", "apikey": SUPABASE_SERVICE_KEY}


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


# ── Wiskundige antwoordcontrole ──────────────────────────────────────────────
# Vergelijkt antwoorden symbolisch (via sympy) in plaats van als kale tekst, zodat
# "3x^2 * sin(x) + x^3 * cos(x)" en "3x^2sin(x)+x^3cos(x)" als gelijk herkend worden.

_MATH_TRANSFORMS = standard_transformations + (implicit_multiplication_application, convert_xor)
_FUNC_NAMES = ("sin", "cos", "tan", "sqrt", "exp", "ln", "log")
_MULT_BEFORE_FUNC = re.compile(r"(?<=[0-9A-Za-z\)])(?=(?:" + "|".join(_FUNC_NAMES) + r")\()")
_TRIG_POWER = re.compile(r"(sin|cos|tan)\^(\d+)\(([^)]*)\)")
_DECIMAL_COMMA = re.compile(r"(\d),(\d)")


def _prepare_expr(s):
    s = s.strip()
    s = _DECIMAL_COMMA.sub(r"\1.\2", s)          # 3,75 -> 3.75
    s = _TRIG_POWER.sub(r"(\1(\3))^\2", s)        # sin^4(x) -> (sin(x))^4
    s = _MULT_BEFORE_FUNC.sub("*", s)             # 6xcos(..) -> 6x*cos(..)
    return s


def _parse_math(s):
    return parse_expr(_prepare_expr(s), transformations=_MATH_TRANSFORMS)


def answers_match(submitted, correct):
    """True als submitted en correct wiskundig gelijkwaardig zijn, met een simpele
    tekstvergelijking als terugvaloptie wanneer sympy het antwoord niet kan parsen."""
    try:
        if "=" in submitted and "=" in correct:
            sl, sr = submitted.split("=", 1)
            cl, cr = correct.split("=", 1)
            a = _parse_math(sl) - _parse_math(sr)
            b = _parse_math(cl) - _parse_math(cr)
            # een vergelijking blijft gelijk als je beide kanten omdraait (a = -b)
            return bool(simplify(a - b) == 0) or bool(simplify(a + b) == 0)
        diff = _parse_math(submitted) - _parse_math(correct)
        return bool(simplify(diff) == 0)
    except Exception:
        norm = lambda s: re.sub(r"\s+", "", s.strip().lower())
        return norm(submitted) == norm(correct)


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


@app.route("/exercise/<int:exercise_id>/check", methods=["POST"])
def exercise_check(exercise_id):
    guard = require_login()
    if guard:
        return jsonify({"error": "not_logged_in"}), 401

    rows = sb_get("exercises", {"id": f"eq.{exercise_id}", "select": "id,answer_type,correct_answer"})
    if not rows:
        abort(404)
    exercise = rows[0]

    submitted = (request.json or {}).get("answer", "").strip()
    is_correct = None
    if exercise["answer_type"] in ("numeric", "expression") and exercise.get("correct_answer") and submitted:
        is_correct = answers_match(submitted, exercise["correct_answer"])

    sb_post("exercise_attempts", {
        "user_id": session["user_id"],
        "exercise_id": exercise_id,
        "submitted_answer": submitted,
        "is_correct": is_correct,
    }, prefer="return=minimal")

    return jsonify({"is_correct": is_correct})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
