# -*- coding: utf-8 -*-
# Nivel 6: Bancos comerciales e intermediación financiera

L6 = {
    "id": 6,
    "name": "Bancos comerciales e intermediación financiera",
    "icon": "💳",
    "parts": [
        {
            "title": "Intermediación financiera y flujo de fondos",
            "theory": """
<p>Los <b>bancos comerciales</b> (privados o estatales) son los principales intermediarios del sistema financiero.</p>
<h3>Objetivo empresarial</h3>
<p><span class="tag">Del PDF</span> Como cualquier otra empresa, <b>los bancos comerciales también buscan maximizar beneficios</b>.</p>
<h3>El negocio histórico: la intermediación financiera</h3>
<p><span class="tag">Del PDF</span> Su negocio ha sido históricamente la <b>intermediación financiera</b>: canalizar fondos desde <b>agentes superavitarios</b> hacia <b>agentes deficitarios</b>.</p>
<ul>
  <li><b>Unidades superavitarias:</b> hogares, empresas o dependencias del gobierno que tienen <i>fondos sobrantes o excedentes de ahorro</i>. En lugar de dejarlos ociosos, los depositan en el sistema financiero.</li>
  <li><b>Unidades deficitarias:</b> empresas que necesitan financiamiento para invertir en maquinaria, hogares que necesitan comprar una vivienda o consumir, y el gobierno cuando requiere financiar infraestructura. Reciben fondos a través de préstamos y créditos bancarios.</li>
</ul>
<h3>Esquema gráfico del flujo de fondos</h3>
<p>Ahorristas (superávit) ➔ Depósitos ➔ <b>BANCO COMERCIAL</b> ➔ Créditos ➔ Prestatarios (déficit).</p>
""",
            "quiz": [
                {
                    "t": "¿Cuál es el objetivo primordial que persigue un banco comercial según el PDF?",
                    "o": [
                        "Maximizar sus beneficios como cualquier otra empresa",
                        "Prestar dinero sin cobrar ningún interés",
                        "Distribuir alimentos entre la población",
                        "Sustituir al Poder Legislativo en la redacción de leyes"
                    ],
                    "a": [0],
                    "c": "Objetivo de maximización de beneficios",
                    "e": "El PDF establece con franqueza económica que, como cualquier otra empresa, los bancos comerciales buscan maximizar beneficios.",
                    "d": 1
                },
                {
                    "t": "¿En qué consiste la 'intermediación financiera' realizada por los bancos comerciales?",
                    "o": [
                        "En canalizar fondos desde agentes superavitarios (con sobrantes) hacia agentes deficitarios (que necesitan fondos)",
                        "En imprimir billetes de curso legal en las cajas",
                        "En fijar el tipo de cambio oficial por decreto",
                        "En retener todo el dinero recibido en bóvedas selladas"
                    ],
                    "a": [0],
                    "c": "Canalización de fondos en la economía",
                    "e": "La intermediación es precisamente el puente que traslada el ahorro desde agentes superavitarios hacia agentes deficitarios.",
                    "d": 1
                },
                {
                    "t": "¿Quiénes son los 'agentes superavitarios' en el esquema de flujo de fondos del documento?",
                    "o": [
                        "Hogares, empresas o gobiernos que cuentan con fondos sobrantes o excedentes de liquidez",
                        "Personas endeudadas que no pueden pagar sus cuotas",
                        "Entidades que solo operan con billetes de orfebres",
                        "Instituciones que están legalmente quebradas"
                    ],
                    "a": [0],
                    "c": "Agentes superavitarios (ahorristas)",
                    "e": "Un agente superavitario es aquel cuyos ingresos superan sus gastos inmediatos, generando excedentes para ahorrar o depositar.",
                    "d": 1
                },
                {
                    "t": "¿Quiénes integran las 'unidades deficitarias' que reciben préstamos del sistema financiero?",
                    "o": [
                        "Empresas, familias o el gobierno que requieren fondos adicionales para invertir o consumir",
                        "Únicamente los bancos extranjeros",
                        "Los inspectores del Banco Central exclusivamente",
                        "Los depositantes que no desean cobrar intereses"
                    ],
                    "a": [0],
                    "c": "Agentes deficitarios (prestatarios)",
                    "e": "Las unidades deficitarias son aquellas que presentan requerimientos de financiamiento para proyectos o gastos.",
                    "d": 1
                },
                {
                    "t": "Verdadero o Falso: En Uruguay los bancos comerciales son únicamente empresas multinacionales privadas; no existen bancos comerciales estatales.",
                    "o": ["Verdadero", "Falso"],
                    "a": [1],
                    "c": "Naturaleza de los bancos comerciales (privados y estatales)",
                    "e": "Falso. En Uruguay existen bancos comerciales tanto privados como estatales (como el Banco de la República Oriental del Uruguay - BROU).",
                    "d": 1
                }
            ]
        },
        {
            "title": "Tasa activa, pasiva y Spread bancario",
            "theory": """
<p>¿Cómo obtiene sus ganancias un banco comercial mediante la intermediación financiera?</p>
<h3>Tasa pasiva vs. Tasa activa</h3>
<p><span class="tag">Del PDF</span> En su actividad normal:</p>
<ul>
  <li><b>Tasa de interés pasiva ($i_p$):</b> es la tasa de interés que el banco <b>les paga a los ahorristas</b> por depositar sus fondos excedentes en el banco. Se llama "pasiva" porque para el banco el depósito es un pasivo (una obligación que debe devolver).</li>
  <li><b>Tasa de interés activa ($i_a$):</b> es la tasa de interés que el banco <b>les cobra a los agentes que necesitan fondos</b> a través del otorgamiento de créditos o préstamos. Se llama "activa" porque el crédito es un activo para el banco (un derecho de cobro).</li>
</ul>
<h3>Regla de viabilidad económica</h3>
<p>Para que el banco cubra sus costos y genere ganancias, necesariamente la tasa activa debe ser mayor que la pasiva: <b>$i_a > i_p$</b>.</p>
<h3>El Spread bancario</h3>
<p><span class="tag">Del PDF</span> <b>La diferencia entre las tasas activas y pasivas, llamada spread bancario, es la que determina la rentabilidad de los bancos.</b></p>
<div class="exp">
  <b>Spread bancario = Tasa activa (iₐ) - Tasa pasiva (iₚ)</b><br>
  <i>Ejemplo:</i> Si un banco cobra una tasa activa del 16% anual en créditos y paga una tasa pasiva del 4% anual en depósitos:<br>
  <b>Spread = 16% - 4% = 12%</b> (12 puntos porcentuales de margen financiero bruto).
</div>
""",
            "quiz": [
                {
                    "t": "¿Qué es la 'tasa pasiva' ($i_p$) en la actividad de un banco comercial?",
                    "o": [
                        "La tasa de interés que el banco paga a los particulares por los fondos que depositan en la entidad",
                        "La tasa de interés que el banco cobra a las empresas por otorgarles préstamos",
                        "La tasa de inflación calculada por el Instituto Nacional de Estadística",
                        "El encaje bancario obligatorio fijado por el BCU"
                    ],
                    "a": [0],
                    "c": "Tasa de interés pasiva (ip)",
                    "e": "La tasa pasiva es la retribución que el banco paga a los ahorristas por captar sus depósitos.",
                    "d": 1
                },
                {
                    "t": "¿Qué es la 'tasa activa' ($i_a$) en la operativa bancaria?",
                    "o": [
                        "La tasa de interés que el banco cobra a los agentes deficitarios por los créditos otorgados",
                        "El interés que abona el Banco Central a los ministros",
                        "El rendimiento de los billetes en la billetera",
                        "El porcentaje de billetes deteriorados"
                    ],
                    "a": [0],
                    "c": "Tasa de interés activa (ia)",
                    "e": "La tasa activa es el precio que cobra el banco a los prestatarios por prestarles dinero.",
                    "d": 1
                },
                {
                    "t": "¿Cómo se define formalmente el 'spread bancario' y cuál es su trascendencia económica?",
                    "o": [
                        "Es la diferencia entre la tasa activa y la pasiva ($i_a - i_p$), y determina la rentabilidad de los bancos",
                        "Es la suma de todos los billetes emitidos por el BCU",
                        "Es la división entre la deuda externa y la cantidad de habitantes",
                        "Es el encaje voluntario de los orfebres"
                    ],
                    "a": [0],
                    "c": "Spread bancario (ia - ip)",
                    "e": "El PDF establece textualmente que la diferencia entre las tasas activas y pasivas, llamada spread bancario, es la que determina la rentabilidad de los bancos.",
                    "d": 1
                },
                {
                    "t": "Un banco privado uruguayo abona a sus depositantes un 3% anual ($i_p$) y cobra por sus préstamos personales un 15% anual ($i_a$). ¿A cuánto asciende su spread bancario?",
                    "o": ["12 puntos porcentuales (12%)", "18%", "45%", "5%"],
                    "a": [0],
                    "c": "Spread como determinante de la rentabilidad bancaria",
                    "e": "$\\text{Spread} = i_a - i_p = 15\\% - 3\\% = 12\\%$.",
                    "d": 1
                },
                {
                    "t": "¿Qué ocurriría si un banco comercial cobrara una tasa activa MENOR a la tasa pasiva ($i_a < i_p$)?",
                    "o": [
                        "Operaría a pérdida en su actividad de intermediación, comprometiendo su viabilidad financiera",
                        "Duplicaría inmediatamente su patrimonio neto",
                        "Crearía más billetes de curso legal",
                        "Se transformaría automáticamente en el Banco Central"
                    ],
                    "a": [0],
                    "c": "Condición fundamental: ia > ip",
                    "e": "Pagar más por captar depósitos de lo que se cobra por prestar causaría pérdidas directas e insolvencia.",
                    "d": 2
                }
            ]
        },
        {
            "title": "El dilema rentabilidad vs. liquidez y los servicios modernos",
            "theory": """
<p>La gestión de un banco comercial implica balancear constantemente dos objetivos contrapuestos: <b>ganar dinero (rentabilidad)</b> y <b>no quebrar (liquidez)</b>.</p>
<h3>El conflicto entre rentabilidad y liquidez</h3>
<p><span class="tag">Del PDF</span> Un banco que intente maximizar su beneficio desearía <b>prestar el 100% de los fondos recibidos</b> para cobrar la mayor cantidad de intereses activos posibles.</p>
<p>Pero, por otro lado, <b>los bancos deben estar preparados para hacer frente al retiro de los depósitos de los particulares en cualquier momento</b>. Si un día los clientes acuden a retirar sus saldos a la vista y el banco prestó absolutamente todo, caería en cesación de pagos por iliquidez.</p>
<h3>Encajes bancarios</h3>
<p><span class="tag">Del PDF</span> Por este motivo, los bancos comerciales deben mantener permanentemente cierto dinero en efectivo o depositado a la vista en el Banco Central, llamados <b>encajes bancarios</b>. <i>Dicho de otra manera: los bancos deben tener en todo momento cierto grado de liquidez.</i></p>
<h3>Ampliación del menú de servicios bancarios</h3>
<p><span class="tag">Del PDF</span> En la actualidad, para mejorar su rentabilidad en un mercado competitivo, los bancos ofrecen un mayor menú de servicios:</p>
<ul>
  <li>Transferencias de dinero a cualquier parte del mundo.</li>
  <li>Pago automático de facturas y servicios (débitos automáticos).</li>
  <li>Emisión y administración de tarjetas de crédito y débito.</li>
  <li>Creación y administración de fondos de inversión.</li>
  <li>Asesoramiento financiero a empresas e inversores.</li>
</ul>
<p>Sin embargo, el documento subraya: <b>su principal fuente de beneficios continúa siendo la intermediación financiera</b>.</p>
""",
            "quiz": [
                {
                    "t": "¿Por qué un banco comercial no presta el 100% de los depósitos que recibe de sus clientes?",
                    "o": [
                        "Porque debe mantener encajes bancarios líquidos para hacer frente al retiro de depósitos en cualquier momento",
                        "Porque el gobierno le confisca la mitad de los billetes que ingresan",
                        "Porque no existen personas que necesiten préstamos",
                        "Porque está prohibido prestar dinero a agentes deficitarios"
                    ],
                    "a": [0],
                    "c": "Conflicto entre rentabilidad y liquidez",
                    "e": "El banco debe conservar liquidez para atender la demanda cotidiana de retiros de sus ahorristas.",
                    "d": 1
                },
                {
                    "t": "¿Qué son los 'encajes bancarios' según la explicación del documento?",
                    "o": [
                        "Dinero que los bancos mantienen en efectivo en caja o depositado a la vista en el Banco Central para asegurar liquidez",
                        "El interés cobrado a los deudores morosos",
                        "El sueldo de los gerentes bancarios",
                        "Un impuesto aplicado a las compras con tarjeta"
                    ],
                    "a": [0],
                    "c": "Encajes bancarios como reserva de liquidez",
                    "e": "El PDF define los encajes bancarios como el dinero en efectivo o depositado a la vista en el BCU que los bancos deben mantener para garantizar liquidez.",
                    "d": 1
                },
                {
                    "t": "¿Cuáles de las siguientes actividades corresponden a la ampliación moderna de servicios bancarios mencionada en el PDF?",
                    "o": [
                        "Transferencias internacionales, pago automático de facturas, tarjetas de crédito y asesoramiento financiero",
                        "Emisión de billetes de curso legal",
                        "Cultivo y acopio de trigo para trueque",
                        "Custodia exclusiva de lingotes de plata en cofres medievales"
                    ],
                    "a": [0],
                    "c": "Menú de servicios bancarios modernos",
                    "e": "El documento enumera expresamente transferencias mundiales, pago automático de facturas, tarjetas de crédito, fondos de inversión y asesoramiento.",
                    "d": 1
                },
                {
                    "t": "A pesar de la multiplicidad de servicios modernos (tarjetas, transferencias, fondos), ¿cuál sigue siendo la fuente principal de beneficios bancarios?",
                    "o": [
                        "La intermediación financiera (el spread entre tasa activa y pasiva)",
                        "El cobro de comisiones por imprimir extractos de cuenta",
                        "La venta de bienes raíces",
                        "La especulación con monedas de orfebres"
                    ],
                    "a": [0],
                    "c": "Diversificación de ingresos bancarios",
                    "e": "El PDF aclara categóricamente: 'su principal fuente de beneficios continúa siendo la intermediación financiera'.",
                    "d": 1
                },
                {
                    "t": "Un banco comercial reduce sus reservas de encaje al mínimo absoluto para prestar casi todo a tasas altas. ¿Qué trade-off (conflicto) describe esta situación?",
                    "o": [
                        "Aumenta su rentabilidad potencial pero incrementa peligrosamente su riesgo de iliquidez",
                        "Disminuye su ganancia y aumenta su liquidez",
                        "Se convierte automáticamente en una AFAP",
                        "Pierde el monopolio de emisión"
                    ],
                    "a": [0],
                    "c": "Conflicto entre rentabilidad y liquidez",
                    "e": "A mayor volumen prestado mayor es el ingreso por intereses (rentabilidad), pero menor es el colchón de seguridad para atender retiros (liquidez).",
                    "d": 2
                }
            ]
        }
    ],
    "exam": [
        {
            "t": "¿Cuál es la función histórica primordial de los bancos comerciales según el texto?",
            "o": [
                "La intermediación financiera entre agentes superavitarios y agentes deficitarios",
                "La acuñación de monedas de oro con valor intrínseco",
                "El control electoral de las autoridades nacionales",
                "La fijación obligatoria de los salarios de la economía"
            ],
            "a": [0],
            "c": "Canalización de fondos en la economía",
            "e": "Históricamente el negocio bancario ha sido intermediar fondos entre ahorristas con excedentes y agentes con necesidades de crédito."
        },
        {
            "t": "En el esquema de intermediación, una familia que ahorra el 20% de sus ingresos y los deposita en el banco califica como:",
            "o": ["Unidad superavitaria", "Unidad deficitaria", "Autoridad Monetaria", "Institución Financiera Externa"],
            "a": [0],
            "c": "Agentes superavitarios (ahorristas)",
            "e": "Quien tiene fondos sobrantes y los deposita en el sistema actúa como unidad superavitaria."
        },
        {
            "t": "Una pequeña fábrica solicita un préstamo bancario a 3 años para ampliar sus instalaciones. En este flujo califica como:",
            "o": ["Unidad deficitaria", "Unidad superavitaria", "Encaje legal", "Prestamista de última instancia"],
            "a": [0],
            "c": "Agentes deficitarios (prestatarios)",
            "e": "La empresa que demanda financiamiento para proyectos es una unidad deficitaria de fondos."
        },
        {
            "t": "¿Cómo se denomina la tasa de interés que los bancos comerciales cobran a las empresas y hogares por los créditos concedidos?",
            "o": ["Tasa de interés activa ($i_a$)", "Tasa pasiva", "Tasa de encaje técnico", "Multiplicador del dinero"],
            "a": [0],
            "c": "Tasa de interés activa (ia)",
            "e": "La tasa activa es la que el banco cobra a los prestatarios."
        },
        {
            "t": "¿Cómo se denomina la tasa que los bancos pagan a los depositantes por colocar sus fondos en la entidad?",
            "o": ["Tasa de interés pasiva ($i_p$)", "Tasa activa", "Spread financiero", "Base monetaria"],
            "a": [0],
            "c": "Tasa de interés pasiva (ip)",
            "e": "La tasa pasiva es la que abona la entidad bancaria a quienes le confían sus ahorros."
        },
        {
            "t": "¿Cuál es la fórmula para calcular el spread bancario según el documento?",
            "o": [
                "Spread = Tasa activa (iₐ) - Tasa pasiva (iₚ)",
                "Spread = Tasa pasiva (iₚ) / Tasa activa (iₐ)",
                "Spread = Tasa activa + Encaje legal",
                "Spread = Tasa pasiva × Multiplicador"
            ],
            "a": [0],
            "c": "Spread bancario (ia - ip)",
            "e": "El spread bancario es la diferencia aritmética entre la tasa activa y la tasa pasiva ($i_a - i_p$)."
        },
        {
            "t": "Si un banco paga una tasa pasiva del 5% y cobra una tasa activa del 18%, ¿cuál es su margen de spread bancario?",
            "o": ["13 puntos porcentuales", "23%", "3,6%", "90%"],
            "a": [0],
            "c": "Spread como determinante de la rentabilidad bancaria",
            "e": "$18\\% - 5\\% = 13\\%$."
        },
        {
            "t": "¿Por qué un banco no puede maximizar sus ganancias prestando el 100% de todo el dinero depositado?",
            "o": [
                "Porque debe mantener encajes bancarios para responder a los retiros diarios de depósitos",
                "Porque el multiplicador bancario se volvería negativo",
                "Porque los cheques dejarían de ser de curso legal",
                "Porque los prestatarios solo aceptan la mitad del dinero"
            ],
            "a": [0],
            "c": "Conflicto entre rentabilidad y liquidez",
            "e": "Prestar el 100% dejaría al banco sin un solo peso en caja para atender los retiros cotidianos de los depositantes."
        },
        {
            "t": "¿Dónde guardan los bancos comerciales los fondos que forman parte de sus encajes bancarios?",
            "o": [
                "En efectivo en su propio poder (bóvedas) o depositados a la vista en el Banco Central",
                "En cuentas en la bolsa de valores exclusivamente",
                "En acciones de empresas privadas",
                "En cofres de orfebres en Europa"
            ],
            "a": [0],
            "c": "Encajes bancarios como reserva de liquidez",
            "e": "Los encajes se integran con el efectivo en bóveda del banco y los depósitos a la vista en el Banco Central ($RT_B = EM_B + DV_B$)."
        },
        {
            "t": "¿Cuál es la consecuencia directa de un aumento en el spread bancario para una entidad financiera, manteniendo constantes los costos y el volumen de créditos?",
            "o": [
                "Aumenta la rentabilidad bruta de la intermediación bancaria",
                "Disminuye automáticamente su nivel de depósitos a cero",
                "El banco queda obligado a estatizarse",
                "Se reduce el número de cajeros automáticos"
            ],
            "a": [0],
            "c": "Spread como determinante de la rentabilidad bancaria",
            "e": "El spread mide el margen financiero unitario: si se amplía, se incrementa la rentabilidad de la intermediación."
        },
        {
            "t": "El débito automático para el pago de la tarifa de energía eléctrica (UTE) o telecomunicaciones (Antel) es un ejemplo de:",
            "o": [
                "Servicios complementarios modernos ofrecidos por los bancos comerciales",
                "Creación primaria de dinero por el Banco Central",
                "Financiamiento directo en la bolsa de valores",
                "Operación exclusiva de instituciones financieras externas"
            ],
            "a": [0],
            "c": "Menú de servicios bancarios modernos",
            "e": "El pago automático de facturas integra el catálogo de nuevos servicios bancarios que optimizan la gestión de clientes."
        },
        {
            "t": "Verdadero o Falso: Los bancos comerciales tienen como fuente primordial de ganancias las comisiones de tarjetas, habiendo superado a la intermediación financiera.",
            "o": ["Verdadero", "Falso"],
            "a": [1],
            "c": "Diversificación de ingresos bancarios",
            "e": "Falso. El texto señala expresamente que la principal fuente de beneficios continúa siendo la intermediación financiera."
        },
        {
            "t": "Si los ahorristas de un banco pierden la confianza y retiran masivamente sus depósitos a la vista, ¿a qué problema inmediato se enfrenta el banco?",
            "o": [
                "A un problema agudo de liquidez para devolver el efectivo en ventanilla",
                "A un problema de falta de clientes que pidan créditos",
                "A una suba forzosa del spread bancario",
                "A la obligación de emitir moneda de curso forzoso"
            ],
            "a": [0],
            "c": "Riesgo de iliquidez frente a retiros de depósitos",
            "e": "La corrida bancaria ataca la liquidez inmediata disponible antes de que los préstamos otorgados puedan cobrarse."
        },
        {
            "t": "¿Qué relación existe entre la tasa activa ($i_a$) y la pasiva ($i_p$) en cualquier sistema bancario sustentable?",
            "o": [
                "iₐ > iₚ (la tasa activa es superior a la tasa pasiva)",
                "iₚ > iₐ (la tasa pasiva es superior a la activa)",
                "iₐ = iₚ exactamente en todo momento",
                "iₐ debe ser obligatoriamente igual a cero"
            ],
            "a": [0],
            "c": "Condición fundamental: ia > ip",
            "e": "El banco cobra a los deudores más de lo que paga a los ahorristas ($i_a > i_p$) para cubrir costos y obtener beneficios."
        },
        {
            "t": "Un banco comercial asesora financieramente a una firma exportadora y administra la emisión de sus tarjetas de crédito corporativas. ¿Con qué fin amplía estos servicios según el PDF?",
            "o": [
                "Buscando mejorar su rentabilidad en un mercado potencialmente competitivo",
                "Para cumplir una orden del Poder Ejecutivo que le prohíbe dar préstamos",
                "Porque los depósitos a la vista fueron derogados por el BCU",
                "Para operar exclusivamente con clientes no residentes"
            ],
            "a": [0],
            "c": "Menú de servicios bancarios modernos",
            "e": "El PDF explica que esta expansión de servicios responde a la búsqueda de mejorar la rentabilidad en un mercado competitivo."
        }
    ]
}
