# -*- coding: utf-8 -*-
# Nivel 7: Creación primaria del dinero y base monetaria

L7 = {
    "id": 7,
    "name": "Creación primaria del dinero y base monetaria",
    "icon": "🖨️",
    "parts": [
        {
            "title": "¿Quiénes crean dinero? y la Creación Primaria",
            "theory": """
<p>Una de las preguntas más fascinantes de la economía monetaria es: <b>¿de dónde surge el dinero?</b></p>
<h3>¿Quiénes crean el dinero en la economía?</h3>
<p><span class="tag">Del PDF</span> <b>La creación del dinero se hace a través del sistema bancario; crean dinero tanto el Banco Central como los bancos comerciales.</b></p>
<p>Es un error común pensar que solo el Banco Central crea dinero. El Banco Central realiza la creación <i>primaria</i> y los bancos comerciales realizan la creación <i>secundaria</i>.</p>
<h3>La autoridad monetaria y la creación primaria de dinero</h3>
<p><span class="tag">Del PDF</span> <b>La creación primaria de dinero la hace el Banco Central a través de la emisión y de los depósitos de encaje de los bancos comerciales.</b></p>
<ul>
  <li>El poder de crear dinero en forma más directa lo tiene el <b>Banco Central: simplemente emite nuevos billetes y monedas</b>.</li>
  <li>De la misma forma que los particulares tienen depósitos a la vista en los bancos comerciales ($DV_p$), los bancos comerciales tienen <b>depósitos a la vista en el Banco Central ($DV_B$)</b>, llamados también <b>depósitos de encaje</b>. Ambos elementos constituyen el pasivo monetario de la Autoridad Monetaria.</li>
</ul>
""",
            "quiz": [
                {
                    "t": "¿Quiénes tienen la potestad técnica y legal de crear dinero en una economía según el PDF?",
                    "o": [
                        "Tanto el Banco Central como los bancos comerciales",
                        "Únicamente el Ministerio de Economía",
                        "Solo las empresas de la bolsa de valores",
                        "Exclusivamente las Administradoras de Fondos de Pensiones (AFAPs)"
                    ],
                    "a": [0],
                    "c": "Agentes creadores de dinero: BCU y bancos comerciales",
                    "e": "El PDF establece con total claridad que crean dinero tanto el Banco Central (creación primaria) como los bancos comerciales (creación secundaria).",
                    "d": 1
                },
                {
                    "t": "¿Quién realiza exclusivamente la 'creación primaria' de dinero en la economía?",
                    "o": [
                        "El Banco Central",
                        "Los bancos comerciales privados",
                        "Las casas de cambio",
                        "Los particulares al comprar con tarjeta"
                    ],
                    "a": [0],
                    "c": "Definición de creación primaria de dinero",
                    "e": "La creación primaria de dinero es responsabilidad exclusiva de la Autoridad Monetaria (el Banco Central).",
                    "d": 1
                },
                {
                    "t": "¿Cuáles son los dos mecanismos a través de los cuales el Banco Central realiza la creación primaria de dinero?",
                    "o": [
                        "A través de la emisión de billetes y monedas y de los depósitos de encaje de los bancos comerciales",
                        "A través del cobro del IVA y aranceles de aduana",
                        "Mediante el trueque directo de trigo y metales",
                        "A través de la venta de bonos en el mercado minorista únicamente"
                    ],
                    "a": [0],
                    "c": "Definición de creación primaria de dinero",
                    "e": "El PDF señala textualmente que la creación primaria la hace el BCU a través de la emisión y de los depósitos de encaje de los bancos comerciales.",
                    "d": 1
                },
                {
                    "t": "¿Por qué los depósitos de los bancos comerciales en el BCU ($DV_B$) forman parte del dinero creado por la Autoridad Monetaria?",
                    "o": [
                        "Porque el BCU es el 'banco de bancos' y esos depósitos son pasivos monetarios directos de la Autoridad Monetaria",
                        "Porque están impresos en monedas de oro físico de orfebres",
                        "Porque solo pueden retirarse cada diez años",
                        "Porque pertenecen enteramente al Banco Mundial"
                    ],
                    "a": [0],
                    "c": "Depósitos de encaje de los bancos en el BCU",
                    "e": "Al ser el BCU el banco de los bancos, los saldos a la vista de las entidades en el BCU son dinero primario de encaje.",
                    "d": 2
                },
                {
                    "t": "Verdadero o Falso: Los billetes y monedas recién impresos por el BCU que entran a circular constituyen creación primaria de dinero.",
                    "o": ["Verdadero", "Falso"],
                    "a": [0],
                    "c": "Emisión de billetes y monedas por el BCU",
                    "e": "Verdadero. La emisión física de billetes y monedas es la manifestación directa de la creación primaria monetaria.",
                    "d": 1
                }
            ]
        },
        {
            "title": "Base Monetaria (BM) y sus componentes",
            "theory": """
<p>El dinero primario creado por el Banco Central recibe el nombre técnico de <b>Base Monetaria (BM)</b>.</p>
<h3>Fórmula básica de la Base Monetaria</h3>
<p><span class="tag">Del PDF</span> La Base Monetaria se compone de la emisión total más los depósitos a la vista de los bancos en el Banco Central:</p>
<div class="exp">
  <b>BM = EM + DVᵦ</b><br>
  • <b>EM:</b> Emisión total de billetes y monedas efectuada por el BCU.<br>
  • <b>DVᵦ:</b> Depósitos a la vista de los bancos comerciales en el Banco Central.
</div>
<h3>Desglose de la emisión total ($EM$)</h3>
<p>La emisión total de billetes puede encontrarse en dos lugares físicos distintos:</p>
<ul>
  <li>En manos de las familias y empresas: <b>Emisión en poder del público ($EM_p$)</b>.</li>
  <li>En las cajas y bóvedas de los bancos comerciales: <b>Emisión en poder de los bancos ($EM_B$)</b>.</li>
</ul>
<p>Por lo tanto: <b>$EM = EM_p + EM_B$</b>.</p>
<h3>Fórmula extendida y fórmula con Reservas Totales ($RT_B$)</h3>
<p><span class="tag">Del PDF</span> Al sustituir la emisión desglosada en la ecuación de la Base Monetaria:</p>
<div class="exp">
  <b>BM = EMₚ + EMᵦ + DVᵦ</b><br>
  Y como las Reservas Totales de los bancos son <b>RTᵦ = EMᵦ + DVᵦ</b>:<br>
  <b>BM = EMₚ + RTᵦ</b>
</div>
<p>Esta fórmula nos dice que toda la Base Monetaria está en poder del público como efectivo ($EM_p$) o guardada en los bancos como reservas ($RT_B$).</p>
""",
            "quiz": [
                {
                    "t": "¿Cuál es la expresión inicial básica de la Base Monetaria ($BM$) según el PDF?",
                    "o": [
                        "BM = EM + DVᵦ",
                        "BM = M₁ + M₂",
                        "BM = EMₚ + DVₚ",
                        "BM = DVₚ × e"
                    ],
                    "a": [0],
                    "c": "Fórmula BM = EM + DVB",
                    "e": "El PDF define la Base Monetaria inicial como $BM = EM + DV_B$ (emisión total más depósitos a la vista de los bancos en el BCU).",
                    "d": 1
                },
                {
                    "t": "¿Cómo se descompone la emisión total de billetes y monedas ($EM$) según quién la retiene físicamente?",
                    "o": [
                        "EM = EMₚ + EMᵦ (emisión en poder del público más emisión en poder de los bancos)",
                        "EM = DVₚ + DPₚ",
                        "EM = BM - RTᵦ",
                        "EM = M₁ + Dₘ/ₑ"
                    ],
                    "a": [0],
                    "c": "Desglose de la emisión: EM = EMp + EMB",
                    "e": "Los billetes emitidos están o bien en manos de los particulares ($EM_p$) o bien en bóvedas de los bancos comerciales ($EM_B$).",
                    "d": 1
                },
                {
                    "t": "¿Cómo se define el término Reservas Totales de los bancos comerciales ($RT_B$) en las fórmulas?",
                    "o": [
                        "RTᵦ = EMᵦ + DVᵦ",
                        "RTᵦ = EMₚ + DVₚ",
                        "RTᵦ = M₂ - M₁",
                        "RTᵦ = DVₚ / e"
                    ],
                    "a": [0],
                    "c": "Fórmula con Reservas Totales: BM = EMp + RTB",
                    "e": "Las reservas bancarias totales se componen de los billetes en caja del banco ($EM_B$) más sus depósitos de encaje en el BCU ($DV_B$).",
                    "d": 1
                },
                {
                    "t": "¿Cuál es la fórmula final consolidada de la Base Monetaria ($BM$) en función de las Reservas Totales ($RT_B$)?",
                    "o": [
                        "BM = EMₚ + RTᵦ",
                        "BM = DVₚ + RTᵦ",
                        "BM = EMᵦ + DPₚ",
                        "BM = M₁ + RTᵦ"
                    ],
                    "a": [0],
                    "c": "Fórmula con Reservas Totales: BM = EMp + RTB",
                    "e": "El PDF concluye que $BM = EM_p + RT_B$ (efectivo en poder del público más las reservas totales bancarias).",
                    "d": 1
                },
                {
                    "t": "Si $EM_p = \$600$, $EM_B = \$150$ y $DV_B = \$250$ millones, ¿cuánto valen las Reservas Totales ($RT_B$) y la Base Monetaria ($BM$)?",
                    "o": [
                        "RTᵦ = $400 millones y BM = $1.000 millones",
                        "RTᵦ = $750 millones y BM = $850 millones",
                        "RTᵦ = $600 millones y BM = $600 millones",
                        "RTᵦ = $250 millones y BM = $400 millones"
                    ],
                    "a": [0],
                    "c": "Definición formal de Base Monetaria (BM)",
                    "e": "$RT_B = EM_B + DV_B = 150 + 250 = 400$. $BM = EM_p + RT_B = 600 + 400 = 1.000$ millones.",
                    "d": 2
                }
            ]
        },
        {
            "title": "Reservas Totales y la distinción clave DVp vs. DVB",
            "theory": """
<p>Llegamos a uno de los puntos conceptuales más decisivos de todo el PDF.</p>
<h3>Definición formal de Reservas Totales</h3>
<p><span class="tag">Del PDF</span> <b>Reservas totales: es el dinero que los bancos comerciales mantienen para poder hacer frente a eventuales retiros de depósitos, y está formado por la emisión en su poder ($EM_B$) y los depósitos de encaje en el Banco Central ($DV_B$).</b></p>
<h3>La distinción crucial: $DV_p$ vs. $DV_B$</h3>
<p><span class="tag">Del PDF</span> <b>Es importante diferenciar entre los depósitos a la vista de los particulares en los bancos comerciales ($DV_p$) y los depósitos de encaje o a la vista de los bancos comerciales en el Banco Central ($DV_B$); esta distinción permitirá entender la creación secundaria de dinero.</b></p>
<div class="exp">
  <b>Comparativa directa:</b><br>
  • <b>DVₚ:</b> Son depósitos de las personas y empresas en los bancos comerciales. Forman parte directa de la oferta de <b>Medios de Pago ($M_1$)</b>. Es dinero disponible para transacciones de la economía real.<br>
  • <b>DVᵦ:</b> Son depósitos de los bancos comerciales en la cuenta del Banco Central (encaje). Forman parte de la <b>Base Monetaria ($BM$)</b>, NO forman parte de $M_1$. Son reservas de respaldo institucional del sistema.
</div>
""",
            "quiz": [
                {
                    "t": "¿Qué son exactamente las 'Reservas Totales' de los bancos comerciales según el PDF?",
                    "o": [
                        "El dinero que los bancos comerciales mantienen para poder hacer frente a eventuales retiros de depósitos, formado por $EM_B$ y $DV_B$",
                        "Los préstamos concedidos a largo plazo a empresas industriales",
                        "Las ganancias netas distribuidas a los accionistas privados",
                        "Los billetes que los particulares guardan en sus billeteras"
                    ],
                    "a": [0],
                    "c": "Definición de Reservas Totales (RTB = EMB + DVB)",
                    "e": "El PDF define textualmente las Reservas Totales como el dinero para retiros, integrado por emisión en bóveda ($EM_B$) y depósitos en el BCU ($DV_B$).",
                    "d": 1
                },
                {
                    "t": "¿Cuál es la diferencia medular entre $DV_p$ y $DV_B$?",
                    "o": [
                        "$DV_p$ son depósitos de particulares en bancos comerciales; $DV_B$ son depósitos de bancos comerciales en el Banco Central",
                        "$DV_p$ es emitido por orfebres y $DV_B$ por casas financieras",
                        "$DV_p$ solo se puede usar en el extranjero y $DV_B$ en Montevideo",
                        "Son exactamente la misma variable y tienen el mismo valor en la Base Monetaria"
                    ],
                    "a": [0],
                    "c": "Distinción crucial entre DVp y DVB",
                    "e": "$DV_p$ pertenece a particulares (hace a $M_1$), mientras que $DV_B$ pertenece a bancos comerciales en el BCU (hace a $BM$).",
                    "d": 2
                },
                {
                    "t": "¿En cuál magnitud monetaria se computa directamente el componente $DV_p$?",
                    "o": [
                        "En los medios de pago ($M_1$)",
                        "En la Base Monetaria ($BM$)",
                        "En el capital accionario del BROU",
                        "En las reservas internacionales de oro"
                    ],
                    "a": [0],
                    "c": "Impacto de DVp en M1 vs DVB en Base Monetaria",
                    "e": "$M_1 = EM_p + DV_p$. Por lo tanto, $DV_p$ integra los medios de pago disponibles.",
                    "d": 2
                },
                {
                    "t": "¿En cuál magnitud monetaria se incluye el componente $DV_B$?",
                    "o": [
                        "En la Base Monetaria ($BM$)",
                        "En los medios de pago ($M_1$)",
                        "En el Producto Interno Bruto",
                        "En el spread bancario activo"
                    ],
                    "a": [0],
                    "c": "Impacto de DVp en M1 vs DVB en Base Monetaria",
                    "e": "$BM = EM + DV_B = EM_p + RT_B$. $DV_B$ integra la Base Monetaria creada por el BCU.",
                    "d": 2
                },
                {
                    "t": "¿Por qué el PDF recalca que distinguir $DV_p$ de $DV_B$ es imprescindible?",
                    "o": [
                        "Porque esta distinción permitirá entender el proceso de creación secundaria de dinero por parte de los bancos comerciales",
                        "Para saber cuántos billetes se deben destruir cada mes",
                        "Porque está prohibido por ley que existan depósitos de particulares",
                        "Para calcular la tasa de natalidad del país"
                    ],
                    "a": [0],
                    "c": "Distinción crucial entre DVp y DVB",
                    "e": "El PDF señala textualmente: 'esta distinción permitirá entender la creación secundaria de dinero'.",
                    "d": 1
                }
            ]
        }
    ],
    "exam": [
        {
            "t": "¿Quiénes crean dinero en una economía moderna según el capítulo del PDF?",
            "o": [
                "Tanto el Banco Central (creación primaria) como los bancos comerciales (creación secundaria)",
                "Exclusivamente el Banco Central mediante la acuñación de monedas",
                "Únicamente los bancos comerciales privados a través del cobro de comisiones",
                "Las familias al ahorrar en alcancías"
            ],
            "a": [0],
            "c": "Agentes creadores de dinero: BCU y bancos comerciales",
            "e": "La creación monetaria la realiza conjuntamente el sistema bancario: primaria por el BCU y secundaria por bancos comerciales."
        },
        {
            "t": "¿A través de qué instrumentos lleva a cabo el Banco Central la creación primaria de dinero?",
            "o": [
                "De la emisión de billetes y monedas y de los depósitos de encaje de los bancos comerciales",
                "De la colocación de acciones en Wall Street",
                "Del cobro de multas de tránsito",
                "De la compraventa de ganado vacuno"
            ],
            "a": [0],
            "c": "Definición de creación primaria de dinero",
            "e": "El BCU crea dinero primario emitiendo efectivo y recibiendo depósitos de encaje bancario."
        },
        {
            "t": "¿Cuál de las siguientes fórmulas representa de manera exacta la Base Monetaria ($BM$)?",
            "o": [
                "BM = EMₚ + RTᵦ",
                "BM = M₁ + DPₚ",
                "BM = DVₚ + DPₚ",
                "BM = EMₚ / e"
            ],
            "a": [0],
            "c": "Fórmula con Reservas Totales: BM = EMp + RTB",
            "e": "La Base Monetaria equivale a la emisión en poder del público más las reservas totales bancarias ($BM = EM_p + RT_B$)."
        },
        {
            "t": "Si la emisión total es $EM = \$800$ millones y los depósitos de encaje de los bancos en el BCU son $DV_B = \$200$ millones, ¿cuál es la Base Monetaria?",
            "o": ["$1.000 millones", "$600 millones", "$1.600 millones", "$400 millones"],
            "a": [0],
            "c": "Fórmula BM = EM + DVB",
            "e": "$BM = EM + DV_B = 800 + 200 = 1.000$ millones."
        },
        {
            "t": "Los billetes que se encuentran guardados físicamente en las cajas de seguridad y cajeros de los bancos comerciales se denominan:",
            "o": [
                "Emisión en poder de los bancos ($EM_B$)",
                "Emisión en poder del público ($EM_p$)",
                "Medios de pago restringidos ($M_1$)",
                "Dinero fiduciario diferido"
            ],
            "a": [0],
            "c": "Emisión en bóveda de los bancos (EMB)",
            "e": "$EM_B$ es la fracción de la emisión total retenida en bóvedas y sucursales de los bancos comerciales."
        },
        {
            "t": "¿Qué componen en conjunto las 'Reservas Totales' de los bancos comerciales ($RT_B$)?",
            "o": [
                "La emisión en poder de los bancos ($EM_B$) más los depósitos de encaje en el BCU ($DV_B$)",
                "El saldo de las cuentas corrientes de los clientes particulares",
                "Los préstamos concedidos a empresas públicas",
                "Los depósitos a plazo fijo en moneda extranjera"
            ],
            "a": [0],
            "c": "Definición de Reservas Totales (RTB = EMB + DVB)",
            "e": "Las reservas bancarias totales integran tanto el dinero en caja del banco como sus fondos depositados en el Banco Central."
        },
        {
            "t": "¿Cuál es la diferencia sustancial entre $DV_p$ y $DV_B$ que se enfatiza en el texto?",
            "o": [
                "$DV_p$ son depósitos del público en bancos (componen $M_1$), mientras que $DV_B$ son depósitos de bancos en el BCU (componen $BM$)",
                "$DV_p$ no se puede retirar y $DV_B$ se retira en cajeros de la calle",
                "$DV_B$ devenga una tasa activa del 40% y $DV_p$ no existe en Uruguay",
                "Son nombres sinónimos para el mismo concepto"
            ],
            "a": [0],
            "c": "Distinción crucial entre DVp y DVB",
            "e": "La distinción clave separa el dinero de los particulares ($DV_p$, en $M_1$) de los encajes de los bancos en el BCU ($DV_B$, en $BM$)."
        },
        {
            "t": "Si $EM_p = \$500$ y las reservas totales de los bancos comerciales son $RT_B = \$300$, ¿cuál es el monto total de la Base Monetaria?",
            "o": ["$800", "$200", "$1.500", "$500"],
            "a": [0],
            "c": "Fórmula con Reservas Totales: BM = EMp + RTB",
            "e": "$BM = EM_p + RT_B = 500 + 300 = 800$."
        },
        {
            "t": "Si un banco comercial envía $10 millones en billetes desde su bóveda ($EM_B$) para depositarlos en su cuenta de encaje en el BCU ($DV_B$), ¿qué ocurre con las Reservas Totales ($RT_B$)?",
            "o": [
                "Permanecen sin cambios: disminuye $EM_B$ en $10 millones y aumenta $DV_B$ en $10 millones",
                "Aumentan en $20 millones",
                "Disminuyen a cero",
                "Se transforman automáticamente en depósitos a la vista del público"
            ],
            "a": [0],
            "c": "Definición de Reservas Totales (RTB = EMB + DVB)",
            "e": "Es un movimiento interno dentro de las reservas: $RT_B = EM_B + DV_B$, por lo que el total de reservas bancarias no se altera."
        },
        {
            "t": "¿Forman los depósitos de encaje de los bancos en el BCU ($DV_B$) parte de los medios de pago $M_1$ en manos del público?",
            "o": [
                "No, porque están inmovilizados en el Banco Central como respaldo y no circulan para compras cotidianas",
                "Sí, cualquier persona puede pagar un café librando cheques contra $DV_B$",
                "Sí, porque están sumados dentro de la fórmula $M_1 = EM_p + DV_p$",
                "Solo los fines de semana"
            ],
            "a": [0],
            "c": "Impacto de DVp en M1 vs DVB en Base Monetaria",
            "e": "$DV_B$ es reserva institucional del sistema bancario en el BCU, no dinero transaccional del público ($M_1$)."
        },
        {
            "t": "Si el Banco Central emite $\$100$ millones en billetes nuevos y los transfiere directamente a la economía, ¿qué magnitud monetaria se expande de forma primaria inmediata?",
            "o": ["La Base Monetaria (BM)", "El spread bancario", "La tasa de encaje técnico", "Los depósitos en moneda extranjera exclusivamente"],
            "a": [0],
            "c": "Definición de creación primaria de dinero",
            "e": "Toda nueva emisión del BCU incrementa directamente la Base Monetaria."
        },
        {
            "t": "¿Cuál de las siguientes afirmaciones sobre la Base Monetaria es FALSA?",
            "o": [
                "La Base Monetaria incluye los depósitos a plazo fijo de los particulares en moneda nacional",
                "La Base Monetaria es igual a $EM + DV_B$",
                "La Base Monetaria es igual a $EM_p + EM_B + DV_B$",
                "La Base Monetaria es igual a $EM_p + RT_B$"
            ],
            "a": [0],
            "c": "Definición formal de Base Monetaria (BM)",
            "e": "Es falsa: los depósitos a plazo de particulares ($DP_p$) forman parte de $M_2$, no de la Base Monetaria."
        },
        {
            "t": "¿Por qué a la Base Monetaria se la conoce también en la doctrina como 'dinero de alto poder expansivo'?",
            "o": [
                "Porque sobre ella el sistema bancario comercial monta el proceso de creación secundaria de dinero y multiplicador",
                "Porque está hecha de metales explosivos",
                "Porque solo se utiliza en transacciones de satélites espaciales",
                "Porque nunca puede perder valor adquisitivo"
            ],
            "a": [0],
            "c": "Definición formal de Base Monetaria (BM)",
            "e": "La Base Monetaria sirve como cimiento sobre el cual los bancos comerciales multiplican los depósitos y créditos."
        },
        {
            "t": "Si una economía tiene $EM_p = \$1.000$, $EM_B = \$200$, $DV_B = \$300$ y $DV_p = \$1.200$, ¿cuánto valen la Base Monetaria ($BM$) y los Medios de Pago ($M_1$)?",
            "o": [
                "BM = $1.500 y M₁ = $2.200",
                "BM = $2.700 y M₁ = $1.000",
                "BM = $1.000 y M₁ = $1.500",
                "BM = $1.200 y M₁ = $2.000"
            ],
            "a": [0],
            "c": "Definición formal de Base Monetaria (BM)",
            "e": "$BM = EM_p + EM_B + DV_B = 1.000 + 200 + 300 = 1.500$. $M_1 = EM_p + DV_p = 1.000 + 1.200 = 2.200$."
        },
        {
            "t": "Al estudiar la creación de dinero, ¿qué rol cumplen los particulares al depositar sus fondos en un banco comercial?",
            "o": [
                "Aportan depósitos a la vista ($DV_p$) que permiten a los bancos mantener una fracción como reserva ($RT_B$) y prestar el resto",
                "Efectúan la creación primaria emitiendo moneda",
                "Anulan la Base Monetaria de la economía",
                "Actúan como prestamistas de última instancia"
            ],
            "a": [0],
            "c": "Impacto de DVp en M1 vs DVB en Base Monetaria",
            "e": "Los depósitos del público alimentan el circuito de encajes y nuevos préstamos que activa el multiplicador bancario."
        }
    ]
}
