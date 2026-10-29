# -*- coding: utf-8 -*-
# Nivel 1: Fundamentos y evolución del dinero

L1 = {
    "id": 1,
    "name": "Fundamentos y evolución del dinero",
    "icon": "🪙",
    "parts": [
        {
            "title": "¿Qué es el dinero y para qué sirve?",
            "theory": """
<p>Vamos a aprender <b>qué es el dinero</b> y <b>qué hace por nosotros</b> todos los días en la economía.</p>
<h3>Definición según el PDF</h3>
<p><span class="tag">Del PDF</span> Dinero es <b>todo medio de pago aceptado como tal por una comunidad para realizar transacciones</b>. Lo esencial no es el material físico del que está hecho, sino que toda la comunidad lo reconozca y lo acepte como medio para cancelar obligaciones.</p>
<h3>Las tres funciones básicas del dinero</h3>
<ul>
  <li><b>i) Medio de pago o de cambio:</b> el dinero se utiliza para realizar transacciones corrientes (comprar bienes y servicios, pagar salarios a los trabajadores, abonar facturas de servicios públicos como UTE, etc.). Elimina las trabas del intercambio directo.</li>
  <li><b>ii) Unidad de medida o numerario:</b> todos los precios de la economía se fijan en unidades monetarias. De esta forma se conoce el valor relativo de cada bien o servicio en función de un elemento único: la cantidad de pesos (o unidades monetarias) que se debe pagar por él. Por ejemplo, si un kilo de asado cuesta $450 y un kilo de pan cuesta $90, sabemos de inmediato que un kilo de asado equivale a cinco kilos de pan sin necesidad de hacer cuentas complejas.</li>
  <li><b>iii) Reserva de valor:</b> el dinero se usa también para mantener un poder de compra a lo largo del tiempo, con el objetivo de comprar bienes y servicios en el futuro (ahorro).</li>
</ul>
<h3>Error frecuente</h3>
<p>Creer que "dinero" equivale únicamente a monedas o billetes de papel. Los billetes son solo una forma histórica y operativa; la definición académica abarca <i>cualquier medio de pago aceptado por la comunidad</i>.</p>
<p><span class="tag x">Ejemplo práctico</span> Al pagar un café con tarjeta de débito por un precio fijado en pesos, estás utilizando el dinero como medio de pago (cancelás la cuenta) y como unidad de medida (el precio estaba expresado en moneda nacional).</p>
""",
            "quiz": [
                {
                    "t": "Según el PDF, ¿qué es el dinero?",
                    "o": [
                        "Todo medio de pago aceptado como tal por una comunidad para realizar transacciones",
                        "Únicamente los billetes de papel emitidos por el gobierno",
                        "Cualquier activo financiero que devengue una tasa de interés positiva",
                        "Cualquier bien que tenga un alto costo de producción y sea escaso"
                    ],
                    "a": [0],
                    "c": "Definición de dinero",
                    "e": "El PDF define textualmente al dinero como todo medio de pago aceptado como tal por una comunidad para realizar transacciones. La clave es la aceptación comunitaria.",
                    "d": 1
                },
                {
                    "t": "Pagás la cuota de la mutualista o la factura de UTE. ¿Qué función del dinero estás utilizando principalmente?",
                    "o": [
                        "Medio de pago o de cambio",
                        "Reserva de valor",
                        "Unidad de medida o numerario",
                        "Monopolio de emisión"
                    ],
                    "a": [0],
                    "c": "Funciones del dinero: medio de pago",
                    "e": "Estás cancelando una transacción y liquidando una obligación: esa es la función de medio de pago o de cambio.",
                    "d": 1
                },
                {
                    "t": "Un litro de leche cuesta $40 y un paquete de yerba cuesta $120. ¿Qué función te permite comparar sus valores inmediatamente?",
                    "o": [
                        "Unidad de medida o numerario",
                        "Reserva de valor",
                        "Medio de pago",
                        "Curso legal forzoso"
                    ],
                    "a": [0],
                    "c": "Funciones del dinero: unidad de medida (numerario)",
                    "e": "Al fijarse todos los precios en una misma unidad monetaria, el dinero actúa como común denominador o numerario para comparar el valor de los bienes.",
                    "d": 2
                },
                {
                    "t": "Una persona guarda $3.000 de su sueldo hoy para comprarse una bicicleta dentro de seis meses. ¿Qué función cumple el dinero en este caso?",
                    "o": [
                        "Reserva de valor",
                        "Unidad de medida",
                        "Medio de cambio inmediato",
                        "Dinero-mercancía"
                    ],
                    "a": [0],
                    "c": "Funciones del dinero: reserva de valor",
                    "e": "Permite trasladar capacidad de compra hacia el futuro: esa es la función de reserva de valor.",
                    "d": 2
                },
                {
                    "t": "Elegí TODAS las funciones básicas del dinero señaladas en el documento:",
                    "o": [
                        "Medio de pago o de cambio",
                        "Unidad de medida o numerario",
                        "Reserva de valor",
                        "Generar rentabilidad e intereses obligatorios"
                    ],
                    "a": [0, 1, 2],
                    "c": "Funciones del dinero",
                    "e": "Las tres funciones básicas son: medio de pago, unidad de medida y reserva de valor. La generación de intereses no es una función del dinero.",
                    "d": 2
                }
            ]
        },
        {
            "title": "¿Cuándo y por qué surgió el dinero? Dificultades del trueque y dinero-mercancía",
            "theory": """
<p>Históricamente, el dinero surgió cuando se pasó de una <b>economía de subsistencia</b> a una <b>economía de intercambio</b>.</p>
<h3>Las dificultades del trueque</h3>
<p><span class="tag">Del PDF</span> Cuando se comenzó a intercambiar bienes apareció inicialmente el <b>trueque</b> (cambiar directamente un bien por otro). A medida que las economías se volvían más complejas, el trueque mostró dos grandes limitaciones:</p>
<ol>
  <li><b>Simultaneidad o coincidencia de necesidades:</b> una persona con escasez del bien A y abundancia del bien B debía encontrar a otra persona que tuviera exactamente exceso del bien A y necesitara el bien B. Si no coincidían los deseos en el mismo momento, no había transacción posible.</li>
  <li><b>Poca o nula divisibilidad de las unidades transadas:</b> si una persona necesitaba bienes pequeños (huevos, zapallos, piedras talladas) y solo disponía de una vaca para ofrecer en pago, el problema no tenía solución porque no se podía fraccionar la vaca sin destruirla.</li>
</ol>
<h3>Aparición del dinero-mercancía</h3>
<p><span class="tag">Del PDF</span> Para superar estas trabas, las sociedades buscaron un bien que fuera <b>divisible, fácilmente transportable, no perecedero y escaso</b>. Se utilizaron el trigo y la sal, y finalmente <b>los metales preciosos (oro y plata)</b> por su mayor eficiencia.</p>
<p><b>Valor intrínseco:</b> en la época del dinero-mercancía, el dinero tenía valor en sí mismo. Podía utilizarse como mercancía (joyas, herramientas, consumo) además de ser el numerario del sistema.</p>
""",
            "quiz": [
                {
                    "t": "Tenés queso y necesitás zapatos, pero el zapatero solo acepta trigo a cambio de su calzado. ¿Qué traba del trueque enfrentás?",
                    "o": [
                        "Falta de simultaneidad (coincidencia) de necesidades",
                        "Falta de curso legal",
                        "Problema de divisibilidad de las unidades transadas",
                        "Exceso de liquidez en la economía"
                    ],
                    "a": [0],
                    "c": "Problemas del trueque: simultaneidad de necesidades",
                    "e": "El trueque exige que ambas partes deseen mutuamente lo que la otra ofrece al mismo tiempo: es la simultaneidad de necesidades.",
                    "d": 1
                },
                {
                    "t": "Un productor posee un caballo y necesita sal, verduras y clavos. ¿Qué dificultad del trueque le impide realizar el intercambio fraccionado?",
                    "o": [
                        "Poca o nula divisibilidad de la unidad transada",
                        "Falta de numerario estatal",
                        "Falta de reserva de valor",
                        "Exceso de oferta monetaria"
                    ],
                    "a": [0],
                    "c": "Problemas del trueque: divisibilidad",
                    "e": "Los animales grandes no pueden dividirse en fracciones pequeñas sin perder la vida y su valor: es el problema de divisibilidad.",
                    "d": 2
                },
                {
                    "t": "Elegí TODAS las propiedades que debía reunir un bien para funcionar adecuadamente como dinero-mercancía:",
                    "o": [
                        "Ser divisible",
                        "Ser fácilmente transportable",
                        "Ser no perecedero",
                        "Ser escaso (tener valor en sí mismo)"
                    ],
                    "a": [0, 1, 2, 3],
                    "c": "Dinero-mercancía",
                    "e": "El PDF establece cuatro características esenciales: divisible, transportable, no perecedero y escaso.",
                    "d": 2
                },
                {
                    "t": "¿Por qué los metales preciosos (oro y plata) terminaron imponiéndose sobre el trigo y la sal como dinero-mercancía?",
                    "o": [
                        "Porque cumplían con mayor facilidad y eficiencia las funciones de ser divisibles, transportables, duraderos y escasos",
                        "Porque los gobiernos de la antigüedad prohibieron el uso de alimentos por decreto",
                        "Porque eran bienes perecederos que se consumían rápidamente",
                        "Porque tenían menor valor que otros bienes"
                    ],
                    "a": [0],
                    "c": "Dinero-mercancía",
                    "e": "Los metales preciosos satisfacían con superioridad técnica todos los requisitos: máxima durabilidad, alta divisibilidad y gran valor en poco volumen.",
                    "d": 2
                },
                {
                    "t": "Una moneda de oro posee 'valor intrínseco'. ¿Qué significa este concepto según el texto?",
                    "o": [
                        "Que tiene valor por sí misma y puede utilizarse como mercancía además de numerario",
                        "Que su valor está determinado exclusivamente por la firma de una autoridad política",
                        "Que carece de utilidad práctica fuera del sistema bancario",
                        "Que solo puede cambiarse por billetes de papel"
                    ],
                    "a": [0],
                    "c": "Valor intrínseco",
                    "e": "El valor intrínseco implica que el bien tiene valor en sí mismo, independientemente de que se use o no como medio de cambio.",
                    "d": 2
                }
            ]
        },
        {
            "title": "Los orfebres de la Edad Media, el dinero-signo y el curso legal",
            "theory": """
<p>¿Cómo se pasó de las monedas de oro pesado al dinero fiduciario actual?</p>
<h3>Los orfebres de la Edad Media y el rudimento del papel moneda</h3>
<p><span class="tag">Del PDF</span> Los orfebres disponían de cofres de seguridad para proteger sus propios metales. Las élites, preocupadas por la seguridad de sus tesoros, comenzaron a entregarles su oro en custodia. El orfebre entregaba a cambio un <b>recibo al portador</b> donde reconocía el depósito y se comprometía a devolverlo cuando el depositante lo requiriese.</p>
<p>Con el tiempo, al realizar transacciones comerciales importantes, en lugar de retirar el oro físico, las personas comenzaron a <b>entregar directamente los recibos</b>. Así surgió el <b>rudimento del papel moneda</b>, el cual era aceptado porque <b>se podía cambiar en cualquier momento por los metales depositados (oro y plata)</b>.</p>
<h3>El dinero-signo y el curso legal en la actualidad</h3>
<ul>
  <li><b>Dinero-signo:</b> en la actualidad, el dinero ya <b>no tiene valor intrínseco ni está respaldado por metales preciosos</b>. Billetes y monedas circulan simplemente porque la comunidad confía en que serán aceptados como pago. Es un signo aceptado por convención social.</li>
  <li><b>Curso legal:</b> la confianza descansa en las costumbres y en el marco normativo. La ley establece la obligación jurídica de que los billetes de un país sean aceptados como contrapartida extintiva de deudas en las transacciones internas.</li>
</ul>
<h3>Error frecuente</h3>
<p>Creer que hoy podemos ir al Banco Central a exigir que nos entreguen oro a cambio de nuestros billetes de $100. El dinero contemporáneo es dinero-signo de curso legal, sin convertibilidad metálica.</p>
""",
            "quiz": [
                {
                    "t": "¿Por qué los comerciantes de la Edad Media aceptaban los recibos emitidos por los orfebres como medio de pago?",
                    "o": [
                        "Porque esos recibos podían canjearse en cualquier momento por el oro o la plata depositados",
                        "Porque el papel tenía un altísimo valor intrínseco de mercado",
                        "Porque una ley internacional de curso legal obligaba a aceptarlos",
                        "Porque devengaban intereses mensuales en las ferias"
                    ],
                    "a": [0],
                    "c": "Orfebres y papel moneda",
                    "e": "La confianza en los recibos de los orfebres residía en su convertibilidad inmediata en el oro y la plata en custodia.",
                    "d": 2
                },
                {
                    "t": "En la actualidad, ¿en qué reside el valor de un billete de $500 pesos uruguayos?",
                    "o": [
                        "En que es un dinero-signo respaldado por la confianza social y de curso legal obligatorio fijado por ley",
                        "En una cantidad equivalente de lingotes de oro custodiada en el Banco Central para su canje libre",
                        "En el costo industrial de la tinta y el papel de algodón empleados",
                        "En que devenga automáticamente una tasa de interés pasiva"
                    ],
                    "a": [0],
                    "c": "Dinero-signo",
                    "e": "El dinero actual no tiene valor intrínseco ni respaldo en oro; se basa en la confianza y en la condición de curso legal por ley.",
                    "d": 2
                },
                {
                    "t": "¿Qué establece concretamente el principio de 'curso legal'?",
                    "o": [
                        "La obligación legal de que los billetes de un país sean aceptados como medio de pago en las transacciones internas",
                        "Que el dinero debe tener un contenido mínimo de plata o bronce",
                        "Que solo el gobierno central puede realizar compras en el mercado",
                        "Que está prohibido depositar billetes en bancos comerciales"
                    ],
                    "a": [0],
                    "c": "Curso legal",
                    "e": "El curso legal es la disposición legal que otorga poder liberatorio forzoso a la moneda nacional para cancelar pagos en el territorio.",
                    "d": 2
                },
                {
                    "t": "Un comerciante en Rivera se niega a recibir granos de café como pago por una compra. ¿Por qué la ley lo ampara?",
                    "o": [
                        "Porque el café no es moneda de curso legal obligatoria en Uruguay",
                        "Porque el café carece de valor económico",
                        "Porque el café no se puede transportar",
                        "Porque el café solo puede usarse en trueques internacionales"
                    ],
                    "a": [0],
                    "c": "Curso legal",
                    "e": "Aunque el café tenga valor, la ley no impone su aceptación obligatoria; solo la moneda de curso legal goza de esa potestad.",
                    "d": 2
                },
                {
                    "t": "Elegí TODAS las afirmaciones correctas sobre el dinero-signo contemporáneo:",
                    "o": [
                        "No posee valor intrínseco",
                        "No está respaldado por metales preciosos convertibles",
                        "Circula porque la comunidad confía en que será aceptado",
                        "Es de curso legal dentro del país"
                    ],
                    "a": [0, 1, 2, 3],
                    "c": "Dinero-signo",
                    "e": "Todas las opciones son verdaderas: el dinero contemporáneo es dinero-signo, sin respaldo metálico, fiduciario y de curso legal.",
                    "d": 3
                }
            ]
        }
    ],
    "exam": [
        {
            "t": "Un almacenero de Paysandú exhibe todos los precios de sus productos en pesos uruguayos. ¿Qué función del dinero se refleja prioritariamente?",
            "o": ["Unidad de medida o numerario", "Reserva de valor", "Dinero-mercancía", "Monopolio de encaje"],
            "a": [0],
            "c": "Funciones del dinero: unidad de medida (numerario)",
            "e": "Exhibir precios en una unidad común permite valorar y comparar todos los bienes: función de numerario."
        },
        {
            "t": "Verdadero o Falso: En una economía de trueque puro, es posible comerciar sin que exista coincidencia simultánea de necesidades.",
            "o": ["Verdadero", "Falso"],
            "a": [1],
            "c": "Problemas del trueque: simultaneidad de necesidades",
            "e": "Falso. El trueque requiere imprescindiblemente simultaneidad de necesidades entre quienes intercambian."
        },
        {
            "t": "Elegí los DOS problemas principales del trueque identificados explícitamente en el PDF:",
            "o": [
                "Simultaneidad o coincidencia de necesidades",
                "Poca o nula divisibilidad de las unidades transadas",
                "Exceso de emisión inorgánica de billetes",
                "Cobro excesivo de tasas de interés pasivas"
            ],
            "a": [0, 1],
            "c": "Problemas del trueque",
            "e": "El PDF identifica textualmente la simultaneidad de necesidades y la poca o nula divisibilidad de las unidades transadas."
        },
        {
            "t": "Un pastor tiene una vaca y desea conseguir tres huevos, dos zapallos y una piedra tallada. ¿Con qué traba insalvable del trueque se topa?",
            "o": ["Poca divisibilidad del bien que ofrece", "Falta de reserva de valor", "Exceso de dinero-signo", "Desvalorización del oro"],
            "a": [0],
            "c": "Problemas del trueque: divisibilidad",
            "e": "La vaca es indivisible en partes pequeñas para pagar bienes de escaso valor relativo."
        },
        {
            "t": "¿Por qué el trigo y la sal fueron utilizados en distintas épocas como dinero primitivo?",
            "o": ["Eran formas de dinero-mercancía con valor propio", "Eran billetes de curso legal", "Eran emitidos por el Banco Central", "Eran pasivos de los orfebres"],
            "a": [0],
            "c": "Dinero-mercancía",
            "e": "Constituyeron ejemplos típicos de dinero-mercancía con valor intrínseco."
        },
        {
            "t": "Una moneda de plata colonial tiene un valor comercial derivado del metal que contiene. Este atributo se denomina formalmente:",
            "o": ["Valor intrínseco", "Curso forzoso", "Encaje legal", "Multiplicador bancario"],
            "a": [0],
            "c": "Valor intrínseco",
            "e": "El valor intrínseco es el valor que posee un bien en sí mismo."
        },
        {
            "t": "Los recibos que entregaban los orfebres medievales a quienes les confiaban su oro representaban:",
            "o": [
                "Un reconocimiento del depósito con compromiso de devolver el oro a solicitud",
                "Una orden de pago no convertible",
                "Un préstamo con tasa activa fija",
                "Un título de deuda pública emitido por el Estado"
            ],
            "a": [0],
            "c": "Orfebres y papel moneda",
            "e": "El orfebre extendía un recibo donde reconocía el depósito y se obligaba a devolverlo cuando el cliente lo dispusiera."
        },
        {
            "t": "Verdadero o Falso: Los billetes de 100 pesos uruguayos actuales pueden cambiarse en ventanilla del BCU por una cantidad fija de oro.",
            "o": ["Verdadero", "Falso"],
            "a": [1],
            "c": "Dinero-signo",
            "e": "Falso. El dinero actual es dinero-signo fiduciario sin respaldo en oro convertible."
        },
        {
            "t": "¿Qué consecuencia práctica tiene que los billetes uruguayos sean de 'curso legal'?",
            "o": [
                "Que los acreedores están legalmente obligados a aceptarlos como medio de pago liberatorio en el país",
                "Que solo pueden utilizarse en bancos estatales",
                "Que tienen un valor garantizado en dólares",
                "Que pierden validez al cabo de un año calendario"
            ],
            "a": [0],
            "c": "Curso legal",
            "e": "El curso legal impone la aceptación legal obligatoria de los billetes en transacciones interiores."
        },
        {
            "t": "Una familia deposita su aguinaldo en una alcancía para costear los gastos de las vacaciones del próximo verano. ¿Qué función del dinero está aprovechando?",
            "o": ["Reserva de valor", "Unidad de medida", "Medio de cambio inmediato", "Creación secundaria"],
            "a": [0],
            "c": "Funciones del dinero: reserva de valor",
            "e": "Preservar poder de compra para adquisiciones futuras es la función de reserva de valor."
        },
        {
            "t": "Un contrato de alquiler estipula un canon mensual de $24.000 pagaderos mediante transferencia bancaria. ¿Qué funciones del dinero se aprecian aquí?",
            "o": [
                "Unidad de medida (fijación del canon) y medio de pago (la transferencia)",
                "Únicamente reserva de valor metálica",
                "Exclusivamente dinero-mercancía perecedero",
                "Spread bancario activo"
            ],
            "a": [0],
            "c": "Funciones del dinero",
            "e": "El monto en pesos es unidad de medida (numerario) y la transferencia que cancela el mes es medio de pago."
        },
        {
            "t": "¿Cuál es la secuencia cronológica correcta en la evolución histórica del dinero descripta en el PDF?",
            "o": [
                "Trueque → Dinero-mercancía → Recibos de orfebres (papel moneda) → Dinero-signo y curso legal",
                "Dinero-signo → Trueque → Orfebres → Dinero-mercancía",
                "Orfebres → Dinero-mercancía → Trueque → Dinero-signo",
                "Trueque → Dinero-signo → Orfebres → Dinero-mercancía"
            ],
            "a": [0],
            "c": "Evolución del dinero",
            "e": "Se pasó del trueque al dinero-mercancía, luego al papel moneda respaldado de orfebres y finalmente al dinero-signo contemporáneo."
        },
        {
            "t": "¿Por qué un bien altamente perecedero (como pescado fresco) no resulta idóneo para utilizarse como dinero-mercancía?",
            "o": [
                "Porque se descompone con rapidez y no permite conservar el valor en el tiempo",
                "Porque es excesivamente escaso en las costas",
                "Porque no tiene ningún valor intrínseco",
                "Porque la ley prohíbe comer alimentos transados"
            ],
            "a": [0],
            "c": "Dinero-mercancía",
            "e": "Al ser perecedero se destruye velozmente, perdiendo su utilidad como reserva de valor y medio de cambio confiable."
        },
        {
            "t": "¿Cuál es la característica definitoria del dinero-signo que circula hoy en día?",
            "o": [
                "Carece de valor intrínseco propio y se acepta por confianza social y respaldo del marco normativo",
                "Está hecho de metales preciosos escasos",
                "Es emitido libremente por cualquier particular sin contralor",
                "Solo tiene validez para operaciones internacionales"
            ],
            "a": [0],
            "c": "Dinero-signo",
            "e": "El dinero contemporáneo es un signo aceptado por la comunidad y con fuerza de ley."
        },
        {
            "t": "Si 1 kilo de carne cuesta $400 y 1 kilo de manzanas cuesta $80, ¿cuántos kilos de manzanas equivalen a 1 kilo de carne gracias a la función de numerario?",
            "o": ["5 kilos", "4 kilos", "10 kilos", "2 kilos"],
            "a": [0],
            "c": "Funciones del dinero: unidad de medida (numerario)",
            "e": "$400 / $80 = 5 kilos de manzanas. La unidad de cuenta permite establecer relaciones de valor sin recurrir al trueque."
        }
    ]
}
