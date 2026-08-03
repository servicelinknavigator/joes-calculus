# Build prompt: Calculus-app voor Joes (v1.0)

Dit document is de volledige spec/prompt om app 1.0 te bouwen. Alles wat hieronder staat is besproken en bevestigd met de opdrachtgever (Anna) in de aanloop naar dit document. Bouw hierop verder in `C:\Users\annak\Joes` — niet in andere repo's.

## 1. Context en doel

Joes heeft het niveau bovenbouw VWO wiskunde B al volledig onder de knie en wil zich nu verder ontwikkelen richting calculus, op een niveau dat aansluit bij een eerstejaars universitair wiskundepakket. Hij heeft deze stof **nog nooit gehad** — dit is voor hem compleet nieuwe leerstof, geen herhaling.

De app is een persoonlijk leertraject: geen generieke oefentool, maar een doorlopend "boek" met hoofdstukken dat Joes op zijn eigen tempo doorwerkt.

## 2. Doelgroep

- **Eindgebruiker:** Joes. Sterk in wiskunde, gemotiveerd, VWO B-niveau als basis, geen calculus-voorkennis.
- **Beheerder:** Anna (contact@slnsolutions.nl), zelfde rol-patroon als bij de Belladonna-app (super-admin/beheerder-account).

## 3. Tech stack (consistent met bestaande projecten)

- **Backend:** Flask (Python), zelfde patroon als de Meta Ads Automation-app en de Belladonna-app.
- **Database/auth:** Supabase (Postgres + Supabase Auth + RLS policies).
- **Deployment:** Render, zelfde workflow als de andere twee apps (commit + push → auto-deploy).
- **Frontend:** Server-rendered templates (Jinja2) + lichte JS voor interactiviteit (bijv. hoofdstuknavigatie, opgave-checks), geen zware SPA-framework nodig tenzij de MVP dat vraagt.

## 4. Kernprincipe: het "boek-gevoel"

De app moet aanvoelen als een boek met hoofdstukken:

- Een duidelijke, doorlopend genummerde hoofdstukkenlijst (inhoudsopgave/TOC), zichtbaar als sidebar of startpagina.
- **Vrije navigatie:** Joes moet op elk moment naar elk hoofdstuk kunnen springen (bijv. direct naar hoofdstuk 4), ook als hij voorgaande hoofdstukken niet heeft afgerond. Geen verplichte lineaire lock-in.
- Voortgang per hoofdstuk wordt wel bijgehouden en getoond (bijv. "niet gestart / bezig / afgerond"), puur informatief — niet blokkerend.
- Elk hoofdstuk heeft een vaste opbouw: uitleg → opgaven → (optioneel) samenvatting/afsluiting.

## 5. Pedagogisch model per hoofdstuk (hard vereiste)

Omdat de stof volledig nieuw is voor Joes, moet uitleg op drie momenten beschikbaar zijn bij **elke opgave**:

1. **Vooraf:** theorie-uitleg van het onderwerp/de techniek voordat de opgave getoond wordt (tekst, uitgewerkte voorbeelden, eventueel formules).
2. **Tijdens:** een hint- of stappenplan-functie die Joes kan raadplegen als hij vastloopt, zonder meteen het volledige antwoord te geven (bijv. progressieve hints: hint 1 → hint 2 → volledige uitwerking).
3. **Achteraf:** een volledig uitgewerkte oplossing met toelichting, zichtbaar nadat hij zijn antwoord heeft ingevoerd of expliciet om de uitwerking vraagt.

Dit moet in het datamodel verankerd zitten (elke opgave heeft velden voor theorie, hints, en uitwerking), niet als los toegevoegde feature.

## 6. Inhoud: volledige hoofdstukkenlijst

Doorlopend genummerd over 5 modules heen (zodat "spring naar hoofdstuk X" een eenduidig, uniek hoofdstuk aanwijst). Modules dienen als organisatie/groepering in de UI, hoofdstuknummering loopt door.

### Module I — Calculus 1 (aansluitend op VWO B)
1. Limieten: van intuïtief (VWO B) naar de formele ε-δ-definitie
2. Continuïteit en de tussenwaardestelling
3. De afgeleide: definitie via het differentiequotiënt
4. Differentiatieregels en de kettingregel
5. Impliciet differentiëren en gerelateerde snelheden
6. Extrema, de middelwaardestelling en krommeonderzoek
7. De regel van De l'Hôpital
8. Optimalisatieproblemen
9. Riemannsommen en de hoofdstelling van de integraalrekening
10. Integratie: de substitutiemethode
11. Toepassingen van integralen: oppervlakte, inhoud (schijven/schillen), booglengte

### Module II — Calculus 2
12. Partieel integreren
13. Partieelbreuksplitsing
14. Goniometrische substitutie
15. Oneigenlijke integralen
16. Rijen en reeksen: convergentie
17. Convergentiecriteria (vergelijkings-, verhoudings-, worteltest)
18. Machtreeksen
19. Taylor- en Maclaurinreeksen
20. Parametrische krommen
21. Poolcoördinaten

### Module III — Calculus 3 (meerdere variabelen)
22. Vectoren in de ruimte, in-/uitproduct, lijnen en vlakken in 3D
23. Vectorwaardige functies en ruimtekrommen
24. Functies van meerdere variabelen, partiële afgeleiden
25. Gradiënt en richtingsafgeleide
26. Dubbele integralen
27. Drievoudige integralen, cilinder- en bolcoördinaten
28. Vectorvelden en lijnintegralen
29. Stelling van Green
30. Divergentie, rotatie, stellingen van Stokes en Gauss

### Module IV — Lineaire algebra
31. Vectoren en vectorruimten
32. Matrices en bewerkingen
33. Stelsels lineaire vergelijkingen, Gauss-eliminatie
34. Determinanten
35. Basis, dimensie en rang
36. Lineaire afbeeldingen
37. Eigenwaarden en eigenvectoren
38. Diagonaliseren
39. Inproductruimten en orthogonaliteit *(optioneel, kan later)*

### Module V — Differentiaalvergelijkingen (ODE's)
40. Eerste-orde ODE's: scheiden van variabelen
41. Eerste-orde lineaire ODE's
42. Exacte vergelijkingen
43. Tweede-orde lineaire ODE's: homogeen, karakteristieke vergelijking
44. Particuliere oplossingen: onbepaalde coëfficiënten
45. Variatie van parameters
46. Toepassingen: groei/verval, mengproblemen, mechanische trillingen
47. Stelsels ODE's en Laplace-transformatie *(optioneel, kan later)*

## 7. Voorgesteld datamodel (Supabase)

```
profiles
  id (uuid, fk auth.users)
  email
  name
  role            -- 'admin' | 'student'
  created_at

modules
  id
  order_index
  title           -- bv. "Calculus 1"

chapters
  id
  module_id (fk)
  chapter_number  -- doorlopende nummering 1..47
  title
  theory_content  -- markdown/rich text: de "vooraf"-uitleg
  summary         -- optionele afsluitende samenvatting

exercises
  id
  chapter_id (fk)
  order_index
  difficulty          -- bv. 1-3
  question            -- opgavetekst (markdown/LaTeX)
  hints               -- jsonb array, progressieve hints ("tijdens")
  full_solution        -- volledige uitwerking met toelichting ("achteraf")
  answer_type          -- bv. 'numeric' | 'expression' | 'open'
  correct_answer        -- indien automatisch controleerbaar

progress
  id
  user_id (fk profiles)
  chapter_id (fk)
  status            -- 'not_started' | 'in_progress' | 'completed'
  updated_at

exercise_attempts
  id
  user_id (fk)
  exercise_id (fk)
  submitted_answer
  is_correct
  hints_used
  created_at
```

RLS: student ziet alleen eigen progress/attempts; admin (Anna) ziet alles, zelfde patroon als Belladonna (coach/admin rollen).

Wiskundige notatie: gebruik LaTeX-rendering (bijv. MathJax of KaTeX) in de templates voor alle formules, opgaven en uitwerkingen.

## 8. UX-richtlijnen

- Startpagina/dashboard: overzicht van modules + hoofdstukken met voortgangsindicatie, direct klikbaar naar elk hoofdstuk.
- Hoofdstukpagina: theorie bovenaan (inklapbaar zodra gelezen), daaronder de opgaven in oplopende moeilijkheid.
- Opgave-component: vraag → invoerveld → knop "hint" (progressief) → knop "toon uitwerking" → feedback (correct/incorrect indien automatisch controleerbaar).
- Sidebar of topbar met permanente toegang tot de volledige hoofdstukkenlijst (het "boek-gevoel").

## 9. Scope v1.0 (MVP) — voorstel, ter bevestiging

Gezien de omvang (47 hoofdstukken, 5 modules) is volledige content voor alles in v1.0 niet realistisch. Voorstel:

- **Volledig gebouwd:** het complete framework — navigatie, datamodel, auth, hoofdstuk-/opgave-weergave, hint/uitwerking-mechaniek, voortgang-tracking — plus **volledige content voor Module I (Calculus 1, hoofdstukken 1-11)**.
- **Skeleton aanwezig, content later:** hoofdstukken 12-47 staan al in de inhoudsopgave (zichtbaar, navigeerbaar) maar met placeholder-content ("binnenkort beschikbaar"), zodat de structuur meteen compleet aanvoelt en Anna later per hoofdstuk content kan toevoegen zonder de app opnieuw te hoeven bouwen.
- Simpele auth: Joes (student) + Anna (admin), geen zelfregistratie nodig voor v1.0.

**Dit scope-voorstel moet nog bevestigd worden door Anna voordat er gebouwd wordt.**

## 10. Niet in v1.0 (expliciet uitgesteld)

- Content voor modules II t/m V (alleen skeleton/placeholders)
- Geavanceerde adaptieve leerpaden of AI-gegenereerde opgaven
- Mobiele native app (web/PWA is voldoende, zelfde patroon als Belladonna)
- Sociale features (geen andere gebruikers dan Joes + Anna)

## 11. Openstaande vragen voor Anna

1. Bevestig je de MVP-scope (framework + volledige Module I, rest als skeleton)?
2. Moet Joes zelf een account aanmaken (Supabase auth met e-mail/wachtwoord of magic link), of maak jij zijn account handmatig aan zoals bij Belladonna?
3. Is er al een gewenste naam/branding voor de app, of gebruiken we een werktitel tot later?
