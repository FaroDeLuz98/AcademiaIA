# -*- coding: utf-8 -*-
# Nivel 3: Agregados monetarios M1, M2 y M3

L3 = {
    "id": 3,
    "name": "Agregados monetarios M1, M2 y M3",
    "icon": "📊",
    "parts": [
        {
            "title": "Medios de pago (M1) — La definición más restringida",
            "theory": """
<p>Los bancos centrales clasifican el dinero en <b>agregados monetarios</b> según su grado de liquidez y amplitud.</p>
<h3>Definición de Medios de Pago ($M_1$)</h3>
<p><span class="tag">Del PDF</span> Se denomina <b>medios de pago ($M_1$)</b> a la <b>emisión en poder del público</b> más los <b>depósitos a la vista de los particulares en los bancos comerciales en moneda nacional</b>.</p>
<p>Constituye la <b>definición más restringida de dinero</b>, porque incluye exclusivamente aquellos activos financieros que gozan de liquidez perfecta o casi perfecta para realizar compras directas e inmediatas.</p>
<h3>Fórmula formal de $M_1$</h3>
<div class="exp">
  <b>M₁ = EMₚ + DVₚ</b><br>
  • <b>EMₚ:</b> Emisión en poder del público (billetes y monedas físicos en manos de particulares y empresas).<br>
  • <b>DVₚ:</b> Depósitos a la vista de los particulares en los bancos comerciales en moneda nacional (pesos uruguayos).
</div>
<h3>Ejemplo numérico</h3>
<p>Si la emisión en poder del público en Uruguay es de $50.000 millones y los particulares tienen depositados a la vista en los bancos comerciales $80.000 millones en moneda nacional:</p>
<p><b>M₁ = $50.000 + $80.000 = $130.000 millones de pesos</b>.</p>
""",
            "quiz": [
                {
                    "t": "¿Cuál es la fórmula matemática de los medios de pago ($M_1$) según el PDF?",
                    "o": [
                        "M₁ = EMₚ + DVₚ",
                        "M₁ = EMₚ + DPₚ",
                        "M₁ = DVₚ + DPₚ",
                        "M₁ = EMₚ + RTᵦ"
                    ],
                    "a": [0],
                    "c": "Definición y fórmula de M1 (EMp + DVp)",
                    "e": "El PDF establece de forma explícita que M₁ = EMₚ + DVₚ (emisión en poder del público más depósitos a la vista de particulares en moneda nacional).",
                    "d": 1
                },
                {
                    "t": "¿Por qué se denomina a $M_1$ la 'definición más restringida de dinero'?",
                    "o": [
                        "Porque sólo incluye los activos con máxima liquidez de uso inmediato como medio de pago directo",
                        "Porque está prohibido usarlo fuera de Montevideo",
                        "Porque únicamente incluye los billetes que tienen más de 10 años",
                        "Porque solo pueden tenerlo las instituciones estatales"
                    ],
                    "a": [0],
                    "c": "Por qué M1 es la definición más restringida",
                    "e": "Es la definición más restringida porque se limita al efectivo en manos de la gente y depósitos a la vista, excluyendo depósitos a plazo y monedas extranjeras.",
                    "d": 1
                },
                {
                    "t": "¿Qué representa la sigla $DV_p$ dentro de la fórmula de $M_1$?",
                    "o": [
                        "Depósitos a la vista de los particulares en los bancos comerciales en moneda nacional",
                        "Deuda vencida del público en dólares",
                        "Depósitos voluntarios de los bancos en el Banco Central",
                        "Divisas en poder del público"
                    ],
                    "a": [0],
                    "c": "Componente DVp: depósitos a la vista en moneda nacional",
                    "e": "$DV_p$ designa a los depósitos a la vista de particulares en bancos comerciales en moneda nacional.",
                    "d": 1
                },
                {
                    "t": "Si en una economía $EM_p = \$400$ millones y $DV_p = \$700$ millones, ¿cuál es el total de medios de pago ($M_1$)?",
                    "o": ["$1.100 millones", "$300 millones", "$280.000 millones", "$700 millones"],
                    "a": [0],
                    "c": "Definición y fórmula de M1 (EMp + DVp)",
                    "e": "$M_1 = EM_p + DV_p = \$400 + \$700 = \$1.100$ millones.",
                    "d": 1
                },
                {
                    "t": "Un ciudadano retira $5.000 en efectivo de su caja de ahorros en un cajero automático. ¿Qué sucede con el valor total del agregado $M_1$?",
                    "o": [
                        "Permanece exactamente igual, porque disminuye $DV_p$ en $5.000 y aumenta $EM_p$ en la misma cantidad",
                        "Aumenta en $5.000 porque ahora hay más billetes físicos",
                        "Disminuye en $5.000 porque salió dinero del banco",
                        "Se duplica automáticamente"
                    ],
                    "a": [0],
                    "c": "Definición y fórmula de M1 (EMp + DVp)",
                    "e": "Es una sustitución interna entre componentes de $M_1$: $\\Delta EM_p = +5.000$ y $\\Delta DV_p = -5.000$, por lo que $M_1$ no se modifica.",
                    "d": 2
                }
            ]
        },
        {
            "title": "Cantidad de dinero (M2) — Incorporación de depósitos a plazo",
            "theory": """
<p>Para medir el dinero con mayor amplitud, se debe considerar el ahorro colocado a plazo en el sistema bancario.</p>
<h3>Definición de Cantidad de Dinero ($M_2$)</h3>
<p><span class="tag">Del PDF</span> Una definición más amplia de dinero considera, además, a los <b>depósitos a plazo</b>.</p>
<p>Se denomina <b>cantidad de dinero ($M_2$)</b> a la <b>emisión, más los depósitos de los particulares en los bancos comerciales en moneda nacional, ya sean a la vista o a plazo fijo ($DP_p$)</b>.</p>
<h3>Fórmulas de $M_2$</h3>
<div class="exp">
  <b>M₂ = EMₚ + DVₚ + DPₚ</b><br>
  O expresado de forma resumida:<br>
  <b>M₂ = M₁ + DPₚ</b>
</div>
<h3>¿Por qué $M_2$ es menos líquido que $M_1$?</h3>
<p><span class="tag">Del PDF</span> <b>El $M_2$ es menos líquido que el $M_1$</b>, ya que un <b>depósito a plazo sólo puede retirarse a la fecha de su vencimiento</b>. No podés pagar una compra en el supermercado entregando un certificado de depósito a plazo fijo.</p>
<h3>Efecto de traspasos entre cuentas</h3>
<p>Si una persona traslada $20.000 de su cuenta a la vista a un plazo fijo a 180 días:</p>
<ul>
  <li>$M_1$ disminuye en $20.000 (porque cayó $DV_p$).</li>
  <li>$M_2$ <b>permanece sin cambios</b> (porque la caída de $DV_p$ se compensa con el aumento de $DP_p$).</li>
</ul>
""",
            "quiz": [
                {
                    "t": "¿Cuál es la expresión equivalente de la cantidad de dinero ($M_2$) en función de $M_1$?",
                    "o": [
                        "M₂ = M₁ + DPₚ",
                        "M₂ = M₁ - DVₚ",
                        "M₂ = M₁ × e",
                        "M₂ = M₁ + RTᵦ"
                    ],
                    "a": [0],
                    "c": "Definición y fórmula de M2 (M1 + DPp)",
                    "e": "El PDF establece que $M_2 = EM_p + DV_p + DP_p = M_1 + DP_p$.",
                    "d": 1
                },
                {
                    "t": "¿Por qué el agregado $M_2$ es menos líquido que los medios de pago ($M_1$)?",
                    "o": [
                        "Porque incorpora depósitos a plazo fijo ($DP_p$), los cuales sólo pueden retirarse al vencimiento pactado",
                        "Porque incluye monedas de oro que están bajo tierra",
                        "Porque está formado únicamente por dólares billete",
                        "Porque está prohibido canjearlo por bienes"
                    ],
                    "a": [0],
                    "c": "Comparación de liquidez entre M1 y M2",
                    "e": "Los depósitos a plazo fijo pierden liquidez transitoria al no poder retirarse antes del vencimiento.",
                    "d": 1
                },
                {
                    "t": "Si $M_1 = \$2.500$ millones y los depósitos a plazo en moneda nacional suman $DP_p = \$1.500$ millones, ¿cuánto vale $M_2$?",
                    "o": ["$4.000 millones", "$1.000 millones", "$2.500 millones", "$3.750 millones"],
                    "a": [0],
                    "c": "Cálculo de M2 a partir de M1 y DPp",
                    "e": "$M_2 = M_1 + DP_p = \$2.500 + \$1.500 = \$4.000$ millones.",
                    "d": 1
                },
                {
                    "t": "Una empresa transfiere $100.000 de su cuenta corriente bancaria ($DV_p$) a un plazo fijo a 60 días ($DP_p$). ¿Qué ocurre con $M_1$ y con $M_2$?",
                    "o": [
                        "$M_1$ se reduce en $100.000 y $M_2$ no cambia",
                        "$M_1$ y $M_2$ aumentan ambos en $100.000",
                        "$M_1$ no cambia y $M_2$ disminuye en $100.000",
                        "Ambos agregados se reducen a cero"
                    ],
                    "a": [0],
                    "c": "Definición y fórmula de M2 (M1 + DPp)",
                    "e": "Al salir de la cuenta corriente, $M_1$ cae en $100.000. Pero como $DP_p$ entra en $M_2$, el total de $M_2$ se mantiene constante.",
                    "d": 2
                },
                {
                    "t": "Elegí TODAS las afirmaciones correctas sobre el agregado $M_2$ según el PDF:",
                    "o": [
                        "Incluye la emisión en poder del público ($EM_p$)",
                        "Incluye los depósitos a la vista en moneda nacional ($DV_p$)",
                        "Incluye los depósitos a plazo fijo en moneda nacional ($DP_p$)",
                        "Es más líquido que $M_1$"
                    ],
                    "a": [0, 1, 2],
                    "c": "Definición y fórmula de M2 (M1 + DPp)",
                    "e": "Las tres primeras opciones componen $M_2$. La cuarta es falsa, porque $M_2$ es MENOS líquido que $M_1$.",
                    "d": 2
                }
            ]
        },
        {
            "title": "Agregado M3 y dolarización en Uruguay",
            "theory": """
<p>El Uruguay y diversos países de la región presentan una característica estructural clave: la <b>dolarización</b>.</p>
<h3>La dolarización y la necesidad del agregado $M_3$</h3>
<p><span class="tag">Del PDF</span> En economías con un <b>alto grado de dolarización</b>, como ocurre en América Latina y específicamente en Uruguay, puede ser muy útil incluir en una definición más amplia de dinero a los <b>depósitos en moneda extranjera</b>.</p>
<p>Muchas familias y empresas uruguayas ahorran y mantienen saldos bancarios en dólares estadounidenses. Por eso, para medir toda la liquidez del sistema bancario, el BCU define el agregado <b>$M_3$</b>.</p>
<h3>Definición y fórmulas de $M_3$</h3>
<p><span class="tag">Del PDF</span> Se define <b>$M_3$</b> como la <b>emisión más los depósitos en el sistema bancario, tanto en moneda nacional como en moneda extranjera (para el caso de nuestro país, esto implica considerar pesos y dólares)</b>.</p>
<div class="exp">
  <b>M₃ = EMₚ + (DVₚ + DPₚ)ₘ/ₙ + DPₘ/ₑ</b><br>
  O expresado de forma compacta:<br>
  <b>M₃ = M₂ + Dₘ/ₑ</b><br>
  • <b>Dₘ/ₑ:</b> Depósitos en moneda extranjera en el sistema bancario (valuados en moneda nacional).
</div>
<h3>Relación de amplitud entre los tres agregados</h3>
<p><b>M₁ ⊂ M₂ ⊂ M₃</b></p>
<ul>
  <li><b>M₁:</b> La más restringida y líquida (efectivo + depósitos a la vista en pesos).</li>
  <li><b>M₂:</b> Intermedia (agrega depósitos a plazo en pesos).</li>
  <li><b>M₃:</b> La más amplia (agrega todos los depósitos en moneda extranjera).</li>
</ul>
""",
            "quiz": [
                {
                    "t": "¿Por qué motivo fundamental se define el agregado monetario $M_3$ en el sistema uruguayo?",
                    "o": [
                        "Por el alto grado de dolarización de la economía, que exige computar depósitos en moneda extranjera",
                        "Para calcular cuántas monedas de oro quedan en las bóvedas públicas",
                        "Para medir únicamente las transacciones del sector agrícola",
                        "Porque el BCU dejó de usar el peso uruguayo"
                    ],
                    "a": [0],
                    "c": "Dolarización financiera en América Latina y Uruguay",
                    "e": "El PDF señala expresamente que por el alto grado de dolarización en América Latina y Uruguay resulta útil considerar depósitos en moneda extranjera mediante $M_3$.",
                    "d": 1
                },
                {
                    "t": "¿Cuál es la fórmula compacta de $M_3$ expresada a partir de $M_2$ según el texto?",
                    "o": [
                        "M₃ = M₂ + Dₘ/ₑ",
                        "M₃ = M₂ - DPₚ",
                        "M₃ = M₂ / e",
                        "M₃ = M₂ + BM"
                    ],
                    "a": [0],
                    "c": "Definición y fórmula de M3 (M2 + Dm/e)",
                    "e": "El PDF define textualmente: $M_3 = M_2 + D_{m/e}$, donde $D_{m/e}$ son los depósitos en moneda extranjera.",
                    "d": 1
                },
                {
                    "t": "Una persona abre una cuenta con un depósito a plazo fijo en dólares en un banco de Montevideo. ¿En cuál agregado se computa?",
                    "o": [
                        "En $M_3$, pero no en $M_1$ ni en $M_2$",
                        "En $M_1$ exclusivamente",
                        "En $M_2$ únicamente",
                        "En ninguno, porque los dólares no se consideran dinero bancario"
                    ],
                    "a": [0],
                    "c": "Depósitos en moneda extranjera (dólares)",
                    "e": "$M_1$ y $M_2$ consideran depósitos en moneda nacional (pesos). Los depósitos en moneda extranjera se incorporan al definir $M_3$.",
                    "d": 2
                },
                {
                    "t": "Si $M_2 = \$5.000$ millones y los depósitos en moneda extranjera equivalen a $D_{m/e} = \$3.000$ millones, ¿cuál es el valor de $M_3$?",
                    "o": ["$8.000 millones", "$2.000 millones", "$15.000 millones", "$5.000 millones"],
                    "a": [0],
                    "c": "Definición y fórmula de M3 (M2 + Dm/e)",
                    "e": "$M_3 = M_2 + D_{m/e} = \$5.000 + \$3.000 = \$8.000$ millones.",
                    "d": 1
                },
                {
                    "t": "Ordená los tres agregados monetarios desde el MÁS RESTRINGIDO (más líquido) hacia el MÁS AMPLIO:",
                    "o": [
                        "M₁ → M₂ → M₃",
                        "M₃ → M₂ → M₁",
                        "M₂ → M₁ → M₃",
                        "M₁ → M₃ → M₂"
                    ],
                    "a": [0],
                    "c": "Comparación de amplitud entre M1, M2 y M3",
                    "e": "$M_1$ es el más restringido ($EM_p + DV_p$), $M_2$ agrega $DP_p$, y $M_3$ es el más amplio al sumar depósitos en moneda extranjera.",
                    "d": 1
                }
            ]
        }
    ],
    "exam": [
        {
            "t": "¿Cuál es la definición académica formal de 'medios de pago' ($M_1$) según el PDF?",
            "o": [
                "La emisión en poder del público más los depósitos a la vista de los particulares en bancos comerciales en moneda nacional",
                "El total de billetes impresos por el Banco Central guardados en su bóveda",
                "La suma de todos los préstamos bancarios otorgados a empresas",
                "El total de depósitos a plazo fijo en dólares estadounidenses"
            ],
            "a": [0],
            "c": "Definición y fórmula de M1 (EMp + DVp)",
            "e": "$M_1$ abarca la emisión en poder del público ($EM_p$) más los depósitos a la vista de particulares en moneda nacional ($DV_p$)."
        },
        {
            "t": "Si $EM_p = \$300$, $DV_p = \$500$ y $DP_p = \$400$ (todos en moneda nacional), ¿cuánto valen $M_1$ y $M_2$ respectivamente?",
            "o": [
                "M₁ = $800 y M₂ = $1.200",
                "M₁ = $300 y M₂ = $700",
                "M₁ = $1.200 y M₂ = $800",
                "M₁ = $500 y M₂ = $900"
            ],
            "a": [0],
            "c": "Cálculo de M2 a partir de M1 y DPp",
            "e": "$M_1 = 300 + 500 = 800$. $M_2 = M_1 + DP_p = 800 + 400 = 1.200$."
        },
        {
            "t": "¿Por qué un depósito a la vista forma parte de $M_1$ pero un depósito a plazo fijo solo entra a partir de $M_2$?",
            "o": [
                "Por la diferencia de liquidez: el depósito a la vista está disponible de inmediato, mientras que el plazo fijo está inmovilizado hasta vencer",
                "Porque los depósitos a la vista están gravados con impuestos y los plazos fijos no",
                "Porque el depósito a plazo solo lo emite el gobierno central",
                "Porque los depósitos a la vista son en dólares y los plazos fijos en pesos"
            ],
            "a": [0],
            "c": "Comparación de liquidez entre M1 y M2",
            "e": "$M_1$ se reserva a los activos de liquidez inmediata; el plazo fijo, al no ser disponible hasta su vencimiento, entra en la definición más amplia $M_2$."
        },
        {
            "t": "En una economía con alto grado de dolarización como Uruguay, ¿qué agregado permite medir tanto depósitos en pesos como en dólares?",
            "o": ["M₃", "M₁", "M₂", "Base Monetaria"],
            "a": [0],
            "c": "Dolarización financiera en América Latina y Uruguay",
            "e": "$M_3$ incluye depósitos en moneda nacional y en moneda extranjera ($M_3 = M_2 + D_{m/e}$)."
        },
        {
            "t": "Un comerciante cobra $20.000 en billetes y los deposita en su cuenta corriente a la vista en un banco. ¿Qué efecto tiene sobre $M_1$?",
            "o": [
                "Ningún efecto en el valor total de $M_1$: disminuyó $EM_p$ y aumentó $DV_p$ en idéntico monto",
                "Aumenta $M_1$ en $20.000",
                "Disminuye $M_1$ en $20.000",
                "$M_1$ se transforma en $M_3$"
            ],
            "a": [0],
            "c": "Definición y fórmula de M1 (EMp + DVp)",
            "e": "Solo cambió la composición interna de $M_1$, pero la suma total $EM_p + DV_p$ no se modificó."
        },
        {
            "t": "Un ahorrista retira $50.000 de su plazo fijo que acaba de vencer y los transfiere a su caja de ahorro a la vista. ¿Qué sucede con $M_1$ y con $M_2$?",
            "o": [
                "$M_1$ aumenta en $50.000 y $M_2$ no se modifica",
                "$M_1$ disminuye en $50.000 y $M_2$ aumenta en $50.000",
                "Ambos agregados aumentan en $50.000",
                "Ninguno de los dos agregados cambia"
            ],
            "a": [0],
            "c": "Definición y fórmula de M2 (M1 + DPp)",
            "e": "$M_1$ aumenta porque subió $DV_p$. $M_2$ no cambia porque la suba de $DV_p$ compensa la baja de $DP_p$ dentro de su misma fórmula."
        },
        {
            "t": "¿Qué componente de $M_2$ remunera al titular con una tasa de interés pasiva a cambio de inmovilizar sus fondos?",
            "o": ["Los depósitos a plazo ($DP_p$)", "La emisión en poder del público ($EM_p$)", "Las monedas fraccionarias de $10", "Los cheques rechazados"],
            "a": [0],
            "c": "Componente DPp: depósitos a plazo en moneda nacional",
            "e": "Los depósitos a plazo remuneran la inmovilización temporal de fondos con una tasa pasiva."
        },
        {
            "t": "Si $M_1 = \$1.000$, los depósitos a plazo en pesos son $\$500$ y los depósitos en dólares equivalen a $\$800$, ¿cuánto vale $M_3$?",
            "o": ["$2.300", "$1.500", "$1.800", "$2.800"],
            "a": [0],
            "c": "Definición y fórmula de M3 (M2 + Dm/e)",
            "e": "$M_2 = 1.000 + 500 = 1.500$. $M_3 = M_2 + D_{m/e} = 1.500 + 800 = 2.300$."
        },
        {
            "t": "¿Cuál es la relación de inclusión correcta entre los agregados monetarios?",
            "o": [
                "Todo lo que está en M₁ está incluido en M₂, y todo lo que está en M₂ está incluido en M₃",
                "M₁ incluye a M₂ y M₂ incluye a M₃",
                "M₃ no contiene a M₁ bajo ninguna circunstancia",
                "M₁ y M₂ no tienen ningún componente en común"
            ],
            "a": [0],
            "c": "Comparación de amplitud entre M1, M2 y M3",
            "e": "$M_1 \\subset M_2 \\subset M_3$. Cada agregado subsiguiente incorpora componentes adicionales manteniendo los anteriores."
        },
        {
            "t": "¿Qué representa el término $(DV_p + DP_p)_{m/n}$ en la fórmula extendida de $M_3$?",
            "o": [
                "Los depósitos totales de los particulares en los bancos comerciales en moneda nacional",
                "Los depósitos del Banco Central en el exterior",
                "Los préstamos a no residentes en dólares",
                "Las reservas de oro del Estado"
            ],
            "a": [0],
            "c": "Depósitos en moneda nacional vs moneda extranjera en M3",
            "e": "Representa los depósitos bancarios de particulares en moneda nacional (tanto a la vista como a plazo)."
        },
        {
            "t": "Verdadero o Falso: Un billete de $2.000 en la billetera de un particular forma parte de $M_1$, de $M_2$ y de $M_3$.",
            "o": ["Verdadero", "Falso"],
            "a": [0],
            "c": "Componente EMp: emisión en poder del público",
            "e": "Verdadero. Al formar parte de $EM_p$, está incluido en $M_1$, y por ende en todos los agregados más amplios ($M_2$ y $M_3$)."
        },
        {
            "t": "¿Por qué un cheque librado contra una cuenta corriente puede utilizarse para cancelar una transacción en el acto?",
            "o": [
                "Porque la cuenta corriente es un depósito a la vista de disponibilidad inmediata que forma parte de M₁",
                "Porque los cheques tienen valor intrínseco de papel",
                "Porque los cheques devengan intereses diarios en el banco",
                "Porque los cheques son de curso legal internacional forzoso"
            ],
            "a": [0],
            "c": "Componente DVp: depósitos a la vista en moneda nacional",
            "e": "El cheque moviliza fondos de un depósito a la vista ($DV_p$), integrando los medios de pago inmediatos ($M_1$)."
        },
        {
            "t": "Si el Banco Central informa que $M_1$ aumentó pero $M_2$ se mantuvo constante, ¿qué hecho económico pudo haber ocurrido?",
            "o": [
                "Los ahorristas pasaron fondos de depósitos a plazo fijo hacia cuentas a la vista",
                "El público aumentó masivamente sus plazos fijos disminuyendo su efectivo",
                "Llegaron millones de dólares del exterior para depósitos a plazo",
                "El gobierno prohibió el retiro de depósitos"
            ],
            "a": [0],
            "c": "Definición y fórmula de M2 (M1 + DPp)",
            "e": "Al pasar de plazo fijo ($DP_p$) a la vista ($DV_p$), sube $M_1$ pero la suma de ambos ($M_2$) permanece constante."
        },
        {
            "t": "¿Cuál de los siguientes activos NO se incluye en el cálculo de $M_2$ en Uruguay?",
            "o": [
                "Un depósito a plazo fijo en dólares estadounidenses",
                "Un depósito a plazo fijo en pesos uruguayos",
                "La emisión en poder del público en pesos uruguayos",
                "Un depósito en cuenta corriente en pesos uruguayos"
            ],
            "a": [0],
            "c": "Depósitos en moneda extranjera (dólares)",
            "e": "Los depósitos en dólares no entran en $M_2$; recién entran en $M_3$."
        },
        {
            "t": "¿Qué agregado monetario refleja de manera más fiel la totalidad de medios líquidos y cuasidinero bancario en la economía uruguaya?",
            "o": ["M₃", "M₁", "El dinero-mercancía de orfebres", "Los recibos de oro"],
            "a": [0],
            "c": "Comparación de amplitud entre M1, M2 y M3",
            "e": "$M_3$ abarca toda la emisión y los depósitos bancarios tanto en pesos como en dólares, siendo la medida más comprehensiva."
        }
    ]
}
