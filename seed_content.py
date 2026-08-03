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

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_SERVICE_KEY = os.environ["SUPABASE_SERVICE_KEY"]
HEADERS = {
    "Authorization": f"Bearer {SUPABASE_SERVICE_KEY}",
    "apikey": SUPABASE_SERVICE_KEY,
    "Content-Type": "application/json",
}


# ── Placeholder-titels voor hoofdstuk 12-47 (module_id, chapter_number, title) ──
PLACEHOLDER_CHAPTERS = [
    (2, 12, "Partieel integreren"),
    (2, 13, "Partieelbreuksplitsing"),
    (2, 14, "Goniometrische substitutie"),
    (2, 15, "Oneigenlijke integralen"),
    (2, 16, "Rijen en reeksen: convergentie"),
    (2, 17, "Convergentiecriteria"),
    (2, 18, "Machtreeksen"),
    (2, 19, "Taylor- en Maclaurinreeksen"),
    (2, 20, "Parametrische krommen"),
    (2, 21, "Poolcoördinaten"),
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


# ── Module I: Calculus 1 — volledig uitgewerkt ──────────────────────────────
CHAPTERS = [
    {
        "module_id": 1,
        "chapter_number": 1,
        "title": "Limieten: van intuïtief naar de formele ε-δ-definitie",
        "theory_content": r"""
In VWO B heb je limieten al informeel gezien: het gedrag van een functie als $x$ steeds dichter bij een waarde $a$ komt (bijvoorbeeld bij asymptoten). In calculus maken we dit begrip **precies**.

**Formele definitie.** We zeggen $\lim_{x \to a} f(x) = L$ als geldt: voor elke $\varepsilon > 0$ bestaat er een $\delta > 0$ zodat

$$0 < |x - a| < \delta \implies |f(x) - L| < \varepsilon$$

In woorden: hoe klein je de foutmarge $\varepsilon$ rond $L$ ook kiest, er is altijd een marge $\delta$ rond $a$ te vinden waarbinnen $f(x)$ gegarandeerd binnen die foutmarge blijft.

**Voorbeeld.** Bewijs dat $\lim_{x \to 2} (3x - 1) = 5$.

We werken $|f(x) - L|$ uit in termen van $|x - a|$:
$$|(3x - 1) - 5| = |3x - 6| = 3|x - 2|$$

We willen $3|x-2| < \varepsilon$, dus $|x - 2| < \varepsilon/3$. Kies dus $\delta = \varepsilon/3$.

**Controle:** als $0 < |x-2| < \delta = \varepsilon/3$, dan $|(3x-1)-5| = 3|x-2| < 3 \cdot \frac{\varepsilon}{3} = \varepsilon$. ✓

Bij kwadratische (of hogere-graads) functies moet je vaak eerst een extra grens op $\delta$ afspreken (bijvoorbeeld $\delta \le 1$) om een factor als $|x+a|$ te kunnen begrenzen, voordat je de uiteindelijke $\delta$ kiest. Dat zie je in opgave 4.
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
                    "Invullen geeft $0/0$ — dit is een onbepaalde vorm, geen antwoord.",
                    "Ontbind de teller in factoren: $x^2-9 = (x-3)(x+3)$, en deel weg tegen de noemer.",
                ],
                "full_solution": r"""Directe substitutie geeft $\frac{0}{0}$, een onbepaalde vorm — dat betekent niet dat de limiet niet bestaat, alleen dat je niet direct mag invullen.

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

**Stap 1 — begrens $|x+4|$:** spreek af dat $\delta \le 1$. Als $|x-4|<1$, dan $3<x<5$, dus $7<x+4<9$, dus $|x+4|<9$.

**Stap 2 — kies $\delta$:** we willen $|x-4|\cdot|x+4| < \varepsilon$. Met $|x+4|<9$ volstaat $|x-4| < \varepsilon/9$.

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
Een functie $f$ is **continu in $a$** als drie dingen kloppen: $f(a)$ bestaat, $\lim_{x\to a} f(x)$ bestaat, en beide zijn aan elkaar gelijk:
$$\lim_{x \to a} f(x) = f(a)$$

Is één van die drie voorwaarden niet vervuld, dan is $f$ discontinu (niet continu) in $a$. Er zijn grofweg drie soorten discontinuïteit:

- **Ophefbaar (removable):** de limiet bestaat wel, maar is niet gelijk aan $f(a)$, of $f(a)$ bestaat niet. Voorbeeld: $f(x) = \frac{x^2-1}{x-1}$ in $x=1$ (de factor $(x-1)$ valt weg, maar $f(1)$ is niet gedefinieerd).
- **Sprong (jump):** linker- en rechterlimiet bestaan, maar zijn ongelijk.
- **Oneindig (infinite):** de functie gaat naar $\pm\infty$, zoals $f(x)=1/x$ in $x=0$.

**Tussenwaardestelling (TWS).** Als $f$ continu is op $[a,b]$ en $y$ ligt tussen $f(a)$ en $f(b)$, dan bestaat er een $c \in [a,b]$ met $f(c) = y$. Een veelgebruikte toepassing: als $f(a)$ en $f(b)$ tegengesteld teken hebben, dan heeft $f$ minstens één nulpunt tussen $a$ en $b$.

**Voorbeeld.** Toon aan dat $f(x) = x^3 - x - 1$ een nulpunt heeft tussen $x=1$ en $x=2$.

$f$ is een polynoom, dus overal continu. $f(1) = 1-1-1 = -1 < 0$ en $f(2) = 8-2-1 = 5 > 0$. Omdat $f(1)$ en $f(2)$ tegengesteld teken hebben, is er volgens de TWS een $c \in (1,2)$ met $f(c)=0$.
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
                "full_solution": r"""$f(x) = \frac{(x-1)(x+1)}{x-1} = x+1$ voor $x\ne1$. De limiet $\lim_{x\to1} f(x) = 2$ bestaat wél, maar $f(1)$ is niet gedefinieerd (delen door 0). Dit is een **ophefbare discontinuïteit** — je kunt $f$ continu maken door $f(1):=2$ te definiëren.

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
De afgeleide van $f$ in een punt $x$ is de helling van de raaklijn aan de grafiek in dat punt. Formeel is dit een limiet van een differentiequotiënt:

$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

Dit differentiequotiënt is de richtingscoëfficiënt van de lijn door $(x, f(x))$ en $(x+h, f(x+h))$ — een **secans**. Als $h \to 0$, nadert de secans de **raaklijn**.

**Voorbeeld.** Bepaal met de definitie de afgeleide van $f(x) = x^2$.

$$f'(x) = \lim_{h\to0} \frac{(x+h)^2 - x^2}{h} = \lim_{h\to0} \frac{x^2+2xh+h^2-x^2}{h} = \lim_{h\to0} \frac{2xh+h^2}{h} = \lim_{h\to0} (2x+h) = 2x$$

Dit bevestigt de bekende regel $\frac{d}{dx}x^2 = 2x$, maar nu volledig vanuit de definitie afgeleid.

**Notatie:** $f'(x)$, $\frac{dy}{dx}$, en $\frac{d}{dx}f(x)$ betekenen allemaal hetzelfde.
""",
        "summary": "De afgeleide is een limiet van een differentiequotiënt: de helling van de secans terwijl de twee punten naar elkaar toe kruipen, tot je de helling van de raaklijn overhoudt.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Bepaal met de definitie de afgeleide van $f(x) = x^3$.",
                "hints": [
                    "Werk $(x+h)^3$ volledig uit met het binomium (of stap voor stap vermenigvuldigen).",
                    "Na uitwerken houd je een teller over die deelbaar is door $h$ — deel weg en laat $h\\to0$.",
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
                    "Je krijgt $\\frac{\\sqrt{x+h}-\\sqrt{x}}{h}$, wat direct $0/0$ geeft bij $h=0$ — vermenigvuldig teller én noemer met de toegevoegde vorm $\\sqrt{x+h}+\\sqrt{x}$.",
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
In plaats van elke keer de definitie te gebruiken, werk je in de praktijk met regels:

- **Somregel:** $(f+g)' = f' + g'$
- **Productregel:** $(fg)' = f'g + fg'$
- **Quotiëntregel:** $\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2}$
- **Kettingregel:** als $y = f(g(x))$, dan $y' = f'(g(x))\cdot g'(x)$

Standaardafgeleiden (bekend uit VWO B): $\frac{d}{dx}x^n = nx^{n-1}$, $\frac{d}{dx}e^x = e^x$, $\frac{d}{dx}\ln x = \frac{1}{x}$, $\frac{d}{dx}\sin x = \cos x$, $\frac{d}{dx}\cos x = -\sin x$.

**Voorbeeld (kettingregel).** Differentieer $f(x) = \sin(x^2)$.

Zie dit als "buitenfunctie $\sin(\cdot)$ om binnenfunctie $x^2$": $f'(x) = \cos(x^2)\cdot 2x$.

**Voorbeeld (productregel + kettingregel).** Differentieer $f(x) = x^2 e^{3x}$.

$f'(x) = 2x\cdot e^{3x} + x^2 \cdot e^{3x}\cdot 3 = e^{3x}(2x+3x^2)$.
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
                "correct_answer": "6xcos(3x^2-1)",
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
Niet elk verband tussen $x$ en $y$ is expliciet als $y=f(x)$ te schrijven (denk aan een cirkel: $x^2+y^2=25$). Bij **impliciet differentiëren** differentieer je beide kanten van de vergelijking naar $x$, waarbij je $y$ behandelt als een functie van $x$ (dus telkens de kettingregel toepassen op termen met $y$, met een factor $\frac{dy}{dx}$).

**Voorbeeld.** Bepaal $\frac{dy}{dx}$ voor $x^2+y^2=25$.

Differentieer beide kanten naar $x$:
$$2x + 2y\frac{dy}{dx} = 0 \implies \frac{dy}{dx} = -\frac{x}{y}$$

**Gerelateerde snelheden** gebruiken dezelfde techniek, maar dan met de tijd $t$ als variabele: je differentieert een vergelijking tussen grootheden naar $t$, waarbij elke grootheid een eigen "snelheid" (afgeleide naar $t$) heeft.

**Voorbeeld.** Een cirkelvormige olievlek breidt uit; de straal $r$ groeit met $2$ m/min. Hoe snel groeit de oppervlakte $A$ als $r=5$ m?

$A = \pi r^2$. Differentieer naar $t$: $\frac{dA}{dt} = 2\pi r \frac{dr}{dt}$. Invullen: $\frac{dA}{dt} = 2\pi(5)(2) = 20\pi \approx 62{,}8$ m²/min.
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
Een **kritiek punt** van $f$ is een $x$-waarde waar $f'(x)=0$ of $f'(x)$ niet bestaat. Kandidaten voor lokale extrema liggen altijd bij kritieke punten.

**Eerste-afgeleide-test:** verandert $f'$ van teken bij een kritiek punt (van $+$ naar $-$: lokaal maximum; van $-$ naar $+$: lokaal minimum)?

**Middelwaardestelling (MWS):** als $f$ continu is op $[a,b]$ en differentieerbaar op $(a,b)$, dan bestaat er een $c\in(a,b)$ met
$$f'(c) = \frac{f(b)-f(a)}{b-a}$$
Meetkundig: ergens tussen $a$ en $b$ is de raaklijn evenwijdig aan de lijn door $(a,f(a))$ en $(b,f(b))$.

**Tweede afgeleide en concaviteit:** $f''(x)>0$ betekent hol/convex (kromme "houdt water vast"), $f''(x)<0$ betekent bol/concaaf. Een **buigpunt** is waar $f''$ van teken wisselt.

**Voorbeeld — krommeonderzoek van $f(x)=x^3-3x$:** $f'(x)=3x^2-3=0 \Rightarrow x=\pm1$. $f'$ is positief buiten $[-1,1]$, negatief erbinnen: lokaal maximum in $x=-1$ ($f(-1)=2$), lokaal minimum in $x=1$ ($f(1)=-2$). $f''(x)=6x=0 \Rightarrow x=0$: buigpunt in $(0,0)$.
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
Sommige limieten geven bij directe substitutie een **onbepaalde vorm**: $\frac{0}{0}$ of $\frac{\infty}{\infty}$. De regel van De l'Hôpital zegt: als $\lim_{x\to a}\frac{f(x)}{g(x)}$ zo'n onbepaalde vorm oplevert, en $f,g$ zijn differentieerbaar rond $a$, dan geldt (mits het rechterlid bestaat):

$$\lim_{x\to a}\frac{f(x)}{g(x)} = \lim_{x\to a}\frac{f'(x)}{g'(x)}$$

**Let op:** controleer bij elke stap opnieuw of je écht een onbepaalde vorm hebt, anders mag je de regel niet toepassen.

**Voorbeeld.** $\lim_{x\to0}\frac{\sin x}{x}$. Invullen geeft $\frac{0}{0}$. De l'Hôpital: $\lim_{x\to0}\frac{\cos x}{1} = \cos(0)=1$.

**Andere onbepaalde vormen** ($0\cdot\infty$, $\infty-\infty$, $1^\infty$, $0^0$, $\infty^0$) kun je vaak herschrijven tot $\frac{0}{0}$ of $\frac{\infty}{\infty}$ om de regel toch toe te kunnen passen. Bijvoorbeeld $x\ln x$ (vorm $0\cdot\infty$ als $x\to0^+$) herschrijf je als $\frac{\ln x}{1/x}$ (vorm $\frac{-\infty}{\infty}$).
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
                    "Invullen geeft $0/0$; pas De l'Hôpital toe. Na de eerste keer differentiëren krijg je opnieuw $0/0$ — dus nogmaals toepassen.",
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
Een vast recept voor optimalisatieproblemen:

1. **Model:** vertaal de situatie naar een formule voor de te optimaliseren grootheid, meestal in twee variabelen.
2. **Nevenvoorwaarde:** gebruik een gegeven relatie om één variabele te elimineren, zodat je één functie van één variabele overhoudt.
3. **Domein:** bepaal welke waarden praktisch zinvol zijn (bijv. lengtes $>0$).
4. **Differentiëren:** bepaal de afgeleide en zoek kritieke punten.
5. **Verifiëren:** controleer met de eerste- of tweede-afgeleide-test (of door randwaarden te vergelijken) dat het inderdaad een maximum/minimum is.
6. **Interpreteren:** vertaal het wiskundige antwoord terug naar de praktijksituatie.

**Voorbeeld.** Een blik (cilinder) moet $500\text{ cm}^3$ inhoud hebben. Welke straal $r$ en hoogte $h$ minimaliseren het materiaalgebruik (totale oppervlakte)?

Inhoud: $\pi r^2 h = 500 \Rightarrow h = \frac{500}{\pi r^2}$. Oppervlakte: $S(r) = 2\pi r^2 + 2\pi r h = 2\pi r^2 + \frac{1000}{r}$.

$S'(r) = 4\pi r - \frac{1000}{r^2} = 0 \Rightarrow r^3 = \frac{1000}{4\pi} = \frac{250}{\pi} \Rightarrow r = \sqrt[3]{250/\pi} \approx 4{,}30\text{ cm}$.

Dan $h = \frac{500}{\pi r^2} \approx 8{,}60$ cm.
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
Om de oppervlakte onder een grafiek te benaderen, verdeel je het interval $[a,b]$ in $n$ even brede stroken van breedte $\Delta x = \frac{b-a}{n}$, en tel je de oppervlaktes van $n$ rechthoeken op — een **Riemannsom**. Bij een rechter-Riemannsom gebruik je de functiewaarde aan de rechterkant van elke strook:

$$\sum_{i=1}^{n} f(x_i)\, \Delta x$$

De **bepaalde integraal** is de limiet hiervan als $n\to\infty$ (de stroken oneindig dun worden):
$$\int_a^b f(x)\,dx = \lim_{n\to\infty} \sum_{i=1}^n f(x_i)\Delta x$$

**Hoofdstelling van de integraalrekening.** Als $F$ een primitieve is van $f$ (dus $F'=f$), dan:
$$\int_a^b f(x)\,dx = F(b) - F(a)$$

Dit koppelt integreren (oppervlakte) direct aan differentiëren (het omgekeerde van een afgeleide zoeken) — een fundamenteel resultaat.

**Voorbeeld.** $\int_1^3 (2x+1)\,dx$. Een primitieve is $F(x) = x^2+x$. Dan $F(3)-F(1) = (9+3)-(1+1) = 12-2=10$.
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

(Ter vergelijking: de exacte waarde is $\int_0^2x^2dx = \frac{8}{3}\approx2{,}67$ — de rechter-Riemannsom overschat hier omdat $x^2$ stijgend is.)""",
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
De substitutiemethode is het omgekeerde van de kettingregel. Als je een integraal ziet met een "binnenfunctie" en (op een constante na) de afgeleide daarvan, substitueer je $u = $ die binnenfunctie.

**Stappenplan:**
1. Kies $u$ = een geschikt deel van de integrand.
2. Bereken $du = u'(x)\,dx$ en schrijf $dx$ hierin uit.
3. Herschrijf de hele integraal in termen van $u$.
4. Integreer naar $u$, en substitueer aan het eind $u$ terug in termen van $x$.
5. **Bij een bepaalde integraal:** je kunt ook de grenzen meteen omrekenen naar $u$-grenzen, dan hoef je aan het eind niet terug te substitueren.

**Voorbeeld.** $\int 2x(x^2+1)^4\,dx$. Kies $u=x^2+1$, dan $du = 2x\,dx$. De integraal wordt $\int u^4\,du = \frac{u^5}{5}+C = \frac{(x^2+1)^5}{5}+C$.

**Voorbeeld (bepaalde integraal, grenzen omrekenen).** $\int_0^1 x\,e^{x^2}\,dx$. Kies $u=x^2$, $du=2x\,dx$, dus $x\,dx = \frac{1}{2}du$. Grenzen: $x=0\Rightarrow u=0$; $x=1\Rightarrow u=1$.
$$\int_0^1 x e^{x^2}dx = \frac12\int_0^1 e^u\,du = \frac12\left[e^u\right]_0^1 = \frac12(e-1)$$
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
                    "Kies $u=\\sin(x)$, dan $du=\\cos(x)\\,dx$ — precies wat er nog staat.",
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
**Oppervlakte tussen twee grafieken.** Als $f(x) \ge g(x)$ op $[a,b]$:
$$A = \int_a^b \big(f(x)-g(x)\big)\,dx$$

**Inhoud van omwentelingslichamen — schijvenmethode.** Als het gebied onder $y=f(x)$ op $[a,b]$ om de $x$-as wentelt:
$$V = \pi\int_a^b [f(x)]^2\,dx$$

**Inhoud — schillenmethode.** Als het gebied tussen $y=f(x)$ en de $y$-as (op $[a,b]$, $a\ge0$) om de $y$-as wentelt:
$$V = 2\pi\int_a^b x\,f(x)\,dx$$

**Booglengte.** De lengte van de grafiek van $y=f(x)$ van $x=a$ tot $x=b$:
$$L = \int_a^b \sqrt{1+[f'(x)]^2}\,dx$$

**Voorbeeld (schijvenmethode).** Het gebied onder $y=\sqrt{x}$, $0\le x\le4$, wentelt om de $x$-as.
$$V = \pi\int_0^4 (\sqrt{x})^2\,dx = \pi\int_0^4 x\,dx = \pi\left[\frac{x^2}{2}\right]_0^4 = \pi\cdot 8 = 8\pi$$
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


def main():
    print("Seeding volledige hoofdstukken (Module I)...")
    for ch in CHAPTERS:
        chapter_id = upsert_chapter(
            ch["module_id"], ch["chapter_number"], ch["title"],
            theory_content=ch["theory_content"], summary=ch["summary"], is_placeholder=False,
        )
        replace_exercises(chapter_id, ch["exercises"])
        print(f"  H{ch['chapter_number']:>2} {ch['title'][:60]} — {len(ch['exercises'])} opgaven")

    print("Seeding placeholder-hoofdstukken (Module II-V)...")
    for module_id, chapter_number, title in PLACEHOLDER_CHAPTERS:
        upsert_chapter(module_id, chapter_number, title, is_placeholder=True)
        print(f"  H{chapter_number:>2} {title[:60]} (placeholder)")

    print("Klaar.")


if __name__ == "__main__":
    main()
