# -*- coding: utf-8 -*-
"""Module V: Differentiaalvergelijkingen (hoofdstuk 40-47), zelfde 'vanaf nul opgebouwd'-aanpak."""

CHAPTERS_5 = [
    {
        "module_id": 5,
        "chapter_number": 40,
        "title": "Eerste-orde ODE's: scheiden van variabelen",
        "theory_content": r"""
### Wat je al weet

Tot nu toe was de onbekende in een vergelijking meestal een getal ($x$). Je kent ook al integreren als het omgekeerde van differentiëren (hoofdstuk 9).

### Een vergelijking waarin de onbekende een hele functie is

Een **differentiaalvergelijking** (afgekort ODE, van "ordinary differential equation") is een vergelijking waarin niet een getal, maar een **functie** $y(x)$ de onbekende is, en waarin ook de afgeleide(n) van die functie voorkomen. Bijvoorbeeld: $\dfrac{dy}{dx} = xy$. "Oplossen" betekent hier: vind alle functies $y(x)$ die aan deze vergelijking voldoen.

### De simpelste methode: scheiden van variabelen

Sommige ODE's zijn te schrijven in de vorm $\dfrac{dy}{dx} = g(x)h(y)$: het rechterlid splitst netjes in een deel dat alleen van $x$ afhangt en een deel dat alleen van $y$ afhangt. Dan kun je, enigszins informeel maar effectief, alle $y$'s naar de ene kant schuiven en alle $x$'s naar de andere:
$$\frac{dy}{h(y)} = g(x)\,dx$$
en beide kanten los van elkaar integreren. Dit werkt omdat $dy/dx$ zich (in dit soort manipulaties) laat behandelen als een breuk van twee oneindig kleine stukjes, precies zoals je bij substitutie in hoofdstuk 10 al deed met $du$ en $dx$.

### Een volledig uitgewerkt voorbeeld

**Los op: $\dfrac{dy}{dx} = xy$.**

**Stap 1.** Scheid de variabelen: breng alle $y$'s naar links, alle $x$'s naar rechts.
$$\frac{dy}{y} = x\,dx$$

**Stap 2.** Integreer beide kanten apart:
$$\int \frac{dy}{y} = \int x\,dx \implies \ln|y| = \frac{x^2}{2} + C$$

**Stap 3.** Los op naar $y$: neem van beide kanten de exponent.
$$y = e^{x^2/2 + C} = e^C \cdot e^{x^2/2}$$
Omdat $e^C$ zelf gewoon een positieve constante is, herschrijven we die als een nieuwe, vrij te kiezen constante $A$:
$$y = Ae^{x^2/2}$$
""",
        "summary": "Bij een scheidbare ODE $dy/dx=g(x)h(y)$ schuif je alle $y$'s naar links en alle $x$'s naar rechts, en integreer je beide kanten apart. Los daarna op naar $y$ om de algemene oplossing (met een vrije constante) te krijgen.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Los op: $\dfrac{dy}{dx} = 2xy$.",
                "hints": [
                    "Scheid de variabelen: $\\frac{dy}{y} = 2x\\,dx$.",
                    "Integreer beide kanten en los op naar $y$ (net als in het voorbeeld).",
                ],
                "full_solution": r"""$$\int\frac{dy}{y} = \int 2x\,dx \implies \ln|y| = x^2+C \implies y = Ae^{x^2}$$""",
                "answer_type": "expression",
                "correct_answer": "A*exp(x^2)",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Los op: $\dfrac{dy}{dx} = \dfrac{y}{x}$, met de beginvoorwaarde $y(1)=2$.",
                "hints": [
                    "Scheid de variabelen: $\\frac{dy}{y} = \\frac{dx}{x}$.",
                    "Bepaal na het integreren de constante door $x=1, y=2$ in te vullen.",
                ],
                "full_solution": r"""$$\int\frac{dy}{y} = \int\frac{dx}{x} \implies \ln|y| = \ln|x| + C \implies y = Ax$$
Vul $y(1)=2$ in: $2 = A\cdot1 \implies A=2$.
$$y = 2x$$""",
                "answer_type": "expression",
                "correct_answer": "2*x",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Los op: $\dfrac{dy}{dx} = \dfrac{x^2}{y}$ (een impliciete oplossing mag).",
                "hints": [
                    "Scheid de variabelen: $y\\,dy = x^2\\,dx$.",
                    "Integreer beide kanten; je hoeft niet per se expliciet naar $y$ op te lossen.",
                ],
                "full_solution": r"""$$\int y\,dy = \int x^2\,dx \implies \frac{y^2}{2} = \frac{x^3}{3} + C \implies y^2 = \frac{2x^3}{3} + C'$$""",
                "answer_type": "open",
            },
            {
                "order_index": 4, "difficulty": 3,
                "question": r"Los op: $\dfrac{dy}{dx} = -y^2$, met $y(0)=1$.",
                "hints": [
                    "Scheid de variabelen: $\\frac{dy}{y^2} = -dx$.",
                    "Na integreren krijg je $-\\frac1y$ links; los op naar $y$ en bepaal de constante met de beginvoorwaarde.",
                ],
                "full_solution": r"""$$\int \frac{dy}{y^2} = \int -dx \implies -\frac1y = -x+C \implies \frac1y = x-C \implies y = \frac{1}{x-C}$$
Vul $y(0)=1$ in: $1 = \frac{1}{0-C} \implies -C=1 \implies C=-1$.
$$y = \frac{1}{x+1}$$""",
                "answer_type": "expression",
                "correct_answer": "1/(x+1)",
            },
        ],
    },
    {
        "module_id": 5,
        "chapter_number": 41,
        "title": "Eerste-orde lineaire ODE's",
        "theory_content": r"""
### Wat je al weet

Scheiden van variabelen (hoofdstuk 40) lost ODE's op waarbij je $x$ en $y$ kunt scheiden. Maar niet elke ODE laat zich zo splitsen.

### Een ODE die niet scheidbaar is

Bekijk $\dfrac{dy}{dx} + y = e^x$. Hier zit $y$ vast aan een losse term, niet vermenigvuldigd met iets dat alleen van $x$ afhangt: scheiden van variabelen lukt hier niet. Dit is een voorbeeld van een **lineaire eerste-orde ODE**, met de standaardvorm $y' + p(x)y = q(x)$.

### Het idee: vermenigvuldig met iets dat het linkerlid "opruimt"

De truc: vermenigvuldig de hele vergelijking met een slim gekozen functie $\mu(x)$ (de **integrerende factor**) zodanig dat het linkerlid $\mu(x)y' + \mu(x)p(x)y$ precies de afgeleide wordt van het product $\mu(x)y$ (herken de productregel: $(\mu y)' = \mu y' + \mu' y$). Dat lukt als $\mu'(x) = \mu(x)p(x)$, oftewel als $\mu$ zelf een scheidbare ODE oplost met oplossing:
$$\mu(x) = e^{\int p(x)\,dx}$$
Vermenigvuldig je de oorspronkelijke vergelijking met deze $\mu(x)$, dan wordt het linkerlid automatisch $(\mu y)'$, en kun je beide kanten gewoon integreren.

### Een volledig uitgewerkt voorbeeld

**Los op: $y' + y = e^x$.**

**Stap 1.** Herken $p(x)=1$, dus de integrerende factor is $\mu(x) = e^{\int 1\,dx} = e^x$.

**Stap 2.** Vermenigvuldig de hele vergelijking met $\mu(x)=e^x$:
$$e^xy' + e^xy = e^{2x}$$
Het linkerlid is nu precies $(e^xy)'$ (controleer met de productregel).

**Stap 3.** Integreer beide kanten:
$$e^xy = \int e^{2x}\,dx = \frac{e^{2x}}{2} + C$$

**Stap 4.** Los op naar $y$ door te delen door $e^x$:
$$y = \frac{e^x}{2} + Ce^{-x}$$
""",
        "summary": "Bij een lineaire ODE $y'+p(x)y=q(x)$ vermenigvuldig je met de integrerende factor $\\mu(x)=e^{\\int p(x)dx}$, waardoor het linkerlid $(\\mu y)'$ wordt. Integreer daarna beide kanten en los op naar $y$.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Los op: $y' + 2y = 0$.",
                "hints": [
                    "Hier is $p(x)=2$, dus $\\mu(x)=e^{2x}$.",
                    "Vermenigvuldig met $\\mu$, herken $(\\mu y)'=0$, en integreer.",
                ],
                "full_solution": r"""$\mu=e^{2x}$. $(e^{2x}y)' = e^{2x}\cdot0=0 \implies e^{2x}y = C \implies y = Ce^{-2x}$.""",
                "answer_type": "expression",
                "correct_answer": "C*exp(-2*x)",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Los op: $y' + y = x$.",
                "hints": [
                    "Hier is $p(x)=1$, dus $\\mu(x)=e^x$.",
                    "Na vermenigvuldigen krijg je $(e^xy)' = xe^x$. Deze integraal is exact het voorbeeld uit hoofdstuk 12 (partieel integreren, opgave 1 uit die theorie): $\\int xe^x dx = xe^x - e^x + C$.",
                ],
                "full_solution": r"""$\mu=e^x$. $(e^xy)' = xe^x$.
$$e^xy = \int xe^x\,dx = xe^x - e^x + C$$
$$y = x - 1 + Ce^{-x}$$""",
                "answer_type": "expression",
                "correct_answer": "x-1+C*exp(-x)",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Los op: $y' - 3y = e^{3x}$.",
                "hints": [
                    "Hier is $p(x)=-3$, dus $\\mu(x)=e^{-3x}$.",
                    "Vermenigvuldig en let op: $e^{-3x}\\cdot e^{3x}=1$, dus rechts blijft alleen een constante over om te integreren.",
                ],
                "full_solution": r"""$\mu=e^{-3x}$. $(e^{-3x}y)' = e^{-3x}\cdot e^{3x} = 1$.
$$e^{-3x}y = \int 1\,dx = x+C$$
$$y = xe^{3x} + Ce^{3x}$$""",
                "answer_type": "expression",
                "correct_answer": "x*exp(3*x)+C*exp(3*x)",
            },
            {
                "order_index": 4, "difficulty": 3,
                "question": r"Los op: $y' + \dfrac{1}{x}y = x$, voor $x>0$.",
                "hints": [
                    "Hier is $p(x)=1/x$, dus $\\mu(x)=e^{\\int 1/x\\,dx} = e^{\\ln x} = x$.",
                    "Vermenigvuldig met $\\mu=x$: je krijgt $(xy)' = x^2$. Integreer en los op naar $y$.",
                ],
                "full_solution": r"""$\mu=x$. $(xy)' = x\cdot x = x^2$.
$$xy = \int x^2\,dx = \frac{x^3}{3}+C$$
$$y = \frac{x^2}{3} + \frac{C}{x}$$""",
                "answer_type": "expression",
                "correct_answer": "x^2/3+C/x",
            },
        ],
    },
    {
        "module_id": 5,
        "chapter_number": 42,
        "title": "Exacte vergelijkingen",
        "theory_content": r"""
### Wat je al weet

Je kent inmiddels twee soorten eerste-orde ODE's die je kunt oplossen: scheidbare (hoofdstuk 40) en lineaire (hoofdstuk 41). Je kent ook partiële afgeleiden (denk aan hoofdstuk 24, of vooruitlopend: gewoon differentiëren naar één variabele terwijl je de andere vasthoudt).

### Een derde type: exacte vergelijkingen

Schrijf een ODE in de vorm $M(x,y)\,dx + N(x,y)\,dy = 0$. Soms is de linkerkant precies de **totale afgeleide** van een functie $F(x,y)$, dat wil zeggen: $\dfrac{\partial F}{\partial x}=M$ en $\dfrac{\partial F}{\partial y}=N$. In dat geval is de vergelijking simpelweg $dF=0$, en is de oplossing direct $F(x,y)=C$ (een constante functie heeft immers overal afgeleide nul).

### Hoe herken je dit, en hoe vind je F?

Er bestaat zo'n $F$ precies dan als (vergelijkbaar met een gemengde partiële afgeleide die niet van de volgorde afhangt):
$$\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$$
Is dit het geval, dan vind je $F$ door $M$ naar $x$ te integreren (met een nog onbekende functie $g(y)$ als "integratieconstante", omdat je naar $x$ integreerde), en daarna $g(y)$ te bepalen door de $y$-afgeleide van je tussenresultaat te vergelijken met $N$.

### Een volledig uitgewerkt voorbeeld

**Los op: $2xy\,dx + (x^2+3y^2)\,dy = 0$.**

**Stap 1.** Controleer exactheid: $M=2xy$, $N=x^2+3y^2$. $\dfrac{\partial M}{\partial y}=2x$, $\dfrac{\partial N}{\partial x}=2x$. Gelijk, dus exact.

**Stap 2.** Integreer $M$ naar $x$: $F(x,y) = \int 2xy\,dx = x^2y + g(y)$.

**Stap 3.** Differentieer dit tussenresultaat naar $y$ en vergelijk met $N$: $\dfrac{\partial F}{\partial y} = x^2 + g'(y)$, en dit moet gelijk zijn aan $N=x^2+3y^2$, dus $g'(y)=3y^2 \implies g(y)=y^3$.

**Stap 4.** De oplossing is $F(x,y)=C$:
$$x^2y + y^3 = C$$
""",
        "summary": "Een vergelijking $M\\,dx+N\\,dy=0$ is exact als $\\partial M/\\partial y = \\partial N/\\partial x$. Vind dan $F$ door $M$ naar $x$ te integreren (met onbekende $g(y)$), en bepaal $g(y)$ door te vergelijken met $N$. De oplossing is $F(x,y)=C$.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 2,
                "question": r"Ga na of $(3x^2+2y)\,dx + (2x+3y^2)\,dy = 0$ exact is, en los op als dat zo is.",
                "hints": [
                    "Controleer $\\partial M/\\partial y$ tegen $\\partial N/\\partial x$.",
                    "Integreer $M$ naar $x$, en bepaal $g(y)$ door te vergelijken met $N$.",
                ],
                "full_solution": r"""$M=3x^2+2y$, $N=2x+3y^2$. $\partial M/\partial y = 2 = \partial N/\partial x$. Exact.

$F=\int M\,dx = x^3+2xy+g(y)$. $\partial F/\partial y = 2x+g'(y) = N = 2x+3y^2 \implies g'(y)=3y^2 \implies g(y)=y^3$.
$$x^3+2xy+y^3 = C$$""",
                "answer_type": "expression",
                "correct_answer": "x^3+2*x*y+y^3=C",
            },
            {
                "order_index": 2, "difficulty": 1,
                "question": r"Ga na of $y\,dx + x\,dy = 0$ exact is, en los op.",
                "hints": [
                    "Controleer $\\partial M/\\partial y$ tegen $\\partial N/\\partial x$ (dit zou je zelfs direct als de productregel op $xy$ kunnen herkennen).",
                ],
                "full_solution": r"""$M=y,N=x$. $\partial M/\partial y=1=\partial N/\partial x$. Exact.

$F=\int M\,dx = xy+g(y)$. $\partial F/\partial y = x+g'(y)=N=x \implies g'(y)=0$.
$$xy = C$$
(Dit is meteen te herkennen als $d(xy)=y\,dx+x\,dy$, de productregel achterstevoren.)""",
                "answer_type": "expression",
                "correct_answer": "x*y=C",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Ga na of $(2xy+1)\,dx + x^2\,dy = 0$ exact is, en los op.",
                "hints": [
                    "Controleer eerst de exactheidsvoorwaarde.",
                    "Integreer $M$ naar $x$; let op dat de losse term $+1$ ook meegenomen wordt.",
                ],
                "full_solution": r"""$M=2xy+1,N=x^2$. $\partial M/\partial y=2x=\partial N/\partial x$. Exact.

$F=\int M\,dx = x^2y+x+g(y)$. $\partial F/\partial y=x^2+g'(y)=N=x^2 \implies g'(y)=0$.
$$x^2y+x = C$$""",
                "answer_type": "expression",
                "correct_answer": "x^2*y+x=C",
            },
            {
                "order_index": 4, "difficulty": 3,
                "question": r"Ga na of $\cos(y)\,dx - x\sin(y)\,dy = 0$ exact is, en los op.",
                "hints": [
                    "Controleer $\\partial M/\\partial y$ (met $M=\\cos y$) tegen $\\partial N/\\partial x$ (met $N=-x\\sin y$).",
                    "Integreer $M$ naar $x$ (met $y$ als constante behandeld), en bepaal $g(y)$.",
                ],
                "full_solution": r"""$M=\cos y,N=-x\sin y$. $\partial M/\partial y = -\sin y = \partial N/\partial x$. Exact.

$F=\int M\,dx = x\cos y + g(y)$. $\partial F/\partial y = -x\sin y+g'(y) = N=-x\sin y \implies g'(y)=0$.
$$x\cos(y) = C$$""",
                "answer_type": "expression",
                "correct_answer": "x*cos(y)=C",
            },
        ],
    },
    {
        "module_id": 5,
        "chapter_number": 43,
        "title": "Tweede-orde lineaire ODE's: homogeen, karakteristieke vergelijking",
        "theory_content": r"""
### Wat je al weet

Je hebt eerste-orde ODE's opgelost (hoofdstuk 40-42). Uit hoofdstuk 37 ken je ook al het idee van een **karakteristieke vergelijking**: bij eigenwaarden loste je $\det(A-\lambda I)=0$ op door te gokken dat de oplossing van een bepaalde vorm was.

### Een tweede afgeleide erbij

Een **tweede-orde lineaire ODE met constante coëfficiënten** heeft de vorm $ay''+by'+cy=0$ (homogeen, want het rechterlid is $0$). Hoe pak je dit aan?

### Het idee: gok een exponentiële oplossing

Probeer $y=e^{rx}$ voor een of andere constante $r$. Dan is $y'=re^{rx}$ en $y''=r^2e^{rx}$. Vul dit in:
$$ar^2e^{rx} + bre^{rx} + ce^{rx} = 0 \implies e^{rx}(ar^2+br+c) = 0$$
Omdat $e^{rx}$ nooit $0$ is, moet de rest wel $0$ zijn:
$$ar^2+br+c=0$$
Dit heet de **karakteristieke vergelijking**, een gewoon kwadratisch polynoom in $r$ (vergelijk met de karakteristieke vergelijking $\det(A-\lambda I)=0$ uit hoofdstuk 37, dezelfde denkwijze: gok een speciale vorm, en het invullen levert een polynoomvergelijking op die je moet oplossen). Afhankelijk van het soort wortels krijg je drie soorten oplossingen:

- **Twee verschillende reële wortels** $r_1,r_2$: $y = C_1e^{r_1x}+C_2e^{r_2x}$.
- **Eén dubbele wortel** $r$: $y = (C_1+C_2x)e^{rx}$ (de extra factor $x$ is nodig om twee onafhankelijke oplossingen te houden).
- **Complexe wortels** $r=\alpha\pm\beta i$: $y = e^{\alpha x}(C_1\cos(\beta x)+C_2\sin(\beta x))$ (de trilling komt uit de complexe exponent, via de bekende relatie tussen $e^{i\theta}$ en sin/cos).

### Een volledig uitgewerkt voorbeeld

**Los op: $y''-3y'+2y=0$.**

**Stap 1.** Stel de karakteristieke vergelijking op: $r^2-3r+2=0$.

**Stap 2.** Ontbind: $(r-1)(r-2)=0$, dus $r=1$ of $r=2$: twee verschillende reële wortels.

**Stap 3.** De algemene oplossing is:
$$y = C_1e^{x} + C_2e^{2x}$$
""",
        "summary": "Bij $ay''+by'+cy=0$ gok je $y=e^{rx}$, wat leidt tot de karakteristieke vergelijking $ar^2+br+c=0$. Twee reële wortels geven $C_1e^{r_1x}+C_2e^{r_2x}$; een dubbele wortel geeft $(C_1+C_2x)e^{rx}$; complexe wortels $\\alpha\\pm\\beta i$ geven $e^{\\alpha x}(C_1\\cos\\beta x+C_2\\sin\\beta x)$.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Los op: $y''-5y'+6y=0$.",
                "hints": [
                    "Stel de karakteristieke vergelijking op: $r^2-5r+6=0$.",
                    "Ontbind in factoren.",
                ],
                "full_solution": r"""$r^2-5r+6=0 \implies (r-2)(r-3)=0 \implies r=2$ of $r=3$.
$$y = C_1e^{2x}+C_2e^{3x}$$""",
                "answer_type": "expression",
                "correct_answer": "C1*exp(2*x)+C2*exp(3*x)",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Los op: $y''-4y'+4y=0$.",
                "hints": [
                    "Stel de karakteristieke vergelijking op en ontbind: let op of dit een perfect kwadraat is.",
                    "Bij een dubbele wortel $r$ is de algemene oplossing $(C_1+C_2x)e^{rx}$.",
                ],
                "full_solution": r"""$r^2-4r+4=0 \implies (r-2)^2=0 \implies r=2$ (dubbele wortel).
$$y = (C_1+C_2x)e^{2x}$$""",
                "answer_type": "expression",
                "correct_answer": "(C1+C2*x)*exp(2*x)",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Los op: $y''+4y=0$.",
                "hints": [
                    "Stel de karakteristieke vergelijking op: $r^2+4=0$. Dit heeft geen reële oplossingen: los op met $i=\\sqrt{-1}$.",
                    "Herken de vorm $\\alpha\\pm\\beta i$ (hier is $\\alpha=0$) en gebruik de bijbehorende oplossingsvorm.",
                ],
                "full_solution": r"""$r^2+4=0 \implies r^2=-4 \implies r=\pm2i$. Complexe wortels met $\alpha=0,\ \beta=2$.
$$y = C_1\cos(2x) + C_2\sin(2x)$$""",
                "answer_type": "expression",
                "correct_answer": "C1*cos(2*x)+C2*sin(2*x)",
            },
            {
                "order_index": 4, "difficulty": 3,
                "question": r"Los op: $y''+2y'+5y=0$.",
                "hints": [
                    "Stel de karakteristieke vergelijking op: $r^2+2r+5=0$, en gebruik de abc-formule (de discriminant is negatief).",
                    "Schrijf de wortels in de vorm $\\alpha\\pm\\beta i$ en gebruik de bijbehorende oplossingsvorm.",
                ],
                "full_solution": r"""$r^2+2r+5=0$. Discriminant: $4-20=-16$. $r = \dfrac{-2\pm\sqrt{-16}}{2} = \dfrac{-2\pm4i}{2} = -1\pm2i$.

$\alpha=-1,\ \beta=2$.
$$y = e^{-x}\left(C_1\cos(2x)+C_2\sin(2x)\right)$$""",
                "answer_type": "expression",
                "correct_answer": "exp(-x)*(C1*cos(2*x)+C2*sin(2*x))",
            },
        ],
    },
    {
        "module_id": 5,
        "chapter_number": 44,
        "title": "Particuliere oplossingen: onbepaalde coëfficiënten",
        "theory_content": r"""
### Wat je al weet

Hoofdstuk 43 loste $ay''+by'+cy=0$ op: het rechterlid was steeds $0$ (**homogeen**).

### Wat als er wel iets rechts staat?

Bij $ay''+by'+cy=f(x)$ (met $f(x)\ne0$, **inhomogeen**) blijkt de algemene oplossing altijd te bestaan uit twee delen:
$$y = y_h + y_p$$
waarbij $y_h$ de algemene oplossing van de bijbehorende **homogene** vergelijking is (hoofdstuk 43, met de vrije constanten $C_1,C_2$), en $y_p$ **één enkele** oplossing is die specifiek bij het rechterlid $f(x)$ hoort (een **particuliere oplossing**, geen vrije constanten).

**Waarom dit werkt:** vul $y_h+y_p$ in de vergelijking in. De $y_h$-termen leveren $0$ op (want $y_h$ lost de homogene versie op), en de $y_p$-termen leveren precies $f(x)$ op, samen dus $f(x)$. ✓

### De methode van onbepaalde coëfficiënten

Gok een vorm voor $y_p$ die "lijkt" op $f(x)$, met nog onbekende coëfficiënten, en bepaal die coëfficiënten door in te vullen:

| Vorm van $f(x)$ | Gok voor $y_p$ |
|---|---|
| polynoom van graad $n$ | polynoom van graad $n$ |
| $e^{kx}$ | $Ae^{kx}$ |
| $\sin(kx)$ of $\cos(kx)$ | $A\sin(kx)+B\cos(kx)$ |

### Een volledig uitgewerkt voorbeeld

**Bepaal een particuliere oplossing van $y''-3y'+2y=e^{3x}$.**

**Stap 1.** Gok $y_p = Ae^{3x}$ (want $f(x)=e^{3x}$). Dan $y_p'=3Ae^{3x}$, $y_p''=9Ae^{3x}$.

**Stap 2.** Vul in:
$$9Ae^{3x} - 3(3Ae^{3x}) + 2Ae^{3x} = e^{3x} \implies (9A-9A+2A)e^{3x} = e^{3x} \implies 2Ae^{3x}=e^{3x}$$

**Stap 3.** Los op: $A=\frac12$, dus $y_p = \frac12e^{3x}$.

Combineer je dit met de homogene oplossing $y_h=C_1e^x+C_2e^{2x}$ uit hoofdstuk 43, dan is de volledige algemene oplossing $y = C_1e^x+C_2e^{2x}+\frac12e^{3x}$.
""",
        "summary": "De algemene oplossing van $ay''+by'+cy=f(x)$ is $y=y_h+y_p$: de homogene oplossing plus één particuliere oplossing. Gok voor $y_p$ een vorm die lijkt op $f(x)$ (polynoom, exponentieel, of sin/cos), en bepaal de coëfficiënten door in te vullen.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 2,
                "question": r"Bepaal een particuliere oplossing van $y''-5y'+6y=x$.",
                "hints": [
                    "Gok $y_p=Ax+B$ (een polynoom van dezelfde graad als $f(x)=x$). Bereken $y_p'$ en $y_p''$.",
                    "Vul in, en vergelijk de coëfficiënten van $x$ en de constante term apart om $A$ en $B$ te vinden.",
                ],
                "full_solution": r"""$y_p=Ax+B$, $y_p'=A$, $y_p''=0$.
$$0 - 5A + 6(Ax+B) = x \implies 6Ax + (6B-5A) = x$$
Coëfficiënt van $x$: $6A=1 \implies A=\frac16$. Constante term: $6B-5(\frac16)=0 \implies B=\frac{5}{36}$.
$$y_p = \frac{x}{6}+\frac{5}{36}$$""",
                "answer_type": "open",
            },
            {
                "order_index": 2, "difficulty": 1,
                "question": r"Bepaal een particuliere oplossing van $y''+4y=8$.",
                "hints": [
                    "Het rechterlid is een constante, dus gok $y_p=A$ (constant), zodat $y_p'=y_p''=0$.",
                ],
                "full_solution": r"""$y_p=A$, $y_p'=y_p''=0$.
$$0 + 4A = 8 \implies A=2$$
$$y_p = 2$$""",
                "answer_type": "numeric",
                "correct_answer": "2",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Bepaal een particuliere oplossing van $y''-4y'+4y=e^{3x}$.",
                "hints": [
                    "Gok $y_p=Ae^{3x}$, bereken $y_p'$ en $y_p''$.",
                    "Vul in en los op voor $A$.",
                ],
                "full_solution": r"""$y_p=Ae^{3x}$, $y_p'=3Ae^{3x}$, $y_p''=9Ae^{3x}$.
$$9Ae^{3x} - 12Ae^{3x} + 4Ae^{3x} = e^{3x} \implies Ae^{3x}=e^{3x} \implies A=1$$
$$y_p = e^{3x}$$""",
                "answer_type": "expression",
                "correct_answer": "exp(3*x)",
            },
            {
                "order_index": 4, "difficulty": 2,
                "question": r"Geef de algemene oplossing van $y''-5y'+6y=x$, gebruikmakend van opgave 1 hierboven en de homogene oplossing $y_h=C_1e^{2x}+C_2e^{3x}$ (hoofdstuk 43, opgave 1).",
                "hints": [
                    "De algemene oplossing is $y=y_h+y_p$.",
                    "Tel de $y_h$ uit hoofdstuk 43 en de $y_p$ uit opgave 1 hierboven bij elkaar op.",
                ],
                "full_solution": r"""$$y = C_1e^{2x}+C_2e^{3x} + \frac{x}{6}+\frac{5}{36}$$""",
                "answer_type": "open",
            },
        ],
    },
    {
        "module_id": 5,
        "chapter_number": 45,
        "title": "Variatie van parameters",
        "theory_content": r"""
### Wat je al weet

Onbepaalde coëfficiënten (hoofdstuk 44) werkt goed, maar alleen als $f(x)$ een "nette" vorm heeft (polynoom, exponentieel, sin/cos). Voor iets als $f(x)=\tan(x)$ staat er geen gok klaar in het rijtje.

### Een methode die altijd werkt: laat de constanten meebewegen

Stel de homogene oplossing is $y_h = C_1y_1(x) + C_2y_2(x)$ (met $y_1,y_2$ bekende functies uit hoofdstuk 43). Het idee van **variatie van parameters**: vervang de vaste constanten $C_1,C_2$ door **functies** $u_1(x), u_2(x)$, en zoek een particuliere oplossing van de vorm:
$$y_p = u_1(x)y_1(x) + u_2(x)y_2(x)$$
Met een handige extra eis (die het rekenwerk enorm vereenvoudigt: $u_1'y_1+u_2'y_2=0$) volgt na invullen in de oorspronkelijke vergelijking een oplosbaar stelsel voor $u_1'$ en $u_2'$:
$$u_1'y_1+u_2'y_2=0, \qquad u_1'y_1'+u_2'y_2'=f(x)$$
Met de **Wronskiaan** $W=y_1y_2'-y_2y_1'$ (die je ook al kende als een soort determinant, vergelijk hoofdstuk 34) is de oplossing van dit stelsel:
$$u_1' = \frac{-y_2f(x)}{W}, \qquad u_2' = \frac{y_1f(x)}{W}$$
Integreer $u_1'$ en $u_2'$, en je hebt $y_p$.

### Een volledig uitgewerkt voorbeeld

**Los op: $y''+y=\tan(x)$ (waarbij onbepaalde coëfficiënten niet werkt, want $\tan(x)$ staat niet in het rijtje).**

**Stap 1.** De homogene oplossing (karakteristieke vergelijking $r^2+1=0 \Rightarrow r=\pm i$) is $y_h=C_1\cos x+C_2\sin x$, dus $y_1=\cos x,\ y_2=\sin x$.

**Stap 2.** Bereken de Wronskiaan: $W = \cos x\cdot\cos x - \sin x\cdot(-\sin x) = \cos^2x+\sin^2x=1$.

**Stap 3.** Bereken $u_1'$ en $u_2'$ met $f(x)=\tan x$:
$$u_1' = -\sin x\tan x = -\frac{\sin^2x}{\cos x}, \qquad u_2' = \cos x\tan x = \sin x$$

**Stap 4.** Integreer: $u_2 = -\cos x$. Voor $u_1$: schrijf $-\frac{\sin^2x}{\cos x} = -\frac{1-\cos^2x}{\cos x} = -\sec x+\cos x$, dus $u_1 = -\ln|\sec x+\tan x|+\sin x$.

**Stap 5.** Stel $y_p$ samen:
$$y_p = u_1\cos x+u_2\sin x = \left(-\ln|\sec x+\tan x|+\sin x\right)\cos x + (-\cos x)\sin x = -\cos(x)\ln|\sec x+\tan x|$$
(de twee $\sin x\cos x$-termen vallen tegen elkaar weg).
""",
        "summary": "Variatie van parameters vervangt de constanten in $y_h=C_1y_1+C_2y_2$ door functies $u_1(x),u_2(x)$. Met de Wronskiaan $W=y_1y_2'-y_2y_1'$ vind je $u_1'=-y_2f/W$ en $u_2'=y_1f/W$; integreer die om $y_p=u_1y_1+u_2y_2$ te krijgen. Werkt voor elke $f(x)$, ook waar onbepaalde coëfficiënten faalt.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Bereken de Wronskiaan $W=y_1y_2'-y_2y_1'$ voor $y_1=\cos(x)$, $y_2=\sin(x)$ (de homogene oplossingen van $y''+y=0$).",
                "hints": [
                    "Bereken eerst $y_1'$ en $y_2'$.",
                    "Vul in de formule $W=y_1y_2'-y_2y_1'$ in en gebruik $\\sin^2+\\cos^2=1$.",
                ],
                "full_solution": r"""$y_1'=-\sin x$, $y_2'=\cos x$.
$$W = \cos x\cdot\cos x - \sin x\cdot(-\sin x) = \cos^2x+\sin^2x = 1$$""",
                "answer_type": "numeric",
                "correct_answer": "1",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Voor de vergelijking $y''+y=\sec(x)$ (met dezelfde $y_1,y_2,W$ als opgave 1), stel $u_1'$ en $u_2'$ op (je hoeft nog niet te integreren).",
                "hints": [
                    "Gebruik $u_1'=-y_2f/W$ en $u_2'=y_1f/W$ met $f(x)=\\sec(x)$ en $W=1$.",
                    "Vereenvoudig waar mogelijk (denk aan $\\sin(x)\\sec(x)=\\tan(x)$ en $\\cos(x)\\sec(x)=1$).",
                ],
                "full_solution": r"""$$u_1' = -\sin(x)\sec(x) = -\tan(x), \qquad u_2' = \cos(x)\sec(x) = 1$$""",
                "answer_type": "open",
            },
            {
                "order_index": 3, "difficulty": 1,
                "question": r"Los $u_2$ op uit opgave 2 (integreer $u_2'$).",
                "hints": [
                    "$u_2' = 1$: dit is een triviale integraal.",
                ],
                "full_solution": r"""$$u_2 = \int 1\,dx = x$$""",
                "answer_type": "expression",
                "correct_answer": "x",
            },
            {
                "order_index": 4, "difficulty": 2,
                "question": r"Los $u_1$ op uit opgave 2 (integreer $u_1'=-\tan(x)$).",
                "hints": [
                    "Schrijf $\\tan(x) = \\sin(x)/\\cos(x)$ en gebruik substitutie $w=\\cos(x)$.",
                    "Dit is dezelfde soort integraal als $\\int \\tan(x)\\,dx$, een standaardresultaat.",
                ],
                "full_solution": r"""$$\int -\tan(x)\,dx = -\int \frac{\sin x}{\cos x}\,dx$$
Substitutie $w=\cos x$, $dw=-\sin x\,dx$:
$$= \int \frac{dw}{w} = \ln|w| + C = \ln|\cos(x)| + C$$
Dus $u_1 = \ln|\cos(x)|$.""",
                "answer_type": "expression",
                "correct_answer": "ln(abs(cos(x)))",
            },
        ],
    },
    {
        "module_id": 5,
        "chapter_number": 46,
        "title": "Toepassingen: groei/verval, mengproblemen, mechanische trillingen",
        "theory_content": r"""
### Wat je al weet

Je hebt nu het volledige gereedschap: scheidbare ODE's (hoofdstuk 40), lineaire eerste-orde ODE's (hoofdstuk 41), en tweede-orde lineaire ODE's (hoofdstuk 43-45). Tijd om dat gereedschap op echte situaties los te laten.

### Exponentiële groei en verval

De simpelste en meest voorkomende ODE in de praktijk: een grootheid verandert met een snelheid **evenredig aan zichzelf**. Denk aan een bacteriekolonie (hoe meer bacteriën, hoe sneller de groei) of radioactief verval (hoe meer materiaal, hoe meer atomen er per tijdseenheid vervallen):
$$\frac{dy}{dt} = ky$$
Dit is scheidbaar (hoofdstuk 40) met oplossing $y(t) = y_0e^{kt}$, waarbij $y_0=y(0)$ de beginwaarde is. Voor $k>0$ heb je groei, voor $k<0$ verval.

### Mengproblemen

Een tank met vloeistof waar iets in- en uitstroomt levert typisch een **lineaire eerste-orde ODE** (hoofdstuk 41) op voor de hoeveelheid opgeloste stof $Q(t)$:
$$\frac{dQ}{dt} = (\text{instroomsnelheid}) - (\text{uitstroomsnelheid})$$
waarbij de uitstroomsnelheid meestal afhangt van de huidige concentratie (dus van $Q(t)$ zelf), wat precies de $y$-term in $y'+p(x)y=q(x)$ oplevert.

### Mechanische trillingen

Een massa aan een veer (zonder wrijving) voldoet aan Newtons wet $F=ma$, waarbij de veerkracht evenredig is met de uitwijking (wet van Hooke, $F=-kx$): $mx''=-kx$, oftewel $mx''+kx=0$. Dit is precies een **tweede-orde lineaire homogene ODE** (hoofdstuk 43) met complexe wortels: de oplossing is een trilling, $x(t)=C_1\cos(\omega t)+C_2\sin(\omega t)$ met $\omega=\sqrt{k/m}$.

### Een volledig uitgewerkt voorbeeld

**Een radioactieve stof vervalt met snelheid evenredig aan de aanwezige hoeveelheid, met vervalconstante $k=0{,}1$ per jaar. Bepaal de halveringstijd.**

**Stap 1.** Het model is $\dfrac{dN}{dt}=-kN$, met oplossing $N(t)=N_0e^{-kt}$ (zoals hierboven, met $k=0{,}1$).

**Stap 2.** De halveringstijd $T$ is het moment waarop nog maar de helft over is: $N(T)=\frac{N_0}{2}$.
$$\frac{N_0}{2} = N_0e^{-kT} \implies \frac12 = e^{-kT} \implies \ln\left(\frac12\right) = -kT \implies T = \frac{\ln 2}{k}$$

**Stap 3.** Vul $k=0{,}1$ in: $T = \dfrac{\ln 2}{0{,}1} = 10\ln 2 \approx 6{,}93$ jaar.
""",
        "summary": "Exponentiële groei/verval ($y'=ky$, scheidbaar) modelleert populaties en radioactief verval. Mengproblemen leiden tot lineaire eerste-orde ODE's. Massa-veersystemen ($mx''+kx=0$) leiden tot tweede-orde homogene ODE's met een trillingsoplossing.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Een bacteriekolonie groeit volgens $\dfrac{dN}{dt}=0{,}3N$, met $N(0)=100$. Bepaal $N(t)$.",
                "hints": [
                    "Gebruik het standaardresultaat $N(t)=N_0e^{kt}$ met $k=0{,}3$.",
                    "Vul de beginwaarde in voor $N_0$.",
                ],
                "full_solution": r"""$$N(t) = 100e^{0{,}3t}$$""",
                "answer_type": "expression",
                "correct_answer": "100*exp(0.3*t)",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Een radioactieve stof heeft een vervalconstante $k=0{,}1$ per jaar. Bepaal de halveringstijd (reproduceer de aanpak uit de theorie).",
                "hints": [
                    "Gebruik de formule $T=\\dfrac{\\ln2}{k}$ die in de theorie is afgeleid.",
                ],
                "full_solution": r"""$$T = \frac{\ln2}{0{,}1} = 10\ln2 \approx 6{,}93 \text{ jaar}$$""",
                "answer_type": "numeric",
                "correct_answer": "6.93",
            },
            {
                "order_index": 3, "difficulty": 3,
                "question": r"Een tank bevat $100$ L zoet water. Er stroomt zout water (concentratie $2$ g/L) in met $5$ L/min, en het (goed gemengde) mengsel stroomt met dezelfde snelheid weer uit. Stel de differentiaalvergelijking op voor de hoeveelheid zout $Q(t)$ (in gram) in de tank (je hoeft 'm niet op te lossen).",
                "hints": [
                    "De instroomsnelheid van zout is (concentratie instroom) $\\times$ (instroomsnelheid vloeistof) $= 2 \\times 5$.",
                    "De uitstroomsnelheid van zout is (concentratie in de tank, dus $Q(t)/100$) $\\times$ (uitstroomsnelheid vloeistof, ook 5 L/min, want het volume blijft constant).",
                ],
                "full_solution": r"""Instroom van zout: $2 \text{ g/L} \times 5 \text{ L/min} = 10$ g/min.

Uitstroom van zout: concentratie in de tank is $\dfrac{Q(t)}{100}$ g/L, dus uitstroom $= \dfrac{Q(t)}{100}\times5 = \dfrac{Q(t)}{20}$ g/min.

$$\frac{dQ}{dt} = 10 - \frac{Q}{20}$$
(Dit is een lineaire eerste-orde ODE, op te lossen met de methode uit hoofdstuk 41.)""",
                "answer_type": "open",
            },
            {
                "order_index": 4, "difficulty": 2,
                "question": r"Een massa-veersysteem zonder demping voldoet aan $x''+9x=0$. Bepaal de periode (trillingstijd) van de beweging.",
                "hints": [
                    "Stel de karakteristieke vergelijking op (hoofdstuk 43): $r^2+9=0$, en bepaal $\\omega$ uit de complexe wortels $r=\\pm\\omega i$.",
                    "De periode van $\\cos(\\omega t)$ en $\\sin(\\omega t)$ is $2\\pi/\\omega$.",
                ],
                "full_solution": r"""$r^2+9=0 \implies r=\pm3i$, dus $\omega=3$.

De oplossing is $x(t)=C_1\cos(3t)+C_2\sin(3t)$, met periode:
$$T = \frac{2\pi}{\omega} = \frac{2\pi}{3}$$""",
                "answer_type": "numeric",
                "correct_answer": "2*pi/3",
            },
        ],
    },
    {
        "module_id": 5,
        "chapter_number": 47,
        "title": "Stelsels ODE's en Laplace-transformatie",
        "theory_content": r"""
### Wat je al weet

Je hebt tweede-orde ODE's opgelost met de karakteristieke vergelijking (hoofdstuk 43), en je kent eigenwaarden van matrices (hoofdstuk 37, ook via een karakteristieke vergelijking $\det(A-\lambda I)=0$). Deze twee onderwerpen blijken nauw verbonden.

### Elke hogere-orde ODE is een stelsel van eerste-orde ODE's

Een truc die het bestuderen van ODE's enorm vereenvoudigt: elke tweede-orde ODE is te herschrijven als een **stelsel** van twee eerste-orde ODE's, door een hulpvariabele voor de afgeleide in te voeren. Voor $y''+by'+cy=0$: stel $x_1=y$ en $x_2=y'$. Dan is $x_1'=x_2$ (per definitie), en $x_2'=y''=-by'-cy=-bx_2-cx_1$. In matrixvorm:
$$\begin{pmatrix}x_1\\x_2\end{pmatrix}' = \begin{pmatrix}0&1\\-c&-b\end{pmatrix}\begin{pmatrix}x_1\\x_2\end{pmatrix}$$

Reken je de eigenwaarden van deze matrix uit (hoofdstuk 37), dan blijken die **exact** de wortels van de karakteristieke vergelijking $r^2+br+c=0$ te zijn: twee verschillende manieren om naar hetzelfde probleem te kijken, met precies dezelfde uitkomst.

### Een andere aanpak: de Laplace-transformatie

Een heel andere techniek om ODE's op te lossen is de **Laplace-transformatie**: een functie $f(t)$ wordt omgezet in een nieuwe functie van $s$:
$$\mathcal{L}\{f(t)\} = \int_0^\infty e^{-st}f(t)\,dt$$
(een oneigenlijke integraal, zoals je in hoofdstuk 15 hebt geleerd te berekenen). Het slimme: de Laplace-transformatie zet **differentiëren om in vermenigvuldigen**, waardoor een differentiaalvergelijking verandert in een gewone algebraïsche vergelijking in $s$, die je oplost en daarna terugvertaalt naar een functie van $t$.

### Een volledig uitgewerkt voorbeeld

**Herschrijf $y''-3y'+2y=0$ als stelsel, en vergelijk de eigenwaarden met de karakteristieke vergelijking.**

**Stap 1.** Stel $x_1=y,\ x_2=y'$. Dan $x_1'=x_2$, en $x_2'=y''=3y'-2y=3x_2-2x_1$.
$$\begin{pmatrix}x_1\\x_2\end{pmatrix}' = \begin{pmatrix}0&1\\-2&3\end{pmatrix}\begin{pmatrix}x_1\\x_2\end{pmatrix}$$

**Stap 2.** Bereken de eigenwaarden van deze matrix: $\det\begin{pmatrix}-\lambda&1\\-2&3-\lambda\end{pmatrix} = -\lambda(3-\lambda)+2 = \lambda^2-3\lambda+2=0$.

**Stap 3.** Dit is precies de karakteristieke vergelijking van hoofdstuk 43 voor deze ODE! De wortels zijn $\lambda=1,2$, exact gelijk aan de $r$-waarden die je met de directe methode zou vinden.
""",
        "summary": "Elke tweede-orde ODE is te herschrijven als een stelsel van eerste-orde ODE's; de eigenwaarden van de bijbehorende matrix zijn precies de wortels van de karakteristieke vergelijking. De Laplace-transformatie $\\mathcal{L}\\{f(t)\\}=\\int_0^\\infty e^{-st}f(t)dt$ is een alternatieve techniek die differentiëren omzet in algebra.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 2,
                "question": r"Herschrijf $y''-3y'+2y=0$ als een stelsel van twee eerste-orde vergelijkingen (met $x_1=y,\ x_2=y'$).",
                "hints": [
                    "$x_1'=x_2$ per definitie.",
                    "Los $y''$ op uit de oorspronkelijke vergelijking en schrijf het in termen van $x_1$ en $x_2$.",
                ],
                "full_solution": r"""$x_1'=x_2$. Uit $y''-3y'+2y=0$ volgt $y''=3y'-2y=3x_2-2x_1$, dus:
$$x_1'=x_2, \qquad x_2' = -2x_1+3x_2$$""",
                "answer_type": "open",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Bepaal de eigenwaarden van de matrix uit opgave 1, en vergelijk met de wortels van de karakteristieke vergelijking $r^2-3r+2=0$ (hoofdstuk 43).",
                "hints": [
                    "De matrix is $\\begin{pmatrix}0&1\\\\-2&3\\end{pmatrix}$. Stel $\\det(A-\\lambda I)=0$ op.",
                    "Vergelijk de resulterende vergelijking in $\\lambda$ met $r^2-3r+2=0$.",
                ],
                "full_solution": r"""$$\det\begin{pmatrix}-\lambda&1\\-2&3-\lambda\end{pmatrix} = -\lambda(3-\lambda)+2 = \lambda^2-3\lambda+2=0$$
Dit is exact dezelfde vergelijking als $r^2-3r+2=0$, met dezelfde wortels $\lambda=1,2$: de twee methodes (karakteristieke vergelijking direct, of via eigenwaarden van het stelsel) geven precies hetzelfde antwoord.""",
                "answer_type": "open",
            },
            {
                "order_index": 3, "difficulty": 1,
                "question": r"Gebruik de definitie om de Laplace-getransformeerde van $f(t)=1$ te bepalen.",
                "hints": [
                    "Werk $\\int_0^\\infty e^{-st}\\cdot1\\,dt$ uit als een oneigenlijke integraal (hoofdstuk 15): $\\lim_{b\\to\\infty}\\int_0^b e^{-st}dt$.",
                    "Neem aan dat $s>0$, zodat $e^{-sb}\\to0$ als $b\\to\\infty$.",
                ],
                "full_solution": r"""$$\mathcal{L}\{1\} = \int_0^\infty e^{-st}\,dt = \lim_{b\to\infty}\left[-\frac{1}{s}e^{-st}\right]_0^b = \lim_{b\to\infty}\left(-\frac{e^{-sb}}{s}+\frac1s\right) = \frac1s \quad (s>0)$$""",
                "answer_type": "expression",
                "correct_answer": "1/s",
            },
            {
                "order_index": 4, "difficulty": 2,
                "question": r"Gebruik de definitie om de Laplace-getransformeerde van $f(t)=e^{at}$ te bepalen.",
                "hints": [
                    "Werk $\\int_0^\\infty e^{-st}e^{at}\\,dt$ uit; combineer eerst de twee exponenten tot $e^{-(s-a)t}$.",
                    "Reken uit als een oneigenlijke integraal, net als opgave 3, nu met $s-a$ in plaats van $s$ (neem aan $s>a$).",
                ],
                "full_solution": r"""$$\mathcal{L}\{e^{at}\} = \int_0^\infty e^{-st}e^{at}\,dt = \int_0^\infty e^{-(s-a)t}\,dt = \frac{1}{s-a} \quad (s>a)$$
(Dezelfde berekening als opgave 3, met $s$ vervangen door $s-a$.)""",
                "answer_type": "expression",
                "correct_answer": "1/(s-a)",
            },
        ],
    },
]
