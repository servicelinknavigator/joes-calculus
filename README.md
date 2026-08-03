# Calculus-app voor Joes (v1.0)

Persoonlijke calculus-leeromgeving: boek-gevoel met 47 doorlopend genummerde hoofdstukken
(Calculus 1-3, lineaire algebra, differentiaalvergelijkingen), vrije navigatie, en bij elke
opgave uitleg vooraf (theorie), tijdens (progressieve hints) en achteraf (volledige uitwerking).

Zie [BUILD_PROMPT.md](BUILD_PROMPT.md) voor de volledige spec/scope van v1.0.

**Stack:** Flask + Supabase + Render (zelfde patroon als de andere SLN-apps).

**Status v1.0:** volledig framework + volledig uitgewerkt Module I (Calculus 1, hoofdstuk 1-11).
Hoofdstuk 12-47 staan al in de inhoudsopgave als "binnenkort beschikbaar" placeholder.

---

## 1. Supabase-project opzetten

1. Maak een nieuw project aan op [supabase.com](https://supabase.com) (of gebruik een bestaand project).
2. Open de **SQL editor** en plak de volledige inhoud van [supabase_schema.sql](supabase_schema.sql). Dit maakt alle tabellen, RLS-policies en de 5 modules aan.
3. Ga naar **Authentication → Users** en maak twee gebruikers handmatig aan (geen zelfregistratie in v1.0):
   - `contact@slnsolutions.nl` (wordt automatisch admin, zie de trigger in het schema) met een wachtwoord naar keuze.
   - Joes' e-mailadres, met een wachtwoord naar keuze — dit wordt automatisch een `student`-account.
4. Noteer uit **Project Settings → API**:
   - `Project URL` → `SUPABASE_URL`
   - `anon public` key → `SUPABASE_ANON_KEY`
   - `service_role` key → `SUPABASE_SERVICE_KEY` (geheim houden, nooit in de browser gebruiken)

## 2. Content seeden (hoofdstuk 1-11 + placeholders 12-47)

```bash
cp .env.example .env
# vul SUPABASE_URL, SUPABASE_ANON_KEY, SUPABASE_SERVICE_KEY in .env in
pip install -r requirements.txt
python seed_content.py
```

Dit script is idempotent: opnieuw draaien overschrijft de bestaande hoofdstukken/opgaven met de
inhoud uit `seed_content.py` (handig als je content later aanpast).

## 3. Lokaal draaien

```bash
python app.py
```
Open `http://localhost:5000` en log in met een van de hierboven aangemaakte accounts.

## 4. Deployen op Render

1. Push deze repo naar GitHub.
2. Maak op [render.com](https://render.com) een nieuwe **Web Service** aan vanaf de repo (of gebruik `render.yaml` via "New → Blueprint").
3. Zet de environment variables (`SUPABASE_URL`, `SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_KEY`, `ADMIN_EMAIL`) in de Render-dashboard.
4. Render bouwt automatisch met `pip install -r requirements.txt` en start met `gunicorn app:app`.

## Content later uitbreiden (hoofdstuk 12-47)

Voeg per hoofdstuk een dict toe aan de `CHAPTERS`-lijst in [seed_content.py](seed_content.py)
(zelfde structuur als hoofdstuk 1-11: `theory_content`, `summary`, `exercises` met `hints` en
`full_solution`), verwijder het bijbehorende item uit `PLACEHOLDER_CHAPTERS`, en run
`python seed_content.py` opnieuw.

## Projectstructuur

```
app.py                 Flask-app: routes, auth, Supabase REST-helpers
seed_content.py         Alle hoofdstuk- en opgave-content + seed-logica
supabase_schema.sql      Database-schema, RLS-policies, seed van de 5 modules
templates/               base.html (layout + sidebar TOC), login.html, dashboard.html, chapter.html
static/css/main.css      Styling
```
