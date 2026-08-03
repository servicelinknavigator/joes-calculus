# -*- coding: utf-8 -*-
"""Module IV: Lineaire algebra (hoofdstuk 31-39), zelfde 'vanaf nul opgebouwd'-aanpak."""

CHAPTERS_4 = [
    {
        "module_id": 4,
        "chapter_number": 31,
        "title": "Vectoren en vectorruimten",
        "theory_content": r"""
### Wat je al weet

Uit hoofdstuk 22 ken je vectoren als pijltjes in het vlak of de ruimte: $(a_x,a_y,a_z)$, met optellen en schalen (vermenigvuldigen met een getal).

### Een vector is meer dan alleen een pijltje

Wat een vector eigenlijk bruikbaar maakt, is niet dat het een "pijltje" is, maar dat je vectoren **bij elkaar kunt optellen** en **kunt schalen**, en dat die twee bewerkingen zich netjes gedragen (bijvoorbeeld: het maakt niet uit in welke volgorde je optelt). Zodra een verzameling objecten die twee bewerkingen heeft, en die zich netjes gedragen, mag je die objecten "vectoren" noemen, ook als ze er totaal niet als pijltjes uitzien. Denk aan polynomen: je kunt twee polynomen optellen en een polynoom met een getal vermenigvuldigen, en dat gedraagt zich net zo netjes als bij pijltjes.

### De formele definitie: een vectorruimte

Een **vectorruimte** is een verzameling $V$ met een optelling en een scalaire vermenigvuldiging die aan een lijst regels (axioma's) voldoen, waaronder:

- **Geslotenheid:** de som van twee vectoren uit $V$, en een scalair veelvoud van een vector uit $V$, zitten weer in $V$.
- **Er bestaat een nulvector** $\vec 0$ met $\vec v + \vec 0 = \vec v$ voor elke $\vec v$.
- **Elke vector heeft een tegengestelde:** voor elke $\vec v$ bestaat $-\vec v$ met $\vec v+(-\vec v)=\vec 0$.
- Optelling is commutatief en associatief, en scalaire vermenigvuldiging verdeelt netjes over optelling.

Deze regels lijken misschien vanzelfsprekend, maar het punt is: zodra je een nieuwe verzameling objecten tegenkomt (polynomen, matrices, functies, rijen getallen), hoef je alleen te checken of deze regels gelden om te weten dat je alle vector-technieken (basis, dimensie, lineaire onafhankelijkheid, die je in de volgende hoofdstukken leert) direct mag toepassen.

### Een volledig uitgewerkt voorbeeld

**Ga na dat $\mathbb{R}^2$ (met de gewone optelling en scalaire vermenigvuldiging) geslotenheid onder optelling heeft, en dat er een nulvector bestaat.**

**Stap 1 (geslotenheid):** neem twee willekeurige vectoren $\vec u=(u_1,u_2)$ en $\vec v=(v_1,v_2)$ uit $\mathbb{R}^2$. Hun som is $\vec u+\vec v=(u_1+v_1,\ u_2+v_2)$, en dat is weer een paar reële getallen, dus weer een element van $\mathbb{R}^2$. ✓

**Stap 2 (nulvector):** de vector $\vec 0=(0,0)$ zit in $\mathbb{R}^2$, en voor elke $\vec v=(v_1,v_2)$ geldt $\vec v+\vec 0=(v_1+0,v_2+0)=(v_1,v_2)=\vec v$. ✓
""",
        "summary": "Een vectorruimte is elke verzameling met een optelling en scalaire vermenigvuldiging die zich netjes gedragen (geslotenheid, nulvector, tegengestelden, enzovoort). Pijltjes in $\\mathbb{R}^n$ zijn het bekendste voorbeeld, maar ook polynomen en matrices vormen vectorruimten.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Gegeven $\vec v=(2,-1,3)$ en $\vec w=(1,4,-2)$, bereken $\vec v+\vec w$ en $3\vec v$.",
                "hints": [
                    "Tel corresponderende componenten bij elkaar op voor $\\vec v+\\vec w$.",
                    "Vermenigvuldig elke component apart met $3$ voor $3\\vec v$.",
                ],
                "full_solution": r"""$$\vec v+\vec w = (2+1,\ -1+4,\ 3-2) = (3,3,1)$$
$$3\vec v = (6,-3,9)$$""",
                "answer_type": "open",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Ga na of de verzameling $\{(x,y) : x+y=1\}$ een deelruimte is van $\mathbb{R}^2$.",
                "hints": [
                    "Een deelruimte moet in elk geval de nulvector $(0,0)$ bevatten.",
                    "Geldt $0+0=1$?",
                ],
                "full_solution": r"""Voor $(0,0)$ geldt $0+0=0 \ne 1$, dus de nulvector zit niet in deze verzameling.

Dit is dus **geen** deelruimte (het is een rechte lijn die niet door de oorsprong gaat).""",
                "answer_type": "open",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Ga na of de verzameling $\{(x,y) : x=2y\}$ een deelruimte is van $\mathbb{R}^2$.",
                "hints": [
                    "Controleer eerst of de nulvector erin zit.",
                    "Controleer daarna geslotenheid: als $(x_1,y_1)$ en $(x_2,y_2)$ allebei aan $x=2y$ voldoen, voldoet hun som dan ook?",
                ],
                "full_solution": r"""Nulvector: $(0,0)$ voldoet aan $0=2\cdot0$. ✓

Geslotenheid: stel $(x_1,y_1)$ en $(x_2,y_2)$ voldoen allebei ($x_1=2y_1$, $x_2=2y_2$). De som is $(x_1+x_2, y_1+y_2)$, en $x_1+x_2 = 2y_1+2y_2 = 2(y_1+y_2)$. ✓ voldoet ook.

Dit **is** een deelruimte (het is een rechte lijn door de oorsprong).""",
                "answer_type": "open",
            },
            {
                "order_index": 4, "difficulty": 3,
                "question": r"Laat zien dat de verzameling van polynomen van graad $\le 2$ (met gewone optelling en scalaire vermenigvuldiging) geslotenheid onder optelling heeft.",
                "hints": [
                    "Neem twee willekeurige polynomen $p(x)=a_2x^2+a_1x+a_0$ en $q(x)=b_2x^2+b_1x+b_0$.",
                    "Tel ze op en controleer dat de graad van de som ook niet boven de 2 uitkomt.",
                ],
                "full_solution": r"""Neem $p(x)=a_2x^2+a_1x+a_0$ en $q(x)=b_2x^2+b_1x+b_0$, beide van graad $\le2$.

$$p(x)+q(x) = (a_2+b_2)x^2 + (a_1+b_1)x + (a_0+b_0)$$

Dit is weer een polynoom van graad $\le2$ (de coëfficiënten zijn gewoon opgeteld, er ontstaat geen hogere macht van $x$), dus de verzameling is gesloten onder optelling.""",
                "answer_type": "open",
            },
        ],
    },
    {
        "module_id": 4,
        "chapter_number": 32,
        "title": "Matrices en bewerkingen",
        "theory_content": r"""
### Wat je al weet

Vectoren zijn rijtjes getallen (hoofdstuk 31). Bij lineaire afbeeldingen straks (hoofdstuk 36) blijkt het handig om meerdere vectoren, of een hele "machine" die vectoren omzet, in één rechthoekig schema te vatten.

### Een matrix: een rechthoekig schema van getallen

Een **matrix** is een rechthoekig rooster van getallen, bijvoorbeeld:
$$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$$
Een matrix met $m$ rijen en $n$ kolommen heet een $m\times n$-matrix. Optellen en schalen werkt zoals je zou verwachten: component-voor-component, net als bij vectoren (een vector is eigenlijk gewoon een matrix met één kolom).

### Matrixvermenigvuldiging: rij maal kolom

Vermenigvuldigen is minder voor de hand liggend. Het idee: elk element van het product $AB$ ontstaat door een **rij** van $A$ met een **kolom** van $B$ te "inproducten" (paarsgewijs vermenigvuldigen en optellen). Voor $2\times2$-matrices:
$$\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}e&f\\g&h\end{pmatrix} = \begin{pmatrix}ae+bg & af+bh\\ ce+dg & cf+dh\end{pmatrix}$$
Het element linksboven in het product komt bijvoorbeeld van rij 1 van $A$ met kolom 1 van $B$: $(a,b)\cdot(e,g) = ae+bg$.

### Een matrix als machine

Een matrix kun je ook zien als een "machine" die een vector omzet in een andere vector, via $A\vec v$ (matrix maal vector, hetzelfde rij-maal-kolom-recept). Dit idee werk je in hoofdstuk 36 (lineaire afbeeldingen) verder uit.

### Een volledig uitgewerkt voorbeeld

**Bereken $AB$ voor $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$ en $B=\begin{pmatrix}0&1\\1&0\end{pmatrix}$.**

**Stap 1 (linksboven):** rij 1 van $A$ ($1,2$) met kolom 1 van $B$ ($0,1$): $1\cdot0+2\cdot1=2$.

**Stap 2 (rechtsboven):** rij 1 van $A$ met kolom 2 van $B$ ($1,0$): $1\cdot1+2\cdot0=1$.

**Stap 3 (linksonder):** rij 2 van $A$ ($3,4$) met kolom 1 van $B$: $3\cdot0+4\cdot1=4$.

**Stap 4 (rechtsonder):** rij 2 van $A$ met kolom 2 van $B$: $3\cdot1+4\cdot0=3$.

$$AB = \begin{pmatrix}2&1\\4&3\end{pmatrix}$$
""",
        "summary": "Een matrix is een rechthoekig schema getallen. Optellen en schalen gaat component-voor-component; vermenigvuldigen gaat via het rij-maal-kolom-recept (elk element is een inproduct van een rij van de eerste met een kolom van de tweede matrix).",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Bereken $A+B$ voor $A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$ en $B=\begin{pmatrix}5&0\\-1&2\end{pmatrix}$.",
                "hints": [
                    "Tel corresponderende elementen bij elkaar op.",
                ],
                "full_solution": r"""$$A+B = \begin{pmatrix}1+5&2+0\\3-1&4+2\end{pmatrix} = \begin{pmatrix}6&2\\2&6\end{pmatrix}$$""",
                "answer_type": "open",
            },
            {
                "order_index": 2, "difficulty": 1,
                "question": r"Bereken $2A$ voor $A=\begin{pmatrix}1&-3\\4&2\end{pmatrix}$.",
                "hints": [
                    "Vermenigvuldig elk element apart met $2$.",
                ],
                "full_solution": r"""$$2A = \begin{pmatrix}2&-6\\8&4\end{pmatrix}$$""",
                "answer_type": "open",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Bereken $AB$ voor $A=\begin{pmatrix}2&1\\0&3\end{pmatrix}$ en $B=\begin{pmatrix}1&2\\3&1\end{pmatrix}$.",
                "hints": [
                    "Gebruik het rij-maal-kolom-recept voor elk van de vier elementen.",
                    "Linksboven: rij 1 van $A$ met kolom 1 van $B$: $2\\cdot1+1\\cdot3$.",
                ],
                "full_solution": r"""Linksboven: $2\cdot1+1\cdot3=5$. Rechtsboven: $2\cdot2+1\cdot1=5$.
Linksonder: $0\cdot1+3\cdot3=9$. Rechtsonder: $0\cdot2+3\cdot1=3$.
$$AB = \begin{pmatrix}5&5\\9&3\end{pmatrix}$$""",
                "answer_type": "open",
            },
            {
                "order_index": 4, "difficulty": 2,
                "question": r"Bereken $A\vec v$ voor $A=\begin{pmatrix}2&0\\0&3\end{pmatrix}$ en $\vec v=\begin{pmatrix}5\\4\end{pmatrix}$, en interpreteer wat deze matrix met een vector doet.",
                "hints": [
                    "Behandel $\\vec v$ als een matrix met één kolom, en pas hetzelfde rij-maal-kolom-recept toe.",
                    "Kijk naar wat er met elke coördinaat gebeurt: wordt de $x$-coördinaat anders geschaald dan de $y$-coördinaat?",
                ],
                "full_solution": r"""$$A\vec v = \begin{pmatrix}2\cdot5+0\cdot4\\0\cdot5+3\cdot4\end{pmatrix} = \begin{pmatrix}10\\12\end{pmatrix}$$
Deze matrix is diagonaal: hij schaalt de $x$-coördinaat met factor $2$ en de $y$-coördinaat met factor $3$, onafhankelijk van elkaar (een "uitrekking" langs de assen).""",
                "answer_type": "open",
            },
        ],
    },
    {
        "module_id": 4,
        "chapter_number": 33,
        "title": "Stelsels lineaire vergelijkingen, Gauss-eliminatie",
        "theory_content": r"""
### Wat je al weet

Uit VWO B ken je het oplossen van een stelsel van twee lineaire vergelijkingen met twee onbekenden, bijvoorbeeld door substitutie of optellen/aftrekken.

### Het probleem: dat wordt onhandig bij veel vergelijkingen

Bij drie, vier, of meer vergelijkingen met evenveel onbekenden wordt substitutie al snel rommelig. **Gauss-eliminatie** is een systematische, stap-voor-stap methode die altijd werkt, hoeveel vergelijkingen je ook hebt.

### Het idee: rijoperaties die de oplossing niet veranderen

Je mag drie dingen doen met de vergelijkingen van een stelsel zonder de oplossing te veranderen: twee vergelijkingen omwisselen, een vergelijking met een getal (ongelijk aan 0) vermenigvuldigen, of een veelvoud van de ene vergelijking bij een andere optellen. Met dit soort stappen werk je systematisch naar een vorm toe waarin je makkelijk kunt aflezen: begin met de laatste vergelijking (die dan nog maar één onbekende bevat), en werk terug naar boven (**terugsubstitutie**).

### Drie mogelijke uitkomsten

- **Eén unieke oplossing:** het gebruikelijke geval.
- **Oneindig veel oplossingen:** als twee vergelijkingen eigenlijk hetzelfde zeggen (afhankelijk stelsel).
- **Geen oplossing:** als je op een tegenstrijdigheid stuit, zoals $0=3$ (strijdig stelsel).

### Een volledig uitgewerkt voorbeeld

**Los op: $x+y=5$ en $3x-y=1$.**

**Stap 1.** Tel de twee vergelijkingen bij elkaar op om $y$ weg te werken: $(x+y)+(3x-y) = 5+1 \Rightarrow 4x = 6 \Rightarrow x = \frac{3}{2}$.

**Stap 2 (terugsubstitutie).** Vul $x=\frac32$ in de eerste vergelijking in: $\frac32+y=5 \Rightarrow y=\frac72$.

**Controle:** $3(\frac32)-\frac72 = \frac92-\frac72=1$. ✓
""",
        "summary": "Gauss-eliminatie lost een stelsel systematisch op met rijoperaties (optellen, vermenigvuldigen, omwisselen) die de oplossing niet veranderen, gevolgd door terugsubstitutie. Een stelsel heeft precies één oplossing, oneindig veel (afhankelijk), of geen (strijdig).",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Los op: $x+2y=5$ en $3x-y=1$.",
                "hints": [
                    "Los bijvoorbeeld $y$ op uit de tweede vergelijking ($y=3x-1$) en vul dat in de eerste in.",
                    "Werk uit tot je $x$ hebt, en bepaal daarna $y$ via terugsubstitutie.",
                ],
                "full_solution": r"""Uit de tweede vergelijking: $y=3x-1$. Invullen in de eerste: $x+2(3x-1)=5 \Rightarrow x+6x-2=5 \Rightarrow 7x=7 \Rightarrow x=1$.

Terugsubstitutie: $y=3(1)-1=2$.

Oplossing: $(x,y)=(1,2)$.""",
                "answer_type": "open",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Los met Gauss-eliminatie op: $x+y+z=6$, $2y+5z=-4$, $2x+5y-z=27$.",
                "hints": [
                    "Werk $x$ weg uit de derde vergelijking door $2\\times$(eerste vergelijking) van de derde af te trekken.",
                    "Je houdt dan twee vergelijkingen in $y$ en $z$ over; los die op, en werk terug naar $x$.",
                ],
                "full_solution": r"""Derde $-\ 2\times$eerste: $(2x+5y-z) - 2(x+y+z) = 27-12 \Rightarrow 3y-3z=15 \Rightarrow y-z=5$.

Samen met $2y+5z=-4$: uit $y=z+5$, invullen: $2(z+5)+5z=-4 \Rightarrow 2z+10+5z=-4 \Rightarrow 7z=-14 \Rightarrow z=-2$.

Dan $y=-2+5=3$. Terugsubstitutie in de eerste: $x+3-2=6 \Rightarrow x=5$.

Oplossing: $(x,y,z)=(5,3,-2)$.""",
                "answer_type": "open",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Los op: $x+y=2$ en $2x+2y=4$. Wat valt er op?",
                "hints": [
                    "Probeer $x$ weg te werken door $2\\times$(eerste) van de tweede af te trekken.",
                    "Wat blijft er over als je dat doet?",
                ],
                "full_solution": r"""Tweede $-\ 2\times$eerste: $(2x+2y)-2(x+y) = 4-2\cdot2 \Rightarrow 0=0$.

Dit is altijd waar, geeft geen nieuwe informatie: de twee vergelijkingen beschrijven dezelfde lijn. Er zijn **oneindig veel oplossingen**: elke $(x,y)$ met $y=2-x$ voldoet.""",
                "answer_type": "open",
            },
            {
                "order_index": 4, "difficulty": 1,
                "question": r"Los op: $x+y=2$ en $x+y=5$. Wat valt er op?",
                "hints": [
                    "Trek de eerste vergelijking van de tweede af.",
                    "Wat betekent het als je een tegenstrijdige uitspraak overhoudt, zoals $0=3$?",
                ],
                "full_solution": r"""Tweede $-$ eerste: $(x+y)-(x+y) = 5-2 \Rightarrow 0=3$.

Dit is nooit waar: het stelsel is **strijdig**, er bestaat geen enkele $(x,y)$ die aan beide vergelijkingen tegelijk voldoet (de twee lijnen zijn evenwijdig en vallen niet samen).""",
                "answer_type": "open",
            },
        ],
    },
    {
        "module_id": 4,
        "chapter_number": 34,
        "title": "Determinanten",
        "theory_content": r"""
### Wat je al weet

Bij een stelsel van twee vergelijkingen met twee onbekenden (hoofdstuk 33) kan er precies één, oneindig veel, of geen oplossing zijn, afhankelijk van hoe de vergelijkingen zich tot elkaar verhouden.

### Eén getal dat dat direct vertelt

De **determinant** van een vierkante matrix is één enkel getal dat direct laat zien of een stelsel een unieke oplossing heeft. Voor een $2\times2$-matrix:
$$\det\begin{pmatrix}a&b\\c&d\end{pmatrix} = ad-bc$$
Is $\det A \ne 0$, dan heeft het bijbehorende stelsel een unieke oplossing. Is $\det A = 0$, dan is de matrix **singulier**: de rijen (of kolommen) zijn afhankelijk van elkaar, en er is geen unieke oplossing (oneindig veel of geen).

### Meetkundige betekenis

De absolute waarde van de determinant van een $2\times2$-matrix is de oppervlakte van het parallellogram opgespannen door de twee rijvectoren (vergelijk dit met het uitproduct uit hoofdstuk 22, dat óók een oppervlakte/rotatie-informatie gaf). Een determinant van $0$ betekent dat het parallellogram "platgedrukt" is tot een lijnstuk: de twee vectoren wijzen (op een schaal na) dezelfde kant op.

### Determinant van een 3×3-matrix

Voor grotere matrices ontwikkel je de determinant via **cofactorontwikkeling** langs een rij: neem elk element van die rij, vermenigvuldig met de determinant van de $2\times2$-matrix die overblijft als je de rij en kolom van dat element wegstreept, met afwisselend teken.

### Een volledig uitgewerkt voorbeeld

**Bereken $\det\begin{pmatrix}1&2&3\\0&1&4\\5&6&0\end{pmatrix}$ via cofactorontwikkeling langs de eerste rij.**

**Stap 1.** Streep voor elk element van rij 1 de bijbehorende rij en kolom weg, en bereken de $2\times2$-determinant die overblijft:
- Voor $1$ (kolom 1): $\det\begin{pmatrix}1&4\\6&0\end{pmatrix} = 1\cdot0-4\cdot6=-24$
- Voor $2$ (kolom 2): $\det\begin{pmatrix}0&4\\5&0\end{pmatrix} = 0\cdot0-4\cdot5=-20$
- Voor $3$ (kolom 3): $\det\begin{pmatrix}0&1\\5&6\end{pmatrix} = 0\cdot6-1\cdot5=-5$

**Stap 2.** Combineer met afwisselend teken $(+,-,+)$:
$$\det A = 1\cdot(-24) - 2\cdot(-20) + 3\cdot(-5) = -24+40-15 = 1$$
""",
        "summary": "De determinant $\\det A = ad-bc$ (voor $2\\times2$) vertelt direct of een matrix singulier is ($\\det=0$, geen unieke oplossing) of niet. Meetkundig is $|\\det A|$ de oppervlakte (of inhoud) opgespannen door de rijvectoren. Grotere matrices reken je uit via cofactorontwikkeling.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Bereken $\det\begin{pmatrix}3&5\\1&2\end{pmatrix}$.",
                "hints": [
                    "Gebruik $\\det = ad-bc$.",
                ],
                "full_solution": r"""$$\det = 3\cdot2-5\cdot1 = 6-5=1$$""",
                "answer_type": "numeric",
                "correct_answer": "1",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Bereken $\det\begin{pmatrix}2&0&1\\1&3&2\\0&1&1\end{pmatrix}$ via cofactorontwikkeling langs de eerste rij.",
                "hints": [
                    "Streep voor elk element van rij 1 de rij en kolom weg, en bereken de drie $2\\times2$-determinanten die overblijven.",
                    "Combineer met afwisselend teken $(+,-,+)$, net als in het voorbeeld.",
                ],
                "full_solution": r"""Voor $2$: $\det\begin{pmatrix}3&2\\1&1\end{pmatrix}=3-2=1$.
Voor $0$: (telt niet mee, coëfficiënt is $0$).
Voor $1$: $\det\begin{pmatrix}1&3\\0&1\end{pmatrix}=1-0=1$.

$$\det A = 2(1) - 0(\ldots) + 1(1) = 2+1=3$$""",
                "answer_type": "numeric",
                "correct_answer": "3",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Voor welke waarde(n) van $k$ is de matrix $\begin{pmatrix}k&2\\3&k\end{pmatrix}$ singulier?",
                "hints": [
                    "Stel $\\det = 0$ op met de formule $ad-bc$.",
                    "Los de resulterende vergelijking in $k$ op.",
                ],
                "full_solution": r"""$$\det = k^2 - 6 = 0 \implies k^2=6 \implies k=\pm\sqrt6$$""",
                "answer_type": "open",
            },
            {
                "order_index": 4, "difficulty": 2,
                "question": r"Leg uit wat het meetkundig betekent als $\det A = 0$ voor een $2\times2$-matrix, in termen van de rijvectoren van $A$.",
                "hints": [
                    "Denk aan de determinant als de oppervlakte van het parallellogram opgespannen door de twee rijvectoren.",
                    "Wanneer is de oppervlakte van een parallellogram gelijk aan $0$?",
                ],
                "full_solution": r"""$|\det A|$ is de oppervlakte van het parallellogram opgespannen door de twee rijvectoren van $A$. Die oppervlakte is precies $0$ wanneer de twee vectoren **evenwijdig** zijn (op elkaars verlengde liggen), het parallellogram wordt dan "platgedrukt" tot een lijnstuk zonder oppervlakte.

Dat betekent dat de twee vectoren (en dus de twee vergelijkingen van het bijbehorende stelsel) lineair afhankelijk zijn: de ene is een veelvoud van de andere, en het stelsel heeft geen unieke oplossing.""",
                "answer_type": "open",
            },
        ],
    },
    {
        "module_id": 4,
        "chapter_number": 35,
        "title": "Basis, dimensie en rang",
        "theory_content": r"""
### Wat je al weet

Je kent vectoren optellen en schalen (hoofdstuk 31), en wanneer een stelsel afhankelijke vergelijkingen heeft (hoofdstuk 33-34).

### Hoeveel vectoren heb je minimaal nodig?

Met de standaardvectoren $(1,0)$ en $(0,1)$ kun je, door ze te schalen en op te tellen, **elke** vector in $\mathbb{R}^2$ maken. Dit heet: deze twee vectoren **spannen** $\mathbb{R}^2$ **op**. Zou je een derde vector toevoegen, zoals $(1,1)$, dan voegt die niks nieuws toe, want $(1,1)$ is al te maken uit de eerste twee: hij is **lineair afhankelijk** van $(1,0)$ en $(0,1)$.

### Lineaire onafhankelijkheid

Een verzameling vectoren is **lineair onafhankelijk** als geen van hen te schrijven is als combinatie van de anderen (geen enkele is "overbodig"). Formeler: de enige manier om met een combinatie $c_1\vec v_1+c_2\vec v_2+\cdots$ de nulvector te krijgen, is als alle $c_i=0$ zijn.

### Basis en dimensie

Een **basis** van een vectorruimte is een verzameling vectoren die (1) de hele ruimte opspant, en (2) lineair onafhankelijk is, precies genoeg om alles te maken, zonder overbodige vectoren. Het aantal vectoren in een basis heet de **dimensie** van de ruimte (dit aantal is altijd hetzelfde, ongeacht welke basis je kiest).

### Rang van een matrix

De **rang** van een matrix is de dimensie van de ruimte die door zijn kolommen (of, equivalent, zijn rijen) wordt opgespannen: het aantal "echt onafhankelijke" rijen of kolommen. Je bepaalt de rang door de matrix met Gauss-eliminatie (hoofdstuk 33) te herleiden tot echelonvorm, en de niet-nul rijen te tellen.

### Een volledig uitgewerkt voorbeeld

**Bepaal de rang van $\begin{pmatrix}1&2&1\\2&3&0\end{pmatrix}$.**

**Stap 1.** Werk met een rijoperatie de eerste kolom van rij 2 weg: $R_2 \to R_2 - 2R_1$:
$$R_2 - 2R_1 = (2-2\cdot1,\ 3-2\cdot2,\ 0-2\cdot1) = (0,-1,-2)$$

**Stap 2.** De matrix in echelonvorm is $\begin{pmatrix}1&2&1\\0&-1&-2\end{pmatrix}$, met twee niet-nul rijen.

De rang is dus $2$: beide rijen zijn onafhankelijk (geen van beide is een veelvoud van de ander).
""",
        "summary": "Een basis is een minimale verzameling vectoren die een hele ruimte opspant (lineair onafhankelijk én opspannend); het aantal basisvectoren is de dimensie. De rang van een matrix is het aantal echt onafhankelijke rijen, gevonden via Gauss-eliminatie.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Ga na of $(1,2)$ en $(2,4)$ lineair onafhankelijk zijn.",
                "hints": [
                    "Is de ene vector een scalair veelvoud van de andere?",
                ],
                "full_solution": r"""$(2,4) = 2\cdot(1,2)$: de tweede vector is precies $2$ keer de eerste. Ze zijn dus **lineair afhankelijk** (niet onafhankelijk), ze wijzen dezelfde kant op.""",
                "answer_type": "open",
            },
            {
                "order_index": 2, "difficulty": 1,
                "question": r"Vormen $(1,0)$ en $(0,1)$ een basis voor $\mathbb{R}^2$? Onderbouw kort.",
                "hints": [
                    "Controleer beide voorwaarden: spannen ze samen heel $\\mathbb{R}^2$ op, en zijn ze onafhankelijk?",
                ],
                "full_solution": r"""Elke vector $(x,y) \in \mathbb{R}^2$ is te schrijven als $x(1,0)+y(0,1)$, dus ze spannen $\mathbb{R}^2$ op. Ze zijn ook onafhankelijk (geen van beide is een veelvoud van de ander). Samen vormen ze dus een **basis** voor $\mathbb{R}^2$, wat ook meteen bevestigt dat $\dim(\mathbb{R}^2)=2$.""",
                "answer_type": "open",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Bepaal de rang van $\begin{pmatrix}1&2&1\\2&3&0\end{pmatrix}$ zelf (reproduceer de aanpak uit de theorie).",
                "hints": [
                    "Voer de rijoperatie $R_2 \\to R_2 - 2R_1$ uit.",
                    "Tel het aantal niet-nul rijen in de echelonvorm.",
                ],
                "full_solution": r"""$R_2-2R_1 = (0,-1,-2)$. Echelonvorm: $\begin{pmatrix}1&2&1\\0&-1&-2\end{pmatrix}$, twee niet-nul rijen.

De rang is $2$.""",
                "answer_type": "numeric",
                "correct_answer": "2",
            },
            {
                "order_index": 4, "difficulty": 3,
                "question": r"Bepaal de dimensie van de deelruimte opgespannen door $(1,1,0)$, $(0,1,1)$ en $(1,2,1)$.",
                "hints": [
                    "Onderzoek of de derde vector een combinatie is van de eerste twee: probeer $(1,1,0)+(0,1,1)$ uit te rekenen.",
                    "Als de derde vector afhankelijk blijkt van de eerste twee, hoeveel echt onafhankelijke vectoren blijven er dan over?",
                ],
                "full_solution": r"""$(1,1,0)+(0,1,1) = (1,2,1)$: de derde vector is precies de som van de eerste twee, dus lineair afhankelijk.

De eerste twee vectoren, $(1,1,0)$ en $(0,1,1)$, zijn zelf niet evenredig (geen veelvoud van elkaar), dus wel onafhankelijk. De opgespannen deelruimte heeft dus dimensie $2$.""",
                "answer_type": "numeric",
                "correct_answer": "2",
            },
        ],
    },
    {
        "module_id": 4,
        "chapter_number": 36,
        "title": "Lineaire afbeeldingen",
        "theory_content": r"""
### Wat je al weet

Je hebt gezien dat een matrix als een "machine" werkt die een vector omzet in een andere vector, via $A\vec v$ (hoofdstuk 32).

### Wanneer is zo'n machine "lineair"?

Een afbeelding $T$ (functie die vectoren omzet in vectoren) heet **lineair** als hij zich netjes gedraagt ten opzichte van optellen en schalen:
$$T(\vec u+\vec v) = T(\vec u)+T(\vec v), \qquad T(c\vec v) = c\,T(\vec v)$$
In woorden: het maakt niet uit of je eerst optelt/schaalt en dan de afbeelding toepast, of andersom, de uitkomst is hetzelfde. Denk aan een rotatie: eerst twee vectoren optellen en dan roteren geeft hetzelfde resultaat als eerst allebei roteren en dan optellen.

### Elke lineaire afbeelding is (in eindige dimensie) een matrix

Een belangrijk feit: elke lineaire afbeelding tussen eindig-dimensionale vectorruimten kan geschreven worden als $T(\vec v) = A\vec v$ voor een geschikte matrix $A$. Om die matrix te vinden, hoef je alleen te weten wat $T$ doet met de basisvectoren: de kolommen van $A$ zijn precies de beelden van de standaardbasisvectoren.

### Een volledig uitgewerkt voorbeeld

**Bepaal de matrix die hoort bij een rotatie over $90°$ (tegen de klok in) in het vlak.**

**Stap 1.** Bepaal waar de eerste standaardvector $(1,0)$ naartoe gaat na een rotatie van $90°$: die komt op $(0,1)$ terecht.

**Stap 2.** Bepaal waar de tweede standaardvector $(0,1)$ naartoe gaat: die komt op $(-1,0)$ terecht.

**Stap 3.** Zet deze beelden als kolommen in de matrix:
$$A = \begin{pmatrix}0&-1\\1&0\end{pmatrix}$$
(De eerste kolom is het beeld van $(1,0)$, de tweede kolom is het beeld van $(0,1)$.)
""",
        "summary": "Een lineaire afbeelding respecteert optellen en schalen: $T(\\vec u+\\vec v)=T(\\vec u)+T(\\vec v)$ en $T(c\\vec v)=cT(\\vec v)$. Elke lineaire afbeelding in eindige dimensie is te schrijven als een matrix, waarvan de kolommen de beelden van de standaardbasisvectoren zijn.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 2,
                "question": r"Ga na dat $T(x,y)=(2x,3y)$ lineair is, door beide eigenschappen te controleren.",
                "hints": [
                    "Controleer $T((x_1,y_1)+(x_2,y_2)) = T(x_1,y_1)+T(x_2,y_2)$ door beide kanten uit te schrijven.",
                    "Controleer $T(c\\cdot(x,y)) = c\\cdot T(x,y)$.",
                ],
                "full_solution": r"""**Optellen:** $T((x_1+x_2, y_1+y_2)) = (2(x_1+x_2), 3(y_1+y_2)) = (2x_1+2x_2, 3y_1+3y_2)$.
$T(x_1,y_1)+T(x_2,y_2) = (2x_1,3y_1)+(2x_2,3y_2) = (2x_1+2x_2, 3y_1+3y_2)$. Gelijk. ✓

**Schalen:** $T(cx,cy) = (2cx,3cy) = c(2x,3y) = c\,T(x,y)$. ✓

Beide eigenschappen kloppen, dus $T$ is lineair.""",
                "answer_type": "open",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Bepaal de matrix die hoort bij een rotatie over $180°$.",
                "hints": [
                    "Waar komt $(1,0)$ terecht na een rotatie van $180°$? En $(0,1)$?",
                    "Zet de twee beelden als kolommen in de matrix.",
                ],
                "full_solution": r"""$(1,0) \to (-1,0)$, en $(0,1)\to(0,-1)$.
$$A = \begin{pmatrix}-1&0\\0&-1\end{pmatrix}$$
(Dit is gewoon $-I$: elke vector wordt naar zijn tegengestelde gestuurd, precies wat je verwacht van een halve draai.)""",
                "answer_type": "open",
            },
            {
                "order_index": 3, "difficulty": 1,
                "question": r"Gebruik de rotatiematrix over $90°$ uit de theorie om te berekenen waar het punt $(1,0)$ naartoe gaat.",
                "hints": [
                    "Pas $A\\vec v$ toe met $A=\\begin{pmatrix}0&-1\\\\1&0\\end{pmatrix}$ en $\\vec v=(1,0)$.",
                ],
                "full_solution": r"""$$A\begin{pmatrix}1\\0\end{pmatrix} = \begin{pmatrix}0\cdot1+(-1)\cdot0\\1\cdot1+0\cdot0\end{pmatrix} = \begin{pmatrix}0\\1\end{pmatrix}$$
Dit klopt: $(1,0)$ roteert naar $(0,1)$, precies zoals we in stap 1 van het voorbeeld al hadden vastgesteld.""",
                "answer_type": "open",
            },
            {
                "order_index": 4, "difficulty": 2,
                "question": r"Ga na of $T(x,y) = (x+1, y)$ lineair is.",
                "hints": [
                    "Een lineaire afbeelding moet de nulvector naar de nulvector sturen: $T(\\vec 0)$ moet $\\vec 0$ zijn.",
                    "Bereken $T(0,0)$.",
                ],
                "full_solution": r"""$T(0,0) = (0+1,0) = (1,0) \ne (0,0)$.

Een lineaire afbeelding moet altijd de nulvector op de nulvector afbeelden (dit volgt direct uit $T(0\cdot\vec v)=0\cdot T(\vec v) = \vec 0$). Omdat dat hier niet het geval is, is $T$ **niet lineair** (het is een verschuiving/translatie, geen lineaire afbeelding).""",
                "answer_type": "open",
            },
        ],
    },
    {
        "module_id": 4,
        "chapter_number": 37,
        "title": "Eigenwaarden en eigenvectoren",
        "theory_content": r"""
### Wat je al weet

Een matrix $A$ werkt als een machine die een vector $\vec v$ omzet in een nieuwe vector $A\vec v$ (hoofdstuk 32, 36), meestal met een andere richting én een andere lengte.

### Een bijzonder soort vector: die alleen van lengte verandert

Voor de meeste vectoren verandert $A\vec v$ zowel van richting als van lengte. Maar voor sommige speciale vectoren gebeurt er iets bijzonders: $A\vec v$ wijst nog **precies dezelfde** (of tegengestelde) kant op als $\vec v$ zelf, alleen langer of korter. Zo'n vector heet een **eigenvector**, en de schaalfactor heet de bijbehorende **eigenwaarde** $\lambda$:
$$A\vec v = \lambda\vec v \qquad (\vec v \ne \vec 0)$$

### Hoe vind je eigenwaarden?

Herschrijf $A\vec v=\lambda\vec v$ als $(A-\lambda I)\vec v = \vec 0$ (met $I$ de identiteitsmatrix). Voor een niet-triviale oplossing $\vec v\ne\vec0$ moet de matrix $A-\lambda I$ singulier zijn (hoofdstuk 34: anders is $\vec v=\vec0$ de enige oplossing). Dus:
$$\det(A-\lambda I) = 0$$
Dit heet de **karakteristieke vergelijking**: een polynoom in $\lambda$, waarvan de oplossingen precies de eigenwaarden zijn. Voor elke gevonden eigenwaarde vind je de bijbehorende eigenvector(en) door $(A-\lambda I)\vec v=\vec 0$ op te lossen (een stelsel zoals in hoofdstuk 33).

### Een volledig uitgewerkt voorbeeld

**Bepaal de eigenwaarden van $A=\begin{pmatrix}4&1\\2&3\end{pmatrix}$.**

**Stap 1.** Stel de karakteristieke vergelijking op:
$$\det(A-\lambda I) = \det\begin{pmatrix}4-\lambda&1\\2&3-\lambda\end{pmatrix} = (4-\lambda)(3-\lambda) - 1\cdot2$$

**Stap 2.** Werk uit: $(4-\lambda)(3-\lambda) = 12-4\lambda-3\lambda+\lambda^2 = \lambda^2-7\lambda+12$. Min $2$: $\lambda^2-7\lambda+10=0$.

**Stap 3.** Ontbind: $(\lambda-5)(\lambda-2)=0$, dus $\lambda=5$ of $\lambda=2$.
""",
        "summary": "Een eigenvector van $A$ is een vector die door $A$ alleen geschaald wordt: $A\\vec v=\\lambda\\vec v$. De eigenwaarden $\\lambda$ vind je als oplossingen van de karakteristieke vergelijking $\\det(A-\\lambda I)=0$, en de bijbehorende eigenvectoren door $(A-\\lambda I)\\vec v=\\vec 0$ op te lossen.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Bepaal de eigenwaarden van $A=\begin{pmatrix}2&0\\0&3\end{pmatrix}$.",
                "hints": [
                    "Voor een diagonaalmatrix kun je de karakteristieke vergelijking direct opstellen, of gewoon de diagonaal aflezen.",
                ],
                "full_solution": r"""$\det(A-\lambda I) = (2-\lambda)(3-\lambda) = 0 \implies \lambda=2$ of $\lambda=3$.

(Bij een diagonaalmatrix zijn de eigenwaarden altijd precies de elementen op de diagonaal.)""",
                "answer_type": "open",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Bepaal zelf de eigenwaarden van $A=\begin{pmatrix}4&1\\2&3\end{pmatrix}$ (reproduceer de berekening uit de theorie).",
                "hints": [
                    "Stel $\\det(A-\\lambda I)=0$ op en werk uit tot een kwadratische vergelijking in $\\lambda$.",
                    "Ontbind de vergelijking in factoren.",
                ],
                "full_solution": r"""$(4-\lambda)(3-\lambda)-2 = \lambda^2-7\lambda+10=0 \implies (\lambda-5)(\lambda-2)=0 \implies \lambda=5$ of $\lambda=2$.""",
                "answer_type": "open",
            },
            {
                "order_index": 3, "difficulty": 3,
                "question": r"Bepaal de eigenvector bij de kleinste eigenwaarde ($\lambda=2$) van $A=\begin{pmatrix}4&1\\2&3\end{pmatrix}$.",
                "hints": [
                    "Los $(A-2I)\\vec v=\\vec0$ op: dit is een stelsel met een vrije variabele (want $\\det(A-2I)=0$).",
                    "Schrijf de eerste rij van $(A-2I)$ uit als vergelijking in $x$ en $y$, en kies een simpele oplossing.",
                ],
                "full_solution": r"""$A-2I = \begin{pmatrix}2&1\\2&1\end{pmatrix}$. De vergelijking (uit beide, identieke, rijen): $2x+y=0 \implies y=-2x$.

Kies $x=1$: eigenvector $\vec v = (1,-2)$ (of elk veelvoud daarvan).

Controle: $A(1,-2) = (4\cdot1+1\cdot(-2),\ 2\cdot1+3\cdot(-2)) = (2,-4) = 2\cdot(1,-2)$. ✓""",
                "answer_type": "open",
            },
            {
                "order_index": 4, "difficulty": 2,
                "question": r"Controleer of $\vec v=(1,1)$ een eigenvector is van $A=\begin{pmatrix}3&1\\1&3\end{pmatrix}$, en zo ja, bij welke eigenwaarde.",
                "hints": [
                    "Bereken $A\\vec v$ direct.",
                    "Is het resultaat een scalair veelvoud van $\\vec v$ zelf?",
                ],
                "full_solution": r"""$$A\vec v = \begin{pmatrix}3\cdot1+1\cdot1\\1\cdot1+3\cdot1\end{pmatrix} = \begin{pmatrix}4\\4\end{pmatrix} = 4\begin{pmatrix}1\\1\end{pmatrix}$$
Dit is inderdaad $4\vec v$, dus $\vec v=(1,1)$ is een eigenvector met eigenwaarde $\lambda=4$.""",
                "answer_type": "numeric",
                "correct_answer": "4",
            },
        ],
    },
    {
        "module_id": 4,
        "chapter_number": 38,
        "title": "Diagonaliseren",
        "theory_content": r"""
### Wat je al weet

Uit hoofdstuk 37 ken je eigenwaarden en eigenvectoren van een matrix: $A\vec v=\lambda\vec v$.

### Waarom zou je een matrix willen "diagonaliseren"?

Diagonaalmatrices zijn heerlijk om mee te rekenen: een macht van een diagonaalmatrix bereken je gewoon door elk diagonaalelement apart tot die macht te verheffen. Voor een gewone matrix is $A^{100}$ berekenen (100 keer matrixvermenigvuldigen) juist heel omslachtig. Het idee: kun je een lastige matrix $A$ "vermommen" als een diagonaalmatrix, dan wordt zo'n berekening ineens simpel.

### De methode

Heeft een $n\times n$-matrix $A$ genoeg (namelijk $n$) onafhankelijke eigenvectoren, dan kun je $A$ schrijven als:
$$A = PDP^{-1}$$
waarbij $D$ een diagonaalmatrix is met de eigenwaarden op de diagonaal, en $P$ een matrix waarvan de kolommen de bijbehorende eigenvectoren zijn (in dezelfde volgorde als de eigenwaarden in $D$).

**Waarom dit zo handig is:** machten van $A$ worden ineens simpel, want de $P$'s en $P^{-1}$'s in het midden vallen tegen elkaar weg:
$$A^k = (PDP^{-1})(PDP^{-1})\cdots(PDP^{-1}) = PD^kP^{-1}$$
en $D^k$ bereken je, zoals gezegd, gewoon element-voor-element.

### Een volledig uitgewerkt voorbeeld

**Stel $P$ en $D$ op voor $A=\begin{pmatrix}4&1\\2&3\end{pmatrix}$ (eigenwaarden $\lambda=5,2$ uit hoofdstuk 37).**

**Stap 1.** Vind de eigenvector bij $\lambda=5$: los $(A-5I)\vec v=\vec0$ op. $A-5I=\begin{pmatrix}-1&1\\2&-2\end{pmatrix}$, geeft $-x+y=0 \Rightarrow y=x$. Kies $\vec v_1=(1,1)$.

**Stap 2.** De eigenvector bij $\lambda=2$ ken je al uit hoofdstuk 37: $\vec v_2=(1,-2)$.

**Stap 3.** Zet de eigenvectoren als kolommen in $P$, en de eigenwaarden (in dezelfde volgorde) op de diagonaal van $D$:
$$P = \begin{pmatrix}1&1\\1&-2\end{pmatrix}, \qquad D = \begin{pmatrix}5&0\\0&2\end{pmatrix}$$
Er geldt nu $A=PDP^{-1}$.
""",
        "summary": "Heeft een matrix genoeg onafhankelijke eigenvectoren, dan kun je 'm schrijven als $A=PDP^{-1}$: $P$ heeft de eigenvectoren als kolommen, $D$ is diagonaal met de eigenwaarden. Dit maakt machten van $A$ makkelijk: $A^k=PD^kP^{-1}$.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 2,
                "question": r"Stel $P$ en $D$ op voor $A=\begin{pmatrix}2&0\\0&3\end{pmatrix}$ (gebruik de eigenwaarden uit hoofdstuk 37, opgave 1).",
                "hints": [
                    "Voor een diagonaalmatrix zijn de standaardbasisvectoren $(1,0)$ en $(0,1)$ zelf al de eigenvectoren.",
                    "Zet die als kolommen in $P$, en de eigenwaarden op de diagonaal van $D$.",
                ],
                "full_solution": r"""$A$ is zelf al diagonaal, dus $D=A=\begin{pmatrix}2&0\\0&3\end{pmatrix}$, en $P=I=\begin{pmatrix}1&0\\0&1\end{pmatrix}$ (de standaardvectoren zijn hier zelf de eigenvectoren).""",
                "answer_type": "open",
            },
            {
                "order_index": 2, "difficulty": 3,
                "question": r"Gebruik diagonalisatie om $A^2$ te berekenen voor $A=\begin{pmatrix}4&1\\2&3\end{pmatrix}$, met $P=\begin{pmatrix}1&1\\1&-2\end{pmatrix}$ en $D=\begin{pmatrix}5&0\\0&2\end{pmatrix}$ uit de theorie (je mag $A^2$ ook direct uitrekenen om te controleren).",
                "hints": [
                    "Bereken eerst $A^2$ gewoon direct door $A\\cdot A$ uit te rekenen (matrixvermenigvuldiging, hoofdstuk 32), dat is voor $k=2$ nog goed te doen zonder $P$ en $D$.",
                    "Vergelijk met wat $PD^2P^{-1}$ zou moeten geven: $D^2=\\begin{pmatrix}25&0\\\\0&4\\end{pmatrix}$, ter controle van het principe.",
                ],
                "full_solution": r"""Direct: $A^2 = \begin{pmatrix}4&1\\2&3\end{pmatrix}\begin{pmatrix}4&1\\2&3\end{pmatrix} = \begin{pmatrix}4\cdot4+1\cdot2 & 4\cdot1+1\cdot3\\ 2\cdot4+3\cdot2 & 2\cdot1+3\cdot3\end{pmatrix} = \begin{pmatrix}18&7\\14&11\end{pmatrix}$

Via diagonalisatie zou je $D^2=\begin{pmatrix}25&0\\0&4\end{pmatrix}$ gebruiken en $A^2=PD^2P^{-1}$ berekenen, dat geeft (na het uitrekenen van $P^{-1}$ en de matrixvermenigvuldigingen) hetzelfde resultaat. Het voordeel van deze route wordt vooral zichtbaar bij hoge machten zoals $A^{100}$, waar direct vermenigvuldigen onbegonnen werk is, maar $D^{100}$ nog steeds triviaal blijft.""",
                "answer_type": "open",
            },
            {
                "order_index": 3, "difficulty": 2,
                "question": r"Leg uit waarom diagonaliseren handig is voor het berekenen van hoge machten van een matrix, zoals $A^{100}$.",
                "hints": [
                    "Bedenk hoeveel matrixvermenigvuldigingen $A^{100}$ direct zou kosten, tegenover het apart verheffen van elk diagonaalelement van $D$ tot de 100e macht.",
                    "Wat gebeurt er met de $P$ en $P^{-1}$ in het midden van $A^k=(PDP^{-1})(PDP^{-1})\\cdots$?",
                ],
                "full_solution": r"""Bij $A^k=PDP^{-1}\cdot PDP^{-1}\cdots PDP^{-1}$ ($k$ keer) vallen alle tussenliggende paren $P^{-1}P$ weg (want $P^{-1}P=I$), zodat er $A^k=PD^kP^{-1}$ overblijft. Het enige werk dat overblijft is $D^k$ berekenen, en bij een diagonaalmatrix betekent machtsverheffen gewoon elk diagonaalelement apart tot die macht verheffen, een simpele rekenpartij in plaats van 99 matrixvermenigvuldigingen na elkaar.""",
                "answer_type": "open",
            },
            {
                "order_index": 4, "difficulty": 3,
                "question": r"Een matrix met een dubbele eigenwaarde heeft niet altijd genoeg onafhankelijke eigenvectoren om te diagonaliseren. Leg uit waarom dit een probleem is voor de constructie $A=PDP^{-1}$.",
                "hints": [
                    "$P$ moet een vierkante, inverteerbare matrix zijn (kolommen = eigenvectoren). Wat betekent 'inverteerbaar' in termen van de rang/onafhankelijkheid van de kolommen (hoofdstuk 35)?",
                    "Wat gebeurt er als je voor een $2\\times2$-matrix maar 1 onafhankelijke eigenvector kunt vinden?",
                ],
                "full_solution": r"""Voor de constructie $A=PDP^{-1}$ moet $P$ inverteerbaar zijn, dus zijn kolommen (de eigenvectoren) moeten onafhankelijk zijn en samen de hele ruimte opspannen (hoofdstuk 35). Voor een $n\times n$-matrix heb je dus $n$ onafhankelijke eigenvectoren nodig.

Als een eigenwaarde "dubbel" is (twee keer voorkomt als oplossing van de karakteristieke vergelijking), maar er toch maar één onafhankelijke eigenvector bij hoort, dan kun je nooit genoeg kolommen voor $P$ verzamelen: $P$ zou dan niet-inverteerbaar zijn (rang $<n$). In dat geval is de matrix **niet diagonaliseerbaar**, ook al zijn alle eigenwaarden bekend.""",
                "answer_type": "open",
            },
        ],
    },
    {
        "module_id": 4,
        "chapter_number": 39,
        "title": "Inproductruimten en orthogonaliteit",
        "theory_content": r"""
### Wat je al weet

Uit hoofdstuk 22 ken je het inproduct van twee vectoren in de ruimte: $\vec a\cdot\vec b = a_xb_x+a_yb_y+a_zb_z = |\vec a||\vec b|\cos\theta$, en dat twee vectoren loodrecht (orthogonaal) staan precies als hun inproduct $0$ is.

### Het inproduct in abstracte vectorruimten

Net zoals "vector" veralgemeniseerd is tot elke verzameling die zich netjes gedraagt onder optellen/schalen (hoofdstuk 31), kun je ook het **inproduct**-begrip veralgemeniseren naar abstracte vectorruimten: een **inproductruimte** is een vectorruimte met een extra bewerking $\langle \vec u,\vec v\rangle$ die zich gedraagt zoals je van een inproduct verwacht (symmetrisch, lineair, en positief voor $\vec v\ne\vec 0$). Met zo'n inproduct kun je lengte ($\|\vec v\|=\sqrt{\langle \vec v,\vec v\rangle}$), hoeken, en loodrechtheid definiëren, ook in ruimten die geen "gewone" pijltjes-ruimten zijn.

### Orthogonaliteit en projectie

Twee vectoren zijn **orthogonaal** als $\langle\vec u,\vec v\rangle=0$. Een handige toepassing: de **projectie** van $\vec v$ op $\vec w$ is het deel van $\vec v$ dat in de richting van $\vec w$ wijst:
$$\text{proj}_{\vec w}\vec v = \frac{\vec v\cdot\vec w}{\|\vec w\|^2}\,\vec w$$
Denk aan de schaduw die $\vec v$ werpt op de lijn door $\vec w$ als het licht loodrecht van boven komt.

### Een volledig uitgewerkt voorbeeld

**Bereken de projectie van $\vec v=(3,4)$ op $\vec w=(1,0)$.**

**Stap 1.** Bereken het inproduct: $\vec v\cdot\vec w = 3\cdot1+4\cdot0=3$.

**Stap 2.** Bereken $\|\vec w\|^2 = 1^2+0^2=1$.

**Stap 3.** Vul in de formule in:
$$\text{proj}_{\vec w}\vec v = \frac{3}{1}(1,0) = (3,0)$$
Dit is precies wat je zou verwachten: de "schaduw" van $(3,4)$ op de $x$-as is $(3,0)$.
""",
        "summary": "Een inproductruimte generaliseert het inproduct naar abstracte vectorruimten, met dezelfde eigenschappen: lengte, hoek en orthogonaliteit ($\\langle\\vec u,\\vec v\\rangle=0$). De projectie van $\\vec v$ op $\\vec w$ is $\\frac{\\vec v\\cdot\\vec w}{\\|\\vec w\\|^2}\\vec w$: het deel van $\\vec v$ in de richting van $\\vec w$.",
        "exercises": [
            {
                "order_index": 1, "difficulty": 1,
                "question": r"Ga na of $(1,2)$ en $(2,-1)$ orthogonaal zijn.",
                "hints": [
                    "Bereken het inproduct en kijk of dat $0$ is.",
                ],
                "full_solution": r"""$$(1,2)\cdot(2,-1) = 1\cdot2+2\cdot(-1) = 2-2=0$$
Het inproduct is $0$, dus de vectoren zijn **orthogonaal**.""",
                "answer_type": "open",
            },
            {
                "order_index": 2, "difficulty": 2,
                "question": r"Bereken zelf de projectie van $\vec v=(5,3)$ op $\vec w=(1,0)$ (reproduceer de aanpak uit de theorie).",
                "hints": [
                    "Bereken $\\vec v\\cdot\\vec w$ en $\\|\\vec w\\|^2$.",
                    "Vul in de projectieformule in.",
                ],
                "full_solution": r"""$\vec v\cdot\vec w = 5$. $\|\vec w\|^2=1$.
$$\text{proj}_{\vec w}\vec v = \frac{5}{1}(1,0) = (5,0)$$""",
                "answer_type": "open",
            },
            {
                "order_index": 3, "difficulty": 1,
                "question": r"Normaliseer de vector $(3,4)$ tot een vector met lengte $1$.",
                "hints": [
                    "Bereken eerst de lengte $\\|\\vec v\\| = \\sqrt{v_x^2+v_y^2}$.",
                    "Deel elke component door die lengte.",
                ],
                "full_solution": r"""$\|\vec v\| = \sqrt{3^2+4^2} = \sqrt{25}=5$.
$$\hat v = \left(\frac35, \frac45\right)$$""",
                "answer_type": "open",
            },
            {
                "order_index": 4, "difficulty": 2,
                "question": r"Gebruik het inproduct om de hoek tussen $(1,0)$ en $(1,1)$ te bepalen.",
                "hints": [
                    "Gebruik $\\cos\\theta = \\dfrac{\\vec a\\cdot\\vec b}{|\\vec a||\\vec b|}$.",
                    "Bereken het inproduct en de twee lengtes apart.",
                ],
                "full_solution": r"""$\vec a\cdot\vec b = 1\cdot1+0\cdot1=1$. $|\vec a|=1$, $|\vec b|=\sqrt2$.
$$\cos\theta = \frac{1}{1\cdot\sqrt2} = \frac{1}{\sqrt2} \implies \theta = \frac{\pi}{4} = 45°$$""",
                "answer_type": "open",
            },
        ],
    },
]
