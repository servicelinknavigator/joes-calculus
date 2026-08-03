# -*- coding: utf-8 -*-
"""
Seed-script voor de Joes Calculus-app.

Vult Supabase met:
- alle 47 hoofdstukken (chapters), Module I (1-11) volledig uitgewerkt,
  hoofdstuk 12-47 als placeholder ("binnenkort beschikbaar")
- de opgaven (exercises) voor hoofdstuk 1-11

Gebruik:
    1. Zorg dat supabase_schema.sql al is uitgevoerd in de Supabase SQL editor
       (dat maakt de tabellen + de 5 modules aan).
    2. Zet SUPABASE_URL en SUPABASE_SERVICE_KEY in .env (service role key,
       niet de anon key -- dit script omzeilt RLS bewust).
    3. Run: python seed_content.py
    Het script is idempotent: opnieuw draaien overschrijft bestaande hoofdstukken/opgaven.
"""
import os
import sys
import requests as http
from dotenv import load_dotenv

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

load_dotenv(override=True)

from chapters_module2 import CHAPTERS_2  # noqa: E402

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_SERVICE_KEY = os.environ["SUPABASE_SERVICE_KEY"]
HEADERS = {
    "Authorization": f"Bearer {SUPABASE_SERVICE_KEY}",
    "apikey": SUPABASE_SERVICE_KEY,
    "Content-Type": "application/json",
}


# ── Placeholder-titels voor hoofdstuk 22-47 (module_id, chapter_number, title) ──
# (hoofdstuk 12-21 staan volledig uitgewerkt in chapters_module2.py)
PLACEHOLDER_CHAPTERS = [
    (3, 22, "Vectoren in de ruimte, in-/uitproduct, lijnen en vlakken in 3D"),
    (3, 23, "Vectorwaardige functies en ruimtekrommen"),
    (3, 24, "Functies van meerdere variabelen, partiële afgeleiden"),
    (3, 25, "Gradiënt en richtingsafgeleide"),
    (3, 26, "Dubbele integralen"),
    (3, 27, "Drievoudige integralen, cilinder- en bolcoördinaten"),
    (3, 28, "Vectorvelden en lijnintegralen"),
    (3, 29, "Stelling van Green"),
    (3, 30, "Divergentie, rotatie, stellingen van Stokes en Gauss"),
    (4, 31, "Vectoren en vectorruimten"),
    (4, 32, "Matrices en bewerkingen"),
    (4, 33, "Stelsels lineaire vergelijkingen, Gauss-eliminatie"),
    (4, 34, "Determinanten"),
    (4, 35, "Basis, dimensie en rang"),
    (4, 36, "Lineaire afbeeldingen"),
    (4, 37, "Eigenwaarden en eigenvectoren"),
    (4, 38, "Diagonaliseren"),
    (4, 39, "Inproductruimten en orthogonaliteit"),
    (5, 40, "Eerste-orde ODE's: scheiden van variabelen"),
    (5, 41, "Eerste-orde lineaire ODE's"),
    (5, 42, "Exacte vergelijkingen"),
    (5, 43, "Tweede-orde lineaire ODE's: homogeen, karakteristieke vergelijking"),
    (5, 44, "Particuliere oplossingen: onbepaalde coëfficiënten"),
    (5, 45, "Variatie van parameters"),
    (5, 46, "Toepassingen: groei/verval, mengproblemen, mechanische trillingen"),
    (5, 47, "Stelsels ODE's en Laplace-transformatie"),
]


# ── Module I: Calculus 1 (volledig uitgewerkt) ──────────────────────────────
CHAPTERS = [
    {
        "module_id": 1,
        "chapter_number": 1,
        "title": "Limieten: van intuïtief naar de formele ε-δ-definitie",
        "theory_content": r"""
### Wat je al weet

In VWO B heb je limieten informeel gezien: "als $x$ steeds dichter bij $a$ komt, komt $f(x)$ steeds dichter bij een waarde $L$." Dat werkt prima om een idee te krijgen, bijvoorbeeld bij een asymptoot. Maar "steeds dichter bij" is eigenlijk best vaag. Hóé dichtbij? Dichtbij genoeg waarvoor? In calculus maken we dat idee volledig precies. Dat klinkt misschien intimiderend, dus we bouwen het rustig op, helemaal vanaf nul.

### Een spelletje, geen formule

Stel je hebt de functie $f(x) = 2x$, en we kijken naar $x=1$. Daar geldt $f(1) = 2$.

Iemand daagt je uit: *"Ik wil dat $f(x)$ binnen $0{,}1$ van $2$ blijft, dus $f(x)$ moet tussen $1{,}9$ en $2{,}1$ liggen. Kun jij een marge rond $x=1$ geven waarbinnen dat altijd lukt?"*

Dat kun je: als $x$ tussen $0{,}95$ en $1{,}05$ ligt (een marge van $0{,}05$ rond $1$), dan geldt $f(x)=2x$ automatisch tussen $1{,}9$ en $2{,}1$. Reken maar na: $2\times0{,}95=1{,}9$ en $2\times1{,}05=2{,}1$. Je hebt de uitdaging gewonnen.

De uitdager verhoogt de inzet: *"Nu wil ik dat $f(x)$ binnen $0{,}001$ van $2$ blijft."* Ook dat kun je garanderen: kies $x$ binnen $0{,}0005$ van $1$, dan blijft $f(x)$ binnen $0{,}001$ van $2$.

Dit spel kun je oneindig blijven spelen. Hoe klein de gevraagde marge rond de uitkomst ook is, jij kunt altijd een bijpassende marge rond $x=1$ vinden die het garandeert. **Precies dát is wat een limiet betekent:** niet "het komt dichtbij", maar "voor elke gevraagde nauwkeurigheid is er een garantie te geven."

### Nu geven we het namen

De marge die de uitdager rond de uitkomst $L$ opeist, noemen we $\varepsilon$ (epsilon, een Griekse letter, spreek uit als "epsilon"). De marge die jij daarna rond $x=a$ mag kiezen om dat te garanderen, noemen we $\delta$ (delta). Merk op: de uitdager kiest eerst $\varepsilon$, en jij reageert daarna met een passende $\delta$. Die volgorde is belangrijk.

### De formele definitie, symbool voor symbool

$$\lim_{x \to a} f(x) = L$$

betekent: **voor elke** $\varepsilon > 0$ (hoe klein de uitdager ook kiest) **bestaat er een** $\delta > 0$ (die jij mag kiezen, meestal in termen van $\varepsilon$) **zodat**:

$$0 < |x - a| < \delta \implies |f(x) - L| < \varepsilon$$

Lees dit stukje voor stukje:
- $|x-a|$ is de afstand tussen $x$ en $a$ (hoe dicht $x$ bij $a$ zit).
- $0 < |x-a| < \delta$ betekent: $x$ zit dichter dan $\delta$ bij $a$, maar is niet gelijk aan $a$ zelf (we kijken naar de buurt van $a$, niet naar $a$ zelf).
- $|f(x)-L|$ is de afstand tussen $f(x)$ en $L$.
- De pijl $\implies$ zegt: *als* $x$ binnen jouw gekozen marge $\delta$ van $a$ zit, *dan* zit $f(x)$ gegarandeerd binnen de geëiste marge $\varepsilon$ van $L$.

Dat is exact het spelletje van hierboven, nu in symbolen.

### Een volledig uitgewerkt voorbeeld, met uitleg per stap

**Bewijs dat $\lim_{x \to 2} (3x - 1) = 5$.**

Hier is $a=2$, $L=5$, en $f(x)=3x-1$. We moeten voor elke $\varepsilon$ een bijpassende $\delta$ vinden.

**Stap 1.** Schrijf op wat we willen bewijzen: we willen $|f(x)-L| < \varepsilon$, dus $|(3x-1)-5| < \varepsilon$.

**Stap 2.** Werk de linkerkant uit tot je $|x-a|$ ziet staan, want dat is wat we straks met $\delta$ gaan vergelijken:
$$|(3x-1)-5| = |3x-6| = |3(x-2)| = 3|x-2|$$
(We hebben $3x-6$ ontbonden tot $3(x-2)$, zodat de afstand $|x-2|$ zichtbaar wordt.)

**Stap 3.** Vertaal de eis naar een eis op $|x-2|$: we willen dus $3|x-2| < \varepsilon$, oftewel $|x-2| < \dfrac{\varepsilon}{3}$.

**Stap 4.** Kies $\delta$: dit vertelt ons precies welke $\delta$ werkt. **Kies $\delta = \dfrac{\varepsilon}{3}$.**

**Stap 5.** Controleer dat het klopt (dit is het bewijs zelf): stel dat $0 < |x-2| < \delta = \frac{\varepsilon}{3}$. Dan geldt:
$$|(3x-1)-5| = 3|x-2| < 3\cdot\frac{\varepsilon}{3} = \varepsilon \checkmark$$

Precies wat we wilden. Dus voor elke $\varepsilon>0$ hebben we een werkende $\delta$ gevonden ($\delta=\varepsilon/3$), en dat is exact wat de definitie vraagt.

**Het recept dat hierin zit (en dat je in de opgaven herhaalt):**
1. Werk $|f(x)-L|$ algebraïsch uit tot je een getal keer $|x-a|$ overhoudt.
2. Los op welke $\delta$ (in termen van $\varepsilon$) die uitdrukking kleiner dan $\varepsilon$ maakt.
3. Kies die $\delta$, en laat met een korte controle zien dat de implicatie klopt.

Bij kwadratische (of hogere-graads) functies moet je vaak eerst een extra grens op $\delta$ afspreken (bijvoorbeeld $\delta \le 1$) om een lastige factor als $|x+a|$ te kunnen begrenzen, voordat je de uiteindelijke $\delta$ kiest. Dat zie je uitgewerkt in opgave 4.
""",
        "summary": "De formele limietdefinitie vervangt het intuïtieve 'wat gebeurt er als x naar a gaat' door een precieze uitspraak met $\\varepsilon$ en $\\delta$. Het bewijs volgt altijd hetzelfde stramien: werk $|f(x)-L|$ uit in $|x-a|$, en kies $\\delta$ zo dat de implicatie klopt.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Bewijs met de $\varepsilon$-$\delta$-definitie dat $\lim_{x \to 1} (2x + 3) = 5$.",
                "hints": [
                    "Werk $|f(x) - L|$ uit: bereken $|(2x+3) - 5|$ en schrijf dit als een constante keer $|x-1|$.",
                    "Als $|(2x+3)-5| = 2|x-1|$, voor welke $\\delta$ (uitgedrukt in $\\varepsilon$) geldt dan $2|x-1| < \\varepsilon$ zodra $|x-1|<\\delta$?",
                ],
                "full_solution": r"""$|(2x+3)-5| = |2x-2| = 2|x-1|$. We willen $2|x-1| < \varepsilon$, dus $|x-1| < \varepsilon/2$. Kies $\delta = \varepsilon/2$.

Controle: als $0<|x-1|<\delta=\varepsilon/2$, dan $|(2x+3)-5| = 2|x-1| < 2\cdot\frac{\varepsilon}{2} = \varepsilon$. ✓""",
                "answer_type": "open",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Bewijs met de $\varepsilon$-$\delta$-definitie dat $\lim_{x \to 0} x^2 = 0$.",
                "hints": [
                    "$|f(x)-L| = |x^2 - 0| = |x|^2$. Je wilt $|x|^2 < \\varepsilon$ afdwingen.",
                    "Als $|x| < \\delta$, dan $|x|^2 < \\delta^2$. Welke $\\delta$ zorgt dat $\\delta^2 = \\varepsilon$?",
                ],
                "full_solution": r"""$|x^2 - 0| = |x|^2$. We willen $|x|^2 < \varepsilon$. Kies $\delta = \sqrt{\varepsilon}$.

Controle: als $0<|x|<\delta=\sqrt{\varepsilon}$, dan $|x|^2 < (\sqrt{\varepsilon})^2 = \varepsilon$. ✓""",
                "answer_type": "open",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Bereken $\lim_{x \to 3} \dfrac{x^2 - 9}{x - 3}$ en leg uit waarom je niet zomaar $x=3$ mag invullen.",
                "hints": [
                    "Invullen geeft $0/0$: dit is een onbepaalde vorm, geen antwoord.",
                    "Ontbind de teller in factoren: $x^2-9 = (x-3)(x+3)$, en deel weg tegen de noemer.",
                ],
                "full_solution": r"""Directe substitutie geeft $\frac{0}{0}$, een onbepaalde vorm. Dat betekent niet dat de limiet niet bestaat, alleen dat je niet direct mag invullen.

Ontbinden: $\dfrac{x^2-9}{x-3} = \dfrac{(x-3)(x+3)}{x-3} = x+3$ voor $x \ne 3$.

Omdat de limiet alleen kijkt naar $x$ in de buurt van 3 (niet in $x=3$ zelf), geldt:
$$\lim_{x\to 3}\frac{x^2-9}{x-3} = \lim_{x\to3}(x+3) = 6$$""",
                "answer_type": "numeric",
                "correct_answer": "6",
            },
            {
                "order_index": 4, "difficulty": 3,
                "question": r"Bewijs met de $\varepsilon$-$\delta$-definitie dat $\lim_{x \to 4} x^2 = 16$.",
                "hints": [
                    "$|x^2-16| = |x-4|\\cdot|x+4|$. Het lastige is dat $|x+4|$ ook van $x$ afhangt.",
                    "Spreek eerst af dat $\\delta \\le 1$. Dan geldt $3<x<5$, dus $|x+4|<9$. Gebruik dit om de uiteindelijke $\\delta$ te kiezen.",
                ],
                "full_solution": r"""$|x^2-16| = |x-4|\cdot|x+4|$.

**Stap 1.** Begrens $|x+4|$: spreek af dat $\delta \le 1$. Als $|x-4|<1$, dan $3<x<5$, dus $7<x+4<9$, dus $|x+4|<9$.

**Stap 2.** Kies $\delta$: we willen $|x-4|\cdot|x+4| < \varepsilon$. Met $|x+4|<9$ volstaat $|x-4| < \varepsilon/9$.

Kies dus $\delta = \min(1, \varepsilon/9)$.

**Controle:** als $0<|x-4|<\delta$, dan zowel $|x+4|<9$ (want $\delta\le1$) als $|x-4|<\varepsilon/9$, dus $|x^2-16| = |x-4||x+4| < \frac{\varepsilon}{9}\cdot 9 = \varepsilon$. ✓""",
                "answer_type": "open",
            },
        ],
    },
    {
        "module_id": 1,
        "chapter_number": 2,
        "title": "Continuïteit en de tussenwaardestelling",
        "theory_content": r"""
### Wat je al weet

In vorige hoofdstuk heb je limieten precies leren definiëren: $\lim_{x\to a} f(x) = L$ betekent dat je voor elke gevraagde nauwkeurigheid een marge rond $a$ kunt garanderen. Continuïteit bouwt daar direct op voort.

### Teken de grafiek zonder je pen op te tillen

Stel je tekent de grafiek van een functie met een pen, zonder ooit de pen van het papier te halen. Dat is de intuïtie achter "continu": geen gaten, geen sprongen, geen plekken waar de grafiek plotseling ergens anders opduikt.

Maar wanneer moet je precies je pen optillen? Bekijk drie situaties bij een punt $x=a$:

1. De functie is daar simpelweg niet gedefinieerd (bijvoorbeeld een breuk die daar $0$ in de noemer geeft): je kunt er niet doorheen tekenen, dus je moet de pen optillen.
2. De grafiek "springt" van de ene hoogte naar de andere (denk aan een trapfunctie): ook hier moet de pen omhoog.
3. Er zit een "gaatje": de grafiek nadert netjes een bepaalde hoogte, maar precies in dat ene punt zit de functiewaarde ergens anders (of ontbreekt hij): ook dan kun je niet doortekenen.

In al deze drie gevallen is er een conflict tussen "waar de grafiek naartoe beweegt" (de limiet) en "waar de functie daadwerkelijk zit" (de functiewaarde). Continuïteit in $a$ betekent precies dat dit conflict er niet is.

### De formele definitie

Een functie $f$ is **continu in $a$** als alle drie deze dingen kloppen:

1. $f(a)$ bestaat (er is een functiewaarde),
2. $\lim_{x\to a} f(x)$ bestaat (de grafiek nadert een eenduidige hoogte),
3. en beide zijn aan elkaar gelijk:
$$\lim_{x \to a} f(x) = f(a)$$

Is één van die drie voorwaarden niet vervuld, dan is $f$ discontinu (niet continu) in $a$. Dit levert drie soorten discontinuïteit op, corresponderend met de drie situaties hierboven:

- **Ophefbaar (removable):** de limiet bestaat wel, maar is niet gelijk aan $f(a)$, of $f(a)$ bestaat niet ("het gaatje"). Voorbeeld: $f(x) = \frac{x^2-1}{x-1}$ in $x=1$ (de factor $(x-1)$ valt bij het vereenvoudigen weg, maar $f(1)$ zelf is niet gedefinieerd, delen door 0).
- **Sprong (jump):** linker- en rechterlimiet bestaan allebei, maar zijn ongelijk aan elkaar.
- **Oneindig (infinite):** de functie schiet weg naar $\pm\infty$, zoals $f(x)=1/x$ in $x=0$.

### De tussenwaardestelling: een rivier oversteken

Stel je loopt van de ene oever van een ondiepe rivier naar de andere, dwars door het water. Aan de startoever staat het water bij je enkels, aan de andere oever ben je weer droog. Ergens onderweg moet er dan een moment zijn geweest waarop het water precies kniehoogte had, hoe grillig de rivierbodem ook is, je kunt die diepte onmogelijk overslaan zonder er even doorheen te lopen.

Dat is de **tussenwaardestelling (TWS)**: als een continue functie $f$ op $[a,b]$ de waarde $f(a)$ aanneemt aan het begin en $f(b)$ aan het eind, dan neemt hij onderweg **elke** waarde tussen $f(a)$ en $f(b)$ minstens één keer aan. Formeel: als $y$ ligt tussen $f(a)$ en $f(b)$, dan bestaat er een $c \in [a,b]$ met $f(c) = y$.

**Handige toepassing:** als $f(a)$ negatief is en $f(b)$ positief (of andersom), dan moet $f$ ergens tussen $a$ en $b$ door $0$ heen, dus heeft $f$ daar een nulpunt. Zo kun je het bestaan van een oplossing bewijzen zonder hem uit te rekenen.

**Voorbeeld.** Toon aan dat $f(x) = x^3 - x - 1$ een nulpunt heeft tussen $x=1$ en $x=2$.

**Stap 1.** Controleer dat $f$ continu is: $f$ is een polynoom (som van machten van $x$), en polynomen zijn overal continu, dus de TWS mag toegepast worden.

**Stap 2.** Bereken de functiewaarden aan de randen: $f(1) = 1-1-1 = -1 < 0$ en $f(2) = 8-2-1 = 5 > 0$.

**Stap 3.** Trek de conclusie: omdat $f(1)$ en $f(2)$ tegengesteld teken hebben, en $f$ continu is op $[1,2]$, garandeert de TWS een $c \in (1,2)$ met $f(c)=0$. Dat is precies een nulpunt tussen $1$ en $2$.
""",
        "summary": "Continuïteit betekent dat limiet en functiewaarde overeenkomen. De tussenwaardestelling gebruikt continuïteit om het bestaan van oplossingen aan te tonen zonder ze expliciet te berekenen, met name handig voor nulpunten.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Gegeven $f(x) = \begin{cases} x^2 & x < 2 \\ 3x - 2 & x \ge 2\end{cases}$. Onderzoek of $f$ continu is in $x=2$.",
                "hints": [
                    "Bereken de linkerlimiet ($x \\to 2^-$, gebruik $x^2$) en de rechterlimiet ($x\\to2^+$, gebruik $3x-2$) apart.",
                    "Vergelijk beide limieten met elkaar én met $f(2)$.",
                ],
                "full_solution": r"""Linkerlimiet: $\lim_{x\to2^-} x^2 = 4$. Rechterlimiet: $\lim_{x\to2^+}(3x-2) = 4$. Functiewaarde: $f(2) = 3(2)-2 = 4$.

Alle drie zijn gelijk aan 4, dus $f$ is continu in $x=2$.""",
                "answer_type": "open",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Gebruik de tussenwaardestelling om aan te tonen dat $\cos(x) = x$ een oplossing heeft in het interval $(0,1)$.",
                "hints": [
                    "Definieer $g(x) = \\cos(x) - x$ en onderzoek het teken van $g(0)$ en $g(1)$.",
                    "$g$ is continu (som van continue functies). Wat concludeer je als $g(0)$ en $g(1)$ tegengesteld teken hebben?",
                ],
                "full_solution": r"""Definieer $g(x) = \cos(x) - x$, continu op $[0,1]$ (cosinus en $x$ zijn beide continu, dus ook hun verschil).

$g(0) = \cos(0) - 0 = 1 > 0$.
$g(1) = \cos(1) - 1 \approx 0{,}540 - 1 = -0{,}460 < 0$.

Omdat $g(0)>0$ en $g(1)<0$, bestaat er volgens de TWS een $c\in(0,1)$ met $g(c)=0$, dus $\cos(c) = c$. Dat is precies de gevraagde oplossing.""",
                "answer_type": "open",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Classificeer het type discontinuïteit van $f(x) = \dfrac{x^2-1}{x-1}$ in $x=1$, en van $g(x) = \dfrac{1}{x}$ in $x=0$.",
                "hints": [
                    "Ontbind $f$ eerst: wat gebeurt er met de factor $(x-1)$?",
                    "Bekijk wat er met $g(x)$ gebeurt als $x \\to 0^+$ en $x \\to 0^-$.",
                ],
                "full_solution": r"""$f(x) = \frac{(x-1)(x+1)}{x-1} = x+1$ voor $x\ne1$. De limiet $\lim_{x\to1} f(x) = 2$ bestaat wél, maar $f(1)$ is niet gedefinieerd (delen door 0). Dit is een **ophefbare discontinuïteit**: je kunt $f$ continu maken door $f(1):=2$ te definiëren.

Voor $g(x)=1/x$: als $x\to0^+$ gaat $g(x)\to+\infty$, als $x\to0^-$ gaat $g(x)\to-\infty$. Dit is een **oneindige discontinuïteit** (verticale asymptoot).""",
                "answer_type": "open",
            },
        ],
    },
    {
        "module_id": 1,
        "chapter_number": 3,
        "title": "De afgeleide: definitie via het differentiequotiënt",
        "theory_content": r"""
### Wat je al weet

Uit VWO B ken je de richtingscoëfficiënt (helling) van een **rechte lijn**: hoeveel $y$ stijgt of daalt per stap van $1$ in $x$. Voor een rechte lijn is dat overal hetzelfde getal.

### Maar wat is de helling van een kromme lijn?

Bij een kromme grafiek is dat lastiger: de helling verandert continu van punt tot punt. Wat betekent "de helling in één specifiek punt" eigenlijk?

Pak twee punten op de grafiek van $f$: het punt $(x, f(x))$ en een tweede punt daar vlak naast, $(x+h, f(x+h))$, waarbij $h$ een klein stapje is. De lijn door die twee punten (een **secans**) heeft wél een gewone, berekenbare richtingscoëfficiënt:
$$\text{helling secans} = \frac{f(x+h) - f(x)}{(x+h) - x} = \frac{f(x+h) - f(x)}{h}$$

Dit heet het **differentiequotiënt**. Het is niet de helling in het punt zelf, maar een goede benadering ervan, over een klein stukje $h$.

Nu het idee: laat $h$ steeds kleiner worden, richting $0$. Het tweede punt kruipt dan steeds dichter naar het eerste punt toe, en de secans draait mee totdat hij samenvalt met de **raaklijn**, de lijn die de grafiek precies in dat ene punt raakt. De helling van die raaklijn is wat we de **afgeleide** noemen.

### De formele definitie

$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

Dit is exact het idee van hierboven, nu als limiet: de helling van de secans terwijl $h \to 0$. Merk op dat dit een limiet is zoals je in hoofdstuk 1 hebt geleerd, met dezelfde soort $\varepsilon$-$\delta$-precisie eronder, al werk je in de praktijk meestal met algebraïsche technieken in plaats van de formele definitie zelf.

**Notatie:** $f'(x)$, $\frac{dy}{dx}$, en $\frac{d}{dx}f(x)$ betekenen allemaal hetzelfde: de afgeleide van $f$ naar $x$.

### Een volledig uitgewerkt voorbeeld

**Bepaal met de definitie de afgeleide van $f(x) = x^2$.**

**Stap 1.** Schrijf het differentiequotiënt op met $f(x)=x^2$:
$$f'(x) = \lim_{h\to0} \frac{(x+h)^2 - x^2}{h}$$

**Stap 2.** Werk de teller uit: $(x+h)^2 = x^2 + 2xh + h^2$, dus de teller wordt $x^2+2xh+h^2-x^2 = 2xh+h^2$.
$$f'(x) = \lim_{h\to0} \frac{2xh+h^2}{h}$$

**Stap 3.** Deel $h$ weg uit teller en noemer (mag, want we kijken naar $h \to 0$, niet naar $h=0$ zelf, dus $h \ne 0$):
$$f'(x) = \lim_{h\to0} (2x+h)$$

**Stap 4.** Laat nu $h \to 0$: de term $h$ verdwijnt, en er blijft over:
$$f'(x) = 2x$$

Dit bevestigt de bekende regel $\frac{d}{dx}x^2 = 2x$ die je in het volgende hoofdstuk als kant-en-klare regel gaat gebruiken, maar nu heb je 'm zelf, volledig vanuit de definitie, afgeleid.
""",
        "summary": "De afgeleide is een limiet van een differentiequotiënt: de helling van de secans terwijl de twee punten naar elkaar toe kruipen, tot je de helling van de raaklijn overhoudt.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Bepaal met de definitie de afgeleide van $f(x) = x^3$.",
                "hints": [
                    "Werk $(x+h)^3$ volledig uit met het binomium (of stap voor stap vermenigvuldigen).",
                    "Na uitwerken houd je een teller over die deelbaar is door $h$: deel weg en laat $h\\to0$.",
                ],
                "full_solution": r"""$$f'(x) = \lim_{h\to0}\frac{(x+h)^3 - x^3}{h}$$

$(x+h)^3 = x^3 + 3x^2h + 3xh^2 + h^3$, dus:
$$f'(x) = \lim_{h\to0}\frac{3x^2h+3xh^2+h^3}{h} = \lim_{h\to0}(3x^2+3xh+h^2) = 3x^2$$""",
                "answer_type": "expression",
                "correct_answer": "3x^2",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Bepaal met de definitie de afgeleide van $f(x) = \sqrt{x}$ (voor $x > 0$).",
                "hints": [
                    "Je krijgt $\\frac{\\sqrt{x+h}-\\sqrt{x}}{h}$, wat direct $0/0$ geeft bij $h=0$: vermenigvuldig teller én noemer met de toegevoegde vorm $\\sqrt{x+h}+\\sqrt{x}$.",
                    "Na vermenigvuldigen met de toegevoegde vorm verdwijnt de wortel uit de teller (verschil van kwadraten), en kun je $h$ wegdelen.",
                ],
                "full_solution": r"""$$f'(x) = \lim_{h\to0} \frac{\sqrt{x+h}-\sqrt{x}}{h}$$

Vermenigvuldig met de toegevoegde vorm:
$$= \lim_{h\to0} \frac{\sqrt{x+h}-\sqrt{x}}{h}\cdot\frac{\sqrt{x+h}+\sqrt{x}}{\sqrt{x+h}+\sqrt{x}} = \lim_{h\to0} \frac{(x+h)-x}{h(\sqrt{x+h}+\sqrt{x})} = \lim_{h\to0} \frac{h}{h(\sqrt{x+h}+\sqrt{x})}$$

$$= \lim_{h\to0} \frac{1}{\sqrt{x+h}+\sqrt{x}} = \frac{1}{2\sqrt{x}}$$""",
                "answer_type": "expression",
                "correct_answer": "1/(2sqrt(x))",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Bepaal de vergelijking van de raaklijn aan $f(x) = x^2$ in het punt $(3, 9)$.",
                "hints": [
                    "Gebruik $f'(x) = 2x$ (uit het voorbeeld in de theorie) om de helling in $x=3$ te bepalen.",
                    "Gebruik de puntrichtingsvorm $y - y_0 = m(x - x_0)$ met $(x_0,y_0)=(3,9)$ en $m=f'(3)$.",
                ],
                "full_solution": r"""$f'(x) = 2x$, dus de helling in $x=3$ is $f'(3) = 6$.

Raaklijn: $y - 9 = 6(x-3)$, dus $y = 6x - 18 + 9 = 6x - 9$.""",
                "answer_type": "expression",
                "correct_answer": "y=6x-9",
            },
            {
                "order_index": 4, "difficulty": 3,
                "question": r"Laat met de definitie zien dat $f(x)=|x|$ niet differentieerbaar is in $x=0$.",
                "hints": [
                    "Splits het differentiequotiëont $\\frac{|0+h|-|0|}{h} = \\frac{|h|}{h}$ op in het geval $h>0$ en $h<0$.",
                    "Vergelijk de linker- en rechterlimiet van $\\frac{|h|}{h}$ als $h\\to0$.",
                ],
                "full_solution": r"""$$f'(0) = \lim_{h\to0} \frac{|0+h|-|0|}{h} = \lim_{h\to0}\frac{|h|}{h}$$

Voor $h>0$: $\frac{|h|}{h} = \frac{h}{h} = 1$, dus de rechterlimiet is $1$.
Voor $h<0$: $\frac{|h|}{h} = \frac{-h}{h} = -1$, dus de linkerlimiet is $-1$.

Omdat linker- en rechterlimiet niet gelijk zijn ($-1 \ne 1$), bestaat $\lim_{h\to0}\frac{|h|}{h}$ niet, dus $f$ is niet differentieerbaar in $x=0$. Meetkundig: de grafiek van $|x|$ heeft een "knik" in de oorsprong, er is geen eenduidige raaklijn.""",
                "answer_type": "open",
            },
        ],
    },
    {
        "module_id": 1,
        "chapter_number": 4,
        "title": "Differentiatieregels en de kettingregel",
        "theory_content": r"""
### Wat je al weet

In het vorige hoofdstuk heb je gezien dat het bepalen van een afgeleide via de definitie (met de limiet van het differentiequotiënt) nogal wat werk is, zelfs voor een simpele functie als $x^2$. Voor iets als $\sin(x^3)e^{2x}$ zou dat vrijwel onwerkbaar worden. Daarom bestaan er kant-en-klare regels, ooit met de definitie bewezen, die je nu gewoon mag toepassen.

### Som- en productregel: vrij intuïtief

Als je twee functies optelt, tel je gewoon hun afgeleiden op: $(f+g)' = f' + g'$. Dat volgt direct uit de definitie (een limiet van een som is de som van de limieten).

Bij een product ligt het subtieler: $(fg)' \ne f'g'$. In plaats daarvan geldt de **productregel:** $(fg)' = f'g + fg'$, beide functies "krijgen om de beurt de beurt om te veranderen", terwijl de ander even vastgehouden wordt.

### De kettingregel: de lastigste, dus met een concreet voorbeeld

Stel je fietst, en je snelheid hangt af van hoe uitgerust je bent, en hoe uitgerust je bent hangt weer af van de tijd sinds je wakker werd. Als je conditie twee keer zo snel achteruitgaat naarmate de tijd verstrijkt, én je snelheid daardoor drie keer zo gevoelig is voor je conditie, dan verandert je snelheid per saldo $2 \times 3 = 6$ keer zo snel ten opzichte van de tijd. Veranderingssnelheden die na elkaar inwerken, vermenigvuldig je.

Dat is precies wat er gebeurt bij een **samengestelde functie** $y = f(g(x))$: eerst zet $g$ de $x$ om in een tussenwaarde, daarna zet $f$ die tussenwaarde om in de uiteindelijke uitkomst. De **kettingregel** zegt dat de totale veranderingssnelheid het product is van de twee afzonderlijke veranderingssnelheden:
$$y' = f'(g(x)) \cdot g'(x)$$

In woorden: neem de afgeleide van de buitenfunctie $f$, maar vul daar (nog steeds) de binnenfunctie $g(x)$ in, en vermenigvuldig dat met de afgeleide van de binnenfunctie zelf.

### Overzicht van de regels

- **Somregel:** $(f+g)' = f' + g'$
- **Productregel:** $(fg)' = f'g + fg'$
- **Quotiëntregel:** $\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2}$
- **Kettingregel:** als $y = f(g(x))$, dan $y' = f'(g(x))\cdot g'(x)$

Standaardafgeleiden (bekend uit VWO B): $\frac{d}{dx}x^n = nx^{n-1}$, $\frac{d}{dx}e^x = e^x$, $\frac{d}{dx}\ln x = \frac{1}{x}$, $\frac{d}{dx}\sin x = \cos x$, $\frac{d}{dx}\cos x = -\sin x$.

### Twee volledig uitgewerkte voorbeelden

**Voorbeeld 1 (kettingregel).** Differentieer $f(x) = \sin(x^2)$.

Herken de opbouw: de buitenfunctie is $\sin(\cdot)$, de binnenfunctie is $x^2$. De afgeleide van de buitenfunctie is $\cos(\cdot)$, met de binnenfunctie er weer ingevuld: $\cos(x^2)$. De afgeleide van de binnenfunctie $x^2$ is $2x$. Vermenigvuldig:
$$f'(x) = \cos(x^2)\cdot 2x$$

**Voorbeeld 2 (productregel + kettingregel).** Differentieer $f(x) = x^2 e^{3x}$.

Dit is een product van $x^2$ en $e^{3x}$, dus productregel: $(fg)'=f'g+fg'$. Voor het tweede deel, $e^{3x}$, heb je zelf de kettingregel nodig (buitenfunctie $e^{(\cdot)}$, binnenfunctie $3x$ met afgeleide $3$):
$$f'(x) = 2x\cdot e^{3x} + x^2 \cdot (e^{3x}\cdot 3) = e^{3x}(2x+3x^2)$$
""",
        "summary": "De kettingregel is de belangrijkste nieuwe techniek: buitenafgeleide (in de binnenfunctie ingevuld) keer binnenafgeleide. Combineer met som-, product- en quotiëntregel voor complexere functies.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Differentieer $f(x) = x^3 \sin(x)$.",
                "hints": [
                    "Dit is een product van twee functies: gebruik de productregel $(fg)'=f'g+fg'$.",
                    "$f_1(x)=x^3$ met $f_1'=3x^2$, en $f_2(x)=\\sin(x)$ met $f_2'=\\cos(x)$.",
                ],
                "full_solution": r"""$$f'(x) = 3x^2\sin(x) + x^3\cos(x)$$""",
                "answer_type": "expression",
                "correct_answer": "3x^2sin(x)+x^3cos(x)",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Differentieer $f(x) = \dfrac{2x+1}{x^2+3}$.",
                "hints": [
                    "Gebruik de quotiëntregel: teller-afgeleide keer noemer min teller keer noemer-afgeleide, gedeeld door noemer in het kwadraat.",
                    "$f_1(x)=2x+1$, $f_1'=2$; $f_2(x)=x^2+3$, $f_2'=2x$.",
                ],
                "full_solution": r"""$$f'(x) = \frac{2(x^2+3) - (2x+1)(2x)}{(x^2+3)^2} = \frac{2x^2+6-4x^2-2x}{(x^2+3)^2} = \frac{-2x^2-2x+6}{(x^2+3)^2}$$""",
                "answer_type": "open",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Differentieer $f(x) = \sin(3x^2 - 1)$.",
                "hints": [
                    "Kettingregel: buitenfunctie is $\\sin(\\cdot)$, binnenfunctie is $3x^2-1$.",
                    "Afgeleide binnenfunctie: $\\frac{d}{dx}(3x^2-1) = 6x$.",
                ],
                "full_solution": r"""$$f'(x) = \cos(3x^2-1)\cdot 6x = 6x\cos(3x^2-1)$$""",
                "answer_type": "expression",
                "correct_answer": "6x*cos(3x^2-1)",
            },
            {
                "order_index": 4, "difficulty": 3,
                "question": r"Differentieer $f(x) = e^{x^2}\ln(x)$.",
                "hints": [
                    "Productregel met $f_1(x)=e^{x^2}$ en $f_2(x)=\\ln(x)$.",
                    "Voor $f_1'$ heb je de kettingregel nodig: $\\frac{d}{dx}e^{x^2} = e^{x^2}\\cdot 2x$.",
                ],
                "full_solution": r"""$f_1(x)=e^{x^2}$, met kettingregel $f_1'(x) = 2x\,e^{x^2}$. $f_2(x)=\ln(x)$, $f_2'(x)=\frac{1}{x}$.

Productregel:
$$f'(x) = 2x\,e^{x^2}\ln(x) + e^{x^2}\cdot\frac{1}{x} = e^{x^2}\left(2x\ln(x) + \frac{1}{x}\right)$$""",
                "answer_type": "open",
            },
        ],
    },
    {
        "module_id": 1,
        "chapter_number": 5,
        "title": "Impliciet differentiëren en gerelateerde snelheden",
        "theory_content": r"""
### Wat je al weet

Tot nu toe had je altijd een expliciete formule $y = f(x)$: $y$ helemaal alleen aan één kant, uitgedrukt in $x$. Daar kon je gewoon op differentiëren met de regels uit het vorige hoofdstuk.

### Wat als je y niet kunt vrijmaken?

Neem de vergelijking van een cirkel: $x^2+y^2=25$. Je zou $y$ kunnen oplossen ($y=\pm\sqrt{25-x^2}$), maar dat plusteken en minteken zijn onhandig (het is dan eigenlijk twee functies, de boven- en onderkant van de cirkel). Bij ingewikkeldere vergelijkingen, zoals $x^3+y^3=6xy$, lukt vrijmaken van $y$ soms helemaal niet.

Toch heeft de cirkel op elk punt (behalve links en rechts) gewoon een duidelijke raaklijn met een duidelijke helling. Die helling moet je dus ook kunnen berekenen zonder eerst $y$ expliciet te maken. Dat heet **impliciet differentiëren**.

### Het idee: y is stiekem toch een functie van x

Ook al staat het er niet met zoveel woorden, op elk stukje van de cirkel hangt $y$ af van $x$: verander je $x$ een klein beetje, dan verandert $y$ mee (volgens de vergelijking). Je mag dus doen alsof $y = y(x)$, een verborgen functie van $x$, en beide kanten van de vergelijking naar $x$ differentiëren. Het enige addertje: telkens als je een term met $y$ tegenkomt, moet je de kettingregel gebruiken, want je differentieert eigenlijk "iets met $y(x)$" naar $x$. Dat levert steeds een extra factor $\frac{dy}{dx}$ op. Bijvoorbeeld: $\frac{d}{dx}(y^2) = 2y\cdot\frac{dy}{dx}$, net als bij $\frac{d}{dx}(g(x))^2 = 2g(x)\cdot g'(x)$ in het vorige hoofdstuk, maar dan met $g=y$.

**Voorbeeld.** Bepaal $\frac{dy}{dx}$ voor $x^2+y^2=25$.

**Stap 1.** Differentieer beide kanten naar $x$. Links: $\frac{d}{dx}(x^2) = 2x$, en $\frac{d}{dx}(y^2) = 2y\frac{dy}{dx}$ (kettingregel). Rechts: $\frac{d}{dx}(25)=0$ (een constante verandert niet).
$$2x + 2y\frac{dy}{dx} = 0$$

**Stap 2.** Los op naar $\frac{dy}{dx}$:
$$\frac{dy}{dx} = -\frac{x}{y}$$

### Gerelateerde snelheden: dezelfde truc, maar met de tijd

Bij **gerelateerde snelheden** gebruik je precies dezelfde impliciete techniek, maar nu differentieer je naar de tijd $t$ in plaats van naar $x$. Het scenario: twee (of meer) grootheden zijn aan elkaar gekoppeld via een vergelijking, en beide veranderen in de tijd. Ken je de veranderingssnelheid van de één, dan kun je via de vergelijking de veranderingssnelheid van de ander vinden, ook al ken je op geen enkel moment de expliciete formule van de één in termen van de tijd.

**Voorbeeld.** Een cirkelvormige olievlek breidt uit; de straal $r$ groeit met $2$ m/min. Hoe snel groeit de oppervlakte $A$ als $r=5$ m?

**Stap 1.** Leg het verband tussen de grootheden vast: $A = \pi r^2$ (de bekende oppervlakteformule van een cirkel).

**Stap 2.** Differentieer beide kanten naar $t$, met de kettingregel voor $r^2$ (want $r$ hangt af van $t$):
$$\frac{dA}{dt} = 2\pi r \frac{dr}{dt}$$

**Stap 3.** Vul de gegeven waarden in: $r=5$ en $\frac{dr}{dt}=2$.
$$\frac{dA}{dt} = 2\pi(5)(2) = 20\pi \approx 62{,}8 \text{ m}^2/\text{min}$$
""",
        "summary": "Impliciet differentiëren: differentieer beide kanten naar $x$ en gebruik de kettingregel op elke $y$-term (levert een factor $dy/dx$ op). Gerelateerde snelheden: dezelfde aanpak maar differentiëren naar $t$, met bekende en gevraagde snelheden als $\\frac{d(\\cdot)}{dt}$.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Bepaal $\dfrac{dy}{dx}$ impliciet voor $x^2 + y^2 = 25$ in het punt $(3,4)$.",
                "hints": [
                    "Differentieer beide kanten naar $x$: $2x + 2y\\frac{dy}{dx} = 0$.",
                    "Los op naar $\\frac{dy}{dx}$ en vul daarna $x=3, y=4$ in.",
                ],
                "full_solution": r"""$2x+2y\frac{dy}{dx}=0 \implies \frac{dy}{dx} = -\frac{x}{y}$.

In $(3,4)$: $\frac{dy}{dx} = -\frac{3}{4}$.""",
                "answer_type": "numeric",
                "correct_answer": "-3/4",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Bepaal $\dfrac{dy}{dx}$ impliciet voor $x^3 + y^3 = 6xy$ (folium van Descartes).",
                "hints": [
                    "Differentieer term voor term: $x^3 \\to 3x^2$, $y^3 \\to 3y^2\\frac{dy}{dx}$ (kettingregel), en $6xy$ vraagt de productregel.",
                    "Verzamel alle termen met $\\frac{dy}{dx}$ aan één kant en los op.",
                ],
                "full_solution": r"""Differentieer beide kanten naar $x$, met de productregel voor $6xy$:
$$3x^2 + 3y^2\frac{dy}{dx} = 6y + 6x\frac{dy}{dx}$$

Verzamel $\frac{dy}{dx}$-termen:
$$3y^2\frac{dy}{dx} - 6x\frac{dy}{dx} = 6y - 3x^2$$
$$\frac{dy}{dx}(3y^2-6x) = 6y-3x^2$$
$$\frac{dy}{dx} = \frac{6y-3x^2}{3y^2-6x} = \frac{2y-x^2}{y^2-2x}$$""",
                "answer_type": "open",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Een cirkelvormige olievlek breidt uit met $\frac{dr}{dt}=2$ m/min. Hoe snel neemt de oppervlakte toe wanneer $r=5$ m?",
                "hints": [
                    "$A=\\pi r^2$. Differentieer beide kanten naar $t$ met de kettingregel.",
                    "Vul $r=5$ en $\\frac{dr}{dt}=2$ in.",
                ],
                "full_solution": r"""$$\frac{dA}{dt} = 2\pi r\frac{dr}{dt} = 2\pi(5)(2) = 20\pi \approx 62{,}8 \text{ m}^2/\text{min}$$""",
                "answer_type": "open",
            },
            {
                "order_index": 4, "difficulty": 3,
                "question": r"Een ladder van 5 m staat tegen een muur. De voet glijdt weg met 1 m/s. Hoe snel zakt de top van de ladder wanneer de voet 3 m van de muur staat?",
                "hints": [
                    "Stel $x$ = afstand voet tot muur, $y$ = hoogte top tegen muur. Er geldt $x^2+y^2=25$ (Pythagoras, ladderlengte 5).",
                    "Differentieer naar $t$, bepaal eerst $y$ bij $x=3$ (met Pythagoras), en vul dan alle bekende waarden in.",
                ],
                "full_solution": r"""$x^2+y^2=25$. Differentieer naar $t$: $2x\frac{dx}{dt} + 2y\frac{dy}{dt} = 0$.

Bij $x=3$: $y = \sqrt{25-9} = 4$.

Gegeven $\frac{dx}{dt}=1$ m/s. Invullen:
$$2(3)(1) + 2(4)\frac{dy}{dt} = 0 \implies 6 + 8\frac{dy}{dt} = 0 \implies \frac{dy}{dt} = -\frac{6}{8} = -0{,}75 \text{ m/s}$$

De top zakt dus met $0{,}75$ m/s (het minteken geeft aan dat $y$ afneemt).""",
                "answer_type": "open",
            },
        ],
    },
    {
        "module_id": 1,
        "chapter_number": 6,
        "title": "Extrema, de middelwaardestelling en krommeonderzoek",
        "theory_content": r"""
### Wat je al weet

Begrippen als top, dal, minimum en maximum ken je al uit VWO B: een top is een punt waar de grafiek van stijgen naar dalen overgaat (of andersom voor een dal). Wat nieuw is: hoe je dat met de afgeleide (in plaats van met de grafische rekenmachine) exact opspoort en onderbouwt.

### Waar kunnen extrema zitten?

In een top of dal is de raaklijn horizontal: de grafiek "kantelt" daar precies van stijgend naar dalend (of andersom), en op dat omslagpunt is de helling nul. Dat geeft een simpel opsporingsrecept: zoek de plekken waar $f'(x)=0$ (of waar $f'$ niet bestaat, zoals bij een scherpe knik). Zo'n plek heet een **kritiek punt**. Let op: niet elk kritiek punt is automatisch een top of dal (denk aan een "zadel" waar de grafiek na een vlak stukje toch blijft stijgen), dus je moet nog controleren wat voor soort punt het echt is.

**Eerste-afgeleide-test:** kijk naar het teken van $f'$ links en rechts van een kritiek punt.
- Van $+$ (stijgend) naar $-$ (dalend): een lokaal **maximum**, de top van een berg.
- Van $-$ (dalend) naar $+$ (stijgend): een lokaal **minimum**, de bodem van een dal.
- Geen tekenwisseling: geen extreem, gewoon een moment van "pauzeren" tijdens het stijgen of dalen.

### De middelwaardestelling: je snelheidsmeter tijdens een autorit

Stel je rijdt van A naar B, een rit van 160 km die precies 2 uur duurt. Je gemiddelde snelheid over de hele rit was dus 80 km/u. Betekent dat dat je op enig moment ook echt precies 80 km/u hebt gereden? Ja, dat moet wel: als je de hele rit langzamer dan 80 had gereden, was je nooit op tijd geweest, en als je de hele rit sneller dan 80 had gereden, was je te vroeg geweest. Ergens onderweg moet je snelheidsmeter dus exact door de 80 heen zijn gegaan.

Dat is de **middelwaardestelling (MWS)**: als $f$ continu is op $[a,b]$ en differentieerbaar op $(a,b)$, dan bestaat er een $c\in(a,b)$ waar de **lokale** veranderingssnelheid gelijk is aan de **gemiddelde** veranderingssnelheid over het hele interval:
$$f'(c) = \frac{f(b)-f(a)}{b-a}$$
Meetkundig: ergens tussen $a$ en $b$ is de raaklijn evenwijdig aan de rechte lijn door de eindpunten $(a,f(a))$ en $(b,f(b))$ van de grafiek.

### De tweede afgeleide: hoe de helling zelf verandert

De afgeleide $f'$ vertelt je of $f$ stijgt of daalt. De **tweede afgeleide** $f''$ (de afgeleide van de afgeleide) vertelt je iets subtielers: hoe de helling zelf verandert, oftewel de **concaviteit** van de grafiek.

- $f''(x)>0$: de helling wordt steeds groter (of minder negatief), de grafiek buigt naar boven, zoals de binnenkant van een schaal ("houdt water vast"): dit heet **hol** of **convex**.
- $f''(x)<0$: de helling wordt steeds kleiner, de grafiek buigt naar beneden, als de buitenkant van een koepel: dit heet **bol** of **concaaf**.

Een **buigpunt** is een plek waar de concaviteit omslaat, dus waar $f''$ van teken wisselt.

### Een volledig krommeonderzoek

**Onderzoek de grafiek van $f(x)=x^3-3x$: extrema en buigpunten.**

**Stap 1 (kritieke punten):** $f'(x)=3x^2-3=0 \Rightarrow x^2=1 \Rightarrow x=\pm1$.

**Stap 2 (soort extremum bepalen):** teken van $f'$: voor $x<-1$ is $f'>0$ (want bijvoorbeeld $f'(-2)=9>0$), tussen $-1$ en $1$ is $f'<0$ (bijvoorbeeld $f'(0)=-3<0$), voor $x>1$ is $f'>0$ weer. Dus: van $+$ naar $-$ bij $x=-1$ (lokaal maximum, $f(-1)=2$), van $-$ naar $+$ bij $x=1$ (lokaal minimum, $f(1)=-2$).

**Stap 3 (buigpunt):** $f''(x)=6x=0 \Rightarrow x=0$. Voor $x<0$ is $f''<0$ (bol), voor $x>0$ is $f''>0$ (hol): de concaviteit wisselt echt, dus $(0,0)$ is een buigpunt.
""",
        "summary": "Kritieke punten ($f'=0$) zijn kandidaten voor extrema; de eerste-afgeleide-test bepaalt of het een maximum of minimum is. De tweede afgeleide vertelt iets over concaviteit en buigpunten. De MWS garandeert een punt waar de raaklijn evenwijdig loopt aan de verbindingslijn tussen de eindpunten.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Bepaal de lokale extrema van $f(x) = x^3 - 3x + 1$.",
                "hints": [
                    "Bereken $f'(x)$ en los $f'(x)=0$ op om de kritieke punten te vinden.",
                    "Pas de eerste-afgeleide-test toe: onderzoek het teken van $f'$ links en rechts van elk kritiek punt.",
                ],
                "full_solution": r"""$f'(x) = 3x^2-3 = 3(x-1)(x+1) = 0 \implies x=-1$ of $x=1$.

Teken van $f'$: voor $x<-1$ is $f'>0$ (stijgend), tussen $-1$ en $1$ is $f'<0$ (dalend), voor $x>1$ is $f'>0$ (stijgend).

Dus: lokaal maximum in $x=-1$ met $f(-1) = -1+3+1=3$. Lokaal minimum in $x=1$ met $f(1)=1-3+1=-1$.""",
                "answer_type": "open",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Onderzoek de concaviteit en bepaal de buigpunten van $f(x) = x^4 - 4x^3$.",
                "hints": [
                    "Bereken $f''(x)$ en los $f''(x)=0$ op.",
                    "Controleer of $f''$ echt van teken wisselt bij elke oplossing (anders is het geen buigpunt).",
                ],
                "full_solution": r"""$f'(x) = 4x^3-12x^2$. $f''(x) = 12x^2-24x = 12x(x-2) = 0 \implies x=0$ of $x=2$.

Teken van $f''$: voor $x<0$: $f''>0$ (hol). Tussen $0$ en $2$: $f''<0$ (bol). Voor $x>2$: $f''>0$ (hol).

Bij beide punten wisselt het teken, dus beide zijn buigpunten: $f(0)=0$ geeft buigpunt $(0,0)$; $f(2)=16-32=-16$ geeft buigpunt $(2,-16)$.""",
                "answer_type": "open",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Toon met de middelwaardestelling aan dat er een $c \in (0,2)$ bestaat met $f'(c) = 2$ voor $f(x) = x^2$.",
                "hints": [
                    "$f$ is overal continu en differentieerbaar, dus de MWS is toepasbaar op elk interval.",
                    "Bereken $\\frac{f(2)-f(0)}{2-0}$ en vergelijk met $f'(x)=2x$.",
                ],
                "full_solution": r"""$f(x)=x^2$ is continu op $[0,2]$ en differentieerbaar op $(0,2)$, dus de MWS geldt.

$$\frac{f(2)-f(0)}{2-0} = \frac{4-0}{2} = 2$$

Volgens de MWS bestaat er een $c\in(0,2)$ met $f'(c)=2$. Omdat $f'(x)=2x$, geeft $2c=2$ direct $c=1 \in (0,2)$. ✓""",
                "answer_type": "open",
            },
            {
                "order_index": 4, "difficulty": 3,
                "question": r"Voer een volledig krommeonderzoek uit van $f(x) = x^3 - 3x^2$: bepaal extrema, buigpunten en beschrijf het globale verloop.",
                "hints": [
                    "Begin met $f'(x)=3x^2-6x$ voor de extrema, daarna $f''(x)=6x-6$ voor de buigpunten.",
                    "Beschrijf per interval (tussen en buiten de kritieke punten) of $f$ stijgt/daalt en hol/bol is.",
                ],
                "full_solution": r"""**Domein:** alle reële getallen.

**Eerste afgeleide:** $f'(x)=3x^2-6x=3x(x-2)=0 \implies x=0$ of $x=2$.
Teken: $f'>0$ voor $x<0$ (stijgend), $f'<0$ voor $0<x<2$ (dalend), $f'>0$ voor $x>2$ (stijgend).
$\Rightarrow$ lokaal maximum in $(0, f(0))=(0,0)$, lokaal minimum in $(2,f(2))=(2,-4)$.

**Tweede afgeleide:** $f''(x)=6x-6=0 \implies x=1$.
Teken: $f''<0$ voor $x<1$ (bol), $f''>0$ voor $x>1$ (hol).
$\Rightarrow$ buigpunt in $(1, f(1)) = (1,-2)$.

**Globaal verloop:** de grafiek stijgt tot $(0,0)$, daalt (eerst bol, na $x=1$ hol) tot $(2,-4)$, en stijgt daarna weer. Voor $x\to-\infty$ geldt $f(x)\to-\infty$, voor $x\to\infty$ geldt $f(x)\to\infty$.""",
                "answer_type": "open",
            },
        ],
    },
    {
        "module_id": 1,
        "chapter_number": 7,
        "title": "De regel van De l'Hôpital",
        "theory_content": r"""
### Wat je al weet

In hoofdstuk 1 kwam je $\lim_{x\to3}\frac{x^2-9}{x-3}$ tegen: invullen gaf $\frac00$, maar door te ontbinden ($x^2-9=(x-3)(x+3)$) kon je de storende factor wegdelen en alsnog het antwoord vinden.

### Wanneer die truc niet werkt

Bekijk nu $\lim_{x\to0}\frac{\sin(x)}{x}$. Invullen geeft weer $\frac{\sin(0)}{0} = \frac00$, dezelfde onbepaalde situatie. Maar hoe ontbind je $\sin(x)$? Dat kan niet als een product van eenvoudige factoren zoals bij een polynoom. De algebraïsche truc uit hoofdstuk 1 loopt hier vast, dus is er een nieuw gereedschap nodig.

### Het idee: dichtbij $a$ lijkt elke functie op zijn raaklijn

Je weet uit hoofdstuk 3 dat de afgeleide $f'(a)$ de helling van de raaklijn in $a$ is. Vlak bij $a$ liggen de grafiek van $f$ en die raaklijn vrijwel op elkaar, de raaklijn is de beste rechte-lijn-benadering van $f$ dichtbij $a$.

Stel nu dat zowel $f(a)=0$ als $g(a)=0$ (de $\frac00$-situatie). Vlak bij $a$ gedraagt $f(x)$ zich dus ongeveer als de rechte lijn met helling $f'(a)$ door het punt $(a,0)$, dus $f(x) \approx f'(a)\cdot(x-a)$. Hetzelfde geldt voor $g$: $g(x) \approx g'(a)\cdot(x-a)$. Vul dat in bij het quotiënt:
$$\frac{f(x)}{g(x)} \approx \frac{f'(a)(x-a)}{g'(a)(x-a)} = \frac{f'(a)}{g'(a)}$$
De factor $(x-a)$ valt weg. Dat is precies de intuïtie achter de regel van De l'Hôpital: bij een $\frac00$-botsing mag je teller en noemer allebei vervangen door hun afgeleiden.

### De formele regel

Als $\lim_{x\to a}\frac{f(x)}{g(x)}$ een **onbepaalde vorm** oplevert, $\frac{0}{0}$ of $\frac{\infty}{\infty}$, en $f,g$ zijn differentieerbaar rond $a$, dan geldt (mits het rechterlid bestaat):
$$\lim_{x\to a}\frac{f(x)}{g(x)} = \lim_{x\to a}\frac{f'(x)}{g'(x)}$$

**Let op:** controleer vóór elke toepassing opnieuw of je écht een onbepaalde vorm hebt. Is dat niet zo, dan mag je de regel niet toepassen, en geeft gewoon invullen het antwoord.

**Voorbeeld.** $\lim_{x\to0}\frac{\sin x}{x}$. Invullen geeft $\frac{0}{0}$, dus De l'Hôpital mag: $\lim_{x\to0}\frac{\cos x}{1} = \cos(0)=1$.

### Andere onbepaalde vormen

Vormen als $0\cdot\infty$, $\infty-\infty$, $1^\infty$, $0^0$ en $\infty^0$ zijn geen quotiënt, dus daar kun je De l'Hôpital niet direct op loslaten. Herschrijf ze eerst algebraïsch tot een breuk die wél de vorm $\frac00$ of $\frac{\infty}{\infty}$ heeft. Bijvoorbeeld $x\ln x$ (vorm $0\cdot\infty$ als $x\to0^+$, want $x\to0$ en $\ln x \to -\infty$) herschrijf je als $\frac{\ln x}{1/x}$ (nu vorm $\frac{-\infty}{\infty}$), en dán mag De l'Hôpital toegepast worden.
""",
        "summary": "De l'Hôpital vervangt teller en noemer door hun afgeleiden bij $0/0$- of $\\infty/\\infty$-vormen. Andere onbepaalde vormen herschrijf je eerst tot een breuk voordat je de regel toepast, en na elke toepassing controleer je opnieuw of het weer een onbepaalde vorm is.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Bereken $\lim_{x\to0} \dfrac{\sin(x)}{x}$ met de regel van De l'Hôpital.",
                "hints": [
                    "Controleer eerst dat invullen $0/0$ geeft.",
                    "Differentieer teller en noemer apart: $\\frac{d}{dx}\\sin(x)=\\cos(x)$, $\\frac{d}{dx}x = 1$.",
                ],
                "full_solution": r"""Invullen geeft $\frac{\sin 0}{0} = \frac00$, dus De l'Hôpital is toepasbaar:
$$\lim_{x\to0}\frac{\sin x}{x} = \lim_{x\to0}\frac{\cos x}{1} = \cos(0) = 1$$""",
                "answer_type": "numeric",
                "correct_answer": "1",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Bereken $\lim_{x\to\infty} \dfrac{\ln x}{x}$.",
                "hints": [
                    "Controleer dat dit de vorm $\\infty/\\infty$ heeft.",
                    "Differentieer teller ($\\frac{1}{x}$) en noemer ($1$) apart.",
                ],
                "full_solution": r"""Vorm $\infty/\infty$, dus De l'Hôpital:
$$\lim_{x\to\infty}\frac{\ln x}{x} = \lim_{x\to\infty}\frac{1/x}{1} = \lim_{x\to\infty}\frac{1}{x} = 0$$""",
                "answer_type": "numeric",
                "correct_answer": "0",
            },
            {
                "order_index": 3, "difficulty": 3,
                "question": r"Bereken $\lim_{x\to0} \dfrac{e^x - 1 - x}{x^2}$.",
                "hints": [
                    "Invullen geeft $0/0$; pas De l'Hôpital toe. Na de eerste keer differentiëren krijg je opnieuw $0/0$, dus nogmaals toepassen.",
                    "Na twee keer differentiëren van teller en noemer houd je een limiet over die je direct kunt invullen.",
                ],
                "full_solution": r"""Eerste keer: $\lim_{x\to0}\frac{e^x-1-x}{x^2}$ geeft $\frac{1-1-0}{0}=\frac00$.
$$\lim_{x\to0}\frac{e^x-1}{2x}$$
Dit geeft opnieuw $\frac{1-1}{0}=\frac00$, dus nog een keer:
$$\lim_{x\to0}\frac{e^x}{2} = \frac{e^0}{2} = \frac12$$""",
                "answer_type": "numeric",
                "correct_answer": "1/2",
            },
            {
                "order_index": 4, "difficulty": 3,
                "question": r"Bereken $\lim_{x\to0^+} x\ln(x)$.",
                "hints": [
                    "Dit is de vorm $0\\cdot(-\\infty)$, geen directe De l'Hôpital-vorm. Herschrijf $x\\ln(x)$ als $\\frac{\\ln x}{1/x}$.",
                    "Nu heb je de vorm $-\\infty/\\infty$, differentieer teller en noemer apart.",
                ],
                "full_solution": r"""Herschrijf: $x\ln x = \dfrac{\ln x}{1/x}$, vorm $\dfrac{-\infty}{\infty}$ als $x\to0^+$.

$$\lim_{x\to0^+}\frac{\ln x}{1/x} = \lim_{x\to0^+}\frac{1/x}{-1/x^2} = \lim_{x\to0^+} -x = 0$$

Dus $\lim_{x\to0^+} x\ln(x) = 0$.""",
                "answer_type": "numeric",
                "correct_answer": "0",
            },
        ],
    },
    {
        "module_id": 1,
        "chapter_number": 8,
        "title": "Optimalisatieproblemen",
        "theory_content": r"""
### Wat je al weet

In hoofdstuk 6 heb je geleerd hoe je met $f'(x)=0$ de extrema van een gegeven functie vindt. Optimaliseren is precies datzelfde idee, maar dan omgekeerd toegepast: je krijgt een praktijksituatie ("welke afmetingen geven de grootste oppervlakte", "welke prijs geeft de meeste winst") in woorden, en jouw taak is om daar zelf eerst een functie van te maken voordat je die extrema-technieken kunt gebruiken.

### Waarom heb je vaak twee variabelen in het begin?

Een praktijksituatie beschrijft meestal een grootheid die van **twee** dingen tegelijk afhangt (bijvoorbeeld de oppervlakte van een rechthoek hangt af van zowel breedte als hoogte). Maar $f'(x)=0$ werkt alleen voor een functie van **één** variabele. De truc is: er zit vrijwel altijd een extra gegeven ("nevenvoorwaarde") in de opgave dat de twee variabelen aan elkaar koppelt, waarmee je er één kunt wegwerken.

### Het recept

1. **Model:** vertaal de situatie naar een formule voor de te optimaliseren grootheid, meestal in twee variabelen.
2. **Nevenvoorwaarde:** gebruik het gegeven verband om één variabele uit te drukken in de andere, en vul dat in, zodat je één functie van één variabele overhoudt.
3. **Domein:** bepaal welke waarden praktisch zinvol zijn (bijvoorbeeld lengtes moeten $>0$ zijn).
4. **Differentiëren:** bepaal de afgeleide en zoek kritieke punten, exact zoals in hoofdstuk 6.
5. **Verifiëren:** controleer met de eerste- of tweede-afgeleide-test (of door randwaarden te vergelijken) dat het inderdaad een maximum of minimum is, en niet zomaar een willekeurig kritiek punt.
6. **Interpreteren:** vertaal het wiskundige antwoord terug naar de praktijksituatie (met eenheden, en in woorden wat het betekent).

### Een volledig uitgewerkt voorbeeld

**Een blik (cilinder) moet $500\text{ cm}^3$ inhoud hebben. Welke straal $r$ en hoogte $h$ minimaliseren het materiaalgebruik (de totale oppervlakte)?**

**Stap 1 (model):** de oppervlakte van een cilinder (twee cirkels plus de zijkant) is $S = 2\pi r^2 + 2\pi r h$, een formule met twee variabelen $r$ en $h$.

**Stap 2 (nevenvoorwaarde):** de inhoud ligt vast op $500\text{ cm}^3$: $\pi r^2 h = 500$, dus $h = \dfrac{500}{\pi r^2}$. Vul dit in bij $S$:
$$S(r) = 2\pi r^2 + 2\pi r \cdot \frac{500}{\pi r^2} = 2\pi r^2 + \frac{1000}{r}$$
Nu is $S$ nog maar een functie van de ene variabele $r$.

**Stap 3 (domein):** $r>0$, want een straal kan niet negatief of nul zijn.

**Stap 4 (differentiëren):**
$$S'(r) = 4\pi r - \frac{1000}{r^2} = 0 \implies 4\pi r^3 = 1000 \implies r^3 = \frac{250}{\pi} \implies r = \sqrt[3]{250/\pi} \approx 4{,}30\text{ cm}$$

**Stap 5 (verifiëren):** $S''(r) = 4\pi + \frac{2000}{r^3} > 0$ voor elke $r>0$, dus dit kritieke punt is inderdaad een minimum.

**Stap 6 (interpreteren):** bij $r\approx4{,}30$ cm is $h = \frac{500}{\pi r^2} \approx 8{,}60$ cm. Dat zijn de afmetingen die het materiaalgebruik minimaliseren.
""",
        "summary": "Optimaliseren = model opstellen, met een nevenvoorwaarde herleiden tot één variabele, differentiëren, kritieke punten zoeken, en verifiëren dat het een echt maximum/minimum is binnen het praktische domein.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Van alle rechthoeken met omtrek 40, welke heeft de grootste oppervlakte? Geef de afmetingen.",
                "hints": [
                    "Omtrek: $2b+2h=40 \\Rightarrow h=20-b$. Oppervlakte: $A(b)=b\\cdot h = b(20-b)$.",
                    "Differentieer $A(b)$, stel gelijk aan 0, en los op naar $b$.",
                ],
                "full_solution": r"""$h=20-b$, dus $A(b) = b(20-b) = 20b - b^2$.

$A'(b) = 20-2b = 0 \implies b=10$. Dan $h=20-10=10$.

$A''(b)=-2<0$, dus dit is een maximum. De rechthoek is dus een vierkant van $10\times10$ met oppervlakte $100$.""",
                "answer_type": "open",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Een boer wil met 100 m schrikdraad een rechthoekig weiland tegen een bestaande muur afzetten (dus draad is nodig voor 3 zijden, niet voor de zijde langs de muur). Welke afmetingen maximaliseren de oppervlakte?",
                "hints": [
                    "Als $x$ de breedte loodrecht op de muur is en $y$ de lengte evenwijdig aan de muur: $2x+y=100 \\Rightarrow y=100-2x$.",
                    "Oppervlakte $A(x) = xy = x(100-2x)$. Differentieer en zoek het kritieke punt.",
                ],
                "full_solution": r"""$y=100-2x$, dus $A(x) = x(100-2x) = 100x-2x^2$.

$A'(x) = 100-4x=0 \implies x=25$. Dan $y=100-50=50$.

$A''(x)=-4<0$: maximum. Afmetingen: $25$ m (loodrecht op de muur) bij $50$ m (evenwijdig aan de muur), oppervlakte $1250$ m².""",
                "answer_type": "open",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Bepaal de afmetingen van een blik (cilinder) met inhoud $500\text{ cm}^3$ die het materiaalgebruik minimaliseert (zie het voorbeeld in de theorie, maar reproduceer de berekening zelf).",
                "hints": [
                    "Gebruik $h = \\frac{500}{\\pi r^2}$ om de oppervlakteformule $S(r) = 2\\pi r^2 + \\frac{1000}{r}$ te krijgen.",
                    "Differentieer $S(r)$, stel gelijk aan 0 en los op naar $r$ (let op: $r^3=\\ldots$).",
                ],
                "full_solution": r"""Zoals in de theorie: $S(r) = 2\pi r^2 + \frac{1000}{r}$.

$S'(r) = 4\pi r - \frac{1000}{r^2} = 0 \implies 4\pi r^3 = 1000 \implies r^3 = \frac{250}{\pi} \implies r = \sqrt[3]{250/\pi} \approx 4{,}30\text{ cm}$.

$h = \frac{500}{\pi r^2} \approx 8{,}60\text{ cm}$. Merk op: $h \approx 2r$, een bekend resultaat voor deze klassieke optimalisatie.""",
                "answer_type": "open",
            },
            {
                "order_index": 4, "difficulty": 3,
                "question": r"Bepaal het punt op de parabool $y = x^2$ dat het dichtst bij het punt $(0, 4)$ ligt.",
                "hints": [
                    "Minimaliseer het kwadraat van de afstand (dat scheelt een wortel bij het differentiëren): $D(x) = x^2 + (x^2-4)^2$.",
                    "Werk $D(x)$ uit tot een polynoom in $x$, differentieer, en los $D'(x)=0$ op.",
                ],
                "full_solution": r"""Afstand tot $(0,4)$ vanaf een punt $(x, x^2)$ op de parabool: $d = \sqrt{x^2 + (x^2-4)^2}$. Minimaliseer $D(x) = x^2+(x^2-4)^2$ (het kwadraat, dat heeft hetzelfde minimum).

$D(x) = x^2 + x^4 - 8x^2 + 16 = x^4 - 7x^2 + 16$.

$D'(x) = 4x^3 - 14x = 2x(2x^2-7) = 0 \implies x=0$ of $x^2 = 3{,}5 \implies x = \pm\sqrt{3{,}5}$.

Vergelijk functiewaarden: $D(0)=16$; $D(\pm\sqrt{3{,}5}) = 3{,}5^2\cdot... $ (reken uit: $x^2=3{,}5$, dus $D=(3{,}5)^2-7(3{,}5)+16 = 12{,}25-24{,}5+16=3{,}75$).

Het minimum ligt dus bij $x=\pm\sqrt{3{,}5}\approx\pm1{,}87$, met bijbehorend punt $(\pm1{,}87,\ 3{,}5)$ op de parabool.""",
                "answer_type": "open",
            },
        ],
    },
    {
        "module_id": 1,
        "chapter_number": 9,
        "title": "Riemannsommen en de hoofdstelling van de integraalrekening",
        "theory_content": r"""
### Nieuw terrein
Vanaf dit hoofdstuk verlaat je het "differentiëren"-deel van calculus (hellingen, veranderingssnelheden) en begin je aan het "integreren"-deel: oppervlaktes. Dit voelt in eerste instantie als een compleet ander onderwerp, tot de hoofdstelling verderop in dit hoofdstuk laat zien dat ze eigenlijk twee kanten van dezelfde medaille zijn.

### Hoe bereken je de oppervlakte onder een kromme grafiek?

Van een rechthoek of driehoek ken je de oppervlakteformule. Maar hoe pak je een gebied aan met een kromme bovenrand, zoals het gebied onder de grafiek van $f(x)=x^2$ tussen $x=0$ en $x=2$?

**Het idee: benader met rechthoekjes.** Verdeel het interval $[0,2]$ in een aantal even brede stroken, en teken op elke strook een rechthoek net zo hoog als de functiewaarde (bijvoorbeeld aan de rechterkant van de strook). De oppervlaktes van die rechthoeken zijn makkelijk te berekenen, en samen benaderen ze de werkelijke oppervlakte onder de kromme. Hoe meer (dus smallere) stroken je gebruikt, hoe beter de rechthoekjes de kromme volgen, en hoe nauwkeuriger de benadering.

### Dat precies maken

Verdeel het interval $[a,b]$ in $n$ even brede stroken van breedte $\Delta x = \frac{b-a}{n}$. Bij een **rechter-Riemannsom** gebruik je op elke strook de functiewaarde aan de rechterkant als hoogte van het rechthoekje, en tel je alle oppervlaktes op:
$$\sum_{i=1}^{n} f(x_i)\, \Delta x$$

Dit heet een **Riemannsom**: een eindige som van rechthoek-oppervlaktes, die de werkelijke oppervlakte benadert.

Nu hetzelfde spel als bij de limietdefinitie in hoofdstuk 1: laat $n \to \infty$ (de stroken oneindig dun en oneindig talrijk worden). De Riemannsom nadert dan een exacte waarde, en die waarde noemen we de **bepaalde integraal**:
$$\int_a^b f(x)\,dx = \lim_{n\to\infty} \sum_{i=1}^n f(x_i)\Delta x$$

Het integraalteken $\int$ is zelf een uitgerekte "S" van "som", een herinnering aan waar het vandaan komt.

### De hoofdstelling: het verrassende verband met differentiëren

Stel je definieert een functie $F(x)$ die de (lopende) oppervlakte bijhoudt onder de grafiek van $f$, vanaf een vast startpunt $a$ tot aan een variabele $x$: $F(x) = \int_a^x f(t)\,dt$. Als $x$ een klein stukje opschuift, groeit die oppervlakte met ongeveer $f(x)$ maal dat stukje, oftewel: de **veranderingssnelheid van de opgebouwde oppervlakte is precies $f(x)$ zelf**. Met andere woorden: $F'(x) = f(x)$, dus $F$ is een **primitieve** van $f$ (een functie waarvan $f$ de afgeleide is).

Dat is het fundamentele inzicht van de **hoofdstelling van de integraalrekening**: oppervlakte-opbouwen (integreren) en hellingen-bepalen (differentiëren) zijn elkaars tegenovergestelde bewerkingen, net zoals machtsverheffen en worteltrekken.

Dit levert een enorme rekenkundige besparing op: in plaats van eindeloze Riemannsommen uit te rekenen, hoef je alleen een primitieve $F$ van $f$ te vinden (dus een functie terug te "raden" waarvan $f$ de afgeleide is), en dan geldt:
$$\int_a^b f(x)\,dx = F(b) - F(a)$$

**Voorbeeld.** Bereken $\int_1^3 (2x+1)\,dx$.

**Stap 1.** Zoek een primitieve $F$ van $f(x)=2x+1$: welke functie heeft $2x+1$ als afgeleide? Dat is $F(x) = x^2+x$ (controleer: $\frac{d}{dx}(x^2+x) = 2x+1$ ✓).

**Stap 2.** Pas de hoofdstelling toe: $F(3)-F(1) = (9+3)-(1+1) = 12-2=10$.
""",
        "summary": "Riemannsommen benaderen oppervlakte met rechthoeken; de bepaalde integraal is de limiet daarvan. De hoofdstelling maakt exact rekenen mogelijk: zoek een primitieve $F$ en bereken $F(b)-F(a)$.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Benader $\int_0^2 x^2\,dx$ met een rechter-Riemannsom met $n=4$ rechthoeken.",
                "hints": [
                    "$\\Delta x = \\frac{2-0}{4} = 0{,}5$. De rechterpunten zijn $x=0{,}5,\\ 1,\\ 1{,}5,\\ 2$.",
                    "Bereken $f(x)=x^2$ in elk van die punten en tel op, vermenigvuldigd met $\\Delta x$.",
                ],
                "full_solution": r"""$\Delta x = 0{,}5$, rechterpunten: $0{,}5,\ 1,\ 1{,}5,\ 2$.

$f(0{,}5)=0{,}25$, $f(1)=1$, $f(1{,}5)=2{,}25$, $f(2)=4$.

Som: $(0{,}25+1+2{,}25+4)\times0{,}5 = 7{,}5\times0{,}5 = 3{,}75$.

(Ter vergelijking: de exacte waarde is $\int_0^2x^2dx = \frac{8}{3}\approx2{,}67$, de rechter-Riemannsom overschat hier omdat $x^2$ stijgend is.)""",
                "answer_type": "numeric",
                "correct_answer": "3.75",
            },
            {
                "order_index": 2, "difficulty": 1,
                "question": r"Bereken exact $\int_1^3 (2x+1)\,dx$ via de hoofdstelling.",
                "hints": [
                    "Zoek een primitieve $F(x)$ van $2x+1$.",
                    "Bereken $F(3)-F(1)$.",
                ],
                "full_solution": r"""$F(x) = x^2+x$. $F(3)-F(1) = (9+3)-(1+1) = 12-2 = 10$.""",
                "answer_type": "numeric",
                "correct_answer": "10",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Gegeven $F(x) = \int_0^x (t^2+1)\,dt$. Bepaal $F'(x)$.",
                "hints": [
                    "Dit is direct een toepassing van deel 1 van de hoofdstelling: $F'(x) = f(x)$ als $F(x)=\\int_a^x f(t)dt$.",
                    "Vervang $t$ door $x$ in de integrand.",
                ],
                "full_solution": r"""Volgens de hoofdstelling van de integraalrekening (deel 1) geldt direct:
$$F'(x) = x^2+1$$""",
                "answer_type": "expression",
                "correct_answer": "x^2+1",
            },
            {
                "order_index": 4, "difficulty": 2,
                "question": r"Bereken exact $\int_0^\pi \sin(x)\,dx$ en interpreteer het resultaat.",
                "hints": [
                    "Een primitieve van $\\sin(x)$ is $-\\cos(x)$.",
                    "Bereken $-\\cos(\\pi) - (-\\cos(0))$.",
                ],
                "full_solution": r"""$F(x)=-\cos(x)$. $F(\pi)-F(0) = -\cos(\pi)-(-\cos(0)) = -(-1)-(-1) = 1+1=2$.

Interpretatie: de oppervlakte onder één "boog" van de sinus tussen $0$ en $\pi$ (waar $\sin(x)\ge0$) is exact $2$.""",
                "answer_type": "numeric",
                "correct_answer": "2",
            },
        ],
    },
    {
        "module_id": 1,
        "chapter_number": 10,
        "title": "Integratie: de substitutiemethode",
        "theory_content": r"""
### Wat je al weet

In hoofdstuk 4 heb je de kettingregel geleerd: als $y=f(g(x))$, dan $y' = f'(g(x))\cdot g'(x)$, de afgeleide van de buitenfunctie (met binnenfunctie ingevuld) keer de afgeleide van de binnenfunctie. In hoofdstuk 9 heb je gezien dat integreren het omgekeerde is van differentiëren: een primitieve zoeken.

### Dus: hoe herken je een "reverse kettingregel"?

Als differentiëren van een samengestelde functie een extra factor $g'(x)$ oplevert (dankzij de kettingregel), dan moet integreren van zo'n uitkomst die factor $g'(x)$ juist weer "opeten". Herken je dus in een integrand een binnenfunctie én (op een constante factor na) de afgeleide van die binnenfunctie ergens los erbij staan, dan is de kans groot dat je met de kettingregel achteruit te maken hebt.

Bekijk bijvoorbeeld $\int 2x(x^2+1)^4\,dx$: hierin zit $x^2+1$ als "binnenfunctie", en $2x$ is precies de afgeleide daarvan. Dat is het signaal om **substitutie** te gebruiken: je vervangt de binnenfunctie tijdelijk door een nieuwe letter $u$, waardoor de hele integraal simpeler wordt.

### Het stappenplan

1. **Kies $u$** = de binnenfunctie (het deel van de integrand waarvan de afgeleide, op een constante na, ook aanwezig is).
2. **Bereken $du$**: differentieer $u$ naar $x$, dus $du = u'(x)\,dx$, en schrijf dit om zodat je $dx$ (of een stuk van de integrand) kunt vervangen.
3. **Herschrijf** de hele integraal volledig in termen van $u$, er mag geen $x$ meer in overblijven.
4. **Integreer** naar $u$ (vaak een simpele standaardintegraal), en substitueer aan het eind $u$ terug in termen van $x$.
5. **Bij een bepaalde integraal** kun je ook meteen de grenzen omrekenen naar $u$-grenzen, dan hoef je aan het eind niet terug te substitueren.

### Twee volledig uitgewerkte voorbeelden

**Voorbeeld 1.** Bereken $\int 2x(x^2+1)^4\,dx$.

**Stap 1.** Kies $u=x^2+1$ (de binnenfunctie onder de macht).
**Stap 2.** $du = 2x\,dx$, en die $2x\,dx$ staat toevallig precies zo in de integraal.
**Stap 3.** Vervang: de integraal wordt $\int u^4\,du$.
**Stap 4.** Integreer: $\int u^4\,du = \frac{u^5}{5}+C$, en substitueer $u=x^2+1$ terug:
$$\int 2x(x^2+1)^4\,dx = \frac{(x^2+1)^5}{5}+C$$

**Voorbeeld 2 (bepaalde integraal, grenzen omrekenen).** Bereken $\int_0^1 x\,e^{x^2}\,dx$.

**Stap 1.** Kies $u=x^2$ (de binnenfunctie in de exponent).
**Stap 2.** $du=2x\,dx$, dus $x\,dx = \frac{1}{2}du$.
**Stap 3.** Reken de grenzen meteen om: $x=0 \Rightarrow u=0$; $x=1 \Rightarrow u=1$.
**Stap 4.** Herschrijven en integreren:
$$\int_0^1 x e^{x^2}dx = \frac12\int_0^1 e^u\,du = \frac12\left[e^u\right]_0^1 = \frac12(e-1)$$
Omdat de grenzen al zijn omgerekend naar $u$-waarden, hoef je aan het eind niet meer terug te substitueren.
""",
        "summary": "Substitutie herkent een binnenfunctie-afgeleide-patroon in de integrand. Kies $u$, herschrijf $dx$ via $du$, integreer naar $u$, en substitueer terug (of reken de grenzen om bij een bepaalde integraal).",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Bereken $\displaystyle\int 2x(x^2+1)^4\,dx$.",
                "hints": [
                    "Kies $u=x^2+1$. Wat is $du$?",
                    "Na substitutie houd je $\\int u^4\\,du$ over.",
                ],
                "full_solution": r"""$u=x^2+1$, $du=2x\,dx$.
$$\int u^4\,du = \frac{u^5}{5}+C = \frac{(x^2+1)^5}{5}+C$$""",
                "answer_type": "expression",
                "correct_answer": "(x^2+1)^5/5+C",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Bereken $\displaystyle\int_0^1 x\,e^{x^2}\,dx$.",
                "hints": [
                    "Kies $u=x^2$, dan $du=2x\\,dx$, dus $x\\,dx=\\frac12 du$.",
                    "Reken de grenzen om: $x=0\\to u=0$, $x=1\\to u=1$.",
                ],
                "full_solution": r"""$u=x^2$, $du=2x\,dx \Rightarrow x\,dx = \frac12 du$. Grenzen: $u=0$ tot $u=1$.

$$\int_0^1 xe^{x^2}dx = \frac12\int_0^1 e^u\,du = \frac12[e^u]_0^1 = \frac12(e-1) \approx 0{,}859$$""",
                "answer_type": "open",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Bereken $\displaystyle\int \cos(x)\sin^3(x)\,dx$.",
                "hints": [
                    "Kies $u=\\sin(x)$, dan $du=\\cos(x)\\,dx$: precies wat er nog staat.",
                    "De integraal wordt $\\int u^3\\,du$.",
                ],
                "full_solution": r"""$u=\sin(x)$, $du=\cos(x)dx$.
$$\int u^3\,du = \frac{u^4}{4}+C = \frac{\sin^4(x)}{4}+C$$""",
                "answer_type": "expression",
                "correct_answer": "sin^4(x)/4+C",
            },
            {
                "order_index": 4, "difficulty": 3,
                "question": r"Bereken $\displaystyle\int \dfrac{x}{\sqrt{x^2+9}}\,dx$.",
                "hints": [
                    "Kies $u=x^2+9$, dan $du=2x\\,dx$, dus $x\\,dx=\\frac12 du$.",
                    "Schrijf de wortel als macht: $\\frac{1}{\\sqrt{u}}=u^{-1/2}$, en integreer $u^{-1/2}$.",
                ],
                "full_solution": r"""$u=x^2+9$, $du=2x\,dx \Rightarrow x\,dx=\frac12 du$.

$$\int \frac{x\,dx}{\sqrt{x^2+9}} = \frac12\int u^{-1/2}\,du = \frac12\cdot 2u^{1/2}+C = \sqrt{u}+C = \sqrt{x^2+9}+C$$""",
                "answer_type": "expression",
                "correct_answer": "sqrt(x^2+9)+C",
            },
        ],
    },
    {
        "module_id": 1,
        "chapter_number": 11,
        "title": "Toepassingen van integralen: oppervlakte, inhoud, booglengte",
        "theory_content": r"""
### Wat je al weet

Uit hoofdstuk 9 ken je de bepaalde integraal als limiet van een Riemannsom: een oneindig fijne opdeling van een gebied in dunne stroken, waarvan je de bijdrages optelt. Dat "dun opdelen en optellen"-recept is toepasbaar op veel meer dan alleen oppervlakte onder één grafiek. Bij elke toepassing hieronder is de aanpak steeds hetzelfde: bedenk hoe één oneindig dun plakje eruitziet, schrijf de bijdrage van dat plakje op, en integreer.

### Oppervlakte tussen twee grafieken

Stel $f(x) \ge g(x)$ op $[a,b]$. Een dun verticaal reepje op positie $x$, met breedte $dx$, heeft als hoogte het verschil $f(x)-g(x)$ (de afstand tussen de twee grafieken op die plek), dus oppervlakte $\big(f(x)-g(x)\big)\,dx$. Tel al die reepjes op via een integraal:
$$A = \int_a^b \big(f(x)-g(x)\big)\,dx$$

### Inhoud van omwentelingslichamen: de schijvenmethode

Laat het gebied onder $y=f(x)$ op $[a,b]$ ronddraaien om de $x$-as. Er ontstaat een 3D-lichaam. Snijd dat lichaam in oneindig dunne plakjes loodrecht op de $x$-as: elk plakje is bij benadering een cirkelvormige **schijf** met straal $f(x)$ en dikte $dx$, dus inhoud $\pi[f(x)]^2\,dx$ (de bekende cirkeloppervlakte $\pi r^2$, maal de dikte). Tel alle schijfjes op:
$$V = \pi\int_a^b [f(x)]^2\,dx$$

### Inhoud: de schillenmethode

Soms is het handiger om het lichaam op te delen in dunne, holle **cilinderschillen** in plaats van platte schijven, bijvoorbeeld als je om de $y$-as wentelt. Een schil op positie $x$ heeft straal $x$, hoogte $f(x)$, en dikte $dx$. Rol je die schil "plat", dan krijg je een dun rechthoekig plakje met oppervlakte (omtrek $\times$ hoogte) $= 2\pi x \cdot f(x)$, dus inhoud $2\pi x f(x)\,dx$. Tel alle schillen op:
$$V = 2\pi\int_a^b x\,f(x)\,dx$$

### Booglengte

Om de lengte van de grafiek van $y=f(x)$ te meten, bekijk je een oneindig klein stukje van de kromme tussen $x$ en $x+dx$. Over zo'n microscopisch klein stukje is de kromme praktisch recht, een piepklein rechthoekig driehoekje met basis $dx$ en hoogte $f'(x)\,dx$ (de verticale toename, via de helling). De schuine zijde (de kromme zelf) volgt dan uit Pythagoras:
$$\sqrt{(dx)^2 + (f'(x)\,dx)^2} = \sqrt{1+[f'(x)]^2}\;dx$$
Tel al die piepkleine schuine stukjes op:
$$L = \int_a^b \sqrt{1+[f'(x)]^2}\,dx$$

### Een volledig uitgewerkt voorbeeld (schijvenmethode)

**Het gebied onder $y=\sqrt{x}$, $0\le x\le4$, wentelt om de $x$-as. Bereken de inhoud.**

**Stap 1.** Herken de situatie: wentelen om de $x$-as van het gebied onder één grafiek, dus de schijvenmethode met $f(x)=\sqrt{x}$.

**Stap 2.** Stel de integraal op: $[f(x)]^2 = (\sqrt{x})^2 = x$.
$$V = \pi\int_0^4 x\,dx$$

**Stap 3.** Bereken de integraal: $\pi\left[\frac{x^2}{2}\right]_0^4 = \pi\cdot 8 = 8\pi$.
""",
        "summary": "Vlakke oppervlaktes tussen grafieken, inhoud via schijven- of schillenmethode, en booglengte zijn alle drie directe toepassingen van de bepaalde integraal: stel de juiste integrand op (op basis van een dun plakje/schijfje/schilletje) en integreer.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Bereken de oppervlakte tussen $y=x+2$ en $y=x^2$.",
                "hints": [
                    "Bepaal eerst de snijpunten: los $x+2=x^2$ op.",
                    "Welke functie ligt bovenaan tussen de snijpunten? Integreer het verschil daarvan.",
                ],
                "full_solution": r"""Snijpunten: $x^2 = x+2 \Rightarrow x^2-x-2=0 \Rightarrow (x-2)(x+1)=0 \Rightarrow x=-1$ of $x=2$.

Tussen $-1$ en $2$ geldt $x+2 \ge x^2$ (controleer bijv. bij $x=0$: $2 \ge 0$ ✓).

$$A = \int_{-1}^2 \big((x+2)-x^2\big)\,dx = \left[\frac{x^2}{2}+2x-\frac{x^3}{3}\right]_{-1}^{2}$$

Bij $x=2$: $2+4-\frac{8}{3} = 6-\frac83=\frac{10}{3}$. Bij $x=-1$: $\frac12-2+\frac13 = -\frac{7}{6}$.

$$A = \frac{10}{3}-\left(-\frac{7}{6}\right) = \frac{20}{6}+\frac{7}{6} = \frac{27}{6} = 4{,}5$$""",
                "answer_type": "numeric",
                "correct_answer": "4.5",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Het gebied onder $y=\sqrt{x}$, $0\le x\le4$, wentelt om de $x$-as. Bereken de inhoud met de schijvenmethode.",
                "hints": [
                    "$V=\\pi\\int_0^4 [f(x)]^2\\,dx$ met $f(x)=\\sqrt{x}$, dus $[f(x)]^2=x$.",
                    "Integreer $x$ van 0 tot 4.",
                ],
                "full_solution": r"""$$V = \pi\int_0^4 (\sqrt{x})^2\,dx = \pi\int_0^4 x\,dx = \pi\left[\frac{x^2}{2}\right]_0^4 = \pi\cdot8 = 8\pi \approx 25{,}1$$""",
                "answer_type": "open",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Het gebied tussen $y=x^2$ en $y=0$, $0\le x\le2$, wentelt om de $y$-as. Bereken de inhoud met de schillenmethode.",
                "hints": [
                    "$V = 2\\pi\\int_0^2 x\\,f(x)\\,dx$ met $f(x)=x^2$, dus de integrand is $x\\cdot x^2=x^3$.",
                    "Integreer $x^3$ van 0 tot 2.",
                ],
                "full_solution": r"""$$V = 2\pi\int_0^2 x\cdot x^2\,dx = 2\pi\int_0^2 x^3\,dx = 2\pi\left[\frac{x^4}{4}\right]_0^2 = 2\pi\cdot4 = 8\pi \approx 25{,}1$$""",
                "answer_type": "open",
            },
            {
                "order_index": 4, "difficulty": 3,
                "question": r"Bereken de booglengte van $y=\dfrac{2}{3}x^{3/2}$ van $x=0$ tot $x=3$.",
                "hints": [
                    "Bereken eerst $f'(x)$: $f'(x) = x^{1/2}$.",
                    "$L=\\int_0^3\\sqrt{1+[f'(x)]^2}\\,dx = \\int_0^3\\sqrt{1+x}\\,dx$. Gebruik substitutie $u=1+x$ om deze integraal te berekenen.",
                ],
                "full_solution": r"""$f(x)=\frac23x^{3/2}$, dus $f'(x) = x^{1/2} = \sqrt{x}$, en $[f'(x)]^2 = x$.

$$L = \int_0^3 \sqrt{1+x}\,dx$$

Substitutie $u=1+x$, $du=dx$, grenzen $u=1$ tot $u=4$:
$$L = \int_1^4 \sqrt{u}\,du = \left[\frac23 u^{3/2}\right]_1^4 = \frac23(8-1) = \frac{14}{3} \approx 4{,}67$$""",
                "answer_type": "open",
            },
        ],
    },
]


def upsert_chapter(module_id, chapter_number, title, theory_content="", summary="", is_placeholder=False):
    payload = {
        "module_id": module_id,
        "chapter_number": chapter_number,
        "title": title,
        "theory_content": theory_content,
        "summary": summary,
        "is_placeholder": is_placeholder,
    }
    r = http.post(
        f"{SUPABASE_URL}/rest/v1/chapters?on_conflict=chapter_number",
        headers={**HEADERS, "Prefer": "resolution=merge-duplicates,return=representation"},
        json=payload, timeout=15,
    )
    r.raise_for_status()
    return r.json()[0]["id"]


def replace_exercises(chapter_id, exercises):
    # Verwijder bestaande opgaven voor dit hoofdstuk, en zet de nieuwe erin (simpele, veilige upsert-strategie)
    http.delete(
        f"{SUPABASE_URL}/rest/v1/exercises?chapter_id=eq.{chapter_id}",
        headers=HEADERS, timeout=15,
    ).raise_for_status()

    if not exercises:
        return
    payload = []
    for ex in exercises:
        payload.append({
            "chapter_id": chapter_id,
            "order_index": ex["order_index"],
            "difficulty": ex["difficulty"],
            "question": ex["question"],
            "hints": ex["hints"],
            "full_solution": ex["full_solution"],
            "answer_type": ex["answer_type"],
            "correct_answer": ex.get("correct_answer"),
        })
    r = http.post(
        f"{SUPABASE_URL}/rest/v1/exercises",
        headers={**HEADERS, "Prefer": "return=minimal"},
        json=payload, timeout=15,
    )
    r.raise_for_status()


ALL_CHAPTERS = CHAPTERS + CHAPTERS_2


def main():
    print("Seeding volledige hoofdstukken...")
    for ch in ALL_CHAPTERS:
        chapter_id = upsert_chapter(
            ch["module_id"], ch["chapter_number"], ch["title"],
            theory_content=ch["theory_content"], summary=ch["summary"], is_placeholder=False,
        )
        replace_exercises(chapter_id, ch["exercises"])
        print(f"  H{ch['chapter_number']:>2} {ch['title'][:60]} | {len(ch['exercises'])} opgaven")

    print("Seeding placeholder-hoofdstukken (Module III-V)...")
    for module_id, chapter_number, title in PLACEHOLDER_CHAPTERS:
        upsert_chapter(module_id, chapter_number, title, is_placeholder=True)
        print(f"  H{chapter_number:>2} {title[:60]} (placeholder)")

    print("Klaar.")


if __name__ == "__main__":
    main()
