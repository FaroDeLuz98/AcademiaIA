# -*- coding: utf-8 -*-
# Nivel 5: Banco Central del Uruguay (BCU)

L5 = {
    "id": 5,
    "name": "Banco Central del Uruguay",
    "icon": "🏛️",
    "parts": [
        {
            "title": "Monopolio de emisión y Banco de bancos",
            "theory": """
<p>Todos los sistemas financieros modernos cuentan con una <b>Autoridad Monetaria</b> que los ordena y coordina: en nuestro país es el <b>Banco Central del Uruguay (BCU)</b>.</p>
<h3>1. Monopolio de emisión de dinero</h3>
<p><span class="tag">Del PDF</span> <b>Sólo el Banco Central puede emitir dinero legalmente.</b> Ningún banco comercial ni agente privado tiene permitido imprimir billetes ni acuñar monedas de curso legal. La soberanía monetaria está centralizada en la Autoridad Monetaria.</p>
<h3>2. Banco de bancos</h3>
<p><span class="tag">Del PDF</span> El Banco Central actúa como el banco de las propias entidades bancarias:</p>
<ul>
  <li><b>Recibe depósitos de los bancos comerciales:</b> así como los ciudadanos depositamos nuestro dinero en un banco comercial, los bancos comerciales abren cuentas y depositan parte de sus fondos en el Banco Central (depósitos de encaje, $DV_B$).</li>
  <li><b>Asistencia financiera con crédito:</b> asiste a los bancos comerciales otorgándoles financiamiento. <b>Esta función es especialmente importante en períodos de crisis, pues permite salvar a los bancos con problemas de liquidez</b>, evitando quiebras que perjudiquen a los depositantes.</li>
</ul>
""",
            "quiz": [
                {
                    "t": "¿Quién posee la exclusividad y monopolio legal de la emisión de dinero en Uruguay?",
                    "o": [
                        "El Banco Central del Uruguay (BCU)",
                        "El Banco de la República Oriental del Uruguay (BROU)",
                        "Las casas financieras habilitadas",
                        "El Poder Judicial"
                    ],
                    "a": [0],
                    "c": "Monopolio de emisión de dinero legal",
                    "e": "El PDF establece como primera responsabilidad del BCU el monopolio de emisión de dinero: sólo el Banco Central puede emitir dinero legalmente.",
                    "d": 1
                },
                {
                    "t": "¿Qué significa que el Banco Central funciona como 'banco de bancos'?",
                    "o": [
                        "Que recibe depósitos de los bancos comerciales y los asiste financieramente otorgándoles crédito",
                        "Que es el dueño de todas las sucursales bancarias del territorio",
                        "Que atiende exclusivamente al público en general para compras minoristas",
                        "Que prohíbe a los bancos privados operar con empresas"
                    ],
                    "a": [0],
                    "c": "Función de Banco de bancos",
                    "e": "El BCU recibe depósitos de encaje de los bancos y les otorga créditos de asistencia financiera cuando lo requieren.",
                    "d": 1
                },
                {
                    "t": "¿Por qué la función de 'banco de bancos' resulta crucial durante los períodos de crisis financiera?",
                    "o": [
                        "Porque permite auxiliar y salvar a bancos con problemas puntuales de liquidez, evitando el pánico bancario",
                        "Porque permite incautar el oro de los particulares",
                        "Porque duplica los sueldos de los funcionarios públicos",
                        "Porque obliga a cerrar todas las cuentas corrientes"
                    ],
                    "a": [0],
                    "c": "Asistencia crediticia y salvataje de liquidez bancaria",
                    "e": "El PDF subraya que esta función es vital en crisis, pues permite salvar a bancos con descalces transitorios de liquidez.",
                    "d": 2
                },
                {
                    "t": "¿Qué tipo de cuentas mantienen los bancos comerciales en el Banco Central del Uruguay?",
                    "o": [
                        "Depósitos a la vista y de encaje ($DV_B$)",
                        "Cuentas corrientes para pagar sueldos de maestros",
                        "Plazos fijos en trigo y sal",
                        "Cajas de seguridad con cheques de orfebres"
                    ],
                    "a": [0],
                    "c": "Depósitos de los bancos en el BCU",
                    "e": "Los bancos comerciales mantienen depósitos a la vista en el BCU ($DV_B$), que constituyen sus reservas de encaje legal.",
                    "d": 2
                },
                {
                    "t": "Verdadero o Falso: Un banco comercial que enfrenta retiros masivos imprevistos puede solicitar asistencia crediticia al Banco Central en su rol de banco de bancos.",
                    "o": ["Verdadero", "Falso"],
                    "a": [0],
                    "c": "Asistencia crediticia y salvataje de liquidez bancaria",
                    "e": "Verdadero. La asistencia de liquidez del BCU a bancos comerciales es una de las razones de ser de la Autoridad Monetaria.",
                    "d": 1
                }
            ]
        },
        {
            "title": "Prestamista de última instancia y Contralor",
            "theory": """
<p>Para garantizar que el sistema financiero funcione con estabilidad y solidez, el BCU cuenta con dos potestades regulatorias y de auxilio:</p>
<h3>3. Prestamista en última instancia del sistema financiero</h3>
<p><span class="tag">Del PDF</span> Esto significa que el Banco Central <b>puede otorgar préstamos de corto plazo a instituciones solventes con problemas de liquidez</b>.</p>
<div class="exp">
  <b>Requisito indispensable: Solvencia</b><br>
  No se debe confundir <i>iliquidez</i> con <i>insolvencia</i>:<br>
  • Un banco <b>solvente</b> tiene activos de valor superior a sus pasivos (su patrimonio es positivo), pero sus fondos están colocados en préstamos y no dispone de billetes inmediatos en caja.<br>
  • El BCU actúa como prestamista de última instancia inyectando liquidez a corto plazo para evitar que una dificultad temporal provoque la caída del banco.
</div>
<h3>4. Contralor del sistema financiero</h3>
<p><span class="tag">Del PDF</span> Esta función está íntimamente vinculada con las dos anteriores: implica que el Banco Central <b>regula y supervisa la acción de los bancos como forma de evitar posibles crisis</b>.</p>
<p>El BCU establece normas de prudencia contable, fija los coeficientes de encaje legal y audita permanentemente a las instituciones financieras para proteger a los depositantes.</p>
""",
            "quiz": [
                {
                    "t": "¿A qué condición técnica deben responder las entidades financieras para recibir auxilio del BCU como prestamista de última instancia?",
                    "o": [
                        "Deben ser instituciones solventes que atraviesan problemas transitorios de liquidez",
                        "Deben encontrarse en quiebra definitiva irreversible con patrimonio negativo",
                        "Deben ser exclusivamente bancos extranjeros",
                        "No deben tener ningún tipo de clientes en el país"
                    ],
                    "a": [0],
                    "c": "Préstamos de corto plazo a entidades solventes con iliquidez",
                    "e": "El PDF destaca con total precisión que el BCU presta a instituciones solventes con problemas de liquidez.",
                    "d": 2
                },
                {
                    "t": "¿Cuál es el plazo habitual de los préstamos otorgados por el BCU bajo la figura de prestamista de última instancia?",
                    "o": [
                        "Préstamos de corto plazo",
                        "Créditos hipotecarios a 30 años",
                        "Préstamos perpetuos no reembolsables",
                        "Líneas de financiamiento a 50 años"
                    ],
                    "a": [0],
                    "c": "Prestamista en última instancia",
                    "e": "La asistencia como prestamista de última instancia se orienta a cubrir baches de liquidez inmediata mediante préstamos de corto plazo.",
                    "d": 1
                },
                {
                    "t": "¿En qué consiste concretamente la función de 'contralor del sistema financiero' del Banco Central?",
                    "o": [
                        "En regular y supervisar la acción de los bancos como forma de evitar posibles crisis",
                        "En fijar el precio de venta de los alimentos en los comercios",
                        "En administrar las jubilaciones de los trabajadores rurales",
                        "En cobrar impuestos a las exportaciones de granos"
                    ],
                    "a": [0],
                    "c": "Función de contralor y supervisión bancaria",
                    "e": "La función de contralor abarca la regulación, inspección y supervisión del comportamiento bancario para preservar la solvencia general.",
                    "d": 1
                },
                {
                    "t": "Si un banco tiene clientes que retiran sus fondos por un rumor infundado, pero el banco tiene créditos sanos por cobrar a futuro, ¿qué función del BCU puede auxiliarlo?",
                    "o": [
                        "La función de prestamista en última instancia",
                        "El financiamiento directo en bolsa",
                        "La colocación de bonos de deuda externa",
                        "La creación de una AFAP estatal"
                    ],
                    "a": [0],
                    "c": "Prevención de crisis sistémicas y pánicos financieros",
                    "e": "El banco es solvente pero ilíquido: el BCU le concede préstamos de corto plazo para frenar el pánico y abastecer los retiros.",
                    "d": 2
                },
                {
                    "t": "Elegí los dos objetivos centrales vinculados entre sí en las funciones de contralor y banco de bancos:",
                    "o": [
                        "Supervisar para prevenir crisis y otorgar asistencia financiera temporal a bancos solventes con problemas de liquidez",
                        "Emitir acciones de empresas privadas y comercializarlas en Wall Street",
                        "Fijar el costo de las facturas de agua y luz",
                        "Eliminar el uso de cuentas bancarias en todo el territorio"
                    ],
                    "a": [0],
                    "c": "Regulaciones y normas del Banco Central",
                    "e": "El contralor previene desmanejos y la ventanilla de liquidez asiste a bancos sanos ante shocks imprevistos.",
                    "d": 2
                }
            ]
        },
        {
            "title": "Agente financiero del Gobierno y Custodia de reservas",
            "theory": """
<p>Completamos las seis responsabilidades esenciales que el PDF asigna al Banco Central.</p>
<h3>5. Agente financiero del Gobierno Central</h3>
<p><span class="tag">Del PDF</span> El Banco Central actúa como el brazo financiero del Estado:</p>
<ul>
  <li><b>Recibe los depósitos del Gobierno:</b> custodia las cuentas del Tesoro Nacional.</li>
  <li><b>Coloca títulos de deuda en su nombre:</b> emite y coloca en el mercado títulos públicos, como los <b>Bonos del Tesoro</b> o las <b>Letras de Tesorería en moneda extranjera</b>.</li>
  <li><b>Atiende el servicio de la deuda:</b> efectúa los pagos de intereses y las amortizaciones de capital a los acreedores del Estado.</li>
  <li><b>Otorga asistencia financiera al Gobierno:</b> aunque el documento destaca que <b>esta función está cada vez más acotada</b> por ley para evitar déficits inflacionarios.</li>
</ul>
<h3>6. Administrar y custodiar las reservas internacionales</h3>
<p><span class="tag">Del PDF</span> <b>Administrar y custodiar las reservas de oro y divisas extranjeras del Gobierno.</b> Estas reservas internacionales sustentan la solvencia externa del país y garantizan el cumplimiento de compromisos internacionales.</p>
<h3>Resumen de las 6 responsabilidades del BCU</h3>
<ol>
  <li>Monopolio de emisión de dinero legal.</li>
  <li>Banco de bancos (depósitos y asistencia).</li>
  <li>Prestamista en última instancia (instituciones solventes con iliquidez).</li>
  <li>Contralor del sistema financiero (regulación y supervisión).</li>
  <li>Agente financiero del Gobierno Central (títulos, deuda, depósitos).</li>
  <li>Administrar y custodiar reservas de oro y divisas extranjeras.</li>
</ol>
""",
            "quiz": [
                {
                    "t": "¿Cuáles son los títulos de deuda pública del Gobierno que el BCU coloca en el mercado según el texto?",
                    "o": [
                        "Bonos del Tesoro y Letras de Tesorería en moneda extranjera",
                        "Recibos de orfebres medievales",
                        "Acciones preferenciales de AFAPs privadas",
                        "Certificados de depósito de cooperativas agrarias"
                    ],
                    "a": [0],
                    "c": "Colocación de títulos de deuda: Bonos del Tesoro y Letras de Tesorería",
                    "e": "El PDF cita textualmente como ejemplos a los Bonos del Tesoro y a las Letras de Tesorería en moneda extranjera.",
                    "d": 1
                },
                {
                    "t": "¿Qué señala el PDF acerca de la potestad del Banco Central de otorgar asistencia financiera al Gobierno Central?",
                    "o": [
                        "Que esta función está cada vez más acotada por el marco normativo",
                        "Que es ilimitada y obligatoria en todo momento",
                        "Que el BCU financia el 100% del gasto público mediante emisión",
                        "Que está totalmente transferida a los bancos comerciales privados"
                    ],
                    "a": [0],
                    "c": "Servicio de la deuda pública y asistencia financiera acotada",
                    "e": "El texto aclara textualmente: 'le otorga asistencia financiera, aunque esta función está cada vez más acotada'.",
                    "d": 1
                },
                {
                    "t": "¿Quién es el encargado de custodiar y administrar las reservas de oro y divisas extranjeras de la República?",
                    "o": [
                        "El Banco Central del Uruguay",
                        "El Banco Mundial",
                        "La Administración de Ferrocarriles del Estado",
                        "Las casas financieras no bancarias"
                    ],
                    "a": [0],
                    "c": "Administración y custodia de reservas de oro y divisas",
                    "e": "La custodia y administración de las reservas oficiales del Estado es la sexta responsabilidad atribuida al BCU.",
                    "d": 1
                },
                {
                    "t": "¿En qué consiste la labor de atender el 'servicio de la deuda' pública encomendada al BCU?",
                    "o": [
                        "En efectuar los pagos periódicos de amortización de capital e intereses a los tenedores de bonos del Estado",
                        "En anular unilateralmente las obligaciones financieras del país",
                        "En cobrar peajes en las rutas nacionales",
                        "En canjear bonos por trigo y sal"
                    ],
                    "a": [0],
                    "c": "Servicio de la deuda pública y asistencia financiera acotada",
                    "e": "Atender el servicio de la deuda consiste en pagar puntualmente los intereses y vencimientos comprometidos por el Gobierno.",
                    "d": 2
                },
                {
                    "t": "Elegí TODAS las responsabilidades que el PDF asigna explícitamente al Banco Central del Uruguay:",
                    "o": [
                        "Monopolio de emisión de dinero",
                        "Banco de bancos",
                        "Prestamista en última instancia",
                        "Contralor del sistema financiero",
                        "Agente financiero del Gobierno Central",
                        "Administrar y custodiar las reservas de oro y divisas"
                    ],
                    "a": [0, 1, 2, 3, 4, 5],
                    "c": "Rol del BCU como Autoridad Monetaria",
                    "e": "Las seis opciones constituyen la lista completa de responsabilidades asignadas al Banco Central en el texto del documento.",
                    "d": 2
                }
            ]
        }
    ],
    "exam": [
        {
            "t": "¿Por qué ningún banco comercial privado en Uruguay puede imprimir legítimamente billetes de 500 pesos?",
            "o": [
                "Porque la emisión de dinero legal es un monopolio exclusivo del Banco Central",
                "Porque los bancos privados no tienen papel ni tinta",
                "Porque solo pueden emitir billetes de 2.000 pesos",
                "Porque la Constitución prohíbe el uso de moneda física"
            ],
            "a": [0],
            "c": "Monopolio de emisión de dinero legal",
            "e": "El monopolio de emisión es la atribución exclusiva y excluyente que la ley reserva a la Autoridad Monetaria."
        },
        {
            "t": "¿Qué institución actúa como depositaria de los fondos de encaje de los bancos comerciales?",
            "o": ["El Banco Central del Uruguay (BCU)", "La Bolsa de Valores", "El Ministerio de Transporte", "El Fondo Monetario Internacional"],
            "a": [0],
            "c": "Función de Banco de bancos",
            "e": "En su carácter de 'banco de bancos', el BCU recibe en custodia los depósitos de encaje bancario."
        },
        {
            "t": "Un banco comercial sufre una corrida de depositantes debido a noticias falsas, pero sus cuentas demuestran que tiene solvencia patrimonial. ¿Qué auxilio le brinda el BCU?",
            "o": [
                "Préstamos de corto plazo en su rol de prestamista de última instancia",
                "La clausura inmediata de todas sus oficinas",
                "La emisión de billetes con el logotipo del banco privado",
                "Una condonación de todas las deudas de los particulares"
            ],
            "a": [0],
            "c": "Prestamista en última instancia",
            "e": "El prestamista de última instancia auxilia a entidades solventes con problemas transitorios de liquidez para preservar la confianza."
        },
        {
            "t": "Si una institución bancaria comete desmanejos reiterados y pone en riesgo los ahorros del público, ¿qué función ejerce el BCU al intervenirla?",
            "o": [
                "Contralor del sistema financiero",
                "Monopolio de emisión",
                "Custodia de metales preciosos",
                "Agente financiero gubernamental"
            ],
            "a": [0],
            "c": "Función de contralor y supervisión bancaria",
            "e": "La función de contralor regula, supervisa y sanciona para evitar crisis financieras y proteger a los depositantes."
        },
        {
            "t": "¿Qué títulos de deuda coloca el BCU en los mercados financieros en representación del Gobierno Central según el PDF?",
            "o": [
                "Bonos del Tesoro y Letras de Tesorería en moneda extranjera",
                "Acciones de sociedades anónimas comerciales",
                "Billetes de orfebres medievales",
                "Cuentas corrientes en moneda nacional"
            ],
            "a": [0],
            "c": "Colocación de títulos de deuda: Bonos del Tesoro y Letras de Tesorería",
            "e": "El PDF cita taxativamente los Bonos del Tesoro y las Letras de Tesorería en moneda extranjera."
        },
        {
            "t": "¿Quién administra y custodia las reservas internacionales de divisas y oro de la República Oriental del Uruguay?",
            "o": [
                "El Banco Central del Uruguay",
                "El Banco Hipotecario del Uruguay",
                "La Corporación Nacional para el Desarrollo",
                "Las AFAPs uruguayas"
            ],
            "a": [0],
            "c": "Administración y custodia de reservas de oro y divisas",
            "e": "La custodia de las reservas oficiales es la sexta responsabilidad fundamental del BCU."
        },
        {
            "t": "¿Por qué el marco legal uruguayo acotó progresivamente la asistencia financiera directa del BCU al Gobierno Central?",
            "o": [
                "Para evitar emisiones monetarias desmedidas que generen inflación y desequilibrios macroeconómicos",
                "Porque el gobierno no utiliza dinero para sus operaciones",
                "Porque los bancos comerciales le prohibieron al Estado gastar",
                "Para obligar al gobierno a usar trueque"
            ],
            "a": [0],
            "c": "Servicio de la deuda pública y asistencia financiera acotada",
            "e": "Limitar el financiamiento del déficit público con emisión del BCU es una regla fundamental para preservar el valor de la moneda."
        },
        {
            "t": "Verdadero o Falso: El Banco Central puede otorgar préstamos de rescate a instituciones comprobadamente insolventes que han quebrado su patrimonio.",
            "o": ["Verdadero", "Falso"],
            "a": [1],
            "c": "Préstamos de corto plazo a entidades solventes con iliquidez",
            "e": "Falso. El prestamista de última instancia asiste exclusivamente a instituciones solventes con problemas de liquidez."
        },
        {
            "t": "¿Cuál de las siguientes tareas NO corresponde al Banco Central del Uruguay según el documento?",
            "o": [
                "Conceder créditos de consumo para compras en cuotas a personas en ventanillas minoristas",
                "Ejercer el monopolio de emisión monetaria",
                "Supervisar y regular la actividad bancaria",
                "Custodiar las reservas de oro del país"
            ],
            "a": [0],
            "c": "Rol del BCU como Autoridad Monetaria",
            "e": "El BCU es una Autoridad Monetaria y banco de bancos; no otorga préstamos personales minoristas en ventanillas abiertas al público."
        },
        {
            "t": "¿Qué papel juega el BCU en el pago de intereses de los Bonos del Tesoro del Estado?",
            "o": [
                "Atiende el servicio de la deuda como agente financiero del Gobierno Central",
                "Emite moneda extranjera sin autorización",
                "Subasta las oficinas de los ministerios",
                "Cancela los bonos mediante trueque de bienes"
            ],
            "a": [0],
            "c": "Servicio de la deuda pública y asistencia financiera acotada",
            "e": "Como agente financiero estatal, el BCU atiende operativamente el servicio de la deuda pública."
        },
        {
            "t": "En una economía con sistema bancario de encaje fraccionario, ¿qué entidad define el coeficiente de encaje legal obligatorio?",
            "o": [
                "La Autoridad Monetaria (Banco Central)",
                "Las empresas que solicitan créditos",
                "Las Administradoras de Fondos de Ahorro Previsional",
                "Los clientes que libran cheques"
            ],
            "a": [0],
            "c": "Regulaciones y normas del Banco Central",
            "e": "El Banco Central ejerce su facultad de contralor y regulación determinando la tasa de encaje legal que deben cumplir los bancos."
        },
        {
            "t": "¿Cómo se denominan los depósitos que los bancos comerciales mantienen obligatoriamente en el Banco Central?",
            "o": [
                "Depósitos de encaje o depósitos a la vista de los bancos ($DV_B$)",
                "Depósitos a plazo de no residentes",
                "Billetes de curso diferido",
                "Títulos de deuda pública intransferibles"
            ],
            "a": [0],
            "c": "Depósitos de los bancos en el BCU",
            "e": "Son los depósitos de encaje en el BCU, simbolizados en las fórmulas como $DV_B$."
        },
        {
            "t": "¿Qué riesgo busca neutralizar la función de contralor del Banco Central sobre las entidades financieras privadas?",
            "o": [
                "El riesgo de crisis bancarias, quiebras por insolvencia y fraudes contra ahorristas",
                "El riesgo de que los bancos obtengan beneficios legítimos",
                "El riesgo de que aumente el uso de cheques",
                "El riesgo de que bajen las reservas de trigo"
            ],
            "a": [0],
            "c": "Prevención de crisis sistémicas y pánicos financieros",
            "e": "El contralor supervisa los riesgos crediticios y de liquidez para asegurar la estabilidad del sistema."
        },
        {
            "t": "Cuando el BCU asiste a un banco comercial durante un período de crisis crediticia, ¿en qué condición actúa prioritariamente?",
            "o": [
                "Como Banco de bancos y prestamista en última instancia",
                "Como agente de bolsa en Wall Street",
                "Como institución financiera externa para no residentes",
                "Como fondo de pensión previsional"
            ],
            "a": [0],
            "c": "Asistencia crediticia y salvataje de liquidez bancaria",
            "e": "Actúa simultáneamente como banco de bancos y prestamista de última instancia del sistema financiero."
        },
        {
            "t": "¿Cuál es la entidad que ostenta la potestad de ordenar todo el sistema financiero en Uruguay según el PDF?",
            "o": [
                "El Banco Central del Uruguay (BCU)",
                "La Asociación de Bancos del Uruguay",
                "El Tribunal de Cuentas",
                "El Fondo Monetario Internacional"
            ],
            "a": [0],
            "c": "Rol del BCU como Autoridad Monetaria",
            "e": "El PDF señala que todos los sistemas financieros funcionan con una Autoridad Monetaria que los ordena: el Banco Central."
        }
    ]
}
