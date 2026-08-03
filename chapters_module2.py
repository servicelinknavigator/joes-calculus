# -*- coding: utf-8 -*-
"""Module II: Calculus 2 (hoofdstuk 12-21), zelfde 'vanaf nul opgebouwd'-aanpak als Module I."""

CHAPTERS_2 = [
    {
        "module_id": 2,
        "chapter_number": 12,
        "title": "Partieel integreren",
        "theory_content": r"""
### Wat je al weet

In hoofdstuk 10 heb je de substitutiemethode geleerd: de kettingregel achterstevoren. Dat werkt als je een binnenfunctie en (op een constante na) zijn afgeleide bij elkaar in de integrand ziet staan.

### Wanneer substitutie vastloopt

Bekijk $\int x\,e^x\,dx$. Er is geen binnenfunctie-met-afgeleide-patroon te herkennen: $x$ is niet de afgeleide van iets bruikbaars hier, en $e^x$ is zijn eigen afgeleide. Substitutie biedt hier geen uitweg. We hebben een andere regel achterstevoren nodig: de **productregel**.

### Het idee: de productregel achterstevoren

Je kent de productregel: $(uv)' = u'v + uv'$. Integreer beide kanten naar $x$:
$$uv = \int u'v\,dx + \int uv'\,dx$$
Herschrijf dit naar de vorm die we willen gebruiken:
$$\int uv'\,dx = uv - \int u'v\,dx$$
In de gebruikelijke notatie (met $dv = v'\,dx$ en $du = u'\,dx$):
$$\int u\,dv = uv - \int v\,du$$

Dit heet **partieel integreren**. Het idee: je splitst de integrand in twee stukken, $u$ (dat je differentieert) en $dv$ (dat je integreert), in de hoop dat de nieuwe integraal $\int v\,du$ eenvoudiger is dan de oorspronkelijke.

**Vuistregel voor de keuze van $u$:** kies $u$ zo dat differentiëren het simpeler maakt (bijvoorbeeld $x \to 1$), en $dv$ zo dat je het makkelijk kunt integreren.

### Een volledig uitgewerkt voorbeeld

**Bereken $\int x\,e^x\,dx$.**

**Stap 1.** Kies $u = x$ (wordt bij differentiëren simpeler: $du = dx$) en $dv = e^x\,dx$ (makkelijk te integreren: $v = e^x$).

**Stap 2.** Pas de formule toe:
$$\int x\,e^x\,dx = x e^x - \int e^x\,dx$$

**Stap 3.** Los de nieuwe (simpelere) integraal op:
$$\int x\,e^x\,dx = x e^x - e^x + C$$
""",
        "summary": "Partieel integreren is de productregel achterstevoren: $\\int u\\,dv = uv - \\int v\\,du$. Kies $u$ zo dat differentiëren het simpeler maakt, en $dv$ zo dat integreren eenvoudig is.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Bereken $\displaystyle\int x\cos(x)\,dx$.",
                "hints": [
                    "Kies $u=x$ (dan $du=dx$) en $dv=\\cos(x)\\,dx$ (dan $v=\\sin(x)$).",
                    "Pas $\\int u\\,dv = uv - \\int v\\,du$ toe en los de resterende integraal op.",
                ],
                "full_solution": r"""$u=x,\ du=dx$; $dv=\cos(x)dx,\ v=\sin(x)$.
$$\int x\cos(x)\,dx = x\sin(x) - \int \sin(x)\,dx = x\sin(x) + \cos(x) + C$$""",
                "answer_type": "expression",
                "correct_answer": "x*sin(x)+cos(x)+C",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Bereken $\displaystyle\int \ln(x)\,dx$.",
                "hints": [
                    "Dit lijkt geen product, maar je kunt schrijven $\\ln(x) = \\ln(x)\\cdot 1$. Kies $u=\\ln(x)$ en $dv=dx$.",
                    "Dan is $du = \\frac{1}{x}dx$ en $v=x$. Werk $\\int v\\,du$ uit, dat versimpelt tot een standaardintegraal.",
                ],
                "full_solution": r"""$u=\ln(x),\ du=\frac{1}{x}dx$; $dv=dx,\ v=x$.
$$\int \ln(x)\,dx = x\ln(x) - \int x\cdot\frac{1}{x}\,dx = x\ln(x) - \int 1\,dx = x\ln(x) - x + C$$""",
                "answer_type": "expression",
                "correct_answer": "x*ln(x)-x+C",
            },
            {
                "order_index": 3, "difficulty": 3,
                "question": r"Bereken $\displaystyle\int x^2 e^x\,dx$.",
                "hints": [
                    "Kies $u=x^2$ en $dv=e^x dx$. Na de eerste toepassing houd je $\\int x e^x dx$ over, dat ken je al uit de uitleg vooraf.",
                    "Pas partieel integreren dus twee keer na elkaar toe.",
                ],
                "full_solution": r"""Eerste keer: $u=x^2,\ du=2x\,dx$; $dv=e^x dx,\ v=e^x$.
$$\int x^2 e^x\,dx = x^2 e^x - \int 2x\,e^x\,dx = x^2e^x - 2\int x e^x\,dx$$
Uit de theorie weten we $\int xe^x dx = xe^x - e^x + C$. Invullen:
$$\int x^2 e^x\,dx = x^2 e^x - 2(xe^x - e^x) + C = e^x(x^2 - 2x + 2) + C$$""",
                "answer_type": "open",
            },
            {
                "order_index": 4, "difficulty": 3,
                "question": r"Bereken $\displaystyle\int x\sin(2x)\,dx$.",
                "hints": [
                    "Kies $u=x$ en $dv=\\sin(2x)dx$. Let op de kettingregel bij het bepalen van $v$: een primitieve van $\\sin(2x)$ is $-\\frac12\\cos(2x)$.",
                    "Werk $\\int v\\,du$ verder uit tot een standaardintegraal.",
                ],
                "full_solution": r"""$u=x,\ du=dx$; $dv=\sin(2x)dx,\ v=-\frac12\cos(2x)$.
$$\int x\sin(2x)\,dx = -\frac{x}{2}\cos(2x) - \int -\frac12\cos(2x)\,dx = -\frac{x}{2}\cos(2x) + \frac12\int\cos(2x)\,dx$$
$$= -\frac{x}{2}\cos(2x) + \frac14\sin(2x) + C$$""",
                "answer_type": "open",
            },
        ],
    },
    {
        "module_id": 2,
        "chapter_number": 13,
        "title": "Partieelbreuksplitsing",
        "theory_content": r"""
### Wat je al weet

Je kunt integralen als $\int \frac{1}{x}dx = \ln|x|+C$ direct oplossen. Maar een breuk als $\dfrac{3x+5}{(x-1)(x+2)}$ heeft geen directe standaardvorm, en substitutie of partieel integreren bieden hier geen makkelijke uitweg.

### Het idee: een ingewikkelde breuk terugbrengen tot simpele breuken

De truc is de omgekeerde weg van "breuken optellen": net zoals $\frac{1}{x-1} + \frac{1}{x+2}$ samen tot één breuk met noemer $(x-1)(x+2)$ te herleiden is, kun je een breuk met die noemer weer **uit elkaar trekken** in twee simpele breuken, elk met een lineaire noemer. Simpele breuken zoals $\frac{A}{x-1}$ zijn direct te integreren tot $A\ln|x-1|$.

### De methode

Voor $\dfrac{3x+5}{(x-1)(x+2)}$ zoek je constanten $A$ en $B$ zodat:
$$\frac{3x+5}{(x-1)(x+2)} = \frac{A}{x-1} + \frac{B}{x+2}$$
Vermenigvuldig beide kanten met $(x-1)(x+2)$ om de noemers weg te werken:
$$3x+5 = A(x+2) + B(x-1)$$
Deze gelijkheid moet voor **elke** $x$ gelden, dus mag je slimme waarden van $x$ invullen om $A$ en $B$ snel te vinden: vul $x=1$ in (dan valt de $B$-term weg) en $x=-2$ in (dan valt de $A$-term weg).

### Een volledig uitgewerkt voorbeeld

**Bereken $\displaystyle\int \frac{3x+5}{(x-1)(x+2)}\,dx$.**

**Stap 1.** Stel de splitsing op: $3x+5 = A(x+2) + B(x-1)$.

**Stap 2.** Vul $x=1$ in: $3(1)+5 = A(1+2) \Rightarrow 8 = 3A \Rightarrow A = \frac{8}{3}$.

**Stap 3.** Vul $x=-2$ in: $3(-2)+5 = B(-2-1) \Rightarrow -1 = -3B \Rightarrow B = \frac{1}{3}$.

**Stap 4.** Integreer de twee simpele breuken apart:
$$\int \frac{3x+5}{(x-1)(x+2)}\,dx = \frac{8}{3}\ln|x-1| + \frac{1}{3}\ln|x+2| + C$$
""",
        "summary": "Partieelbreuksplitsing schrijft een breuk met een product van lineaire factoren in de noemer als een som van simpele breuken. Vind de constanten door slimme $x$-waarden in te vullen, en integreer elke simpele breuk apart tot een logaritme.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Bereken $\displaystyle\int \frac{1}{(x-1)(x+3)}\,dx$.",
                "hints": [
                    "Stel $\\frac{1}{(x-1)(x+3)} = \\frac{A}{x-1}+\\frac{B}{x+3}$, dus $1 = A(x+3)+B(x-1)$.",
                    "Vul $x=1$ en $x=-3$ in om $A$ en $B$ te vinden.",
                ],
                "full_solution": r"""$1=A(x+3)+B(x-1)$. $x=1: 1=4A \Rightarrow A=\frac14$. $x=-3: 1=-4B \Rightarrow B=-\frac14$.
$$\int \frac{1}{(x-1)(x+3)}\,dx = \frac14\ln|x-1| - \frac14\ln|x+3| + C$$""",
                "answer_type": "open",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Bereken $\displaystyle\int \frac{5x-1}{x^2-x-2}\,dx$.",
                "hints": [
                    "Ontbind eerst de noemer: $x^2-x-2 = (x-2)(x+1)$.",
                    "Stel $5x-1 = A(x+1)+B(x-2)$ en vul $x=2$ en $x=-1$ in.",
                ],
                "full_solution": r"""$x^2-x-2=(x-2)(x+1)$. $5x-1=A(x+1)+B(x-2)$. $x=2: 9=3A \Rightarrow A=3$. $x=-1: -6=-3B \Rightarrow B=2$.
$$\int \frac{5x-1}{x^2-x-2}\,dx = 3\ln|x-2| + 2\ln|x+1| + C$$""",
                "answer_type": "open",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Bereken $\displaystyle\int \frac{x+3}{x^2+x}\,dx$.",
                "hints": [
                    "Ontbind de noemer: $x^2+x = x(x+1)$.",
                    "Stel $x+3 = A(x+1)+Bx$ en vul $x=0$ en $x=-1$ in.",
                ],
                "full_solution": r"""$x^2+x=x(x+1)$. $x+3=A(x+1)+Bx$. $x=0: 3=A$. $x=-1: 2=-B \Rightarrow B=-2$.
$$\int \frac{x+3}{x^2+x}\,dx = 3\ln|x| - 2\ln|x+1| + C$$""",
                "answer_type": "open",
            },
            {
                "order_index": 4, "difficulty": 3,
                "question": r"Bereken $\displaystyle\int \frac{1}{x(x-1)^2}\,dx$.",
                "hints": [
                    "Bij een dubbele factor $(x-1)^2$ heb je twee termen nodig: stel $\\frac{1}{x(x-1)^2} = \\frac{A}{x}+\\frac{B}{x-1}+\\frac{C}{(x-1)^2}$.",
                    "Vermenigvuldig weg tot $1=A(x-1)^2+Bx(x-1)+Cx$, en vul $x=0$ en $x=1$ in voor $A$ en $C$. Vergelijk daarna de coëfficiënt van $x^2$ (die moet $0$ zijn) om $B$ te vinden.",
                ],
                "full_solution": r"""$1 = A(x-1)^2 + Bx(x-1) + Cx$.

$x=0$: $1 = A \cdot 1 \Rightarrow A=1$.
$x=1$: $1 = C \cdot 1 \Rightarrow C=1$.
Coëfficiënt van $x^2$ links is $0$; rechts is dat $A+B$, dus $A+B=0 \Rightarrow B=-1$.

$$\int \frac{1}{x(x-1)^2}\,dx = \ln|x| - \ln|x-1| - \frac{1}{x-1} + C$$
(want $\int \frac{1}{(x-1)^2}dx = -\frac{1}{x-1}$).""",
                "answer_type": "open",
            },
        ],
    },
    {
        "module_id": 2,
        "chapter_number": 14,
        "title": "Goniometrische substitutie",
        "theory_content": r"""
### Wat je al weet

Substitutie (hoofdstuk 10) vervangt een deel van de integrand door een nieuwe variabele $u$ om de integraal te versimpelen. Ook ken je de identiteit $\sin^2(\theta)+\cos^2(\theta)=1$ en de afgeleiden van sin, cos en tan.

### Het probleem: wortels die niet weg willen

Bekijk $\int \dfrac{dx}{\sqrt{4-x^2}}$. Er zit geen bruikbare binnenfunctie-afgeleide-combinatie in, dus gewone substitutie werkt niet. Het probleem zit 'm in de wortel $\sqrt{4-x^2}$.

### Het idee: vervang x door een goniometrische functie

Als je $x = 2\sin(\theta)$ kiest, dan wordt $4 - x^2 = 4 - 4\sin^2(\theta) = 4(1-\sin^2(\theta)) = 4\cos^2(\theta)$, en de wortel wordt simpelweg $2\cos(\theta)$ (geen wortelteken meer!). Dit werkt dankzij de identiteit $1-\sin^2=\cos^2$.

Er zijn drie standaardgevallen, elk gekoppeld aan een goniometrische identiteit die de wortel laat verdwijnen:

| Vorm in de integrand | Substitutie | Identiteit die de wortel wegwerkt |
|---|---|---|
| $\sqrt{a^2-x^2}$ | $x=a\sin(\theta)$ | $1-\sin^2=\cos^2$ |
| $\sqrt{a^2+x^2}$ | $x=a\tan(\theta)$ | $1+\tan^2=\sec^2$ |
| $\sqrt{x^2-a^2}$ | $x=a\sec(\theta)$ | $\sec^2-1=\tan^2$ |

### Een volledig uitgewerkt voorbeeld

**Bereken $\displaystyle\int \frac{dx}{\sqrt{4-x^2}}$.**

**Stap 1.** Herken het type: $\sqrt{a^2-x^2}$ met $a=2$, dus substitueer $x=2\sin(\theta)$, met $dx = 2\cos(\theta)\,d\theta$.

**Stap 2.** Werk de wortel weg: $\sqrt{4-x^2} = \sqrt{4-4\sin^2(\theta)} = 2\cos(\theta)$.

**Stap 3.** Substitueer alles in de integraal:
$$\int \frac{2\cos(\theta)\,d\theta}{2\cos(\theta)} = \int 1\,d\theta = \theta + C$$

**Stap 4.** Substitueer terug: uit $x=2\sin(\theta)$ volgt $\theta = \arcsin(x/2)$.
$$\int \frac{dx}{\sqrt{4-x^2}} = \arcsin\left(\frac{x}{2}\right) + C$$
""",
        "summary": "Goniometrische substitutie vervangt $x$ door $a\\sin\\theta$, $a\\tan\\theta$ of $a\\sec\\theta$ om een wortel met $a^2\\pm x^2$ weg te werken, met behulp van de identiteiten $1-\\sin^2=\\cos^2$ en $1+\\tan^2=\\sec^2$. Na integreren naar $\\theta$ substitueer je terug naar $x$.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Bereken $\displaystyle\int \frac{dx}{\sqrt{25-x^2}}$.",
                "hints": [
                    "Herken de vorm $\\sqrt{a^2-x^2}$ met $a=5$: substitueer $x=5\\sin(\\theta)$.",
                    "Dit is exact hetzelfde stramien als het voorbeeld in de theorie, alleen met $a=5$ in plaats van $a=2$.",
                ],
                "full_solution": r"""$x=5\sin(\theta)$, $dx=5\cos(\theta)d\theta$, $\sqrt{25-x^2}=5\cos(\theta)$.
$$\int \frac{5\cos(\theta)\,d\theta}{5\cos(\theta)} = \int 1\,d\theta = \theta + C = \arcsin\left(\frac{x}{5}\right) + C$$""",
                "answer_type": "expression",
                "correct_answer": "asin(x/5)+C",
            },
            {
                "order_index": 2, "difficulty": 3,
                "question": r"Bereken $\displaystyle\int \sqrt{9-x^2}\,dx$.",
                "hints": [
                    "Substitueer $x=3\\sin(\\theta)$, $dx=3\\cos(\\theta)d\\theta$, zodat $\\sqrt{9-x^2}=3\\cos(\\theta)$.",
                    "Je krijgt $9\\int\\cos^2(\\theta)\\,d\\theta$. Gebruik de identiteit $\\cos^2(\\theta)=\\frac{1+\\cos(2\\theta)}{2}$, en substitueer aan het eind terug met $\\sin(\\theta)=x/3$ en $\\cos(\\theta)=\\sqrt{9-x^2}/3$.",
                ],
                "full_solution": r"""$x=3\sin(\theta)$, $dx=3\cos(\theta)d\theta$, $\sqrt{9-x^2}=3\cos(\theta)$.
$$\int 3\cos(\theta)\cdot 3\cos(\theta)\,d\theta = 9\int \cos^2(\theta)\,d\theta = 9\int \frac{1+\cos(2\theta)}{2}\,d\theta = \frac{9}{2}\theta + \frac{9}{4}\sin(2\theta) + C$$
Met $\sin(2\theta)=2\sin(\theta)\cos(\theta)$: $\frac{9}{4}\sin(2\theta) = \frac{9}{2}\sin(\theta)\cos(\theta)$. Terugsubstitueren ($\theta=\arcsin(x/3)$, $\sin\theta=x/3$, $\cos\theta=\sqrt{9-x^2}/3$):
$$\int \sqrt{9-x^2}\,dx = \frac{9}{2}\arcsin\left(\frac{x}{3}\right) + \frac{x\sqrt{9-x^2}}{2} + C$$""",
                "answer_type": "open",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Bereken $\displaystyle\int \frac{dx}{\sqrt{x^2+16}}$.",
                "hints": [
                    "Herken de vorm $\\sqrt{a^2+x^2}$ met $a=4$: substitueer $x=4\\tan(\\theta)$, met $1+\\tan^2(\\theta)=\\sec^2(\\theta)$.",
                    "Je krijgt $\\int \\sec(\\theta)\\,d\\theta = \\ln|\\sec\\theta+\\tan\\theta|+C$ (een bekende standaardintegraal). Substitueer terug met $\\tan\\theta=x/4$ en $\\sec\\theta=\\sqrt{x^2+16}/4$.",
                ],
                "full_solution": r"""$x=4\tan(\theta)$, $dx=4\sec^2(\theta)d\theta$, $\sqrt{x^2+16}=4\sec(\theta)$.
$$\int \frac{4\sec^2(\theta)\,d\theta}{4\sec(\theta)} = \int \sec(\theta)\,d\theta = \ln|\sec(\theta)+\tan(\theta)| + C$$
Terugsubstitueren: $\tan\theta = x/4$, $\sec\theta = \sqrt{x^2+16}/4$.
$$= \ln\left|\frac{\sqrt{x^2+16}+x}{4}\right| + C = \ln\left(\sqrt{x^2+16}+x\right) + C'$$
(de constante $-\ln 4$ wordt opgenomen in $C'$).""",
                "answer_type": "open",
            },
            {
                "order_index": 4, "difficulty": 3,
                "question": r"Bereken $\displaystyle\int \frac{dx}{x^2\sqrt{x^2+9}}$.",
                "hints": [
                    "Substitueer $x=3\\tan(\\theta)$, $dx=3\\sec^2(\\theta)d\\theta$, $\\sqrt{x^2+9}=3\\sec(\\theta)$.",
                    "Na invullen en vereenvoudigen (gebruik $\\sec/\\tan^2 = \\cos/\\sin^2$) krijg je een integraal die je met $w=\\sin(\\theta)$ kunt oplossen. Substitueer aan het eind terug met $\\sin(\\theta)=x/\\sqrt{x^2+9}$.",
                ],
                "full_solution": r"""$x=3\tan(\theta)$, $dx=3\sec^2(\theta)d\theta$, $\sqrt{x^2+9}=3\sec(\theta)$, $x^2=9\tan^2(\theta)$.
$$\int \frac{3\sec^2(\theta)\,d\theta}{9\tan^2(\theta)\cdot 3\sec(\theta)} = \frac{1}{9}\int \frac{\sec(\theta)}{\tan^2(\theta)}\,d\theta = \frac{1}{9}\int \frac{\cos(\theta)}{\sin^2(\theta)}\,d\theta$$
Substitutie $w=\sin(\theta)$, $dw=\cos(\theta)d\theta$:
$$\frac{1}{9}\int \frac{dw}{w^2} = -\frac{1}{9w} + C = -\frac{1}{9\sin(\theta)} + C$$
Terugsubstitueren: in de driehoek met $\tan\theta=x/3$ is de overstaande zijde $x$, de aanliggende $3$, de schuine zijde $\sqrt{x^2+9}$, dus $\sin\theta = \dfrac{x}{\sqrt{x^2+9}}$.
$$\int \frac{dx}{x^2\sqrt{x^2+9}} = -\frac{\sqrt{x^2+9}}{9x} + C$$""",
                "answer_type": "open",
            },
        ],
    },
    {
        "module_id": 2,
        "chapter_number": 15,
        "title": "Oneigenlijke integralen",
        "theory_content": r"""
### Wat je al weet

Een bepaalde integraal $\int_a^b f(x)\,dx$ berekent de oppervlakte over een eindig interval $[a,b]$, met een gewone (eindige) functie.

### Wat als het interval oneindig is, of de functie onbegrensd?

Kan een oneindig lang gebied toch een eindige oppervlakte hebben? Denk aan een strook die steeds smaller wordt terwijl hij oneindig doorloopt, het is heel goed mogelijk dat de opgetelde oppervlakte toch naar een eindige waarde nadert. Om dat precies te maken, gebruiken we hetzelfde soort limiet-truc als bij Riemannsommen in hoofdstuk 9: reken eerst tot een eindige grens $b$, en laat daarna $b\to\infty$.

### De definitie

$$\int_a^\infty f(x)\,dx = \lim_{b\to\infty} \int_a^b f(x)\,dx$$

Bestaat deze limiet (is hij een eindig getal), dan heet de integraal **convergent**, en die limietwaarde is de "oppervlakte". Bestaat de limiet niet (gaat hij naar $\pm\infty$), dan heet de integraal **divergent**.

Hetzelfde idee werkt als de **functie zelf** onbegrensd is ergens in het interval (bijvoorbeeld een verticale asymptoot bij een van de grenzen): dan neem je de limiet van de grens die naar het probleempunt toe kruipt.

### Een volledig uitgewerkt voorbeeld

**Onderzoek of $\displaystyle\int_1^\infty \frac{1}{x^2}\,dx$ convergeert, en bereken de waarde als dat zo is.**

**Stap 1.** Schrijf als limiet: $\displaystyle\int_1^\infty \frac{1}{x^2}\,dx = \lim_{b\to\infty}\int_1^b x^{-2}\,dx$.

**Stap 2.** Bereken de gewone bepaalde integraal: $\displaystyle\int_1^b x^{-2}\,dx = \left[-\frac{1}{x}\right]_1^b = -\frac{1}{b} + 1$.

**Stap 3.** Neem de limiet: $\displaystyle\lim_{b\to\infty}\left(1 - \frac{1}{b}\right) = 1 - 0 = 1$.

De integraal is dus convergent, met waarde $1$: een oneindig lang gebied met een eindige oppervlakte.
""",
        "summary": "Een oneigenlijke integraal (oneindig interval of onbegrensde functie) wordt gedefinieerd als een limiet van gewone bepaalde integralen. Bestaat die limiet (eindig), dan is de integraal convergent; anders divergent.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Bereken $\displaystyle\int_1^\infty \frac{1}{x^3}\,dx$, of laat zien dat de integraal divergeert.",
                "hints": [
                    "Schrijf als $\\lim_{b\\to\\infty}\\int_1^b x^{-3}dx$.",
                    "Bereken eerst de bepaalde integraal in termen van $b$, en neem daarna de limiet.",
                ],
                "full_solution": r"""$$\int_1^b x^{-3}dx = \left[-\frac{1}{2x^2}\right]_1^b = -\frac{1}{2b^2}+\frac12$$
$$\lim_{b\to\infty}\left(\frac12 - \frac{1}{2b^2}\right) = \frac12$$
Convergent, waarde $\frac12$.""",
                "answer_type": "numeric",
                "correct_answer": "1/2",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Bewijs dat $\displaystyle\int_1^\infty \frac{1}{x}\,dx$ divergeert.",
                "hints": [
                    "Schrijf als $\\lim_{b\\to\\infty}\\int_1^b \\frac{1}{x}dx$ en bereken de primitieve ($\\ln|x|$).",
                    "Wat gebeurt er met $\\ln(b)$ als $b\\to\\infty$?",
                ],
                "full_solution": r"""$$\int_1^b \frac{1}{x}dx = [\ln|x|]_1^b = \ln(b) - \ln(1) = \ln(b)$$
$$\lim_{b\to\infty} \ln(b) = \infty$$
De limiet bestaat niet (is oneindig), dus de integraal is **divergent**. Vergelijk dit met opgave 1: ondanks dat $1/x$ en $1/x^3$ er op het oog vergelijkbaar uitzien, gedraagt $1/x$ zich anders, hij neemt niet snel genoeg af.""",
                "answer_type": "open",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Bereken $\displaystyle\int_0^1 \frac{1}{\sqrt{x}}\,dx$ (let op: de integrand is onbegrensd bij $x=0$).",
                "hints": [
                    "Schrijf als $\\lim_{a\\to 0^+}\\int_a^1 x^{-1/2}dx$, omdat het probleem bij de ondergrens zit.",
                    "Bereken de bepaalde integraal in termen van $a$, en laat $a\\to 0^+$.",
                ],
                "full_solution": r"""$$\int_a^1 x^{-1/2}dx = \left[2\sqrt{x}\right]_a^1 = 2 - 2\sqrt{a}$$
$$\lim_{a\to0^+}\left(2-2\sqrt{a}\right) = 2$$
Convergent, waarde $2$, ondanks dat de functie zelf onbegrensd is bij $x=0$.""",
                "answer_type": "numeric",
                "correct_answer": "2",
            },
            {
                "order_index": 4, "difficulty": 1,
                "question": r"Bereken $\displaystyle\int_{-\infty}^0 e^x\,dx$.",
                "hints": [
                    "Schrijf als $\\lim_{a\\to-\\infty}\\int_a^0 e^x dx$.",
                    "Wat gebeurt er met $e^a$ als $a\\to-\\infty$?",
                ],
                "full_solution": r"""$$\int_a^0 e^x dx = [e^x]_a^0 = 1 - e^a$$
$$\lim_{a\to-\infty}(1-e^a) = 1 - 0 = 1$$
Convergent, waarde $1$.""",
                "answer_type": "numeric",
                "correct_answer": "1",
            },
        ],
    },
    {
        "module_id": 2,
        "chapter_number": 16,
        "title": "Rijen en reeksen: convergentie",
        "theory_content": r"""
### Een oneindige som die toch eindig is

Stel je hebt een taart. Je eet de helft op. Morgen eet je de helft van wat overblijft (dus een kwart van de hele taart). Overmorgen weer de helft van de rest (een achtste), enzovoort, voor altijd. Hoeveel taart heb je in totaal opgegeten na oneindig veel dagen?

$$\frac12 + \frac14 + \frac18 + \frac{1}{16} + \cdots$$

Intuïtief: de hele taart, natuurlijk (je blijft immers eeuwig kleine stukjes van de rest opeten, en de rest wordt steeds verwaarloosbaarder). Dit is de kern van dit hoofdstuk: een **oneindige som** kan wel degelijk een eindige, precieze waarde hebben.

### Rijen

Een **rij** is een oneindige geordende lijst getallen $a_1, a_2, a_3, \ldots$, meestal gegeven door een formule $a_n$. Een rij heeft een **limiet** $L$ als $a_n$ willekeurig dicht bij $L$ komt naarmate $n\to\infty$, exact zoals de limieten uit hoofdstuk 1, maar nu met een geheel getal $n$ die naar oneindig loopt in plaats van een reëel getal $x$ die naar een punt $a$ kruipt.

### Reeksen en partiële sommen

Een **reeks** is de opgetelde som van een rij: $\sum_{n=1}^\infty a_n$. Om precies te maken wat zo'n oneindige som betekent, kijk je naar de **partiële som** $S_N = a_1+a_2+\cdots+a_N$ (de som van de eerste $N$ termen, een gewoon, eindig getal). De reeks **convergeert** naar $S$ als $\lim_{N\to\infty} S_N = S$.

### De meetkundige reeks

Het taart-voorbeeld is een **meetkundige reeks**: elke term is de vorige keer een vaste factor $r$ (hier $r=\frac12$). Voor $\sum_{n=0}^\infty ar^n$ (beginwaarde $a$, reden $r$) geldt, mits $|r|<1$:
$$\sum_{n=0}^\infty ar^n = \frac{a}{1-r}$$
Voor het taart-voorbeeld: $a=\frac12$, $r=\frac12$, dus $\frac{1/2}{1-1/2} = 1$: de hele taart, precies zoals de intuïtie voorspelde.

### Wanneer een reeks zeker niet convergeert

Als de termen $a_n$ zelf niet naar $0$ gaan, kan de som onmogelijk naar een eindige waarde convergeren (je blijft dan immers steeds ongeveer evenveel toevoegen). Dit heet de **divergentietest**: als $\lim_{n\to\infty} a_n \ne 0$ (of de limiet bestaat niet), dan is $\sum a_n$ divergent.
""",
        "summary": "Een reeks convergeert als de rij partiële sommen een eindige limiet heeft. De meetkundige reeks $\\sum ar^n = \\frac{a}{1-r}$ voor $|r|<1$. Gaan de termen zelf niet naar 0, dan is de reeks gegarandeerd divergent (divergentietest).",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Bepaal $\displaystyle\lim_{n\to\infty} \frac{2n+1}{n+3}$.",
                "hints": [
                    "Deel teller en noemer door de hoogste macht van $n$ die voorkomt, hier $n$.",
                    "Wat gebeurt er met termen als $\\frac{1}{n}$ en $\\frac{3}{n}$ als $n\\to\\infty$?",
                ],
                "full_solution": r"""$$\frac{2n+1}{n+3} = \frac{2+\frac1n}{1+\frac3n} \xrightarrow{n\to\infty} \frac{2+0}{1+0} = 2$$""",
                "answer_type": "numeric",
                "correct_answer": "2",
            },
            {
                "order_index": 2, "difficulty": 1,
                "question": r"Bereken de som van de meetkundige reeks $\displaystyle\sum_{n=0}^\infty 3\left(\frac12\right)^n$.",
                "hints": [
                    "Herken $a=3$ en $r=\\frac12$ in de formule $\\sum ar^n = \\frac{a}{1-r}$.",
                    "Controleer dat $|r|<1$, zodat de formule geldig is.",
                ],
                "full_solution": r"""$a=3$, $r=\frac12$, $|r|<1$.
$$\sum_{n=0}^\infty 3\left(\frac12\right)^n = \frac{3}{1-\frac12} = \frac{3}{\frac12} = 6$$""",
                "answer_type": "numeric",
                "correct_answer": "6",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Onderzoek of $\displaystyle\sum_{n=1}^\infty \frac{n}{n+1}$ convergeert.",
                "hints": [
                    "Bereken $\\lim_{n\\to\\infty} \\frac{n}{n+1}$ (deel teller en noemer door $n$).",
                    "Gebruik de divergentietest: als de termen niet naar 0 gaan, kan de reeks niet convergeren.",
                ],
                "full_solution": r"""$$\lim_{n\to\infty}\frac{n}{n+1} = \lim_{n\to\infty}\frac{1}{1+\frac1n} = 1 \ne 0$$
Omdat de termen niet naar $0$ gaan, is de reeks volgens de divergentietest **divergent**.""",
                "answer_type": "open",
            },
            {
                "order_index": 4, "difficulty": 2,
                "question": r"Bereken $\displaystyle\sum_{n=1}^\infty \left(\frac13\right)^n$.",
                "hints": [
                    "Let op: deze som begint bij $n=1$, niet bij $n=0$. Schrijf de eerste term expliciet uit om $a$ te herkennen.",
                    "$a = \\left(\\frac13\\right)^1 = \\frac13$, en $r=\\frac13$.",
                ],
                "full_solution": r"""Eerste term ($n=1$): $a=\frac13$. Reden $r=\frac13$.
$$\sum_{n=1}^\infty \left(\frac13\right)^n = \frac{1/3}{1-1/3} = \frac{1/3}{2/3} = \frac12$$""",
                "answer_type": "numeric",
                "correct_answer": "1/2",
            },
        ],
    },
    {
        "module_id": 2,
        "chapter_number": 17,
        "title": "Convergentiecriteria",
        "theory_content": r"""
### Wat je al weet

Bij een meetkundige reeks (hoofdstuk 16) ken je een exacte formule voor de som. Bij de meeste andere reeksen bestaat zo'n formule niet, je kunt de exacte som vaak niet uitrekenen. Gelukkig is dat vaak niet eens nodig: meestal wil je alleen weten óf een reeks convergeert, niet wat de exacte waarde is. Daarvoor bestaan **convergentiecriteria** (tests) die je kunt toepassen zonder de som te hoeven berekenen.

**Parate kennis:** de reeks $\sum \frac{1}{n^2}$ is bekend convergent, en de **harmonische reeks** $\sum \frac{1}{n}$ is bekend divergent (zie opgave 4). Deze twee reeksen worden vaak als vergelijkingsmateriaal gebruikt.

### De vergelijkingstest

Idee: als je reeks term-voor-term kleiner is dan een reeks waarvan je al weet dat hij convergeert, dan moet jouw reeks ook convergeren (hij "past eronder"). Formeel: als $0 \le a_n \le b_n$ voor alle (grote genoeg) $n$, en $\sum b_n$ convergeert, dan convergeert $\sum a_n$ ook.

### De verhoudingstest

Bekijk de verhouding tussen opeenvolgende termen, $\dfrac{a_{n+1}}{a_n}$, en laat $n\to\infty$. Wordt die limiet $L$ kleiner dan $1$, dan krimpen de termen uiteindelijk sneller dan een meetkundige reeks met reden $<1$, en convergeert de reeks. Wordt $L>1$, dan groeien de termen juist en divergeert de reeks.

$$L = \lim_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|: \quad L<1 \Rightarrow \text{convergent}, \quad L>1 \Rightarrow \text{divergent}$$

### Een volledig uitgewerkt voorbeeld

**Onderzoek de convergentie van $\displaystyle\sum_{n=1}^\infty \frac{1}{n^2+3}$.**

**Stap 1.** Vergelijk met de bekende convergente reeks $\sum \frac{1}{n^2}$: voor elke $n\ge1$ geldt $n^2+3 > n^2$, dus $\dfrac{1}{n^2+3} < \dfrac{1}{n^2}$.

**Stap 2.** Omdat $\sum \frac{1}{n^2}$ convergent is en onze reeks term-voor-term kleiner is (en positief), is $\sum \frac{1}{n^2+3}$ volgens de vergelijkingstest ook **convergent**.
""",
        "summary": "De vergelijkingstest vergelijkt een reeks met een bekende (convergente of divergente) reeks. De verhoudingstest kijkt naar $\\lim |a_{n+1}/a_n|$: kleiner dan 1 betekent convergent, groter dan 1 betekent divergent.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Onderzoek de convergentie van $\displaystyle\sum_{n=1}^\infty \frac{1}{n^2+3}$ zelf, op dezelfde manier als het voorbeeld in de theorie (reproduceer de redenering).",
                "hints": [
                    "Vergelijk met $\\sum \\frac{1}{n^2}$.",
                    "Voor welke reeks is $\\frac{1}{n^2+3}$ term-voor-term kleiner, en wat weet je al van die reeks?",
                ],
                "full_solution": r"""Voor elke $n\ge1$ geldt $n^2+3>n^2$, dus $0 < \frac{1}{n^2+3} < \frac{1}{n^2}$.

$\sum \frac{1}{n^2}$ is bekend convergent, dus volgens de vergelijkingstest is $\sum \frac{1}{n^2+3}$ ook convergent.""",
                "answer_type": "open",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Onderzoek met de verhoudingstest of $\displaystyle\sum_{n=1}^\infty \frac{n}{2^n}$ convergeert.",
                "hints": [
                    "Bereken $\\frac{a_{n+1}}{a_n} = \\frac{(n+1)/2^{n+1}}{n/2^n}$ en vereenvoudig.",
                    "Neem de limiet van die verhouding voor $n\\to\\infty$ en vergelijk met 1.",
                ],
                "full_solution": r"""$$\frac{a_{n+1}}{a_n} = \frac{(n+1)/2^{n+1}}{n/2^n} = \frac{n+1}{2n}$$
$$\lim_{n\to\infty}\frac{n+1}{2n} = \frac12 < 1$$
Volgens de verhoudingstest is de reeks **convergent**.""",
                "answer_type": "open",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Onderzoek met de verhoudingstest of $\displaystyle\sum_{n=0}^\infty \frac{2^n}{n!}$ convergeert.",
                "hints": [
                    "Bereken $\\frac{a_{n+1}}{a_n} = \\frac{2^{n+1}/(n+1)!}{2^n/n!}$ en vereenvoudig (denk aan $\\frac{n!}{(n+1)!} = \\frac{1}{n+1}$).",
                    "Neem de limiet voor $n\\to\\infty$.",
                ],
                "full_solution": r"""$$\frac{a_{n+1}}{a_n} = \frac{2^{n+1}}{(n+1)!}\cdot\frac{n!}{2^n} = \frac{2}{n+1}$$
$$\lim_{n\to\infty}\frac{2}{n+1} = 0 < 1$$
Volgens de verhoudingstest is de reeks **convergent**.""",
                "answer_type": "open",
            },
            {
                "order_index": 4, "difficulty": 3,
                "question": r"De harmonische reeks $\displaystyle\sum_{n=1}^\infty \frac{1}{n}$ is bekend divergent, terwijl de termen wel degelijk naar $0$ gaan. Leg uit waarom dit niet in tegenspraak is met de divergentietest uit hoofdstuk 16.",
                "hints": [
                    "De divergentietest zegt: als de termen NIET naar 0 gaan, dan is de reeks zeker divergent. Wat zegt de test NIET (in het omgekeerde geval)?",
                    "'Termen gaan naar 0' is een noodzakelijke voorwaarde voor convergentie, geen voldoende voorwaarde. Bedenk wat dat onderscheid betekent.",
                ],
                "full_solution": r"""De divergentietest is een eenrichtingstest: als $a_n \not\to 0$, dan is $\sum a_n$ gegarandeerd divergent. Maar het omgekeerde geldt niet: als $a_n \to 0$, zegt dat **niets** met zekerheid over convergentie, de reeks kan alsnog divergeren.

De harmonische reeks is precies zo'n grensgeval: de termen $\frac1n$ gaan wel naar $0$, maar ze doen dat te langzaam, de opgetelde som blijft toch onbeperkt doorgroeien (al gaat dat heel traag). Dit laat zien dat "termen naar 0" een noodzakelijke, maar geen voldoende voorwaarde is voor convergentie, je hebt dus altijd een echte test (vergelijkings- of verhoudingstest) nodig om convergentie te garanderen.""",
                "answer_type": "open",
            },
        ],
    },
    {
        "module_id": 2,
        "chapter_number": 18,
        "title": "Machtreeksen",
        "theory_content": r"""
### Wat je al weet

Een meetkundige reeks $\sum_{n=0}^\infty r^n$ convergeert voor $|r|<1$ naar $\frac{1}{1-r}$ (hoofdstuk 16). Merk op: hier is $r$ eigenlijk een **variabele**, geen vaste waarde. Als je $r$ door $x$ vervangt, krijg je $\sum x^n = \frac{1}{1-x}$: een reeks die, afhankelijk van welke $x$ je invult, een functie voorstelt.

### Machtreeksen: reeksen die van x afhangen

Een **machtreeks** is een reeks van de vorm $\sum_{n=0}^\infty c_n x^n$ (of algemener, rond een punt $a$: $\sum c_n (x-a)^n$). Voor sommige waarden van $x$ convergeert zo'n reeks, voor andere niet, exact zoals de meetkundige reeks alleen convergeert voor $|x|<1$.

### De convergentiestraal

Het blijkt dat het gebied waar een machtreeks convergeert altijd een symmetrisch interval rond $x=a$ is: $|x-a| < R$, voor een bepaald getal $R$ dat de **convergentiestraal** heet (bij de meetkundige reeks is $R=1$). Je vindt $R$ met de verhoudingstest uit hoofdstuk 17, maar nu toegepast met $x$ er nog in:

$$L = \lim_{n\to\infty}\left|\frac{c_{n+1}x^{n+1}}{c_nx^n}\right| = |x| \cdot \lim_{n\to\infty}\left|\frac{c_{n+1}}{c_n}\right|$$

De reeks convergeert waar $L<1$, dat geeft een voorwaarde op $|x|$, en daaruit lees je $R$ af.

### Een volledig uitgewerkt voorbeeld

**Bepaal de convergentiestraal van $\displaystyle\sum_{n=1}^\infty \frac{x^n}{n}$.**

**Stap 1.** Pas de verhoudingstest toe met de termen $a_n = \dfrac{x^n}{n}$:
$$\left|\frac{a_{n+1}}{a_n}\right| = \left|\frac{x^{n+1}/(n+1)}{x^n/n}\right| = |x|\cdot\frac{n}{n+1}$$

**Stap 2.** Neem de limiet voor $n\to\infty$: $\dfrac{n}{n+1}\to 1$, dus $L = |x|$.

**Stap 3.** De reeks convergeert waar $L<1$, dus waar $|x|<1$. De convergentiestraal is dus $R=1$.
""",
        "summary": "Een machtreeks $\\sum c_n(x-a)^n$ convergeert op een symmetrisch interval $|x-a|<R$. Je vindt de convergentiestraal $R$ door de verhoudingstest toe te passen met $x$ er nog in, en op te lossen voor welke $|x-a|$ de limiet kleiner dan 1 is.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 2,
                "question": r"Bepaal de convergentiestraal van $\displaystyle\sum_{n=0}^\infty \frac{x^n}{n!}$.",
                "hints": [
                    "Pas de verhoudingstest toe: $\\left|\\frac{x^{n+1}/(n+1)!}{x^n/n!}\\right| = |x|\\cdot\\frac{1}{n+1}$.",
                    "Wat gebeurt er met deze limiet voor $n\\to\\infty$, voor welke waarde van $x$ dan ook?",
                ],
                "full_solution": r"""$$\left|\frac{a_{n+1}}{a_n}\right| = |x|\cdot\frac{n!}{(n+1)!} = \frac{|x|}{n+1} \xrightarrow{n\to\infty} 0$$
De limiet is $0$ voor **elke** waarde van $x$, dus de reeks convergeert altijd: de convergentiestraal is $R=\infty$.""",
                "answer_type": "open",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Bepaal de convergentiestraal van $\displaystyle\sum_{n=1}^\infty n\,x^n$.",
                "hints": [
                    "Pas de verhoudingstest toe: $\\left|\\frac{(n+1)x^{n+1}}{nx^n}\\right| = |x|\\cdot\\frac{n+1}{n}$.",
                    "Bereken de limiet voor $n\\to\\infty$ en los op voor welke $|x|$ deze kleiner dan 1 is.",
                ],
                "full_solution": r"""$$\left|\frac{a_{n+1}}{a_n}\right| = |x|\cdot\frac{n+1}{n} \xrightarrow{n\to\infty} |x|$$
Convergent voor $|x|<1$, dus $R=1$.""",
                "answer_type": "numeric",
                "correct_answer": "1",
            },
            {
                "order_index": 3, "difficulty": 3,
                "question": r"Bepaal de convergentiestraal en het convergentie-interval van $\displaystyle\sum_{n=0}^\infty \frac{(x-2)^n}{3^n}$.",
                "hints": [
                    "Pas de verhoudingstest toe: $\\left|\\frac{(x-2)^{n+1}/3^{n+1}}{(x-2)^n/3^n}\\right| = \\frac{|x-2|}{3}$.",
                    "Los op voor welke $|x-2|$ deze verhouding kleiner dan 1 is, en vertaal dat naar een interval rond $x=2$.",
                ],
                "full_solution": r"""$$\left|\frac{a_{n+1}}{a_n}\right| = \frac{|x-2|}{3}$$
Convergent waar $\frac{|x-2|}{3}<1$, dus $|x-2|<3$. De convergentiestraal is $R=3$, het convergentie-interval is $(2-3,\ 2+3) = (-1,\ 5)$.""",
                "answer_type": "open",
            },
            {
                "order_index": 4, "difficulty": 3,
                "question": r"Bepaal de convergentiestraal van $\displaystyle\sum_{n=0}^\infty n!\,x^n$.",
                "hints": [
                    "Pas de verhoudingstest toe: $\\left|\\frac{(n+1)!x^{n+1}}{n!x^n}\\right| = |x|(n+1)$.",
                    "Voor welke $x \\ne 0$ blijft deze limiet eindig (kleiner dan 1) als $n\\to\\infty$?",
                ],
                "full_solution": r"""$$\left|\frac{a_{n+1}}{a_n}\right| = |x|(n+1) \xrightarrow{n\to\infty} \infty \quad \text{voor elke } x \ne 0$$
Alleen voor $x=0$ is de limiet (triviaal) kleiner dan $1$. De reeks convergeert dus alleen in het punt $x=0$: de convergentiestraal is $R=0$.""",
                "answer_type": "numeric",
                "correct_answer": "0",
            },
        ],
    },
    {
        "module_id": 2,
        "chapter_number": 19,
        "title": "Taylor- en Maclaurinreeksen",
        "theory_content": r"""
### Wat je al weet

Machtreeksen (hoofdstuk 18) zijn reeksen die een functie van $x$ voorstellen. Je kent ook al de afgeleide en tweede afgeleide van een functie in een punt (hoofdstuk 3 en 6).

### Het idee: een functie exact "nabouwen" met een oneindig polynoom

Kun je élke functie schrijven als een machtreeks? Voor veel bekende functies (zoals $e^x$, $\sin x$, $\ln x$) is het antwoord ja. De truc: gebruik de afgeleiden van $f$ in één punt om de coëfficiënten van de reeks te bepalen, zodat de reeks in dat punt niet alleen dezelfde waarde heeft als $f$, maar ook dezelfde helling, dezelfde kromming, enzovoort, voor élke afgeleide.

### De Taylorreeks

De **Taylorreeks** van $f$ rond het punt $a$ is:
$$f(x) = \sum_{n=0}^\infty \frac{f^{(n)}(a)}{n!}(x-a)^n = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \cdots$$
waarbij $f^{(n)}(a)$ de $n$-de afgeleide van $f$ in $a$ is. Rond $a=0$ heet dit specifieke geval een **Maclaurinreeks**:
$$f(x) = \sum_{n=0}^\infty \frac{f^{(n)}(0)}{n!}x^n$$

### Een volledig uitgewerkt voorbeeld

**Bepaal de Maclaurinreeks van $f(x)=e^x$.**

**Stap 1.** Bereken de afgeleiden: $f'(x)=e^x$, $f''(x)=e^x$, enzovoort, élke afgeleide van $e^x$ is weer $e^x$.

**Stap 2.** Evalueer in $a=0$: $f^{(n)}(0) = e^0 = 1$ voor elke $n$.

**Stap 3.** Vul in de Maclaurinformule in:
$$e^x = \sum_{n=0}^\infty \frac{1}{n!}x^n = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$$

Deze reeks convergeert voor elke $x$ (zoals je in hoofdstuk 18, opgave 1, al vond voor deze exacte reeks).
""",
        "summary": "De Taylorreeks van $f$ rond $a$ gebruikt alle afgeleiden $f^{(n)}(a)$ als coëfficiënten: $\\sum \\frac{f^{(n)}(a)}{n!}(x-a)^n$. Rond $a=0$ heet dit de Maclaurinreeks. Zo kun je functies als $e^x$, $\\sin x$ en $\\cos x$ als oneindig polynoom schrijven.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 2,
                "question": r"Bepaal de Maclaurinreeks van $f(x)=\cos(x)$.",
                "hints": [
                    "Bereken de eerste vier afgeleiden van $\\cos(x)$ en evalueer ze in $x=0$: je zult een herhaald patroon zien ($1,0,-1,0,\\ldots$).",
                    "Alleen de even machten van $x$ komen voor (de oneven-orde afgeleiden zijn 0 in $x=0$). Gebruik het patroon om de algemene term op te schrijven.",
                ],
                "full_solution": r"""$f(x)=\cos(x)$, $f'(x)=-\sin(x)$, $f''(x)=-\cos(x)$, $f'''(x)=\sin(x)$, $f^{(4)}(x)=\cos(x)$ (patroon herhaalt).

In $x=0$: $f(0)=1,\ f'(0)=0,\ f''(0)=-1,\ f'''(0)=0,\ f^{(4)}(0)=1,\ldots$

$$\cos(x) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \cdots = \sum_{n=0}^\infty \frac{(-1)^n x^{2n}}{(2n)!}$$""",
                "answer_type": "open",
            },
            {
                "order_index": 2, "difficulty": 3,
                "question": r"Bepaal de eerste vier termen van de Taylorreeks van $f(x)=\ln(x)$ rond $a=1$.",
                "hints": [
                    "Bereken $f(1), f'(1), f''(1), f'''(1)$ voor $f(x)=\\ln(x)$: je hebt $f'(x)=1/x$, $f''(x)=-1/x^2$, $f'''(x)=2/x^3$.",
                    "Vul in de Taylorformule in met $a=1$, dus met $(x-1)^n$-termen.",
                ],
                "full_solution": r"""$f(x)=\ln(x)$: $f(1)=0$. $f'(x)=1/x$: $f'(1)=1$. $f''(x)=-1/x^2$: $f''(1)=-1$. $f'''(x)=2/x^3$: $f'''(1)=2$.

$$\ln(x) = 0 + 1\cdot(x-1) + \frac{-1}{2!}(x-1)^2 + \frac{2}{3!}(x-1)^3 + \cdots = (x-1) - \frac{(x-1)^2}{2} + \frac{(x-1)^3}{3} - \cdots$$""",
                "answer_type": "open",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Gebruik de eerste vier termen van de Maclaurinreeks van $e^x$ (uit de theorie) om een benadering van $e$ te geven.",
                "hints": [
                    "Vul $x=1$ in bij de reeks $e^x = 1+x+\\frac{x^2}{2!}+\\frac{x^3}{3!}+\\cdots$, en neem alleen de eerste vier termen (tot en met $\\frac{x^3}{3!}$).",
                    "Reken de vier breuken bij elkaar op.",
                ],
                "full_solution": r"""$$e^1 \approx 1 + 1 + \frac{1}{2!} + \frac{1}{3!} = 1+1+0{,}5+0{,}1667 \approx 2{,}667$$
De echte waarde is $e \approx 2{,}71828$, dus met slechts vier termen zit je al aardig dichtbij, meer termen geven een steeds betere benadering.""",
                "answer_type": "numeric",
                "correct_answer": "2.667",
            },
            {
                "order_index": 4, "difficulty": 2,
                "question": r"Bepaal de Maclaurinreeks van $f(x)=\sin(x)$.",
                "hints": [
                    "Bereken de afgeleiden $f'(x)=\\cos x,\\ f''(x)=-\\sin x,\\ f'''(x)=-\\cos x,\\ f^{(4)}(x)=\\sin x$ en evalueer in $x=0$.",
                    "Net als bij $\\cos(x)$ komen alleen bepaalde machten voor (hier de oneven), met afwisselend teken.",
                ],
                "full_solution": r"""In $x=0$: $f(0)=0,\ f'(0)=1,\ f''(0)=0,\ f'''(0)=-1,\ f^{(4)}(0)=0,\ f^{(5)}(0)=1,\ldots$

$$\sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots = \sum_{n=0}^\infty \frac{(-1)^n x^{2n+1}}{(2n+1)!}$$""",
                "answer_type": "open",
            },
        ],
    },
    {
        "module_id": 2,
        "chapter_number": 20,
        "title": "Parametrische krommen",
        "theory_content": r"""
### Wat je al weet

Tot nu toe beschreef je een kromme altijd als $y=f(x)$: voor elke $x$ precies één $y$-waarde. Maar een cirkel is geen functie in die zin (bij één $x$-waarde horen twee $y$-waarden). Uit VWO B ken je het idee van een bewegend punt waarvan de positie van de tijd afhangt.

### Het idee: x én y allebei afhankelijk van een derde variabele

Bij een **parametrisch beschreven kromme** hangen zowel $x$ als $y$ af van een gemeenschappelijke variabele $t$ (vaak "tijd" genoemd, maar dat hoeft niet): $x=x(t)$, $y=y(t)$. Voor elke waarde van $t$ krijg je een punt $(x(t),y(t))$; laat je $t$ variëren, dan doorloopt dat punt de hele kromme. Zo kan een cirkel bijvoorbeeld beschreven worden als $x(t)=r\cos(t)$, $y(t)=r\sin(t)$.

### De helling van een parametrische kromme

Hoe bepaal je $\frac{dy}{dx}$ als je geen expliciete $y=f(x)$ hebt? Met de kettingregel: $\frac{dy}{dt} = \frac{dy}{dx}\cdot\frac{dx}{dt}$, dus:
$$\frac{dy}{dx} = \frac{dy/dt}{dx/dt}$$
(mits $dx/dt \ne 0$): je deelt simpelweg de twee afgeleiden naar $t$ door elkaar.

### Booglengte van een parametrische kromme

Net als in hoofdstuk 11 (waar $L=\int\sqrt{1+[f'(x)]^2}dx$ kwam uit een piepklein Pythagoras-driehoekje met basis $dx$ en hoogte $dy$), geldt hier hetzelfde idee met $dx=x'(t)dt$ en $dy=y'(t)dt$:
$$L = \int_{t_1}^{t_2} \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\,dt$$

### Een volledig uitgewerkt voorbeeld

**Bepaal $\dfrac{dy}{dx}$ voor $x(t)=\cos(t)$, $y(t)=\sin(t)$, in het punt $t=\frac{\pi}{4}$.**

**Stap 1.** Bereken de afgeleiden naar $t$: $\dfrac{dx}{dt}=-\sin(t)$, $\dfrac{dy}{dt}=\cos(t)$.

**Stap 2.** Deel ze door elkaar: $\dfrac{dy}{dx} = \dfrac{\cos(t)}{-\sin(t)} = -\cot(t)$.

**Stap 3.** Vul $t=\frac{\pi}{4}$ in: $-\cot\left(\frac{\pi}{4}\right) = -1$. De raaklijn aan de cirkel in dat punt heeft dus helling $-1$.
""",
        "summary": "Bij een parametrische kromme $x(t), y(t)$ bereken je de helling als $\\frac{dy}{dx} = \\frac{dy/dt}{dx/dt}$, en de booglengte als $\\int\\sqrt{(dx/dt)^2+(dy/dt)^2}\\,dt$: allebei rechtstreeks voortbouwend op bekende technieken, nu met de afgeleiden naar $t$.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Bepaal $\dfrac{dy}{dx}$ voor $x(t)=t^2$, $y(t)=t^3$.",
                "hints": [
                    "Bereken $\\frac{dx}{dt}$ en $\\frac{dy}{dt}$ apart.",
                    "Deel $\\frac{dy}{dt}$ door $\\frac{dx}{dt}$ en vereenvoudig.",
                ],
                "full_solution": r"""$\frac{dx}{dt}=2t$, $\frac{dy}{dt}=3t^2$.
$$\frac{dy}{dx} = \frac{3t^2}{2t} = \frac{3t}{2} \quad (t\ne0)$$""",
                "answer_type": "expression",
                "correct_answer": "3t/2",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Bereken de booglengte van $x(t)=\cos(t)$, $y(t)=\sin(t)$ voor $0\le t\le\pi$, en controleer je antwoord met een bekende meetkundige formule.",
                "hints": [
                    "Bereken $\\frac{dx}{dt}$ en $\\frac{dy}{dt}$, en vereenvoudig $\\left(\\frac{dx}{dt}\\right)^2+\\left(\\frac{dy}{dt}\\right)^2$ met de identiteit $\\sin^2+\\cos^2=1$.",
                    "Dit is een halve eenheidscirkel: vergelijk je uitkomst met de halve omtrek $\\pi r$.",
                ],
                "full_solution": r"""$\frac{dx}{dt}=-\sin(t)$, $\frac{dy}{dt}=\cos(t)$.
$$\left(\frac{dx}{dt}\right)^2+\left(\frac{dy}{dt}\right)^2 = \sin^2(t)+\cos^2(t) = 1$$
$$L = \int_0^\pi \sqrt{1}\,dt = \int_0^\pi 1\,dt = \pi$$
Dit is inderdaad de halve omtrek van de eenheidscirkel ($\pi r = \pi \cdot 1$). ✓""",
                "answer_type": "numeric",
                "correct_answer": "pi",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Bepaal de vergelijking van de raaklijn aan de kromme $x(t)=t^2$, $y(t)=t^3$ in het punt $t=1$.",
                "hints": [
                    "Gebruik $\\frac{dy}{dx}=\\frac{3t}{2}$ uit opgave 1, en vul $t=1$ in voor de helling.",
                    "Bepaal het punt $(x(1),y(1))$ en gebruik de puntrichtingsvorm.",
                ],
                "full_solution": r"""Helling: $\frac{dy}{dx}\Big|_{t=1} = \frac{3(1)}{2} = \frac32$. Punt: $(x(1),y(1))=(1,1)$.

Raaklijn: $y - 1 = \frac32(x-1)$, dus $y = \frac32 x - \frac12$.""",
                "answer_type": "expression",
                "correct_answer": "y=3/2*x-1/2",
            },
            {
                "order_index": 4, "difficulty": 1,
                "question": r"Bereken de oppervlakte onder de kromme $x(t)=t$, $y(t)=t^2$ voor $0\le t\le 2$, met de formule $A=\int y\,\frac{dx}{dt}\,dt$.",
                "hints": [
                    "Hier is $\\frac{dx}{dt}=1$, dus de integraal wordt gewoon $\\int_0^2 t^2\\,dt$.",
                    "Dit is dezelfde situatie als de gewone (niet-parametrische) grafiek $y=x^2$, controleer of je antwoord daarmee overeenkomt.",
                ],
                "full_solution": r"""$\frac{dx}{dt}=1$, dus $A = \int_0^2 t^2 \cdot 1\,dt = \left[\frac{t^3}{3}\right]_0^2 = \frac{8}{3}$.

Dit is inderdaad hetzelfde als $\int_0^2 x^2\,dx$, want hier is $x(t)=t$ letterlijk gelijk aan $t$ zelf.""",
                "answer_type": "numeric",
                "correct_answer": "8/3",
            },
        ],
    },
    {
        "module_id": 2,
        "chapter_number": 21,
        "title": "Poolcoördinaten",
        "theory_content": r"""
### Wat je al weet

Tot nu toe leg je een punt vast met cartesische coördinaten $(x,y)$: hoe ver naar rechts en hoe ver omhoog.

### Een andere manier om een punt vast te leggen

Er is ook een natuurlijke andere manier: hoe ver een punt van de oorsprong af ligt ($r$), en in welke richting (hoek $\theta$ ten opzichte van de positieve $x$-as). Dit heten **poolcoördinaten** $(r,\theta)$. Voor cirkels en spiralen rond de oorsprong zijn poolcoördinaten vaak veel natuurlijker dan cartesische coördinaten, een cirkel met straal $3$ is in poolcoördinaten simpelweg "$r=3$", terwijl dat in cartesische coördinaten $x^2+y^2=9$ wordt.

### Omrekenen tussen de twee stelsels

Met een rechthoekige driehoek (rechthoekszijden $x$ en $y$, schuine zijde $r$) volgt direct:
$$x = r\cos(\theta), \qquad y = r\sin(\theta), \qquad r = \sqrt{x^2+y^2}, \qquad \tan(\theta) = \frac{y}{x}$$

### Oppervlakte in poolcoördinaten

Bij cartesische coördinaten deel je een oppervlakte op in dunne verticale reepjes. In poolcoördinaten deel je op in dunne **taartpuntjes**: een taartpunt met straal $r$ en hoek $d\theta$ heeft (net als een cirkelsector) oppervlakte $\frac12 r^2\,d\theta$. Tel al die taartpuntjes op:
$$A = \int_{\theta_1}^{\theta_2} \frac12 r^2\,d\theta$$

### Een volledig uitgewerkt voorbeeld

**Bereken de oppervlakte binnen de cirkel $r=3$ met de poolcoördinatenformule, en controleer met de bekende cirkelformule.**

**Stap 1.** Voor een volledige cirkel loopt $\theta$ van $0$ tot $2\pi$, met constante $r=3$.

**Stap 2.** Pas de formule toe:
$$A = \int_0^{2\pi} \frac12 (3)^2\,d\theta = \int_0^{2\pi} \frac{9}{2}\,d\theta = \frac{9}{2}\cdot 2\pi = 9\pi$$

**Stap 3.** Controleer: de bekende formule $\pi r^2 = \pi \cdot 3^2 = 9\pi$. ✓
""",
        "summary": "Poolcoördinaten $(r,\\theta)$ leggen een punt vast via afstand en hoek, met $x=r\\cos\\theta$, $y=r\\sin\\theta$. Oppervlakte bereken je door taartpuntjes van oppervlakte $\\frac12 r^2\\,d\\theta$ op te tellen: $A=\\int \\frac12 r^2\\,d\\theta$.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Zet het punt $(x,y)=(1,1)$ om naar poolcoördinaten.",
                "hints": [
                    "Gebruik $r=\\sqrt{x^2+y^2}$.",
                    "Gebruik $\\tan(\\theta)=y/x$ en let op in welk kwadrant het punt ligt.",
                ],
                "full_solution": r"""$r=\sqrt{1^2+1^2}=\sqrt2$. $\tan(\theta)=1/1=1$, en omdat $(1,1)$ in het eerste kwadrant ligt: $\theta=\frac{\pi}{4}$.

$(r,\theta) = \left(\sqrt2, \frac{\pi}{4}\right)$.""",
                "answer_type": "open",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Laat zien dat $r=2\cos(\theta)$ een cirkel beschrijft, door dit om te zetten naar een cartesische vergelijking.",
                "hints": [
                    "Vermenigvuldig beide kanten met $r$: $r^2 = 2r\\cos(\\theta)$, en gebruik $r^2=x^2+y^2$ en $r\\cos\\theta=x$.",
                    "Breng alles naar één kant en maak een kwadraat af (kwadraat afsplitsen) om de cirkelvorm $(x-a)^2+y^2=R^2$ te herkennen.",
                ],
                "full_solution": r"""$r=2\cos\theta \Rightarrow r^2 = 2r\cos\theta \Rightarrow x^2+y^2 = 2x$.

$$x^2-2x+y^2=0 \Rightarrow (x-1)^2 - 1 + y^2 = 0 \Rightarrow (x-1)^2+y^2=1$$
Dit is een cirkel met middelpunt $(1,0)$ en straal $1$.""",
                "answer_type": "open",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Bereken zelf de oppervlakte binnen de cirkel $r=5$ met de poolcoördinatenformule (reproduceer de aanpak uit de theorie met een andere straal), en controleer met $\pi r^2$.",
                "hints": [
                    "Voor een volledige cirkel loopt $\\theta$ van $0$ tot $2\\pi$.",
                    "$A=\\int_0^{2\\pi} \\frac12 (5)^2\\,d\\theta$.",
                ],
                "full_solution": r"""$$A = \int_0^{2\pi} \frac12(25)\,d\theta = \frac{25}{2}\cdot 2\pi = 25\pi$$
Controle: $\pi r^2 = \pi(5)^2=25\pi$. ✓""",
                "answer_type": "numeric",
                "correct_answer": "25*pi",
            },
            {
                "order_index": 4, "difficulty": 3,
                "question": r"Bereken de oppervlakte binnen de cardioïde $r=1+\cos(\theta)$ (voor $0\le\theta\le 2\pi$).",
                "hints": [
                    "Stel de integraal op: $A=\\frac12\\int_0^{2\\pi}(1+\\cos\\theta)^2\\,d\\theta$, en werk het kwadraat uit tot $1+2\\cos\\theta+\\cos^2\\theta$.",
                    "Gebruik $\\int_0^{2\\pi}\\cos\\theta\\,d\\theta=0$ en $\\int_0^{2\\pi}\\cos^2\\theta\\,d\\theta=\\pi$ (met de identiteit $\\cos^2\\theta=\\frac{1+\\cos2\\theta}{2}$, zoals in hoofdstuk 14).",
                ],
                "full_solution": r"""$$A = \frac12\int_0^{2\pi} (1+\cos\theta)^2\,d\theta = \frac12\int_0^{2\pi}\left(1+2\cos\theta+\cos^2\theta\right)d\theta$$
Splits op: $\int_0^{2\pi}1\,d\theta=2\pi$; $\int_0^{2\pi}2\cos\theta\,d\theta=0$; $\int_0^{2\pi}\cos^2\theta\,d\theta=\pi$.
$$A = \frac12(2\pi+0+\pi) = \frac{3\pi}{2}$$""",
                "answer_type": "numeric",
                "correct_answer": "3*pi/2",
            },
        ],
    },
]
