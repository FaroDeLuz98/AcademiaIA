# -*- coding: utf-8 -*-
# Banco adicional de preguntas de razonamiento, situaciones cotidianas uruguayas y cálculos
# Complementa las 270 preguntas existentes para enriquecer quizzes, exámenes y repasos inteligentes.

EXTRA_QUESTIONS = [
    # --- NIVEL 1: Fundamentos y evolución del dinero ---
    {
        "t": "En una feria vecinal de Montevideo, un puestero marca el cartel: «2 kilos de tomates = $120» y un cliente abona con un billete de $200 recibiendo $80 de cambio. ¿Cómo intervienen aquí las funciones del dinero?",
        "o": [
            "El precio en el cartel es la función de numerario (unidad de medida) y la entrega del billete es la función de medio de pago",
            "El cartel es reserva de valor y el billete es dinero-mercancía con valor intrínseco",
            "El billete es un recibo de orfebre y el tomate es dinero de curso legal",
            "Ambas acciones corresponden exclusivamente a la creación primaria de dinero"
        ],
        "a": [0],
        "c": "Funciones del dinero: medio de pago y numerario",
        "e": "Fijar el precio en pesos expresa el valor en la unidad común de cuenta (numerario), mientras que la entrega de dinero extingue la obligación cancelando la compraventa (medio de pago).",
        "d": 2,
        "lvl": 1, "p": 0
    },
    {
        "t": "Un productor rural dispone de una tonelada de lana y necesita sal, herramientas y aceite comestible. El comerciante de herramientas no necesita lana, sino cueros. ¿Qué limitación del trueque se manifiesta directamente?",
        "o": [
            "Falta de simultaneidad o coincidencia mutua de necesidades",
            "Falta de curso legal del ganado",
            "Incapacidad de emitir cheques bancarios",
            "Exceso de liquidez en el mercado rural"
        ],
        "a": [0],
        "c": "Problemas del trueque: simultaneidad de necesidades",
        "e": "El trueque exige que ambas partes deseen simultáneamente lo que la otra ofrece. Si quien tiene herramientas busca cueros y no lana, el intercambio queda bloqueado.",
        "d": 2,
        "lvl": 1, "p": 1
    },
    {
        "t": "¿Por qué el trigo y la sal resultaban menos eficientes como dinero-mercancía en comparación con las monedas de oro y plata?",
        "o": [
            "Porque eran perecederos o voluminosos, mientras que el oro y la plata concentran gran valor en poco volumen, son duraderos y divisibles",
            "Porque el trigo y la sal carecían de cualquier tipo de valor intrínseco",
            "Porque los reyes medievales prohibieron por completo el consumo de sal",
            "Porque las monedas metálicas no tenían valor intrínseco propio"
        ],
        "a": [0],
        "c": "Dinero-mercancía",
        "e": "El grano puede pudrirse o arruinarse con la humedad (perecedero) y trasladar grandes cantidades es costoso; los metales preciosos son imperecederos, altamente divisibles y transportables.",
        "d": 2,
        "lvl": 1, "p": 1
    },
    {
        "t": "Los recibos emitidos por los orfebres medievales comenzaron a utilizarse como medio de pago entre mercaderes. ¿Qué condición aseguraba que fuesen ampliamente aceptados?",
        "o": [
            "La certeza de que en cualquier momento podían canjearse por el oro y la plata efectivamente depositados en los cofres",
            "Que una ley universal imponía penas de cárcel a quien los rechazara",
            "Que el papel en el que estaban impresos tenía un costo de producción superior al oro",
            "Que generaban una tasa pasiva mensual fijada por el Banco Central"
        ],
        "a": [0],
        "c": "Orfebres y papel moneda",
        "e": "La confianza radicaba en la convertibilidad plena: el tenedor sabía que el orfebre tenía el metal custodiado y se había comprometido a devolverlo contra entrega del recibo.",
        "d": 2,
        "lvl": 1, "p": 2
    },
    {
        "t": "Un comerciante de Maldonado coloca un cartel: «Prohibido pagar con billetes de pesos uruguayos; solo se aceptan monedas de plata». Desde el punto de vista normativo según el PDF:",
        "o": [
            "El comerciante está violando el principio de curso legal, ya que la ley obliga a aceptar la moneda nacional en las transacciones internas",
            "El comerciante actúa legítimamente porque la plata tiene valor intrínseco superior",
            "El curso legal solo rige en Montevideo y no en el interior del país",
            "La ley prohíbe el uso de billetes de papel en transacciones privadas"
        ],
        "a": [0],
        "c": "Curso legal",
        "e": "La moneda nacional es de curso legal: el marco jurídico establece la obligación de que los billetes de un país sean aceptados como medio de pago cancelatorio en transacciones internas.",
        "d": 2,
        "lvl": 1, "p": 2
    },

    # --- NIVEL 2: Definición operativa del dinero ---
    {
        "t": "Un empleado cobra su sueldo de $40.000 acreditado en su cuenta del BROU. Retira $10.000 por cajero RedBrou y deja $30.000 en su caja de ahorros a la vista. ¿Qué composición monetaria tiene ahora?",
        "o": [
            "$10.000 en efectivo en poder del público (EMₚ) y $30.000 en depósitos a la vista (DVₚ)",
            "$40.000 en depósitos a plazo fijo inmovilizados (DPₚ)",
            "$10.000 en reservas del Banco Central y $30.000 en billetes destruidos",
            "$40.000 en creación primaria exclusiva del gobierno"
        ],
        "a": [0],
        "c": "Diferencia entre efectivo y depósito a la vista",
        "e": "Los billetes en el bolsillo son emisión en poder del público ($EM_p = $10.000$) y el saldo bancario con disponibilidad inmediata es depósito a la vista ($DV_p = $30.000$).",
        "d": 2,
        "lvl": 2, "p": 0
    },
    {
        "t": "Una empresa constructora necesita pagar compras de ladrillos y cemento durante la semana. ¿Por qué prefiere mantener un depósito a la vista en lugar de un plazo fijo a 180 días?",
        "o": [
            "Porque el depósito a la vista le permite disponer del dinero en cualquier momento o librar cheques, mientras que el plazo fijo inmoviliza los fondos hasta el vencimiento",
            "Porque el depósito a la vista le paga una tasa de interés pasiva del 20% anual",
            "Porque el Banco Central prohíbe a las empresas tener plazos fijos",
            "Porque los depósitos a la vista solo se pagan en monedas de oro"
        ],
        "a": [0],
        "c": "Características de depósitos a la vista",
        "e": "Para pagos corrientes de operativa diaria se requiere máxima liquidez y disponibilidad. Un plazo fijo no puede retirarse antes de su vencimiento.",
        "d": 2,
        "lvl": 2, "p": 1
    },
    {
        "t": "¿Cuál es la razón económica por la cual los depósitos a plazo fijo pagan una tasa de interés pasiva superior a las cuentas a la vista?",
        "o": [
            "Porque compensan al ahorrista por resignar temporalmente la liquidez y disponibilidad de su dinero hasta la fecha de vencimiento",
            "Porque están emitidos por el Ministerio de Ganadería",
            "Porque los depósitos a plazo no forman parte del sistema financiero uruguayo",
            "Porque los bancos comerciales no pueden usar ese dinero para prestar"
        ],
        "a": [0],
        "c": "Diferencia de disponibilidad y vencimiento",
        "e": "El interés es la recompensa por la renuncia a la liquidez inmediata durante el período pactado contractualmente.",
        "d": 2,
        "lvl": 2, "p": 1
    },
    {
        "t": "Un comerciante tiene: $15.000 en la caja registradora, $80.000 en cuenta corriente bancaria y $100.000 en un depósito a plazo fijo a 6 meses. Clasificá estos fondos por su disponibilidad decreciente (de mayor a menor liquidez):",
        "o": [
            "Caja registradora (efectivo) → Cuenta corriente (depósito a la vista) → Depósito a plazo fijo",
            "Depósito a plazo fijo → Cuenta corriente → Caja registradora",
            "Cuenta corriente → Depósito a plazo fijo → Caja registradora",
            "Todos tienen exactamente el mismo grado de liquidez instantánea"
        ],
        "a": [0],
        "c": "Clasificación de los depósitos según su disponibilidad",
        "e": "El efectivo es inmediatamente líquido. La cuenta a la vista es casi instantánea (retiro o cheque). El plazo fijo requiere esperar hasta el vencimiento.",
        "d": 2,
        "lvl": 2, "p": 2
    },
    {
        "t": "Si una persona traslada $50.000 de su caja de ahorros a la vista ($DV_p$) hacia un depósito a plazo fijo a 1 año ($DP_p$), ¿qué sucede con la cantidad de dinero $M_2$ según la definición operativa?",
        "o": [
            "$M_2$ no se modifica, ya que comprende tanto los depósitos a la vista como los depósitos a plazo en moneda nacional",
            "$M_2$ disminuye en $50.000",
            "$M_2$ se duplica a $100.000",
            "$M_2$ desaparece porque los plazos fijos no son dinero"
        ],
        "a": [0],
        "c": "Diferencia entre depósito a plazo y agregado monetario M2",
        "e": "Como $M_2 = EM_p + DV_p + DP_p$, la caída de $DV_p$ se compensa con el aumento de $DP_p$, dejando el total de $M_2$ constante.",
        "d": 2,
        "lvl": 2, "p": 2
    },

    # --- NIVEL 3: Agregados monetarios M1, M2 y M3 ---
    {
        "t": "En una economía se registran los siguientes datos: EMₚ = $200 millones, DVₚ = $500 millones y DPₚ = $300 millones (todos en moneda nacional). ¿Cuáles son los valores de M₁ y M₂?",
        "o": [
            "M₁ = $700 millones y M₂ = $1.000 millones",
            "M₁ = $200 millones y M₂ = $500 millones",
            "M₁ = $1.000 millones y M₂ = $700 millones",
            "M₁ = $500 millones y M₂ = $300 millones"
        ],
        "a": [0],
        "c": "Cálculo de M2 a partir de M1 y DPp",
        "e": "$M_1 = EM_p + DV_p = 200 + 500 = $700$ millones. $M_2 = M_1 + DP_p = 700 + 300 = $1.000$ millones.",
        "d": 2,
        "lvl": 3, "p": 1
    },
    {
        "t": "A los datos de la economía anterior ($M_2 = $1.000 millones) se incorporan depósitos bancarios en moneda extranjera (dólares) por un equivalente de $600 millones. ¿A cuánto asciende el agregado M₃?",
        "o": [
            "$1.600 millones",
            "$1.000 millones",
            "$600 millones",
            "$2.300 millones"
        ],
        "a": [0],
        "c": "Definición y fórmula de M3 (M2 + Dm/e)",
        "e": "$M_3 = M_2 + D_{m/e} = 1.000 + 600 = $1.600$ millones.",
        "d": 2,
        "lvl": 3, "p": 2
    },
    {
        "t": "Un productor agropecuario uruguayo vende su cosecha de soja y recibe US$ 50.000 que deposita en una cuenta corriente en dólares en un banco de Paysandú. ¿En cuáles agregados monetarios queda contabilizado ese dinero?",
        "o": [
            "Únicamente en M₃, ya que M₁ y M₂ consideran exclusivamente moneda nacional",
            "En M₁ y en M₂ exclusivamente",
            "En la Base Monetaria primaria del BCU",
            "En ninguno, porque las divisas extranjeras no integran la oferta monetaria"
        ],
        "a": [0],
        "c": "Depósitos en moneda extranjera (dólares)",
        "e": "$M_1$ y $M_2$ abarcan moneda nacional. Los depósitos en moneda extranjera ($D_{m/e}$) recién se incorporan en la definición más amplia $M_3$.",
        "d": 2,
        "lvl": 3, "p": 2
    },
    {
        "t": "Un comerciante retira $100.000 de su cuenta corriente en pesos ($DV_p$) y compra dólares billete que guarda en su caja fuerte. ¿Qué ocurre con M₁ y con M₂ en pesos?",
        "o": [
            "Tanto M₁ como M₂ en moneda nacional disminuyen en $100.000",
            "M₁ aumenta y M₂ disminuye",
            "M₁ se mantiene constante porque el dólar es moneda nacional",
            "M₂ aumenta automáticamente en $100.000"
        ],
        "a": [0],
        "c": "Definición y fórmula de M1 (EMp + DVp)",
        "e": "El dinero en pesos salió del sistema bancario local y dejó de ser $DV_p$ en moneda nacional, reduciendo tanto $M_1$ como $M_2$ en pesos.",
        "d": 3,
        "lvl": 3, "p": 1
    },

    # --- NIVEL 4: Sistema financiero y bancario ---
    {
        "t": "En una mesa redonda sobre el sistema financiero uruguayo se debate qué instituciones pueden crear dinero. ¿Cuál afirmación es académicamente correcta según el PDF?",
        "o": [
            "Tanto los bancos comerciales como las cooperativas de ahorro y crédito y las IFEs integran el sistema bancario y tienen poder de crear dinero",
            "Todas las instituciones del sistema financiero crean dinero por igual, incluidas las AFAPs",
            "Únicamente el Banco Central puede crear dinero en la economía",
            "Ninguna institución privada puede crear dinero bajo ninguna circunstancia"
        ],
        "a": [0],
        "c": "Capacidad exclusiva de crear dinero del sistema bancario",
        "e": "El PDF establece con claridad que las instituciones del sistema bancario (bancos, cooperativas, casas financieras, IFEs y Autoridad Monetaria) tienen el poder de crear dinero.",
        "d": 2,
        "lvl": 4, "p": 0
    },
    {
        "t": "¿Por qué las AFAPs (Administradoras de Fondos de Ahorro Previsional) integran el sistema financiero pero NO el sistema bancario?",
        "o": [
            "Porque administran e invierten fondos de pensiones y jubilaciones canalizando ahorro, pero no reciben depósitos a la vista ni crean dinero secundario",
            "Porque están instaladas en el extranjero y solo atienden a no residentes",
            "Porque pertenecen a la bolsa de valores exclusivamente",
            "Porque sus aportes se efectúan en granos de trigo"
        ],
        "a": [0],
        "c": "Fondos de jubilaciones y pensiones (AFAPs en Uruguay)",
        "e": "Las AFAPs son intermediarios financieros no bancarios: canalizan recursos de aportantes hacia inversiones a largo plazo sin generar medios de pago ni multiplicar depósitos.",
        "d": 2,
        "lvl": 4, "p": 1
    },
    {
        "t": "Una empresa naviera radicada en Panamá desea abrir una cuenta en una Institución Financiera Externa (IFE) ubicada en la Ciudad Vieja de Montevideo. ¿Es jurídicamente viable según la normativa expuesta en el PDF?",
        "o": [
            "Sí, porque las IFEs son precisamente bancos instalados en el país habilitados para recibir depósitos y conceder créditos a personas no residentes",
            "No, porque las IFEs solo pueden operar con ciudadanos y empresas residentes uruguayas",
            "No, porque las IFEs no tienen permitido captar depósitos bancarios",
            "Solo si el gobierno central autoriza el pago en trigo"
        ],
        "a": [0],
        "c": "Restricción a no residentes en IFEs",
        "e": "Las IFEs tienen como característica distintiva operar exclusivamente con clientes no residentes, por lo que la operación con la firma panameña es plenamente viable.",
        "d": 2,
        "lvl": 4, "p": 2
    },

    # --- NIVEL 5: Banco Central del Uruguay ---
    {
        "t": "Durante un episodio de incertidumbre económica, los clientes de un banco solvente acuden en masa a retirar depósitos en billetes. El banco tiene préstamos de excelente cobro pero no tiene efectivo inmediato. ¿Qué función del BCU previene la quiebra?",
        "o": [
            "La función de prestamista en última instancia y banco de bancos, otorgando créditos de corto plazo para suplir el descalce de liquidez",
            "La función de custodia exclusiva de lingotes de oro del gobierno",
            "La colocación de acciones en la bolsa de valores de Montevideo",
            "La intervención forzosa para liquidar todos los bienes del banco"
        ],
        "a": [0],
        "c": "Prestamista en última instancia",
        "e": "El prestamista de última instancia auxilia a instituciones solventes con problemas transitorios de liquidez para frenar corridas y proteger el sistema.",
        "d": 2,
        "lvl": 5, "p": 1
    },
    {
        "t": "El Ministerio de Economía y Finanzas necesita financiar una obra portuaria emitiendo Letras de Tesorería en dólares. ¿Qué función cumple el BCU en esta operación?",
        "o": [
            "Actúa como agente financiero del Gobierno Central, colocando los títulos de deuda en el mercado y atendiendo su posterior servicio",
            "Actúa como prestamista a fondo perdido sin obligación de repago",
            "Imprime billetes falsos para comprar los títulos",
            "Transfiere el oro de las reservas a los constructores"
        ],
        "a": [0],
        "c": "Agente financiero del Gobierno Central",
        "e": "El BCU actúa como agente financiero del Gobierno Central: recibe depósitos estatales, coloca títulos de deuda (Bonos y Letras) y atiende el servicio de la deuda.",
        "d": 2,
        "lvl": 5, "p": 2
    },
    {
        "t": "¿Por qué el Banco Central del Uruguay supervisa y audita periódicamente las carteras de crédito y los encajes de los bancos comerciales?",
        "o": [
            "En ejercicio de su función de contralor del sistema financiero para prevenir crisis y garantizar la solvencia ante los depositantes",
            "Para cobrar comisiones comerciales por cada préstamo otorgado",
            "Para obligar a los bancos a cerrar sus sucursales del interior",
            "Para decidir a qué personas particulares se les debe prestar dinero"
        ],
        "a": [0],
        "c": "Función de contralor y supervisión bancaria",
        "e": "La función de contralor regula y supervisa la acción bancaria como mecanismo prudencial para evitar crisis sistémicas.",
        "d": 2,
        "lvl": 5, "p": 1
    },

    # --- NIVEL 6: Bancos comerciales e intermediación ---
    {
        "t": "Un banco comercial uruguayo capta depósitos a plazo fijo pagando un 4% anual (iₚ) y presta esos fondos a empresas constructoras al 16% anual (iₐ). ¿Cuál es su spread bancario y qué determina?",
        "o": [
            "El spread es 12 puntos porcentuales (16% - 4%) y determina la rentabilidad de la intermediación bancaria",
            "El spread es 20% y representa el encaje obligatorio",
            "El spread es 4% y representa la tasa de inflación",
            "El spread es cero porque ambas tasas se anulan mutuamente"
        ],
        "a": [0],
        "c": "Spread bancario (ia - ip)",
        "e": "$\\text{Spread} = i_a - i_p = 16\\% - 4\\% = 12\\%$. Este margen financiero determina la rentabilidad operativa de la intermediación bancaria.",
        "d": 2,
        "lvl": 6, "p": 1
    },
    {
        "t": "¿Cuál es el dilema que enfrenta un banquero comercial entre la maximización del beneficio y la liquidez?",
        "o": [
            "Para ganar más querría prestar el 100% de los depósitos, pero debe retener encajes líquidos para responder a los retiros diarios de sus clientes",
            "Para ganar más debe reducir los préstamos a cero",
            "La ley le prohíbe obtener ganancias superiores al salario mínimo",
            "Los depositantes le exigen que no guarde dinero en efectivo en la bóveda"
        ],
        "a": [0],
        "c": "Conflicto entre rentabilidad y liquidez",
        "e": "Prestar todos los fondos maximizaría los intereses cobrados pero generaría riesgo inmediato de cesación de pagos por iliquidez si los ahorristas retiran fondos.",
        "d": 2,
        "lvl": 6, "p": 2
    },
    {
        "t": "Una familia contrata débito automático en su cuenta para pagar mensualmente OSE, UTE y gastos comunes. Esta operatoria es un ejemplo de:",
        "o": [
            "El menú de servicios bancarios modernos que amplía ingresos complementarios sin ser la fuente principal de beneficios",
            "Creación primaria de dinero por el Banco Central",
            "Una transacción típica de instituciones financieras externas para no residentes",
            "Emisión inorgánica de base monetaria"
        ],
        "a": [0],
        "c": "Menú de servicios bancarios modernos",
        "e": "El pago automático de facturas es uno de los servicios modernos que los bancos ofrecen para mejorar rentabilidad y fidelizar clientes.",
        "d": 2,
        "lvl": 6, "p": 2
    },

    # --- NIVEL 7: Creación primaria del dinero y base monetaria ---
    {
        "t": "En una economía se reportan: emisión en poder del público EMₚ = $1.000 millones, billetes en poder de los bancos EMᵦ = $200 millones y depósitos de encaje en el BCU DVᵦ = $400 millones. ¿Cuánto valen las Reservas Totales (RTᵦ) y la Base Monetaria (BM)?",
        "o": [
            "RTᵦ = $600 millones y BM = $1.600 millones",
            "RTᵦ = $200 millones y BM = $1.200 millones",
            "RTᵦ = $1.000 millones y BM = $2.000 millones",
            "RTᵦ = $400 millones y BM = $800 millones"
        ],
        "a": [0],
        "c": "Fórmula con Reservas Totales: BM = EMp + RTB",
        "e": "$RT_B = EM_B + DV_B = 200 + 400 = 600$. $BM = EM_p + RT_B = 1.000 + 600 = 1.600$ millones.",
        "d": 2,
        "lvl": 7, "p": 1
    },
    {
        "t": "¿Por qué es fundamental no confundir los depósitos a la vista de los particulares (DVₚ) con los depósitos a la vista de los bancos en el BCU (DVᵦ)?",
        "o": [
            "Porque DVₚ forma parte de los medios de pago (M₁) de la economía, mientras que DVᵦ forma parte de la Base Monetaria (BM) como encaje bancario",
            "Porque DVₚ solo existe en dólares y DVᵦ solo en oro",
            "Porque DVᵦ no existe en el sistema financiero uruguayo",
            "Porque ambos son idénticos y se duplican en las estadísticas"
        ],
        "a": [0],
        "c": "Distinción crucial entre DVp y DVB",
        "e": "$DV_p$ es dinero transaccional de los particulares en bancos comerciales ($M_1$), mientras que $DV_B$ es reserva institucional de los bancos en el Banco Central ($BM$).",
        "d": 2,
        "lvl": 7, "p": 2
    },
    {
        "t": "Si el BCU decide emitir $500 millones en billetes nuevos para pagar obras de infraestructura, ¿qué magnitud monetaria se expande directamente en primer lugar?",
        "o": [
            "La Base Monetaria (BM) mediante creación primaria de dinero",
            "El multiplicador bancario que se vuelve infinito",
            "La tasa de interés pasiva exclusivamente",
            "Los depósitos a plazo de no residentes"
        ],
        "a": [0],
        "c": "Definición de creación primaria de dinero",
        "e": "La emisión de dinero legal por parte de la Autoridad Monetaria constituye creación primaria directa y expande la Base Monetaria.",
        "d": 2,
        "lvl": 7, "p": 0
    },

    # --- NIVEL 8: Creación secundaria y multiplicador ---
    {
        "t": "Si la tasa de encaje legal fijada por el Banco Central es de un 10% (e = 0.10) y los particulares depositan todo en los bancos, ¿cuál es el multiplicador bancario (MB)?",
        "o": [
            "MB = 10",
            "MB = 1",
            "MB = 0,10",
            "MB = 5"
        ],
        "a": [0],
        "c": "Fórmula del multiplicador bancario: MB = 1 / e",
        "e": "$MB = 1 / e = 1 / 0.10 = 10$. Por cada peso emitido por el BCU, el sistema bancario puede expandir hasta $10 en depósitos totales.",
        "d": 2,
        "lvl": 8, "p": 2
    },
    {
        "t": "Con una base monetaria inicial de $2.000 y una tasa de encaje del 20% (e = 0.20, MB = 5), ¿cuál es la oferta monetaria total máxima que pueden crear los bancos comerciales?",
        "o": [
            "$10.000 en depósitos totales",
            "$2.000",
            "$400",
            "$20.000"
        ],
        "a": [0],
        "c": "Cálculo de creación total: ΔM = Depósito inicial × (1/e)",
        "e": "$\\Delta M = \\text{Depósito inicial} \\times MB = 2.000 \\times 5 = $10.000$.",
        "d": 2,
        "lvl": 8, "p": 2
    },
    {
        "t": "En el ejemplo iterativo del PDF ($1.000 de emisión inicial, encaje e = 20%), ¿qué ocurre con los fondos en la Etapa 1?",
        "o": [
            "El banco recibe $1.000 de depósito, guarda $200 en reservas (20%) y concede nuevos préstamos por $800 (80%)",
            "El banco presta los $1.000 completos sin reservar nada",
            "El banco retiene $800 en bóveda y solo presta $200",
            "El Banco Central confisca los $1.000"
        ],
        "a": [0],
        "c": "Etapa 1: Depósito 1000, Reserva 200, Préstamo 800",
        "e": "De los $1.000 iniciales, el encaje del 20% exige reservar $200 y el remanente de $800 se vuelca al mercado como nuevo crédito.",
        "d": 2,
        "lvl": 8, "p": 1
    },
    {
        "t": "¿Por qué en la práctica el multiplicador real del dinero suele ser menor al valor teórico calculado con la fórmula MB = 1/e?",
        "o": [
            "Porque las personas retienen parte de los fondos en efectivo en sus bolsillos y no redepositan el 100% en los bancos (filtración hacia efectivo)",
            "Porque los bancos comerciales queman los billetes que reciben",
            "Porque el Banco Central prohíbe cobrar los préstamos",
            "Porque la fórmula solo sirve para economías feudales"
        ],
        "a": [0],
        "c": "Filtración hacia efectivo del público y reducción del multiplicador",
        "e": "El PDF destaca que si el público desea mantener una proporción de fondos en efectivo en su poder fuera del sistema, se frena el proceso de préstamos sucesivos.",
        "d": 2,
        "lvl": 8, "p": 2
    },

    # --- NIVEL 9: Demanda de dinero, ingreso y tasa de interés ---
    {
        "t": "Una persona mantiene $150.000 en billetes guardados en el placard de su dormitorio mientras la tasa de interés bancaria es del 10% anual. ¿Cuál es su costo de oportunidad anual?",
        "o": [
            "$15.000 al año, que es el interés que sacrifica por no colocar esos fondos a rendir",
            "Cero, porque el dinero en el placard no paga comisiones",
            "$150.000 de pérdida total del capital",
            "El 100% de la Base Monetaria"
        ],
        "a": [0],
        "c": "Definición de costo de oportunidad del dinero",
        "e": "Tener efectivo en el bolsillo no genera rendimientos. El 10% anual de $150.000 son $15.000 a los que renuncia por conservar liquidez absoluta.",
        "d": 2,
        "lvl": 9, "p": 1
    },
    {
        "t": "Si en Uruguay la tasa de interés de los instrumentos financieros sube fuertemente del 5% al 15% anual, ¿cómo reaccionan las familias y empresas respecto a su tenencia de dinero en efectivo?",
        "o": [
            "La demanda de dinero cae, porque al ser muy alto el costo de tener liquidez ociosa prefieren invertir en activos rentables",
            "La demanda de dinero se triplica",
            "La gente retira todo el dinero de los bancos para guardarlo en efectivo",
            "La demanda de dinero permanece insensible a la tasa de interés"
        ],
        "a": [0],
        "c": "Efecto de una suba de la tasa de interés (caída de demanda de dinero)",
        "e": "Al subir la tasa de interés, el costo de oportunidad de la liquidez es alto, por lo que la gente prefiere invertir y la demanda de dinero cae ($i \\uparrow \\implies M_d \\downarrow$).",
        "d": 2,
        "lvl": 9, "p": 2
    },
    {
        "t": "Si el Producto Bruto e ingreso nacional (Y) de Uruguay crece con fuerza en un año, ¿qué ocurre con la demanda de dinero transaccional de las familias?",
        "o": [
            "Aumenta, porque a mayor ingreso se realizan más compras y pagos transaccionales habituales",
            "Disminuye, porque con más ingresos las familias dejan de usar dinero",
            "Permanece idéntica porque el ingreso no influye en las compras",
            "Se reduce a cero y se vuelve al trueque"
        ],
        "a": [0],
        "c": "Relación directa entre ingreso y demanda de dinero",
        "e": "A mayor ingreso ($Y \\uparrow$), mayor volumen de transacciones cotidianas y pagos, lo que eleva la demanda de dinero ($M_d \\uparrow$).",
        "d": 2,
        "lvl": 9, "p": 0
    },
    {
        "t": "¿Cuál de las siguientes afirmaciones resume con absoluta precisión matemática y conceptual la función de demanda de dinero según el PDF?",
        "o": [
            "La demanda de dinero depende positivamente del nivel de ingreso (Y) y negativamente de la tasa de interés (i)",
            "La demanda de dinero depende negativamente del ingreso y positivamente de la tasa",
            "La demanda de dinero es constante y no depende ni del ingreso ni de la tasa",
            "La demanda de dinero depende exclusivamente de la cantidad de orfebres"
        ],
        "a": [0],
        "c": "Síntesis de los dos determinantes: Md = f(Y, i)",
        "e": "$M_d = f(Y, i)$: relación directa con el ingreso ($Y$) por motivo transaccional y relación inversa con la tasa de interés ($i$) por costo de oportunidad.",
        "d": 2,
        "lvl": 9, "p": 2
    }
]
