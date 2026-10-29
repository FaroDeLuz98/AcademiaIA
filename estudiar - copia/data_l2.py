# -*- coding: utf-8 -*-
# Nivel 2: Definición operativa del dinero

L2 = {
    "id": 2,
    "name": "Definición operativa del dinero",
    "icon": "💵",
    "parts": [
        {
            "title": "El efectivo y la liquidez",
            "theory": """
<p>En este bloque analizaremos qué activos se consideran operativamente como dinero en una economía moderna.</p>
<h3>El efectivo como la forma más líquida</h3>
<p><span class="tag">Del PDF</span> La forma más intuitiva de definir al dinero es el <b>efectivo</b>, es decir, los <b>billetes y monedas emitidos por la Autoridad Monetaria</b>, que en nuestro país es el <b>Banco Central del Uruguay (BCU)</b>.</p>
<p>Esta es la <b>forma más líquida de mantener dinero</b>, en el sentido de que <b>puede ser utilizado instantáneamente como medio de pago</b> en cualquier mostrador o transacción física sin demoras ni trámites previos.</p>
<h3>¿Qué es exactamente la liquidez?</h3>
<p>La <b>liquidez</b> de un activo es la <i>facilidad, rapidez y certeza con la que puede convertirse o utilizarse de forma inmediata para realizar pagos y cancelar deudas</i>, sin sufrir pérdidas significativas de valor.</p>
<ul>
  <li>El efectivo en billetes es el activo <b>máximamente líquido</b>: lo sacás del bolsillo y pagás al instante.</li>
  <li>Otros activos (inmuebles, autos, bonos a 10 años) son <b>ilíquidos o poco líquidos</b>: para pagar con ellos primero debés venderlos, esperar y asumir costos.</li>
</ul>
<h3>Costo de mantener efectivo</h3>
<p>Tener dinero en efectivo en el bolsillo brinda máxima liquidez, pero tiene un costo de oportunidad: <b>el efectivo no paga ningún tipo de interés ni genera rendimientos</b>.</p>
""",
            "quiz": [
                {
                    "t": "Según el PDF, ¿cuál es la forma más intuitiva y más líquida de mantener dinero en la economía?",
                    "o": [
                        "El efectivo (los billetes y monedas en circulación)",
                        "Las acciones empresariales en la bolsa",
                        "Los depósitos a plazo fijo a un año",
                        "Los bonos del tesoro nacional en dólares"
                    ],
                    "a": [0],
                    "c": "Efectivo como activo más líquido",
                    "e": "El PDF señala textualmente que el efectivo (billetes y monedas) es la forma más intuitiva y más líquida de dinero, porque se usa instantáneamente.",
                    "d": 1
                },
                {
                    "t": "¿Qué significa exactamente que un activo financiero posea un alto grado de 'liquidez'?",
                    "o": [
                        "Facilidad y rapidez para disponer de él y utilizarlo instantáneamente como medio de pago",
                        "Que genera una rentabilidad fija en intereses todos los meses",
                        "Que su valor está determinado exclusivamente por el peso en oro",
                        "Que solo puede utilizarse a través de cheques diferidos"
                    ],
                    "a": [0],
                    "c": "Concepto de liquidez",
                    "e": "La liquidez mide la prontitud y facilidad con que un activo se convierte en medio de pago disponible sin pérdida de valor.",
                    "d": 1
                },
                {
                    "t": "¿Quién es la Autoridad Monetaria encargada de emitir legalmente los billetes y monedas en Uruguay?",
                    "o": [
                        "El Banco Central del Uruguay (BCU)",
                        "El Ministerio de Economía y Finanzas",
                        "El Banco de la República Oriental del Uruguay (BROU)",
                        "Las Administradoras de Fondos de Ahorro Previsional (AFAPs)"
                    ],
                    "a": [0],
                    "c": "Emisión del Banco Central del Uruguay (BCU)",
                    "e": "La Autoridad Monetaria en nuestro país es el Banco Central del Uruguay (BCU), titular exclusivo de la emisión monetaria legal.",
                    "d": 1
                },
                {
                    "t": "Si tenés $1.000 en billetes en la billetera y entrás a un comercio a comprar alimentos, ¿qué ventaja operativa estás aprovechando?",
                    "o": [
                        "Su disponibilidad inmediata para pagar en el acto sin trámites ni autorizaciones",
                        "El alto interés financiero que devenga el papel moneda en el bolsillo",
                        "Que el billete puede canjearse por oro en el mostrador",
                        "Que el billete tiene vencimiento a 30 días"
                    ],
                    "a": [0],
                    "c": "Efectivo como activo más líquido",
                    "e": "La máxima liquidez del efectivo radica en su capacidad de extinguir pagos instantáneamente.",
                    "d": 1
                },
                {
                    "t": "Verdadero o Falso: El dinero en efectivo guardado en la billetera ofrece máxima liquidez pero no genera ninguna tasa de interés.",
                    "o": ["Verdadero", "Falso"],
                    "a": [0],
                    "c": "Costo de mantener efectivo",
                    "e": "Verdadero. El efectivo permite disponer inmediatamente del dinero pero no abona rendimientos ni intereses.",
                    "d": 1
                }
            ]
        },
        {
            "title": "Depósitos a la vista vs. Depósitos a plazo",
            "theory": """
<p>Los agentes económicos no solo conservan dinero físico: también suelen depositarlo en el sistema financiero bancario.</p>
<h3>Depósitos a la vista (alta disponibilidad)</h3>
<p><span class="tag">Del PDF</span> Si una persona o empresa desea mantener una fácil disponibilidad de sus fondos en el banco, la mejor opción es constituir un <b>depósito a la vista</b> (como una cuenta corriente o caja de ahorros a la vista).</p>
<ul>
  <li><b>Disponibilidad:</b> permiten retirar el dinero en el momento en que uno lo desee (por ventanilla o cajero) o librar cheques contra él, los cuales serán cobrados rápidamente por el receptor.</li>
  <li><b>Tasa de interés:</b> en general, los depósitos a la vista <b>no pagan interés</b> y, si lo hacen, <b>éste es muy bajo</b>. El cliente prioriza la disponibilidad inmediata frente al rendimiento.</li>
</ul>
<h3>Depósitos a plazo fijo (menor liquidez, con interés)</h3>
<p><span class="tag">Del PDF</span> Un <b>depósito a plazo</b> ($DP_p$) es aquel en el que los fondos quedan inmovilizados en el banco comercial durante un período acordado (por ejemplo, 30, 90, 180 o 365 días).</p>
<ul>
  <li><b>Disponibilidad:</b> <b>sólo puede retirarse a la fecha de su vencimiento</b>. No se puede usar para pagar transacciones diarias ni para librar cheques de uso corriente.</li>
  <li><b>Tasa de interés:</b> a cambio de resignar temporalmente la liquidez inmediata, el banco comercial le paga al ahorrista una <b>tasa de interés pasiva</b> superior a la de una cuenta a la vista.</li>
</ul>
<h3>Diferencia clave entre efectivo y depósito a la vista</h3>
<div class="exp">
  <b>Efectivo vs. Depósito a la vista:</b><br>
  • El <b>efectivo</b> es dinero físico (billetes y monedas) en manos de las personas (emisión en poder del público, $EM_p$).<br>
  • El <b>depósito a la vista</b> ($DV_p$) es dinero bancarizado: está depositado en una cuenta bancaria comercial, pero goza de disponibilidad casi inmediata mediante retiros o cheques. Ambos componen los medios de pago inmediatos ($M_1$).
</div>
""",
            "quiz": [
                {
                    "t": "¿Cuál es la diferencia fundamental entre el dinero en efectivo y un depósito a la vista en un banco?",
                    "o": [
                        "El efectivo son billetes físicos en manos del público, mientras que el depósito a la vista es saldo en una cuenta bancaria con disponibilidad casi inmediata para retiros o cheques",
                        "El efectivo paga intereses diarios, mientras que el depósito a la vista nunca puede retirarse",
                        "El efectivo es emitido por bancos comerciales privados y el depósito a la vista por el gobierno",
                        "El depósito a la vista solo puede retirarse a la fecha de vencimiento anual"
                    ],
                    "a": [0],
                    "c": "Diferencia entre efectivo y depósito a la vista",
                    "e": "El efectivo es moneda física en poder del público ($EM_p$), mientras que el depósito a la vista ($DV_p$) es dinero en el sistema bancario que se puede retirar a voluntad o movilizar con cheques.",
                    "d": 2
                },
                {
                    "t": "¿Cuál es la característica principal de un depósito a la vista según el PDF?",
                    "o": [
                        "Permite retirar dinero cuando uno lo desea o librar cheques cobrados con rapidez",
                        "Obliga a inmovilizar los fondos hasta una fecha fija sin posibilidad de uso previo",
                        "Paga obligatoriamente una tasa de interés muy elevada fijada por el BCU",
                        "Solo puede constituirse en oro físico en las bóvedas"
                    ],
                    "a": [0],
                    "c": "Características de depósitos a la vista",
                    "e": "El depósito a la vista otorga disponibilidad instantánea o casi instantánea a demanda del depositante.",
                    "d": 1
                },
                {
                    "t": "¿En qué momento puede retirarse el dinero depositado en un depósito a plazo fijo?",
                    "o": [
                        "Únicamente a la fecha de su vencimiento",
                        "En cualquier momento mediante un cajero automático sin penalización alguna",
                        "Todos los días hábiles librando cheques corrientes",
                        "Solo cuando el Banco Central emite nuevos billetes"
                    ],
                    "a": [0],
                    "c": "Características de depósitos a plazo",
                    "e": "El PDF establece con total claridad que un depósito a plazo sólo puede retirarse a la fecha de su vencimiento.",
                    "d": 2
                },
                {
                    "t": "¿Por qué un depósito a plazo fijo suele pagar una tasa de interés más alta que un depósito a la vista?",
                    "o": [
                        "Porque el depositante renuncia a la liquidez y disponibilidad inmediata de sus fondos durante cierto tiempo",
                        "Porque el depósito a plazo está respaldado por oro físico en el exterior",
                        "Porque los depósitos a plazo no forman parte del sistema financiero",
                        "Porque el Banco Central le prohíbe a los bancos prestar ese dinero"
                    ],
                    "a": [0],
                    "c": "Diferencia de disponibilidad y vencimiento",
                    "e": "El interés es la compensación que recibe el ahorrista por inmovilizar sus fondos y ceder liquidez al banco comercial.",
                    "d": 2
                },
                {
                    "t": "Elegí TODAS las afirmaciones correctas sobre los depósitos a la vista:",
                    "o": [
                        "Ofrecen una fácil disponibilidad de los fondos",
                        "Permiten librar cheques contra ellos",
                        "En general no pagan interés, o pagan uno muy bajo",
                        "Solo pueden retirarse cuando vence el plazo contractualmente estipulado"
                    ],
                    "a": [0, 1, 2],
                    "c": "Características de depósitos a la vista",
                    "e": "Las tres primeras describen exactamente a los depósitos a la vista. El retiro al vencimiento corresponde al depósito a plazo.",
                    "d": 2
                }
            ]
        },
        {
            "title": "Clasificación de depósitos según disponibilidad y operativa en Uruguay",
            "theory": """
<p>Para operar y medir el dinero en la práctica se requiere clasificar los depósitos y conocer las tendencias actuales de pago.</p>
<h3>Clasificación de los depósitos según su disponibilidad</h3>
<p><span class="tag">Del PDF</span> El criterio operativo fundamental para ordenar los depósitos bancarios es su <b>grado de disponibilidad temporal (liquidez)</b>:</p>
<ol>
  <li><b>Depósitos a la vista:</b> disponibilidad <i>inmediata</i> a solicitud del cliente (máxima liquidez dentro del banco). No pagan interés o pagan uno mínimo.</li>
  <li><b>Depósitos a plazo fijo:</b> disponibilidad <i>condicionada a la fecha de vencimiento</i> (menor liquidez). Pagan una tasa de interés superior.</li>
</ol>
<h3>La realidad operativa en Uruguay</h3>
<p><span class="tag">Del PDF</span> Los depósitos a la vista y en cuenta corriente están cobrando <b>mayor importancia en Uruguay en la actualidad</b>, ya que existe una <b>marcada tendencia a abandonar el efectivo para pagar sueldos</b> y, en cambio, depositarlos en cuentas bancarias particulares a las que los trabajadores tienen acceso permanente a través de los <b>cajeros automáticos y tarjetas de débito</b>.</p>
<h3>Notación técnica utilizada en las fórmulas del documento</h3>
<ul>
  <li>$EM_p$: <b>Emisión en poder del público</b> (billetes y monedas físicos en circulación en manos de familias y empresas).</li>
  <li>$DV_p$: <b>Depósitos a la vista</b> de los particulares en los bancos comerciales en moneda nacional.</li>
  <li>$DP_p$: <b>Depósitos a plazo</b> de los particulares en los bancos comerciales en moneda nacional.</li>
</ul>
<h3>Diferencia crucial: Depósito a plazo ($DP_p$) vs. Cantidad de dinero ($M_2$)</h3>
<div class="exp">
  <b>No confundir el componente con el agregado:</b><br>
  • El <b>depósito a plazo ($DP_p$)</b> es un tipo específico de colocación bancaria inmovilizada.<br>
  • La <b>cantidad de dinero ($M_2$)</b> es el agregado total que reúne la emisión pública más todos los depósitos en moneda nacional: $M_2 = EM_p + DV_p + DP_p = M_1 + DP_p$. El depósito a plazo es solo una de las partes de $M_2$.
</div>
""",
            "quiz": [
                {
                    "t": "¿Cómo clasifica fundamentalmente el PDF a los depósitos bancarios según su disponibilidad temporal?",
                    "o": [
                        "En depósitos a la vista (disponibilidad inmediata) y depósitos a plazo (disponibilidad sujeta a vencimiento)",
                        "En depósitos en oro y depósitos en plata metálica",
                        "En depósitos gubernamentales y depósitos ilegales",
                        "En depósitos activos y depósitos sin saldo"
                    ],
                    "a": [0],
                    "c": "Clasificación de los depósitos según su disponibilidad",
                    "e": "El criterio del PDF distingue depósitos a la vista (disposición inmediata) y depósitos a plazo (vencimiento pactado).",
                    "d": 1
                },
                {
                    "t": "¿Cuál es la diferencia conceptual precisa entre un depósito a plazo ($DP_p$) y el agregado monetario $M_2$?",
                    "o": [
                        "El depósito a plazo ($DP_p$) es solo un componente individual, mientras que $M_2$ es el agregado monetario total que suma $M_1 + DP_p$",
                        "$DP_p$ incluye el dinero en dólares y $M_2$ solo incluye el oro del Banco Central",
                        "$DP_p$ es emitido por el BCU y $M_2$ es emitido por casas de cambio",
                        "Son exactamente sinónimos y representan el mismo monto en el sistema financiero"
                    ],
                    "a": [0],
                    "c": "Diferencia entre depósito a plazo y agregado monetario M2",
                    "e": "El depósito a plazo es una parte de $M_2$. $M_2$ abarca la emisión en poder del público, los depósitos a la vista y los depósitos a plazo ($M_2 = M_1 + DP_p$).",
                    "d": 2
                },
                {
                    "t": "¿Qué tendencia reciente describe el PDF respecto a la forma de pago de remuneraciones en Uruguay?",
                    "o": [
                        "Una marcada tendencia a abandonar el efectivo y pagar sueldos mediante depósitos bancarios accesibles por cajeros automáticos",
                        "Una vuelta al pago exclusivo con sobres de billetes en mano en todas las empresas",
                        "La obligatoriedad de abonar sueldos únicamente con bonos de deuda pública",
                        "El pago de remuneraciones exclusivamente en moneda extranjera física"
                    ],
                    "a": [0],
                    "c": "Clasificación de los depósitos según su disponibilidad",
                    "e": "El PDF destaca la bancarización de sueldos en Uruguay, abandonando el efectivo para utilizar cuentas bancarias y cajeros automáticos.",
                    "d": 1
                },
                {
                    "t": "¿Qué significa exactamente el símbolo $DP_p$ en la notación del PDF?",
                    "o": [
                        "Depósitos a plazo de los particulares en los bancos comerciales en moneda nacional",
                        "Deuda pública del gobierno en moneda extranjera",
                        "Depósitos a la vista de los bancos en el Banco Central",
                        "Dinero primario del público en efectivo"
                    ],
                    "a": [0],
                    "c": "Diferencia entre depósito a plazo y agregado monetario M2",
                    "e": "$DP_p$ corresponde a Depósitos a Plazo de los Particulares en bancos comerciales en moneda nacional.",
                    "d": 1
                },
                {
                    "t": "Un empleado público cobra su sueldo mediante acreditación en cuenta bancaria y luego retira una parte en un cajero RedBrou. ¿Qué transformación ocurrió?",
                    "o": [
                        "Transformó una parte de su depósito a la vista ($DV_p$) en efectivo en poder del público ($EM_p$)",
                        "Creó dinero primario de la nada",
                        "Constituyó un depósito a plazo fijo no disponible",
                        "Transformó su salario en un depósito en moneda extranjera"
                    ],
                    "a": [0],
                    "c": "Diferencia entre efectivo y depósito a la vista",
                    "e": "El retiro en cajero convierte saldo bancario a la vista ($DV_p$) en billetes físicos en manos del titular ($EM_p$).",
                    "d": 2
                }
            ]
        }
    ],
    "exam": [
        {
            "t": "¿Cuál es la forma más líquida que existe para mantener dinero según la definición operativa del PDF?",
            "o": ["El efectivo (billetes y monedas)", "Un depósito a plazo a 180 días", "Un pagaré empresarial", "Un bono del tesoro en dólares"],
            "a": [0],
            "c": "Efectivo como activo más líquido",
            "e": "El efectivo es el activo más líquido porque puede usarse al instante como medio de cambio en cualquier compra."
        },
        {
            "t": "¿Qué institución estatal emite el dinero en efectivo que circula en la economía uruguaya?",
            "o": ["El Banco Central del Uruguay (BCU)", "El Banco Hipotecario", "La Bolsa de Valores de Montevideo", "El Banco de Seguros del Estado"],
            "a": [0],
            "c": "Emisión del Banco Central del Uruguay (BCU)",
            "e": "La Autoridad Monetaria y único emisor legal del efectivo en Uruguay es el Banco Central del Uruguay (BCU)."
        },
        {
            "t": "¿Por qué un depósito a la vista es considerado casi tan líquido como el efectivo?",
            "o": [
                "Porque permite disponer del dinero en cualquier momento retirándolo o librando cheques de cobro rápido",
                "Porque devenga una tasa de interés anual del 25%",
                "Porque solo se puede retirar al cabo de doce meses",
                "Porque está impreso en papel moneda de curso legal"
            ],
            "a": [0],
            "c": "Características de depósitos a la vista",
            "e": "Su disponibilidad inmediata y la posibilidad de emitir cheques otorgan a los depósitos a la vista una liquidez casi total."
        },
        {
            "t": "¿Cuál es la diferencia fundamental entre el efectivo ($EM_p$) y un depósito a la vista ($DV_p$)?",
            "o": [
                "El efectivo es dinero físico en posesión directa del público; el depósito a la vista es dinero bancarizado con retiro a demanda",
                "El efectivo rinde alta tasa de interés y el depósito a la vista ninguna",
                "El depósito a la vista solo puede usarse a partir del año de constituido",
                "El efectivo no es emitido por el BCU y el depósito a la vista sí"
            ],
            "a": [0],
            "c": "Diferencia entre efectivo y depósito a la vista",
            "e": "Ambos son plenamente líquidos, pero el efectivo está físicamente en manos del público y el depósito a la vista en una entidad bancaria."
        },
        {
            "t": "Un comerciante deposita $50.000 en un plazo fijo a 90 días en el banco. ¿Puede retirar ese dinero a los 10 días para pagar un flete?",
            "o": [
                "No, porque un depósito a plazo sólo puede retirarse a la fecha pactada de su vencimiento",
                "Sí, librando un cheque corriente contra el plazo fijo",
                "Sí, concurriendo al cajero automático en cualquier horario",
                "Sí, porque todos los depósitos bancarios son legalmente a la vista"
            ],
            "a": [0],
            "c": "Características de depósitos a plazo",
            "e": "El depósito a plazo inmoviliza los fondos contractualmente hasta la fecha estipulada de vencimiento."
        },
        {
            "t": "¿Cuál de las siguientes afirmaciones explica la diferencia entre un depósito a plazo ($DP_p$) y el agregado monetario $M_2$?",
            "o": [
                "$DP_p$ es un tipo específico de depósito inmovilizado; $M_2$ es la suma agregada total de emisión, depósitos a la vista y depósitos a plazo",
                "$DP_p$ representa el dinero emitido por el BCU y $M_2$ los préstamos concedidos",
                "Son conceptos idénticos que miden exactamente el mismo volumen financiero",
                "$M_2$ solo incluye monedas metálicas y $DP_p$ billetes de curso forzoso"
            ],
            "a": [0],
            "c": "Diferencia entre depósito a plazo y agregado monetario M2",
            "e": "$DP_p$ es un componente que se suma a $EM_p$ y $DV_p$ para conformar la cantidad total de dinero $M_2$ ($M_2 = M_1 + DP_p$)."
        },
        {
            "t": "Según la clasificación de depósitos del PDF, ¿qué distingue a un depósito a la vista de uno a plazo fijo?",
            "o": [
                "El grado de disponibilidad temporal: inmediata en el depósito a la vista vs diferida al vencimiento en el de plazo fijo",
                "Que el depósito a la vista solo se efectúa en dólares y el de plazo en pesos",
                "Que los depósitos a plazo son emitidos directamente por el gobierno central",
                "Que los depósitos a la vista no están en el sistema bancario"
            ],
            "a": [0],
            "c": "Clasificación de los depósitos según su disponibilidad",
            "e": "El criterio esencial es la disponibilidad: inmediata a demanda (a la vista) versus condicionada a un plazo pactado."
        },
        {
            "t": "¿Qué tendencia destaca el PDF en el mercado laboral uruguayo respecto a los medios de pago?",
            "o": [
                "Se reemplaza progresivamente el pago en efectivo de salarios por depósitos en cuentas con acceso mediante cajeros",
                "Se sustituyó el dinero en pesos por cheques de orfebres",
                "El 100% de los sueldos se paga ahora exclusivamente en oro físico",
                "Se prohibió el uso de tarjetas de débito en comercios"
            ],
            "a": [0],
            "c": "Clasificación de los depósitos según su disponibilidad",
            "e": "El documento señala la marcada tendencia a pagar sueldos en cuentas particulares con acceso a cajeros automáticos."
        },
        {
            "t": "¿Por qué los depósitos a la vista habitualmente no pagan intereses o pagan una tasa muy baja?",
            "o": [
                "Porque el banco debe mantener alta disponibilidad de esos fondos para retiros inmediatos, priorizando liquidez sobre rendimiento",
                "Porque el Banco Central confisca los intereses de las cuentas corrientes",
                "Porque son depósitos que solo pertenecen a no residentes",
                "Porque el dinero bancarizado pierde valor por ley"
            ],
            "a": [0],
            "c": "Características de depósitos a la vista",
            "e": "Al ofrecer disponibilidad inmediata para retiros y cheques, el banco no puede inmovilizar plenamente esos fondos, pagando un interés casi nulo."
        },
        {
            "t": "¿Qué simboliza en las ecuaciones monetarias del texto la expresión $EM_p$?",
            "o": [
                "La emisión de billetes y monedas en poder del público",
                "El encaje monetario de los bancos comerciales",
                "Los préstamos otorgados por el Banco Central al gobierno",
                "La tasa activa promedio cobrada por los bancos"
            ],
            "a": [0],
            "c": "Efectivo como activo más líquido",
            "e": "$EM_p$ es la emisión en poder del público (dinero físico en manos de agentes económicos no bancarios)."
        },
        {
            "t": "¿Cuál de las siguientes combinaciones de activos tiene un orden decreciente de liquidez (del más líquido al menos líquido)?",
            "o": [
                "Efectivo en billetes → Depósito a la vista en pesos → Depósito a plazo fijo a 1 año",
                "Depósito a plazo a 1 año → Depósito a la vista → Efectivo en billetes",
                "Bono del tesoro a 10 años → Efectivo en billetes → Cuenta corriente",
                "Depósito a plazo → Cheque al portador → Billetes en mano"
            ],
            "a": [0],
            "c": "Concepto de liquidez",
            "e": "El efectivo es inmediatamente líquido, le sigue el depósito a la vista (casi inmediato) y por último el depósito a plazo (espera al vencimiento)."
        },
        {
            "t": "Si una persona cobra su sueldo por cajero automático, ¿de qué tipo de depósito bancario procede originalmente ese dinero?",
            "o": [
                "De un depósito a la vista (o cuenta corriente / caja de ahorro)",
                "De un depósito a plazo fijo intransferible",
                "De una colocación de bonos de deuda externa",
                "De un depósito de encaje del BCU"
            ],
            "a": [0],
            "c": "Características de depósitos a la vista",
            "e": "Las cuentas sueldo con tarjeta de débito son depósitos bancarios a la vista con disponibilidad inmediata."
        },
        {
            "t": "¿Por qué un individuo con excedentes de dinero decidiría colocarlo en un plazo fijo en lugar de guardarlo bajo el colchón?",
            "o": [
                "Para obtener una rentabilidad en forma de tasa de interés a cambio de ceder la liquidez por un tiempo",
                "Porque el dinero bajo el colchón está prohibido por el BCU",
                "Porque el plazo fijo permite comprar mercaderías con mayor facilidad que el efectivo",
                "Porque el dinero en el colchón se transforma automáticamente en dólares"
            ],
            "a": [0],
            "c": "Diferencia de disponibilidad y vencimiento",
            "e": "El plazo fijo remunera al ahorrista con una tasa pasiva de interés, compensando la pérdida transitoria de liquidez."
        },
        {
            "t": "¿Cuál de las siguientes afirmaciones sobre la clasificación de los depósitos es FALSA?",
            "o": [
                "Los depósitos a plazo permiten librar cheques de cobro inmediato en cualquier momento sin vencimiento previo",
                "Los depósitos a la vista permiten disponer de los fondos cuando el titular lo desee",
                "Los depósitos a plazo sólo pueden retirarse al llegar a su fecha de vencimiento",
                "Los depósitos a la vista suelen rendir un interés nulo o muy bajo"
            ],
            "a": [0],
            "c": "Clasificación de los depósitos según su disponibilidad",
            "e": "Es falsa: no se pueden librar cheques contra depósitos a plazo fijo; los cheques se libran contra cuentas o depósitos a la vista."
        },
        {
            "t": "Un comerciante traslada $100.000 de su caja de ahorros a la vista a un depósito a plazo fijo a 180 días. ¿Cómo cambia su perfil financiero?",
            "o": [
                "Gana rentabilidad futura por la tasa de interés pero pierde liquidez inmediata hasta el vencimiento",
                "Aumenta su liquidez disponible para pagar compras de mañana",
                "Disminuye su patrimonio total en un 50%",
                "Pasa a tener más billetes físicos en su mostrador"
            ],
            "a": [0],
            "c": "Diferencia de disponibilidad y vencimiento",
            "e": "El traspaso sacrifica la disponibilidad inmediata a cambio del interés pactado al vencimiento de los 180 días."
        }
    ]
}
