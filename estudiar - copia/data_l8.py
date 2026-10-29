# -*- coding: utf-8 -*-
# Nivel 8: Creación secundaria, encajes y multiplicador bancario

L8 = {
    "id": 8,
    "name": "Creación secundaria, encajes y multiplicador bancario",
    "icon": "🔁",
    "parts": [
        {
            "title": "Creación secundaria y tasas de encaje",
            "theory": """
<p>Una vez que el Banco Central crea dinero primario, entra en acción la banca comercial.</p>
<h3>Los bancos comerciales y la creación secundaria de dinero</h3>
<p><span class="tag">Del PDF</span> Los bancos comerciales, al recibir depósitos y conceder préstamos, posibilitan que el dinero ya existente en la economía vuelva a circular nuevamente. <b>Es así como los bancos comerciales crean dinero.</b></p>
<p><b>La creación secundaria se refiere al poder de los bancos comerciales de crear dinero mediante préstamos a los distintos agentes económicos.</b></p>
<h3>La tasa de encaje ($e$)</h3>
<p><span class="tag">Del PDF</span> Como las Reservas Totales ($RT$) pueden expresarse como un porcentaje de los depósitos recibidos, definimos la <b>tasa de encaje ($e$)</b> como la relación entre reservas y depósitos del público:</p>
<div class="exp">
  <b>e = RT / DVₚ</b>
</div>
<h3>Encaje técnico vs. Encaje legal</h3>
<ul>
  <li><b>Encaje técnico:</b> porcentaje de liquidez que los bancos comerciales mantienen de forma <i>voluntaria</i> acorde a sus necesidades operativas de seguridad para atender retiros.</li>
  <li><b>Encaje legal:</b> porcentaje mínimo de reservas que el <i>Banco Central fija con carácter obligatorio</i> para todas las entidades del sistema financiero.</li>
</ul>
<p><span class="tag">Del PDF</span> El banco tendrá más beneficios cuanto más préstamos realice. Dado que existe una tasa legal, <b>la mayor cantidad de préstamos se dará cuando el encaje sea el menor posible; esto es, cuando el encaje técnico y el encaje legal coincidan</b>.</p>
""",
            "quiz": [
                {
                    "t": "¿A qué se refiere la 'creación secundaria de dinero' según la explicación del documento?",
                    "o": [
                        "Al poder de los bancos comerciales de crear dinero mediante la concesión de préstamos a agentes económicos",
                        "A la impresión física de billetes de repuesto por el Ministerio de Economía",
                        "Al rescate de monedas de oro en galeones hundidos",
                        "A la falsificación de cheques en el mercado informal"
                    ],
                    "a": [0],
                    "c": "Mecanismo de creación secundaria por préstamos",
                    "e": "El PDF establece con exactitud que la creación secundaria alude al poder de los bancos comerciales de crear dinero prestando los depósitos recibidos.",
                    "d": 1
                },
                {
                    "t": "¿Cómo se define formalmente la 'tasa de encaje' ($e$) en el texto?",
                    "o": [
                        "Como la relación entre las reservas totales y los depósitos del público: e = RT / DVₚ",
                        "Como la multiplicación entre préstamos y billetes emitidos",
                        "Como el porcentaje de ganancia neta anual del banco",
                        "Como la tasa de interés activa multiplicada por diez"
                    ],
                    "a": [0],
                    "c": "Definición de tasa de encaje: e = RT / DVp",
                    "e": "La tasa de encaje $e$ es la proporción entre las reservas bancarias y los depósitos del público: $e = RT / DV_p$.",
                    "d": 1
                },
                {
                    "t": "¿Qué diferencia existe entre el encaje 'técnico' y el encaje 'legal'?",
                    "o": [
                        "El técnico lo decide voluntariamente el banco según sus necesidades; el legal lo impone obligatoriamente el Banco Central",
                        "El técnico se paga en dólares y el legal en oro",
                        "El legal no existe en Uruguay y el técnico sí",
                        "Son exactamente idénticos y ambos los decide el parlamento"
                    ],
                    "a": [0],
                    "c": "Encaje técnico (voluntario)",
                    "e": "El encaje técnico es la prudencia voluntaria del banco comercial, mientras que el encaje legal es la exigencia regulatoria obligatoria del BCU.",
                    "d": 1
                },
                {
                    "t": "¿En qué condición otorgan los bancos comerciales la mayor cantidad posible de préstamos?",
                    "o": [
                        "Cuando el encaje técnico y el encaje legal coinciden (cuando el encaje adoptado es el menor legalmente posible)",
                        "Cuando el encaje es del 100% de los depósitos",
                        "Cuando el Banco Central prohíbe cobrar intereses",
                        "Cuando los particulares no retiran nunca sus sueldos"
                    ],
                    "a": [0],
                    "c": "Coincidencia encaje técnico = encaje legal para máximo préstamo",
                    "e": "El banco maximiza préstamos cuando opera con el encaje mínimo posible, es decir, cuando su encaje técnico iguala al encaje legal exigido.",
                    "d": 2
                },
                {
                    "t": "Si un banco tiene depósitos del público por $DV_p = \$10.000$ millones y mantiene reservas por $RT = \$2.000$ millones, ¿cuál es su tasa de encaje efectiva ($e$)?",
                    "o": ["20% (e = 0,20)", "5% (e = 0,05)", "50% (e = 0,50)", "2% (e = 0,02)"],
                    "a": [0],
                    "c": "Definición de tasa de encaje: e = RT / DVp",
                    "e": "$e = RT / DV_p = 2.000 / 10.000 = 0,20$ (20%).",
                    "d": 1
                }
            ]
        },
        {
            "title": "Proceso multiplicador y tabla iterativa del PDF",
            "theory": """
<p>Veamos con exactitud matemática el ejemplo que presenta el PDF para ilustrar la multiplicación del dinero.</p>
<h3>El ejemplo numérico del PDF</h3>
<p><span class="tag">Del PDF</span> <b>Suponemos que el Banco Central emite $1000, el encaje legal coincide con el técnico y es de un 20% ($e = 0.2$), y los particulares depositan el total de los fondos recibidos en el sistema bancario.</b></p>
<p>El proceso se desarrolla en etapas sucesivas:</p>
<table border="1" cellpadding="6" style="border-collapse:collapse;margin:12px 0;width:100%;text-align:center">
  <tr style="background:var(--card2)"><th>Etapa</th><th>Nuevos depósitos</th><th>Reservas (20%)</th><th>Nuevos préstamos (80%)</th></tr>
  <tr><td><b>1</b></td><td>$1.000</td><td>$200</td><td>$800</td></tr>
  <tr><td><b>2</b></td><td>$800</td><td>$160</td><td>$640</td></tr>
  <tr><td><b>3</b></td><td>$640</td><td>$128</td><td>$512</td></tr>
  <tr><td><b>4</b></td><td>$512</td><td>$102</td><td>$410</td></tr>
  <tr><td><b>5</b></td><td>$410</td><td>$82</td><td>$328</td></tr>
  <tr><td>...</td><td>...</td><td>...</td><td>...</td></tr>
  <tr style="background:#134e4a;font-weight:bold"><td>TOTALES</td><td>$5.000</td><td>$1.000</td><td>$4.000</td></tr>
</table>
<p><b>¿Qué ocurrió?</b> Con apenas <b>$1.000 iniciales</b> emitidos por el BCU, el sistema de bancos comerciales generó <b>$5.000 en depósitos totales</b>, manteniendo <b>$1.000 en reservas</b> y habiendo concedido <b>$4.000 en nuevos préstamos</b> a la sociedad.</p>
""",
            "quiz": [
                {
                    "t": "En el ejemplo del PDF (emisión inicial de $1.000 y encaje de 20%), ¿cuánto se reserva y cuánto se presta en la Etapa 1?",
                    "o": [
                        "Se reservan $200 y se prestan $800",
                        "Se reservan $500 y se prestan $500",
                        "Se prestan los $1.000 completos sin reservas",
                        "Se retienen $800 en bóveda y se prestan $200"
                    ],
                    "a": [0],
                    "c": "Etapa 1: Depósito 1000, Reserva 200, Préstamo 800",
                    "e": "El 20% de $1.000 son $200 (reservas); el 80% restante ($800) se presta al público.",
                    "d": 1
                },
                {
                    "t": "En la Etapa 2 de la tabla, ¿qué monto ingresa como nuevo depósito y cuánto se otorga en nuevo crédito?",
                    "o": [
                        "Nuevo depósito de $800 y nuevo préstamo de $640 (reservando $160)",
                        "Nuevo depósito de $1.000 y nuevo préstamo de $800",
                        "Nuevo depósito de $640 y nuevo préstamo de $512",
                        "Nuevo depósito de $200 y préstamo de $100"
                    ],
                    "a": [0],
                    "c": "Etapa 2: Depósito 800, Reserva 160, Préstamo 640",
                    "e": "El prestatario anterior gastó los $800, quien los cobró los depositó; de esos $800 se reserva el 20% ($160) y se presta el 80% ($640).",
                    "d": 1
                },
                {
                    "t": "Al completarse todas las etapas hasta el infinito en el ejemplo del documento, ¿a cuánto asciende la suma acumulada de depósitos totales?",
                    "o": ["$5.000", "$1.000", "$4.000", "$10.000"],
                    "a": [0],
                    "c": "Totales: Depósitos $5000, Reservas $1000, Préstamos $4000",
                    "e": "La suma geométrica infinita $1.000 + 800 + 640 + 512 + 410 + ...$ totaliza exactamente $5.000.",
                    "d": 1
                },
                {
                    "t": "¿A cuánto ascienden las Reservas Totales acumuladas en el sistema bancario al final del proceso?",
                    "o": [
                        "$1.000, coincidiendo exactamente con la emisión inicial del Banco Central",
                        "$5.000",
                        "$200",
                        "$0"
                    ],
                    "a": [0],
                    "c": "Totales: Depósitos $5000, Reservas $1000, Préstamos $4000",
                    "e": "Las reservas finales totales son $1.000 (el 20% de los $5.000 de depósitos), que absorben toda la Base Monetaria original.",
                    "d": 2
                },
                {
                    "t": "¿Cuál fue el volumen total de dinero nuevo creado en forma de préstamos por los bancos comerciales en la tabla?",
                    "o": ["$4.000", "$5.000", "$1.000", "$800"],
                    "a": [0],
                    "c": "Totales: Depósitos $5000, Reservas $1000, Préstamos $4000",
                    "e": "La columna de préstamos totales acumulados en la tabla del PDF asciende a $4.000 ($5.000 de depósitos - $1.000 de reservas = $4.000 de crédito).",
                    "d": 1
                }
            ]
        },
        {
            "title": "Fórmulas del multiplicador y factores determinantes",
            "theory": """
<p>La síntesis formal del proceso multiplicador se expresa a través de fórmulas directas.</p>
<h3>La fórmula del multiplicador bancario ($MB$)</h3>
<p><span class="tag">Del PDF</span> Siendo el multiplicador bancario:</p>
<div class="exp">
  <b>MB = 1 / e</b><br>
  En el caso anterior con una tasa de encaje del 20% (e = 0.2):<br>
  <b>MB = 1 / 0.2 = 5</b>
</div>
<h3>Creación total de dinero ($\Delta M$)</h3>
<p><span class="tag">Del PDF</span> Si la serie sigue al infinito, la creación total de dinero responde a la siguiente fórmula:</p>
<div class="exp">
  <b>ΔM = Depósito inicial × (1 / e)</b><br>
  O equivalentemente:<br>
  <b>ΔM = Depósito inicial × MB</b><br>
  <i>En el ejemplo:</i> ΔM = 1.000 × (1 / 0.2) = 1.000 × 5 = <b>$5.000</b> (oferta monetaria máxima).
</div>
<h3>Factores que afectan el valor del multiplicador</h3>
<p><span class="tag">Del PDF</span> Este proceso es el llamado multiplicador del dinero, y da cuenta de la cantidad de dinero que se puede crear en una economía a través de los préstamos concedidos por los bancos comerciales, para un nivel inicial de la base monetaria.</p>
<p>El valor del multiplicador se ve modificado por dos factores centrales:</p>
<ol>
  <li><b>La tasa de encaje ($e$):</b> existe una relación inversa. <i>A mayor tasa de encaje legal o técnica, menor será el multiplicador</i>; a menor encaje, mayor es el multiplicador.</li>
  <li><b>La proporción de fondos que el público desea retener en efectivo:</b> en el ejemplo teórico se supuso que la gente redepositaba el 100% (retención = 0). Pero si los ciudadanos retienen billetes físicos en sus bolsillos y no los depositan en bancos (filtración hacia efectivo), el multiplicador se reduce sensiblemente.</li>
</ol>
""",
            "quiz": [
                {
                    "t": "¿Cuál es la fórmula del multiplicador bancario ($MB$) en función de la tasa de encaje ($e$)?",
                    "o": [
                        "MB = 1 / e",
                        "MB = e / 100",
                        "MB = e × Depósito inicial",
                        "MB = 1 - e"
                    ],
                    "a": [0],
                    "c": "Fórmula del multiplicador bancario: MB = 1 / e",
                    "e": "El PDF establece formalmente: $MB = 1 / e$.",
                    "d": 1
                },
                {
                    "t": "Si la tasa de encaje es del 10% ($e = 0.10$), ¿cuál es el valor del multiplicador bancario?",
                    "o": ["10", "5", "1", "0,10"],
                    "a": [0],
                    "c": "Fórmula del multiplicador bancario: MB = 1 / e",
                    "e": "$MB = 1 / 0.10 = 10$. Por cada peso emitido se pueden generar hasta $10 en dinero bancario.",
                    "d": 1
                },
                {
                    "t": "Si el Banco Central aumenta el encaje legal del 20% al 25% ($e = 0.25$), ¿qué ocurre con el multiplicador bancario?",
                    "o": [
                        "Disminuye de 5 a 4",
                        "Aumenta de 5 a 6",
                        "Se mantiene inalterado en 5",
                        "Pasa a valer 25"
                    ],
                    "a": [0],
                    "c": "Efecto de la tasa de encaje sobre el multiplicador (relación inversa)",
                    "e": "$1 / 0.20 = 5$; $1 / 0.25 = 4$. Al subir el encaje, los bancos deben guardar más y pueden prestar menos, achicando el multiplicador.",
                    "d": 2
                },
                {
                    "t": "¿Qué otro factor real reduce el valor del multiplicador bancario en la economía según el PDF?",
                    "o": [
                        "La proporción de fondos que el público desea mantener en su poder en efectivo",
                        "La cantidad de cajeros automáticos habilitados",
                        "El color de la tinta de los billetes nuevos",
                        "El precio internacional de la carne vacuna"
                    ],
                    "a": [0],
                    "c": "Filtración hacia efectivo del público y reducción del multiplicador",
                    "e": "Si los particulares retienen billetes en sus bolsillos y no los depositan, se frena la cadena de préstamos y el multiplicador cae.",
                    "d": 2
                },
                {
                    "t": "Con un depósito inicial de $3.000 y una tasa de encaje $e = 0.20$ ($MB = 5$), ¿cuál es la oferta monetaria total generada ($\Delta M$)?",
                    "o": ["$15.000", "$3.000", "$600", "$30.000"],
                    "a": [0],
                    "c": "Cálculo de creación total: ΔM = Depósito inicial × (1/e)",
                    "e": "$\\Delta M = \\text{Depósito inicial} \\times MB = 3.000 \\times 5 = 15.000$.",
                    "d": 1
                }
            ]
        }
    ],
    "exam": [
        {
            "t": "¿A través de qué mecanismo específico crean dinero los bancos comerciales según el texto?",
            "o": [
                "Recibiendo depósitos y concediendo préstamos que vuelven a circular en la economía",
                "Acuñando monedas en sus sótanos",
                "Cobrando comisiones por tarjetas de crédito únicamente",
                "Comprando acciones de empresas que cotizan en bolsa"
            ],
            "a": [0],
            "c": "Mecanismo de creación secundaria por préstamos",
            "e": "Los bancos comerciales crean dinero secundario prestando el dinero depositado, el cual al volver a circular genera nuevos depósitos."
        },
        {
            "t": "¿Cómo se define la tasa de encaje ($e$)?",
            "o": [
                "e = RT / DVₚ (relación entre Reservas Totales y Depósitos a la vista del público)",
                "e = DVₚ / RT",
                "e = BM × M₁",
                "e = Préstamos / Depósitos"
            ],
            "a": [0],
            "c": "Definición de tasa de encaje: e = RT / DVp",
            "e": "La tasa de encaje es el cociente entre las reservas líquidas y los depósitos del público: $e = RT / DV_p$."
        },
        {
            "t": "¿Cuándo alcanzan los bancos comerciales su capacidad máxima de concesión de préstamos?",
            "o": [
                "Cuando su encaje técnico voluntario coincide con el encaje legal mínimo exigido por el BCU",
                "Cuando el encaje legal supera el 90%",
                "Cuando dejan de recibir depósitos del público",
                "Cuando prestan exclusivamente al Banco Central"
            ],
            "a": [0],
            "c": "Coincidencia encaje técnico = encaje legal para máximo préstamo",
            "e": "El volumen de crédito es máximo cuando el encaje efectivo retenido es el menor legalmente admitido."
        },
        {
            "t": "En el ejemplo del PDF con emisión inicial de $1.000 y encaje del 20%, ¿cuál es el multiplicador bancario ($MB$)?",
            "o": ["5", "2", "10", "20"],
            "a": [0],
            "c": "Fórmula del multiplicador bancario: MB = 1 / e",
            "e": "$MB = 1 / e = 1 / 0.2 = 5$."
        },
        {
            "t": "Siguiendo el mismo ejemplo del documento, ¿cuál es la oferta monetaria total resultante al cabo de todo el proceso?",
            "o": ["$5.000", "$1.000", "$4.000", "$800"],
            "a": [0],
            "c": "Cálculo de creación total: ΔM = Depósito inicial × (1/e)",
            "e": "Oferta total = $1.000 \\times 5 = $5.000."
        },
        {
            "t": "En la tabla del PDF, ¿cuál es el total acumulado de nuevos préstamos concedidos por el sistema bancario al infinito?",
            "o": ["$4.000", "$5.000", "$1.000", "$2.500"],
            "a": [0],
            "c": "Totales: Depósitos $5000, Reservas $1000, Préstamos $4000",
            "e": "Préstamos totales = Depósitos totales ($5.000) - Reservas retenidas ($1.000) = $4.000."
        },
        {
            "t": "¿Qué sucede con las Reservas Totales de los bancos al final del proceso del ejemplo del PDF?",
            "o": [
                "Suman exactamente $1.000, igualando al monto inicialmente emitido por la Autoridad Monetaria",
                "Se esfuman por completo llegando a cero",
                "Crecen hasta alcanzar los $5.000",
                "Pasan a ser propiedad de una IFE"
            ],
            "a": [0],
            "c": "Totales: Depósitos $5000, Reservas $1000, Préstamos $4000",
            "e": "Toda la emisión primaria de $1.000 termina acumulada en las reservas del sistema bancario respaldando los $5.000 de depósitos al 20%."
        },
        {
            "t": "Si el coeficiente de encaje legal baja del 20% al 10%, ¿qué efecto tiene sobre el multiplicador bancario?",
            "o": [
                "Se duplica, pasando de 5 a 10",
                "Se reduce a la mitad, pasando de 5 a 2,5",
                "Permanece constante en 5",
                "Pasa a ser igual a cero"
            ],
            "a": [0],
            "c": "Efecto de la tasa de encaje sobre el multiplicador (relación inversa)",
            "e": "$1 / 0.10 = 10$, frente a $1 / 0.20 = 5$. El multiplicador se duplica."
        },
        {
            "t": "Si el coeficiente de encaje legal sube del 20% al 50%, ¿cuál será el nuevo multiplicador bancario?",
            "o": ["2", "5", "10", "0,5"],
            "a": [0],
            "c": "Fórmula del multiplicador bancario: MB = 1 / e",
            "e": "$MB = 1 / 0.50 = 2$."
        },
        {
            "t": "¿Por qué la preferencia del público por retener dinero en efectivo frena el proceso multiplicador?",
            "o": [
                "Porque los billetes en el bolsillo de las personas no ingresan al banco y no pueden ser prestados nuevamente",
                "Porque los billetes se deterioran físicamente",
                "Porque el BCU prohíbe gastar efectivo",
                "Porque las monedas metálicas tienen menor velocidad que las tarjetas"
            ],
            "a": [0],
            "c": "Filtración hacia efectivo del público y reducción del multiplicador",
            "e": "Si el dinero sale del circuito bancario como efectivo en mano, se rompe la cadena de depósitos y préstamos sucesivos."
        },
        {
            "t": "En la Etapa 3 del ejemplo del PDF, ¿cuál es el nuevo depósito que recibe el sistema y cuál es el nuevo préstamo otorgado?",
            "o": [
                "Nuevo depósito $640; Reserva $128; Nuevo préstamo $512",
                "Nuevo depósito $800; Reserva $160; Nuevo préstamo $640",
                "Nuevo depósito $512; Reserva $102; Nuevo préstamo $410",
                "Nuevo depósito $1.000; Reserva $200; Nuevo préstamo $800"
            ],
            "a": [0],
            "c": "Etapas sucesivas y convergencia infinita",
            "e": "En la etapa 3: Depósito $640, Reservas $128 (20%) y Préstamo $512 (80%)."
        },
        {
            "t": "Con una tasa de encaje del 25% ($e = 0.25$) y un depósito inicial de $4.000, ¿cuál es el volumen total de dinero creado ($\Delta M$)?",
            "o": ["$16.000", "$4.000", "$1.000", "$8.000"],
            "a": [0],
            "c": "Cálculo de creación total: ΔM = Depósito inicial × (1/e)",
            "e": "$MB = 1 / 0.25 = 4$. $\\Delta M = 4.000 \\times 4 = 16.000$."
        },
        {
            "t": "Verdadero o Falso: Si el encaje bancario fuese del 100% ($e = 1$), los bancos comerciales no podrían crear dinero secundario.",
            "o": ["Verdadero", "Falso"],
            "a": [0],
            "c": "Fórmula del multiplicador bancario: MB = 1 / e",
            "e": "Verdadero. Con $e = 1$, $MB = 1 / 1 = 1$: los bancos deberían retener todo en caja sin prestar un solo peso, impidiendo la creación secundaria."
        },
        {
            "t": "En el modelo del multiplicador, ¿qué representa la serie matemática $1000 + 800 + 640 + 512 + ...$?",
            "o": [
                "La creación sucesiva de depósitos bancarios a lo largo de las distintas etapas de préstamos",
                "La pérdida progresiva de valor de la moneda por inflación",
                "La recaudación tributaria anual del gobierno",
                "El saldo de las cuentas de las AFAPs"
            ],
            "a": [0],
            "c": "Proceso multiplicador y tabla iterativa del PDF",
            "e": "Es la serie de depósitos bancarios generados por el ciclo de préstamos y redepósitos en el sistema."
        },
        {
            "t": "¿Cuál es la fórmula sintética que relaciona la oferta monetaria total ($\Delta M$), la base monetaria inicial y el multiplicador bancario ($MB$)?",
            "o": [
                "ΔM = Depósito inicial × MB",
                "ΔM = Depósito inicial / MB",
                "ΔM = MB + RTᵦ",
                "ΔM = e / Depósito inicial"
            ],
            "a": [0],
            "c": "Fórmulas del multiplicador y factores determinantes",
            "e": "La oferta monetaria total se calcula multiplicando la inyección inicial por el multiplicador bancario: $\\Delta M = \\text{Depósito inicial} \\times MB$."
        }
    ]
}
