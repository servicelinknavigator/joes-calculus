# -*- coding: utf-8 -*-
"""Module III: Calculus 3 (hoofdstuk 22-30), zelfde 'vanaf nul opgebouwd'-aanpak."""

CHAPTERS_3 = [
    {
        "module_id": 3,
        "chapter_number": 22,
        "title": "Vectoren in de ruimte, in-/uitproduct, lijnen en vlakken in 3D",
        "theory_content": r"""
### Wat je al weet

Uit VWO B ken je vectoren in het platte vlak: een grootheid met lengte en richting, genoteerd als een getallenpaar $(a_x, a_y)$, met een inproduct $\vec{a}\cdot\vec{b} = a_xb_x + a_yb_y = |\vec a||\vec b|\cos(\theta)$.

### Eén dimensie erbij

Alles wat je van 2D-vectoren weet, werkt vrijwel ongewijzigd door in 3D: een vector wordt nu $(a_x,a_y,a_z)$, en het inproduct krijgt gewoon een derde term: $\vec a\cdot\vec b = a_xb_x+a_yb_y+a_zb_z$. Het inproduct blijft een **getal** (geen vector), en meet nog steeds hoezeer twee vectoren "dezelfde kant op wijzen".

### Nieuw in 3D: het uitproduct

In 3D is er een tweede soort vermenigvuldiging die in 2D geen zin heeft: het **uitproduct** (kruisproduct) $\vec a \times \vec b$. In tegenstelling tot het inproduct is de uitkomst hier zelf weer een **vector**, en wel eentje die loodrecht op zowel $\vec a$ als $\vec b$ staat (denk aan een schroef die je vanaf $\vec a$ naar $\vec b$ draait: die beweegt in de richting van $\vec a \times \vec b$). De lengte van $\vec a \times \vec b$ is gelijk aan de oppervlakte van het parallellogram opgespannen door $\vec a$ en $\vec b$.

$$\vec a \times \vec b = (a_yb_z - a_zb_y,\ a_zb_x-a_xb_z,\ a_xb_y-a_yb_x)$$

### Lijnen en vlakken in 3D

Een **lijn** in 3D leg je vast met een steunpunt $\vec p$ en een richtingsvector $\vec v$: elk punt op de lijn is $\vec r(t) = \vec p + t\vec v$ voor een of andere $t$ (net als de vectorvoorstelling van een lijn die je al kende, nu met een derde coördinaat).

Een **vlak** in 3D leg je vast met een punt $\vec p_0$ erop en een **normaalvector** $\vec n$ (loodrecht op het hele vlak). Een punt $\vec r=(x,y,z)$ ligt in het vlak precies als de verbindingsvector $\vec r - \vec p_0$ loodrecht op $\vec n$ staat, dus als $\vec n\cdot(\vec r-\vec p_0)=0$. Is $\vec n=(a,b,c)$, dan geeft dit de vlakvergelijking $ax+by+cz=d$ (met $d=\vec n\cdot\vec p_0$).

### Een volledig uitgewerkt voorbeeld

**Stel de vergelijking op van het vlak door het punt $(1,0,0)$ met normaalvector $\vec n=(2,3,-1)$.**

**Stap 1.** Gebruik $\vec n\cdot(\vec r - \vec p_0)=0$ met $\vec p_0=(1,0,0)$: $2(x-1)+3(y-0)-1(z-0)=0$.

**Stap 2.** Werk uit: $2x-2+3y-z=0$, dus $2x+3y-z=2$.
""",
        "summary": "In 3D werkt het inproduct hetzelfde als in 2D, met een extra term. Het uitproduct $\\vec a\\times\\vec b$ geeft een nieuwe vector loodrecht op beide, met lengte gelijk aan de oppervlakte van het opgespannen parallellogram. Een vlak leg je vast met een punt en een normaalvector.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Bereken het inproduct van $\vec a=(1,2,3)$ en $\vec b=(4,-1,2)$.",
                "hints": [
                    "Gebruik $\\vec a\\cdot\\vec b = a_xb_x+a_yb_y+a_zb_z$.",
                    "Tel de drie producten bij elkaar op.",
                ],
                "full_solution": r"""$$\vec a\cdot\vec b = 1(4)+2(-1)+3(2) = 4-2+6 = 8$$""",
                "answer_type": "numeric",
                "correct_answer": "8",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Bereken het uitproduct $\vec a\times\vec b$ van de standaardvectoren $\vec a=(1,0,0)$ en $\vec b=(0,1,0)$, en herken het resultaat.",
                "hints": [
                    "Gebruik de formule $\\vec a\\times\\vec b = (a_yb_z-a_zb_y,\\ a_zb_x-a_xb_z,\\ a_xb_y-a_yb_x)$.",
                    "Vul de coördinaten in en reken elke component apart uit.",
                ],
                "full_solution": r"""$$\vec a\times\vec b = (0\cdot0-0\cdot1,\ 0\cdot0-1\cdot0,\ 1\cdot1-0\cdot0) = (0,0,1)$$
Dit is precies de derde standaardvector, wat logisch is: het vlak opgespannen door de eerste twee standaardrichtingen heeft de derde als loodrechte normaal.""",
                "answer_type": "open",
            },
            {
                "order_index": 3, "difficulty": 1,
                "question": r"Stel de vectorvoorstelling op van de lijn door het punt $(1,2,3)$ met richtingsvector $(2,-1,0)$.",
                "hints": [
                    "Gebruik $\\vec r(t) = \\vec p + t\\vec v$ met $\\vec p$ het gegeven punt en $\\vec v$ de richting.",
                    "Schrijf elke coördinaat apart uit in termen van $t$.",
                ],
                "full_solution": r"""$$\vec r(t) = (1,2,3) + t(2,-1,0) = (1+2t,\ 2-t,\ 3)$$""",
                "answer_type": "open",
            },
            {
                "order_index": 4, "difficulty": 2,
                "question": r"Stel zelf de vergelijking op van het vlak door het punt $(0,1,2)$ met normaalvector $(1,-1,2)$ (reproduceer de aanpak uit de theorie).",
                "hints": [
                    "Gebruik $\\vec n\\cdot(\\vec r-\\vec p_0)=0$ met $\\vec p_0=(0,1,2)$.",
                    "Werk de haakjes uit tot de vorm $ax+by+cz=d$.",
                ],
                "full_solution": r"""$1(x-0) - 1(y-1) + 2(z-2) = 0$
$$x - y + 1 + 2z - 4 = 0 \implies x - y + 2z = 3$$""",
                "answer_type": "expression",
                "correct_answer": "x-y+2z=3",
            },
        ],
    },
    {
        "module_id": 3,
        "chapter_number": 23,
        "title": "Vectorwaardige functies en ruimtekrommen",
        "theory_content": r"""
### Wat je al weet

In hoofdstuk 20 beschreef je een kromme in het platte vlak parametrisch: $x(t), y(t)$. In hoofdstuk 22 heb je vectoren in 3D leren rekenen.

### Combineer die twee: een bewegend punt in de ruimte

Voeg een derde coördinaat toe en je krijgt een **vectorwaardige functie**: $\vec r(t) = (x(t), y(t), z(t))$, een pad dat een punt in de ruimte doorloopt terwijl $t$ varieert (bijvoorbeeld de tijd). Dit is exact hetzelfde idee als in hoofdstuk 20, nu gewoon met een dimensie erbij, en genoteerd als één vector in plaats van twee losse coördinaatfuncties.

### Afgeleide: snelheid

Je differentieert een vectorwaardige functie component-voor-component:
$$\vec r'(t) = (x'(t), y'(t), z'(t))$$
Dit is de **snelheidsvector**: hij wijst in de richting waarin het punt op dat moment beweegt. De **baansnelheid** (een gewoon getal, "hoe hard") is de lengte van die vector: $|\vec r'(t)| = \sqrt{x'(t)^2+y'(t)^2+z'(t)^2}$.

### Booglengte

Net als in hoofdstuk 20 (en hoofdstuk 11 daarvoor) tel je oneindig veel piepkleine stapjes langs de kromme op, nu met drie componenten in het Pythagoras-driehoekje:
$$L = \int_{t_1}^{t_2} |\vec r'(t)|\,dt = \int_{t_1}^{t_2} \sqrt{x'(t)^2+y'(t)^2+z'(t)^2}\,dt$$

### Een volledig uitgewerkt voorbeeld

**Bepaal de snelheidsvector en de baansnelheid van de schroeflijn (helix) $\vec r(t) = (\cos t, \sin t, t)$.**

**Stap 1.** Differentieer component-voor-component: $\vec r'(t) = (-\sin t, \cos t, 1)$.

**Stap 2.** Bereken de lengte (baansnelheid):
$$|\vec r'(t)| = \sqrt{(-\sin t)^2 + (\cos t)^2 + 1^2} = \sqrt{\sin^2t+\cos^2t+1} = \sqrt{1+1} = \sqrt2$$
De baansnelheid is dus constant $\sqrt2$, ook al draait het punt tegelijk rond én stijgt het gestaag: een mooi voorbeeld van hoe een vectorwaardige functie meerdere bewegingen tegelijk kan combineren.
""",
        "summary": "Een vectorwaardige functie $\\vec r(t)$ beschrijft een punt dat door de ruimte beweegt. Differentiëren gebeurt component-voor-component en geeft de snelheidsvector; de lengte daarvan is de baansnelheid, en die integreren over $t$ geeft de booglengte.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Bepaal $\vec r'(t)$ voor $\vec r(t) = (t^2, t^3, t)$.",
                "hints": [
                    "Differentieer elke component apart naar $t$.",
                ],
                "full_solution": r"""$$\vec r'(t) = (2t, 3t^2, 1)$$""",
                "answer_type": "open",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Bereken de snelheidsvector van $\vec r(t) = (\cos(2t), \sin(2t), 3t)$ op $t=0$.",
                "hints": [
                    "Differentieer eerst component-voor-component (denk aan de kettingregel bij $\\cos(2t)$ en $\\sin(2t)$).",
                    "Vul daarna $t=0$ in.",
                ],
                "full_solution": r"""$\vec r'(t) = (-2\sin(2t), 2\cos(2t), 3)$.
$$\vec r'(0) = (-2\sin(0), 2\cos(0), 3) = (0, 2, 3)$$""",
                "answer_type": "open",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Bereken de baansnelheid $|\vec r'(t)|$ van $\vec r(t)=(t, t^2, 0)$ als functie van $t$.",
                "hints": [
                    "Bepaal eerst $\\vec r'(t)$.",
                    "Gebruik $|\\vec r'(t)| = \\sqrt{x'(t)^2+y'(t)^2+z'(t)^2}$.",
                ],
                "full_solution": r"""$\vec r'(t) = (1, 2t, 0)$.
$$|\vec r'(t)| = \sqrt{1^2+(2t)^2+0^2} = \sqrt{1+4t^2}$$""",
                "answer_type": "expression",
                "correct_answer": "sqrt(1+4t^2)",
            },
            {
                "order_index": 4, "difficulty": 2,
                "question": r"Bereken de booglengte van de helix $\vec r(t)=(\cos t, \sin t, t)$ voor $0 \le t \le 2\pi$ (gebruik de baansnelheid uit de theorie).",
                "hints": [
                    "In de theorie is al berekend dat $|\\vec r'(t)|=\\sqrt2$ (constant).",
                    "Integreer die constante snelheid over het gegeven interval.",
                ],
                "full_solution": r"""$$L = \int_0^{2\pi} \sqrt2\,dt = 2\pi\sqrt2$$""",
                "answer_type": "numeric",
                "correct_answer": "2*pi*sqrt(2)",
            },
        ],
    },
    {
        "module_id": 3,
        "chapter_number": 24,
        "title": "Functies van meerdere variabelen, partiële afgeleiden",
        "theory_content": r"""
### Wat je al weet

Tot nu toe hingen je functies af van één variabele, $f(x)$, met een grafiek als een kromme lijn.

### Eén variabele erbij: een landschap in plaats van een lijn

Een functie $f(x,y)$ hangt af van **twee** variabelen. De grafiek is nu geen lijn meer, maar een **oppervlak** in de ruimte: voor elk punt $(x,y)$ in het platte vlak geeft $f(x,y)$ een hoogte $z$. Denk aan een landschap: $x$ en $y$ zijn je positie op de kaart, $f(x,y)$ is de hoogte op die plek.

### Hoe differentieer je zoiets?

Bij een landschap kun je op elk punt in twee (of meer) richtingen lopen, en de helling hangt af van welke kant je op loopt. De simpelste vraag: wat is de helling als je precies in de $x$-richting loopt (dus $y$ vasthoudt), en wat is de helling als je precies in de $y$-richting loopt (dus $x$ vasthoudt)?

Dat zijn de **partiële afgeleiden**: $\dfrac{\partial f}{\partial x}$ is de gewone afgeleide van $f$ naar $x$, waarbij je $y$ gewoon behandelt als een constante (en omgekeerd voor $\dfrac{\partial f}{\partial y}$). Alle differentiatieregels die je al kent (product-, quotiënt-, kettingregel) blijven gewoon werken, je "bevriest" simpelweg de andere variabele.

### Een volledig uitgewerkt voorbeeld

**Bepaal $\dfrac{\partial f}{\partial x}$ en $\dfrac{\partial f}{\partial y}$ voor $f(x,y) = x^2y + 3y^3$.**

**Stap 1 ($\partial f/\partial x$):** behandel $y$ als een constante. De term $x^2y$ is dan "constante $y$ keer $x^2$", met afgeleide $2xy$. De term $3y^3$ bevat helemaal geen $x$, dus die is (net als elke constante) $0$ bij differentiëren naar $x$.
$$\frac{\partial f}{\partial x} = 2xy$$

**Stap 2 ($\partial f/\partial y$):** behandel nu $x$ als een constante. De term $x^2y$ wordt "constante $x^2$ keer $y$", met afgeleide $x^2$. De term $3y^3$ differentieert gewoon tot $9y^2$.
$$\frac{\partial f}{\partial y} = x^2 + 9y^2$$
""",
        "summary": "Bij een functie van meerdere variabelen bevries je alle andere variabelen en differentieer je gewoon naar de ene variabele die je interesseert: dat is een partiële afgeleide $\\partial f/\\partial x$. Alle bekende differentiatieregels blijven gelden.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Bepaal $\dfrac{\partial f}{\partial x}$ en $\dfrac{\partial f}{\partial y}$ voor $f(x,y) = x^3y^2$.",
                "hints": [
                    "Voor $\\partial f/\\partial x$: behandel $y^2$ als een constante voorfactor.",
                    "Voor $\\partial f/\\partial y$: behandel $x^3$ als een constante voorfactor.",
                ],
                "full_solution": r"""$$\frac{\partial f}{\partial x} = 3x^2y^2, \qquad \frac{\partial f}{\partial y} = 2x^3y$$""",
                "answer_type": "open",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Bepaal $\dfrac{\partial f}{\partial x}$ voor $f(x,y) = \sin(xy)$.",
                "hints": [
                    "Gebruik de kettingregel: de buitenfunctie is $\\sin(\\cdot)$, de binnenfunctie is $xy$.",
                    "Behandel $y$ als constante bij het differentiëren van de binnenfunctie $xy$ naar $x$.",
                ],
                "full_solution": r"""Binnenfunctie $xy$ naar $x$ differentiëren (met $y$ constant) geeft $y$.
$$\frac{\partial f}{\partial x} = y\cos(xy)$$""",
                "answer_type": "expression",
                "correct_answer": "y*cos(x*y)",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Bepaal $\dfrac{\partial f}{\partial x}$ en $\dfrac{\partial f}{\partial y}$ voor $f(x,y) = e^x\cos(y)$.",
                "hints": [
                    "Voor $\\partial f/\\partial x$: $\\cos(y)$ is een constante voorfactor, differentieer $e^x$ gewoon.",
                    "Voor $\\partial f/\\partial y$: $e^x$ is een constante voorfactor, differentieer $\\cos(y)$ gewoon.",
                ],
                "full_solution": r"""$$\frac{\partial f}{\partial x} = e^x\cos(y), \qquad \frac{\partial f}{\partial y} = -e^x\sin(y)$$""",
                "answer_type": "open",
            },
            {
                "order_index": 4, "difficulty": 2,
                "question": r"Bepaal de tweede partiële afgeleide $\dfrac{\partial^2 f}{\partial x^2}$ van $f(x,y) = x^3y + 2xy^2$.",
                "hints": [
                    "Bepaal eerst $\\partial f/\\partial x$ (met $y$ als constante).",
                    "Differentieer dat resultaat nog een keer naar $x$.",
                ],
                "full_solution": r"""$\dfrac{\partial f}{\partial x} = 3x^2y + 2y^2$.
$$\frac{\partial^2 f}{\partial x^2} = 6xy$$""",
                "answer_type": "expression",
                "correct_answer": "6*x*y",
            },
        ],
    },
    {
        "module_id": 3,
        "chapter_number": 25,
        "title": "Gradiënt en richtingsafgeleide",
        "theory_content": r"""
### Wat je al weet

Uit hoofdstuk 24 ken je de partiële afgeleiden $\partial f/\partial x$ en $\partial f/\partial y$: de helling precies in de $x$-richting en precies in de $y$-richting.

### Maar wat als je schuin loopt?

Bij een landschap loop je zelden precies in de $x$- of $y$-richting. Hoe steil is het als je een willekeurige richting in loopt? Het antwoord blijkt verrassend compact: bundel de twee partiële afgeleiden samen tot één vector, de **gradiënt**:
$$\nabla f = \left(\frac{\partial f}{\partial x},\ \frac{\partial f}{\partial y}\right)$$
Deze vector heeft een mooie meetkundige betekenis: hij wijst in de richting waarin $f$ het **snelst stijgt**, en zijn lengte is precies die maximale stijgsnelheid.

### De richtingsafgeleide

Wil je de hellingssnelheid in een specifieke richting $\vec u$ (een vector met lengte $1$), dan gebruik je de **richtingsafgeleide**:
$$D_{\vec u}f = \nabla f \cdot \vec u$$
Dit is gewoon het inproduct van de gradiënt met de gekozen richting. Vul je $\vec u$ in als de $x$-richting $(1,0)$ in, dan krijg je simpelweg $\partial f/\partial x$ terug, dat past dus precies bij wat je al wist.

### Een volledig uitgewerkt voorbeeld

**Bepaal de richtingsafgeleide van $f(x,y)=x^2+y^2$ in het punt $(1,1)$, in de richting van de vector $(1,0)$.**

**Stap 1.** Bereken de gradiënt: $\nabla f = (2x, 2y)$, dus in $(1,1)$: $\nabla f(1,1) = (2,2)$.

**Stap 2.** Controleer dat de richting al lengte $1$ heeft: $(1,0)$ heeft lengte $1$. ✓

**Stap 3.** Bereken het inproduct:
$$D_{(1,0)}f(1,1) = (2,2)\cdot(1,0) = 2$$
Dit klopt met $\partial f/\partial x$ in $(1,1)$, wat je al kende: precies zoals verwacht, want $(1,0)$ is de $x$-richting.
""",
        "summary": "De gradiënt $\\nabla f = (\\partial f/\\partial x, \\partial f/\\partial y)$ wijst in de richting van de snelste stijging. De richtingsafgeleide $D_{\\vec u}f = \\nabla f \\cdot \\vec u$ (met $\\vec u$ een eenheidsvector) geeft de stijgsnelheid in een willekeurige richting.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Bepaal $\nabla f$ voor $f(x,y)=x^2y-y^3$ in het punt $(2,1)$.",
                "hints": [
                    "Bereken eerst $\\partial f/\\partial x$ en $\\partial f/\\partial y$ als functies van $x$ en $y$.",
                    "Vul daarna $(x,y)=(2,1)$ in bij beide componenten.",
                ],
                "full_solution": r"""$\nabla f = (2xy,\ x^2-3y^2)$. In $(2,1)$: $(2\cdot2\cdot1,\ 4-3\cdot1) = (4,1)$.""",
                "answer_type": "open",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Bereken de richtingsafgeleide van $f(x,y)=x^2+y^2$ in het punt $(1,2)$, in de richting van de vector $(1,1)$.",
                "hints": [
                    "De vector $(1,1)$ heeft geen lengte $1$: normaliseer hem eerst tot $\\vec u = \\frac{1}{\\sqrt2}(1,1)$.",
                    "Bereken $\\nabla f(1,2)$ en neem daarna het inproduct met $\\vec u$.",
                ],
                "full_solution": r"""$\nabla f = (2x,2y)$, in $(1,2)$: $(2,4)$. Genormaliseerde richting: $\vec u = \frac{1}{\sqrt2}(1,1)$.
$$D_{\vec u}f = (2,4)\cdot\frac{1}{\sqrt2}(1,1) = \frac{2+4}{\sqrt2} = \frac{6}{\sqrt2} = 3\sqrt2$$""",
                "answer_type": "numeric",
                "correct_answer": "3*sqrt(2)",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"In welke richting stijgt $f(x,y)=xy$ het snelst in het punt $(2,3)$? Geef de (niet per se genormaliseerde) richting.",
                "hints": [
                    "De richting van snelste stijging is precies de richting van de gradiënt zelf.",
                    "Bereken $\\nabla f(2,3)$.",
                ],
                "full_solution": r"""$\nabla f = (y,x)$. In $(2,3)$: $\nabla f(2,3) = (3,2)$.

De functie stijgt het snelst in de richting van de vector $(3,2)$ (eventueel te normaliseren tot lengte 1 door te delen door $\sqrt{13}$).""",
                "answer_type": "open",
            },
            {
                "order_index": 4, "difficulty": 3,
                "question": r"Bepaal de vergelijking van het raakvlak aan de grafiek van $f(x,y)=x^2+y^2$ in het punt $(1,1,2)$.",
                "hints": [
                    "Het raakvlak heeft de vorm $z = f(a,b) + f_x(a,b)(x-a) + f_y(a,b)(y-b)$, met $(a,b)=(1,1)$.",
                    "Bereken $f_x=\\partial f/\\partial x$ en $f_y=\\partial f/\\partial y$ in $(1,1)$.",
                ],
                "full_solution": r"""$f_x=2x$, $f_y=2y$. In $(1,1)$: $f_x=2$, $f_y=2$, en $f(1,1)=2$.
$$z = 2 + 2(x-1) + 2(y-1) = 2x+2y-2$$""",
                "answer_type": "expression",
                "correct_answer": "z=2*x+2*y-2",
            },
        ],
    },
    {
        "module_id": 3,
        "chapter_number": 26,
        "title": "Dubbele integralen",
        "theory_content": r"""
### Wat je al weet

Uit hoofdstuk 9 ken je de bepaalde integraal $\int_a^b f(x)\,dx$ als "oppervlakte onder een kromme": je snijdt het gebied onder $f$ in dunne verticale reepjes en telt ze op.

### Van oppervlakte naar inhoud

Bij een functie van twee variabelen $f(x,y)$ (hoofdstuk 24) is de grafiek een oppervlak. Vraag je nu naar de **inhoud** tussen dat oppervlak en het $xy$-vlak, boven een gebied $R$, dan gebruik je precies dezelfde denkwijze: snijd het gebied $R$ in piepkleine rechthoekjes met oppervlakte $dA$, vermenigvuldig elk met de hoogte $f(x,y)$ erboven, en tel alles op. Dit heet een **dubbele integraal**:
$$\iint_R f(x,y)\,dA$$

### Hoe reken je dat uit? Eén variabele tegelijk

Een dubbele integraal over een rechthoekig gebied bereken je als een **herhaalde integraal**: eerst integreer je naar één variabele (de andere hou je vast, precies zoals bij een partiële afgeleide), en daarna integreer je het resultaat naar de andere variabele.
$$\iint_R f(x,y)\,dA = \int_c^d \left(\int_a^b f(x,y)\,dx\right)dy$$

### Een volledig uitgewerkt voorbeeld

**Bereken $\displaystyle\int_0^1\int_0^2 xy\,dy\,dx$.**

**Stap 1 (binnenste integraal, naar $y$, met $x$ vast):**
$$\int_0^2 xy\,dy = x\left[\frac{y^2}{2}\right]_0^2 = x\cdot 2 = 2x$$

**Stap 2 (buitenste integraal, naar $x$):**
$$\int_0^1 2x\,dx = \left[x^2\right]_0^1 = 1$$
""",
        "summary": "Een dubbele integraal $\\iint_R f(x,y)\\,dA$ berekent een inhoud, net zoals een gewone integraal een oppervlakte berekent. Je rekent 'm uit als een herhaalde integraal: eerst naar de ene variabele (de andere vasthoudend), dan naar de andere.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Bereken $\displaystyle\int_0^1\int_0^2 (x+y)\,dy\,dx$.",
                "hints": [
                    "Werk eerst de binnenste integraal uit naar $y$, met $x$ vast.",
                    "Werk daarna de buitenste integraal uit naar $x$.",
                ],
                "full_solution": r"""Binnenste: $\int_0^2(x+y)\,dy = \left[xy+\frac{y^2}{2}\right]_0^2 = 2x+2$.

Buitenste: $\int_0^1(2x+2)\,dx = \left[x^2+2x\right]_0^1 = 1+2=3$.""",
                "answer_type": "numeric",
                "correct_answer": "3",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Bereken $\displaystyle\int_0^2\int_0^1 x^2y\,dx\,dy$.",
                "hints": [
                    "Hier integreer je eerst naar $x$ (met $y$ vast), dan naar $y$.",
                    "Let op de volgorde van de grenzen: de binnenste integraal loopt over $x$ van 0 tot 1.",
                ],
                "full_solution": r"""Binnenste ($naar x$): $\int_0^1 x^2y\,dx = y\left[\frac{x^3}{3}\right]_0^1 = \frac{y}{3}$.

Buitenste (naar $y$): $\int_0^2 \frac{y}{3}\,dy = \left[\frac{y^2}{6}\right]_0^2 = \frac{4}{6}=\frac23$.""",
                "answer_type": "numeric",
                "correct_answer": "2/3",
            },
            {
                "order_index": 3, "difficulty": 1,
                "question": r"Bereken de dubbele integraal van $f(x,y)=1$ over de rechthoek $[0,3]\times[0,2]$, en interpreteer het resultaat.",
                "hints": [
                    "Als $f(x,y)=1$ overal, wat stelt de dubbele integraal dan gewoon voor (denk aan de definitie: hoogte 1 maal oppervlakte van elk stukje)?",
                    "Bereken de oppervlakte van de rechthoek direct.",
                ],
                "full_solution": r"""$$\iint_R 1\,dA = \int_0^2\int_0^3 1\,dx\,dy = \int_0^2 3\,dy = 6$$
De uitkomst is gewoon de oppervlakte van het gebied $R$ zelf ($3\times2=6$): met hoogte $1$ overal is de "inhoud" numeriek gelijk aan de grondoppervlakte.""",
                "answer_type": "numeric",
                "correct_answer": "6",
            },
            {
                "order_index": 4, "difficulty": 3,
                "question": r"Bereken $\displaystyle\int_0^1\int_0^x xy\,dy\,dx$ (let op: de bovengrens van de binnenste integraal is $x$, geen getal).",
                "hints": [
                    "Werk eerst de binnenste integraal naar $y$ uit, van $0$ tot $x$, met $x$ als constante behandeld.",
                    "Het resultaat is een functie van $x$; integreer die daarna naar $x$ van 0 tot 1.",
                ],
                "full_solution": r"""Binnenste: $\int_0^x xy\,dy = x\left[\frac{y^2}{2}\right]_0^x = x\cdot\frac{x^2}{2} = \frac{x^3}{2}$.

Buitenste: $\int_0^1 \frac{x^3}{2}\,dx = \frac12\left[\frac{x^4}{4}\right]_0^1 = \frac18$.""",
                "answer_type": "numeric",
                "correct_answer": "1/8",
            },
        ],
    },
    {
        "module_id": 3,
        "chapter_number": 27,
        "title": "Drievoudige integralen, cilinder- en bolcoördinaten",
        "theory_content": r"""
### Wat je al weet

Een dubbele integraal (hoofdstuk 26) berekent een inhoud door een gebied in het platte vlak op te delen in piepkleine stukjes oppervlakte. Poolcoördinaten (hoofdstuk 21) beschrijven een punt via afstand en hoek in plaats van $x,y$.

### Nog een dimensie erbij

Een **drievoudige integraal** $\iiint_V f(x,y,z)\,dV$ deelt een volume $V$ in de ruimte op in piepkleine blokjes $dV$, precies dezelfde denkwijze als een dubbele integraal, nu één stap verder. Bij een rechthoekig blok is $dV=dx\,dy\,dz$, en je integreert net als bij een dubbele integraal drie keer na elkaar, telkens één variabele tegelijk.

### Cilindercoördinaten

Voor gebieden met cirkelsymmetrie rond een as (bijvoorbeeld een cilinder) is het handiger om poolcoördinaten te gebruiken voor $x,y$, en $z$ gewoon te laten staan:
$$x=r\cos\theta,\quad y=r\sin\theta,\quad z=z, \qquad dV = r\,dr\,d\theta\,dz$$
(De factor $r$ komt uit dezelfde reden als bij poolcoördinaten in hoofdstuk 21: een "taartpuntje" met straal $r$ heeft een grotere oppervlakte naarmate $r$ groter is.)

### Bolcoördinaten

Voor gebieden met symmetrie rond een punt (zoals een bol) gebruik je **bolcoördinaten**: de afstand tot de oorsprong $\rho$, de hoek $\varphi$ vanaf de positieve $z$-as, en de hoek $\theta$ in het $xy$-vlak (net als bij poolcoördinaten):
$$x=\rho\sin\varphi\cos\theta,\quad y=\rho\sin\varphi\sin\theta,\quad z=\rho\cos\varphi, \qquad dV = \rho^2\sin\varphi\,d\rho\,d\varphi\,d\theta$$

### Een volledig uitgewerkt voorbeeld

**Bereken de inhoud van een bol met straal $3$ met een drievoudige integraal in bolcoördinaten, en controleer met de bekende formule.**

**Stap 1.** Voor een volledige bol loopt $\rho$ van $0$ tot $3$, $\varphi$ van $0$ tot $\pi$, en $\theta$ van $0$ tot $2\pi$.

**Stap 2.** Stel de integraal op en splits in drie losse factoren (want de integrand $\rho^2\sin\varphi$ splitst netjes):
$$V = \int_0^{2\pi}\int_0^\pi\int_0^3 \rho^2\sin\varphi\,d\rho\,d\varphi\,d\theta = \left(\int_0^{2\pi}d\theta\right)\left(\int_0^\pi\sin\varphi\,d\varphi\right)\left(\int_0^3\rho^2\,d\rho\right)$$

**Stap 3.** Bereken elke factor: $\int_0^{2\pi}d\theta=2\pi$; $\int_0^\pi\sin\varphi\,d\varphi=[-\cos\varphi]_0^\pi=2$; $\int_0^3\rho^2\,d\rho=\left[\frac{\rho^3}{3}\right]_0^3=9$.

**Stap 4.** Vermenigvuldig: $V = 2\pi \cdot 2 \cdot 9 = 36\pi$. Controle met de bekende formule: $\frac43\pi r^3 = \frac43\pi(3)^3 = 36\pi$. ✓
""",
        "summary": "Een drievoudige integraal berekent een volume door de ruimte in piepkleine blokjes op te delen. Bij cirkel- of bolsymmetrie zijn cilinder- of bolcoördinaten handiger dan $x,y,z$, met $dV=r\\,dr\\,d\\theta\\,dz$ respectievelijk $dV=\\rho^2\\sin\\varphi\\,d\\rho\\,d\\varphi\\,d\\theta$.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Bereken $\displaystyle\int_0^1\int_0^1\int_0^1 xyz\,dz\,dy\,dx$.",
                "hints": [
                    "De integrand splitst netjes in drie factoren die elk maar van één variabele afhangen.",
                    "Bereken $\\int_0^1 x\\,dx$, $\\int_0^1 y\\,dy$ en $\\int_0^1 z\\,dz$ apart en vermenigvuldig de uitkomsten.",
                ],
                "full_solution": r"""$$\int_0^1 x\,dx \cdot \int_0^1 y\,dy \cdot \int_0^1 z\,dz = \frac12\cdot\frac12\cdot\frac12 = \frac18$$""",
                "answer_type": "numeric",
                "correct_answer": "1/8",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Bereken de inhoud van een cilinder met straal $2$ en hoogte $5$ met een drievoudige integraal in cilindercoördinaten, en controleer met de bekende formule $\pi r^2 h$.",
                "hints": [
                    "$r$ loopt van $0$ tot $2$, $\\theta$ van $0$ tot $2\\pi$, $z$ van $0$ tot $5$. Vergeet de factor $r$ in $dV$ niet.",
                    "Splits de integraal weer in drie losse factoren, net als in het voorbeeld.",
                ],
                "full_solution": r"""$$V = \int_0^5\int_0^{2\pi}\int_0^2 r\,dr\,d\theta\,dz = \left(\int_0^5 dz\right)\left(\int_0^{2\pi}d\theta\right)\left(\int_0^2 r\,dr\right) = 5\cdot 2\pi \cdot 2 = 20\pi$$
Controle: $\pi r^2 h = \pi(2)^2(5) = 20\pi$. ✓""",
                "answer_type": "numeric",
                "correct_answer": "20*pi",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Zet het punt $(x,y,z)=(1,1,1)$ om naar bolcoördinaten.",
                "hints": [
                    "Bereken $\\rho=\\sqrt{x^2+y^2+z^2}$.",
                    "Voor $\\theta$ gebruik je $\\tan\\theta=y/x$ (net als bij poolcoördinaten); voor $\\varphi$ gebruik je $\\cos\\varphi = z/\\rho$.",
                ],
                "full_solution": r"""$\rho = \sqrt{1+1+1} = \sqrt3$.

$\theta$: $\tan\theta = 1/1=1$, en het punt ligt in het eerste kwadrant van het $xy$-vlak, dus $\theta=\pi/4$.

$\varphi$: $\cos\varphi = z/\rho = 1/\sqrt3$, dus $\varphi = \arccos(1/\sqrt3)$.

$(\rho,\varphi,\theta) = \left(\sqrt3,\ \arccos(1/\sqrt3),\ \pi/4\right)$.""",
                "answer_type": "open",
            },
            {
                "order_index": 4, "difficulty": 2,
                "question": r"Bereken zelf de inhoud van een bol met straal $2$ met een drievoudige integraal in bolcoördinaten (reproduceer de aanpak uit de theorie met een andere straal), en controleer met $\frac43\pi r^3$.",
                "hints": [
                    "$\\rho$ loopt nu van $0$ tot $2$; $\\varphi$ van $0$ tot $\\pi$, $\\theta$ van $0$ tot $2\\pi$, net als in het voorbeeld.",
                    "Splits weer in drie factoren: $\\int_0^{2\\pi}d\\theta$, $\\int_0^\\pi\\sin\\varphi\\,d\\varphi$, en $\\int_0^2\\rho^2\\,d\\rho$.",
                ],
                "full_solution": r"""$$V = \left(\int_0^{2\pi}d\theta\right)\left(\int_0^\pi\sin\varphi\,d\varphi\right)\left(\int_0^2\rho^2\,d\rho\right) = 2\pi \cdot 2 \cdot \frac{8}{3} = \frac{32\pi}{3}$$
Controle: $\frac43\pi(2)^3 = \frac{32\pi}{3}$. ✓""",
                "answer_type": "numeric",
                "correct_answer": "32*pi/3",
            },
        ],
    },
    {
        "module_id": 3,
        "chapter_number": 28,
        "title": "Vectorvelden en lijnintegralen",
        "theory_content": r"""
### Wat je al weet

Een vectorwaardige functie $\vec r(t)$ (hoofdstuk 23) hangt af van één variabele en beschrijft een pad. Het inproduct van twee vectoren ken je uit hoofdstuk 22.

### Een vector op elk punt van de ruimte

Een **vectorveld** $\vec F(x,y)$ kent aan **elk punt** van het vlak een vector toe (in plaats van aan elke waarde van $t$, zoals bij $\vec r(t)$). Denk aan een windkaart: op elk punt van de kaart staat een pijltje voor windrichting en -snelheid, of een krachtveld zoals de zwaartekracht.

### Werk langs een pad: de lijnintegraal

Stel je beweegt langs een kromme $\vec r(t)$ door zo'n vectorveld (bijvoorbeeld een krachtveld). Hoeveel "werk" verricht het veld op je terwijl je beweegt? Op elk moment telt alleen het stukje van de kracht dat in je bewegingsrichting wijst (het inproduct met je snelheidsvector $\vec r'(t)$). Tel dat op langs het hele pad:
$$\int_C \vec F\cdot d\vec r = \int_{t_1}^{t_2} \vec F(\vec r(t)) \cdot \vec r'(t)\,dt$$

**Stappenplan:** vul de kromme $\vec r(t)$ in het vectorveld $\vec F$ in, bereken $\vec r'(t)$, neem het inproduct, en integreer naar $t$.

### Een volledig uitgewerkt voorbeeld

**Bereken de lijnintegraal van $\vec F(x,y)=(-y,x)$ langs de kwartcirkel $\vec r(t)=(\cos t,\sin t)$, $0\le t\le \frac{\pi}{2}$.**

**Stap 1.** Bereken $\vec r'(t) = (-\sin t, \cos t)$.

**Stap 2.** Vul de kromme in het vectorveld in: $\vec F(\vec r(t)) = (-\sin t, \cos t)$.

**Stap 3.** Neem het inproduct: $\vec F(\vec r(t))\cdot \vec r'(t) = (-\sin t)(-\sin t) + (\cos t)(\cos t) = \sin^2t+\cos^2t = 1$.

**Stap 4.** Integreer: $\displaystyle\int_0^{\pi/2} 1\,dt = \frac{\pi}{2}$.
""",
        "summary": "Een vectorveld kent een vector toe aan elk punt van de ruimte. De lijnintegraal $\\int_C \\vec F\\cdot d\\vec r = \\int \\vec F(\\vec r(t))\\cdot\\vec r'(t)\\,dt$ telt op hoeveel van het veld in de bewegingsrichting langs een kromme wijst, bijvoorbeeld het verrichte werk.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Bereken de lijnintegraal van $\vec F(x,y)=(x,y)$ langs $\vec r(t)=(t,t)$, $0\le t\le1$.",
                "hints": [
                    "Bereken $\\vec r'(t)$ en vul de kromme in het vectorveld in.",
                    "Neem het inproduct en integreer naar $t$.",
                ],
                "full_solution": r"""$\vec r'(t)=(1,1)$. $\vec F(\vec r(t))=(t,t)$. Inproduct: $t\cdot1+t\cdot1=2t$.
$$\int_0^1 2t\,dt = 1$$""",
                "answer_type": "numeric",
                "correct_answer": "1",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Bereken de lijnintegraal van $\vec F(x,y)=(2x,2y)$ langs het lijnstuk van $(0,0)$ naar $(1,1)$.",
                "hints": [
                    "Parametriseer het lijnstuk als $\\vec r(t)=(t,t)$, $0\\le t\\le1$.",
                    "Bereken $\\vec r'(t)$, het inproduct met $\\vec F(\\vec r(t))$, en integreer.",
                ],
                "full_solution": r"""$\vec r(t)=(t,t)$, $\vec r'(t)=(1,1)$. $\vec F(\vec r(t))=(2t,2t)$. Inproduct: $2t+2t=4t$.
$$\int_0^1 4t\,dt = 2$$""",
                "answer_type": "numeric",
                "correct_answer": "2",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Bereken zelf de lijnintegraal van $\vec F(x,y)=(-y,x)$ langs de volle cirkel $\vec r(t)=(\cos t,\sin t)$, $0\le t\le 2\pi$ (reproduceer de aanpak uit de theorie, nu over de hele cirkel).",
                "hints": [
                    "De berekening van het inproduct $\\vec F(\\vec r(t))\\cdot\\vec r'(t)$ is identiek aan het voorbeeld: die kwam uit op $1$.",
                    "Alleen de integratiegrenzen zijn nu anders.",
                ],
                "full_solution": r"""Zoals in de theorie: $\vec F(\vec r(t))\cdot\vec r'(t) = \sin^2t+\cos^2t = 1$.
$$\int_0^{2\pi} 1\,dt = 2\pi$$""",
                "answer_type": "numeric",
                "correct_answer": "2*pi",
            },
            {
                "order_index": 4, "difficulty": 3,
                "question": r"Bereken de lijnintegraal van het scalaire veld $f(x,y)=x+y$ langs de kwartcirkel $\vec r(t)=(\cos t,\sin t)$, $0\le t\le\frac{\pi}{2}$ (dit is $\int_C f\,ds$, gewogen met booglengte in plaats van een vectorveld).",
                "hints": [
                    "Voor een scalair veld gebruik je $\\int_C f\\,ds = \\int f(\\vec r(t))\\,|\\vec r'(t)|\\,dt$. Bereken eerst $|\\vec r'(t)|$ (net als in hoofdstuk 23).",
                    "Voor deze eenheidscirkel is $|\\vec r'(t)|=1$, dus $ds=dt$. Vul $f(\\vec r(t))=\\cos t+\\sin t$ in en integreer.",
                ],
                "full_solution": r"""$\vec r'(t)=(-\sin t,\cos t)$, $|\vec r'(t)|=\sqrt{\sin^2t+\cos^2t}=1$, dus $ds=dt$.

$f(\vec r(t)) = \cos t + \sin t$.
$$\int_0^{\pi/2}(\cos t+\sin t)\,dt = [\sin t - \cos t]_0^{\pi/2} = (1-0)-(0-1) = 2$$""",
                "answer_type": "numeric",
                "correct_answer": "2",
            },
        ],
    },
    {
        "module_id": 3,
        "chapter_number": 29,
        "title": "Stelling van Green",
        "theory_content": r"""
### Wat je al weet

Je kunt een lijnintegraal langs een kromme berekenen (hoofdstuk 28), en een dubbele integraal over een gebied (hoofdstuk 26).

### Een verrassend verband

Stel je hebt een **gesloten** kromme $C$ (die weer uitkomt waar hij begon) die een gebied $R$ omsluit. De **stelling van Green** legt een verband tussen twee dingen die op het oog niets met elkaar te maken hebben: de lijnintegraal van een vectorveld rondom de rand $C$, en een dubbele integraal van de partiële afgeleiden van dat veld over het hele gebied $R$ erbinnen.

$$\oint_C (P\,dx + Q\,dy) = \iint_R \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)dA$$

(hier is $\vec F=(P,Q)$ het vectorveld, en $C$ wordt tegen de klok in doorlopen). Intuïtief: het verschil $\partial Q/\partial x - \partial P/\partial y$ meet hoeveel het veld op elk punt "ronddraait" (dit heet later, in hoofdstuk 30, de rotatie). Al die kleine rotaties in het inwendige van het gebied tellen samen precies op tot de totale "omloop" langs de rand, alsof duizenden kleine radertjes binnenin samen één grote draaiing langs de buitenkant veroorzaken.

**Praktisch nut:** soms is de dubbele integraal veel makkelijker dan de lijnintegraal, of andersom, de stelling geeft je de keuze.

### Een volledig uitgewerkt voorbeeld

**Gebruik de stelling van Green om de oppervlakte-formule $A = \frac12\oint_C (x\,dy - y\,dx)$ te verifiëren voor een cirkel met straal $a$.**

**Stap 1.** Parametriseer de cirkel: $x=a\cos\theta$, $y=a\sin\theta$, $0\le\theta\le2\pi$, dus $dx=-a\sin\theta\,d\theta$ en $dy=a\cos\theta\,d\theta$.

**Stap 2.** Werk de integrand uit:
$$x\,dy - y\,dx = (a\cos\theta)(a\cos\theta\,d\theta) - (a\sin\theta)(-a\sin\theta\,d\theta) = a^2\cos^2\theta\,d\theta + a^2\sin^2\theta\,d\theta = a^2\,d\theta$$

**Stap 3.** Integreer en halveer:
$$A = \frac12\int_0^{2\pi} a^2\,d\theta = \frac12 \cdot a^2 \cdot 2\pi = \pi a^2$$
Precies de bekende oppervlakteformule van een cirkel. ✓
""",
        "summary": "De stelling van Green koppelt een lijnintegraal rondom een gesloten kromme $C$ aan een dubbele integraal over het ingesloten gebied $R$: $\\oint_C(P\\,dx+Q\\,dy) = \\iint_R (\\partial Q/\\partial x - \\partial P/\\partial y)\\,dA$.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 2,
                "question": r"Gebruik de stelling van Green om $\displaystyle\oint_C (xy\,dx + x^2\,dy)$ te berekenen, waarbij $C$ de rand is van het vierkant $[0,1]\times[0,1]$.",
                "hints": [
                    "Hier is $P=xy$, $Q=x^2$. Bereken $\\partial Q/\\partial x - \\partial P/\\partial y$.",
                    "Integreer dat resultaat over het vierkant $[0,1]\\times[0,1]$.",
                ],
                "full_solution": r"""$\partial Q/\partial x = 2x$, $\partial P/\partial y = x$. Verschil: $2x-x=x$.
$$\iint_{[0,1]^2} x\,dA = \int_0^1\int_0^1 x\,dx\,dy = \int_0^1 \frac12\,dy = \frac12$$""",
                "answer_type": "numeric",
                "correct_answer": "1/2",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Verifieer de oppervlakteformule $A=\frac12\oint_C(x\,dy-y\,dx)$ zelf voor een cirkel met straal $5$ (reproduceer de aanpak uit de theorie).",
                "hints": [
                    "Parametriseer met $x=5\\cos\\theta$, $y=5\\sin\\theta$.",
                    "De berekening verloopt identiek aan het voorbeeld, alleen met $a=5$.",
                ],
                "full_solution": r"""$x\,dy-y\,dx = 25\cos^2\theta\,d\theta+25\sin^2\theta\,d\theta = 25\,d\theta$.
$$A = \frac12\int_0^{2\pi}25\,d\theta = \frac12\cdot25\cdot2\pi = 25\pi$$
Klopt met $\pi r^2 = \pi(5)^2=25\pi$. ✓""",
                "answer_type": "numeric",
                "correct_answer": "25*pi",
            },
            {
                "order_index": 3, "difficulty": 3,
                "question": r"Gebruik de stelling van Green om $\displaystyle\oint_C (y^2\,dx + x^2\,dy)$ te berekenen, waarbij $C$ de rand is van de driehoek met hoekpunten $(0,0)$, $(1,0)$, $(0,1)$.",
                "hints": [
                    "Hier is $P=y^2$, $Q=x^2$. Bereken $\\partial Q/\\partial x - \\partial P/\\partial y = 2x-2y$.",
                    "Gebruik dat het zwaartepunt van deze driehoek bij $(x,y)=(1/3,1/3)$ ligt met oppervlakte $\\frac12$, zodat $\\iint x\\,dA = \\iint y\\,dA = \\frac16$ (symmetrie). Wat is dan $\\iint(2x-2y)\\,dA$?",
                ],
                "full_solution": r"""$\partial Q/\partial x-\partial P/\partial y = 2x-2y$.

Voor de driehoek met hoekpunten $(0,0),(1,0),(0,1)$ geldt door symmetrie (verwissel de rollen van $x$ en $y$: de driehoek is symmetrisch in de lijn $y=x$) dat $\iint_T x\,dA = \iint_T y\,dA$ (beide gelijk aan $\frac16$, met oppervlakte $\frac12$ en zwaartepunt $x=y=\frac13$).

$$\iint_T (2x-2y)\,dA = 2\iint_T x\,dA - 2\iint_T y\,dA = 2\cdot\frac16 - 2\cdot\frac16 = 0$$
De lijnintegraal is dus $0$, een mooi voorbeeld van hoe symmetrie een uitkomst zonder verder rekenwerk kan vastleggen.""",
                "answer_type": "numeric",
                "correct_answer": "0",
            },
            {
                "order_index": 4, "difficulty": 2,
                "question": r"Leg uit waarom de stelling van Green alleen geldt voor een gesloten kromme, en wat het betekent dat $C$ 'tegen de klok in' doorlopen moet worden.",
                "hints": [
                    "Denk aan de dubbele integraal aan de rechterkant: die is gedefinieerd over een ingesloten gebied $R$. Wat heb je nodig om een gebied te kunnen 'insluiten'?",
                    "Bedenk wat er verandert aan het teken van een lijnintegraal als je een kromme in de andere richting doorloopt (vergelijk met hoe $\\int_a^b = -\\int_b^a$ bij een gewone integraal).",
                ],
                "full_solution": r"""De rechterkant van de stelling van Green is een dubbele integraal over een gebied $R$, en zo'n gebied moet ergens door een rand omsloten worden: dat kan alleen als de kromme $C$ weer uitkomt waar hij begon, dus gesloten is. Een open kromme laat geen ingesloten gebied over om de dubbele integraal over te nemen.

'Tegen de klok in' bepaalt het teken van de uitkomst: net zoals $\int_a^b f\,dx = -\int_b^a f\,dx$ bij een gewone integraal, keert het teken van de lijnintegraal om als je de kromme in de andere richting doorloopt. De afspraak is dat je tegen de klok in gaat (het gebied blijft dan steeds aan je linkerhand), zodat de formule met een positief teken klopt.""",
                "answer_type": "open",
            },
        ],
    },
    {
        "module_id": 3,
        "chapter_number": 30,
        "title": "Divergentie, rotatie, stellingen van Stokes en Gauss",
        "theory_content": r"""
### Wat je al weet

Bij de stelling van Green (hoofdstuk 29) kwam de combinatie $\partial Q/\partial x - \partial P/\partial y$ tevoorschijn, die iets zei over hoe een vectorveld "ronddraait". Je kent ook al vectorvelden in 3D en het uitproduct (hoofdstuk 22).

### Divergentie: bronsterkte

Voor een vectorveld $\vec F=(P,Q,R)$ in 3D meet de **divergentie** hoezeer het veld op een punt "uit elkaar spat" (een bron) of "naar binnen zuigt" (een put):
$$\operatorname{div}\vec F = \nabla\cdot\vec F = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}$$
Denk aan een stromende vloeistof: positieve divergentie in een punt betekent dat daar netto vloeistof "gemaakt" wordt (een bron), negatieve divergentie betekent dat er vloeistof verdwijnt (een put).

### Rotatie: draaikolken

De **rotatie** (curl) van een vectorveld meet hoezeer het veld om een punt heen "draait" (denk aan een draaikolk):
$$\operatorname{rot}\vec F = \nabla\times\vec F = \left(\frac{\partial R}{\partial y}-\frac{\partial Q}{\partial z},\ \frac{\partial P}{\partial z}-\frac{\partial R}{\partial x},\ \frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)$$
Merk op: de laatste component is exact dezelfde uitdrukking die in de stelling van Green opdook! Dat is geen toeval, in 2D is de $z$-component van de rotatie precies wat Green's stelling gebruikt.

### Twee generalisaties naar 3D

- **Stelling van Stokes:** generaliseert de stelling van Green van een plat gebied naar een gekromd oppervlak in 3D: de lijnintegraal van $\vec F$ rondom de rand van een oppervlak is gelijk aan de oppervlakte-integraal van $\operatorname{rot}\vec F$ over dat hele oppervlak.
- **Stelling van Gauss (divergentiestelling):** koppelt de **flux** (hoeveel van het veld naar buiten stroomt) door een gesloten oppervlak aan de volume-integraal van de divergentie erbinnen: $\displaystyle\oiint_{\partial V}\vec F\cdot d\vec S = \iiint_V \operatorname{div}\vec F\,dV$. Intuïtief: tel alle bronnen en putten binnenin op, en dat vertelt je precies hoeveel er netto naar buiten stroomt.

### Een volledig uitgewerkt voorbeeld

**Gebruik de divergentiestelling om de flux van $\vec F=(x,y,z)$ door het oppervlak van de eenheidsbol te berekenen.**

**Stap 1.** Bereken de divergentie: $\operatorname{div}\vec F = 1+1+1=3$ (een constante).

**Stap 2.** Pas de divergentiestelling toe: de flux is gelijk aan $\iiint_V 3\,dV = 3\cdot(\text{volume van de eenheidsbol})$.

**Stap 3.** Het volume van de eenheidsbol is $\frac43\pi(1)^3=\frac43\pi$. De flux is dus $3\cdot\frac43\pi = 4\pi$.
""",
        "summary": "Divergentie meet bronsterkte ($\\nabla\\cdot\\vec F$), rotatie meet draaikolksterkte ($\\nabla\\times\\vec F$). De stelling van Stokes generaliseert Green naar gekromde oppervlakken; de stelling van Gauss koppelt flux door een gesloten oppervlak aan de divergentie erbinnen.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Bereken de divergentie van $\vec F=(x^2,y^2,z^2)$.",
                "hints": [
                    "Gebruik $\\operatorname{div}\\vec F = \\partial P/\\partial x + \\partial Q/\\partial y + \\partial R/\\partial z$ met $P=x^2,Q=y^2,R=z^2$.",
                ],
                "full_solution": r"""$$\operatorname{div}\vec F = 2x+2y+2z$$""",
                "answer_type": "expression",
                "correct_answer": "2*x+2*y+2*z",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Bereken de rotatie van $\vec F=(y,-x,0)$.",
                "hints": [
                    "Hier is $P=y,\\ Q=-x,\\ R=0$. Bereken elke component van $\\nabla\\times\\vec F$ apart met de formule uit de theorie.",
                    "De eerste twee componenten worden $0$ (geen $z$-afhankelijkheid); reken vooral de derde component ($\\partial Q/\\partial x - \\partial P/\\partial y$) zorgvuldig uit.",
                ],
                "full_solution": r"""Component 1: $\partial R/\partial y - \partial Q/\partial z = 0-0=0$.
Component 2: $\partial P/\partial z - \partial R/\partial x = 0-0=0$.
Component 3: $\partial Q/\partial x - \partial P/\partial y = -1-1=-2$.

$$\operatorname{rot}\vec F = (0,0,-2)$$
Dit veld beschrijft een rotatie (met de klok mee, vandaar het minteken) om de $z$-as, en de rotatie-vector wijst inderdaad in de $-z$-richting.""",
                "answer_type": "open",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Gebruik de divergentiestelling om zelf de flux van $\vec F=(x,y,z)$ door het oppervlak van een bol met straal $2$ te berekenen (reproduceer de aanpak uit de theorie).",
                "hints": [
                    "De divergentie is nog steeds $3$ (die hangt niet van de straal af).",
                    "Vermenigvuldig met het volume van een bol met straal $2$: $\\frac43\\pi r^3$.",
                ],
                "full_solution": r"""$\operatorname{div}\vec F=3$. Volume van de bol: $\frac43\pi(2)^3=\frac{32\pi}{3}$.
$$\text{Flux} = 3\cdot\frac{32\pi}{3} = 32\pi$$""",
                "answer_type": "numeric",
                "correct_answer": "32*pi",
            },
            {
                "order_index": 4, "difficulty": 2,
                "question": r"Leg in woorden uit wat de stelling van Stokes zegt, als generalisatie van de stelling van Green.",
                "hints": [
                    "Green koppelt een lijnintegraal rondom de rand van een PLAT gebied aan een dubbele integraal over dat vlakke gebied. Wat verandert er bij Stokes?",
                    "Denk aan de rotatie als de 3D-generalisatie van de uitdrukking $\\partial Q/\\partial x-\\partial P/\\partial y$ uit Green.",
                ],
                "full_solution": r"""De stelling van Green werkt alleen voor een plat gebied in het $xy$-vlak: de lijnintegraal rondom de rand is gelijk aan de dubbele integraal van $\partial Q/\partial x - \partial P/\partial y$ over dat vlakke gebied.

De stelling van Stokes generaliseert dit naar een **gekromd oppervlak** in 3D (dat niet plat hoeft te zijn, zoals een stuk van een bol): de lijnintegraal van $\vec F$ rondom de rand van dat oppervlak is gelijk aan de oppervlakte-integraal van de rotatie $\operatorname{rot}\vec F$ over het hele (gekromde) oppervlak. De uitdrukking $\partial Q/\partial x-\partial P/\partial y$ uit Green is precies de $z$-component van de rotatie, dus Green is eigenlijk het speciale platte geval van Stokes.""",
                "answer_type": "open",
            },
        ],
    },
]
