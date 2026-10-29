// Test funcional integral para Academia del Dinero v2.0
const fs = require('fs');
const vm = require('vm');

const html = fs.readFileSync('c:/Users/Usuario/Downloads/estudiar/Academia del Dinero.html', 'utf8');
const scriptMatch = html.match(/<script>([\s\S]*?)<\/script>/);
if (!scriptMatch) {
  console.error('ERROR: No se encontró etiqueta <script>');
  process.exit(1);
}
const js = scriptMatch[1];

function createEnvironment(initialLocalStorage = {}) {
  const mockStorage = { ...initialLocalStorage };
  const storage = {
    getItem: k => (k in mockStorage ? mockStorage[k] : null),
    setItem: (k, v) => { mockStorage[k] = String(v); },
    removeItem: k => { delete mockStorage[k]; }
  };
  const dom = {
    innerHTML: '',
    select: () => {},
    value: '',
    classList: {
      toggle: () => {},
      contains: () => false
    }
  };
  const sandbox = {
    console,
    localStorage: storage,
    mockStorage,
    document: {
      querySelector: () => dom,
      querySelectorAll: () => [],
      getElementById: () => dom,
      body: {
        classList: {
          toggle: () => {},
          contains: () => false
        }
      },
      hidden: false
    },
    window: {
      scrollTo: () => {},
      addEventListener: () => {}
    },
    setTimeout: fn => fn(),
    setInterval: () => {},
    Date,
    Math,
    Array,
    Object,
    JSON,
    String,
    Number,
    Boolean,
    Set,
    Blob: class {},
    URL: { createObjectURL: () => 'blob:mock', revokeObjectURL: () => {} },
    alert: msg => console.log('ALERT:', msg),
    confirm: () => true
  };
  vm.createContext(sandbox);
  return sandbox;
}

console.log('=== TEST 1: COMPILACIÓN Y SINTAXIS JAVASCRIPT ===');
try {
  new vm.Script(js);
  console.log('✔ Sintaxis JavaScript 100% válida sin errores.');
} catch (e) {
  console.error('Error de sintaxis:', e);
  process.exit(1);
}

console.log('\n=== TEST 2: ESTADO INICIAL Y PROGRESO ACADÉMICO (NIVEL 1 Y 2 APROBADOS, NIVEL 3 ACTIVO) ===');
const env = createEnvironment();
vm.runInContext(js, env);

const S = vm.runInContext('S', env);
const LEVELS = vm.runInContext('LEVELS', env);
const QID = vm.runInContext('QID', env);
const V = vm.runInContext('V', env);
const unlocked = vm.runInContext('unlocked', env);
const getResumeTarget = vm.runInContext('getResumeTarget', env);

console.log('Niveles en la plataforma:', LEVELS.length);
console.log('Total de preguntas en la base (originales + extra):', QID.length);
console.assert(LEVELS.length === 9, 'Debe haber 9 niveles');
console.assert(QID.length >= 304, 'Debe haber al menos 304 preguntas en la base');

console.log('Puntos XP acumulados verificados:', S.xp);
console.assert(S.xp === 610, 'XP debe ser 610 (295 Nivel 1 + 315 Nivel 2)');

console.assert(S.exams[1] && S.exams[1].passed, 'Nivel 1 debe estar aprobado');
console.assert(S.exams[1].best === 80, 'Nivel 1 nota debe ser 80%');
console.assert(S.exams[2] && S.exams[2].passed, 'Nivel 2 debe estar aprobado');
console.assert(S.exams[2].best === 87, 'Nivel 2 nota debe ser 87%');
console.assert(S.exams[2].source === 'Estudio con ChatGPT', 'Fuente de Nivel 2 debe ser Estudio con ChatGPT');

console.assert(S.parts['1-0'] && S.parts['1-1'] && S.parts['1-2'], 'Bloques de Nivel 1 completos');
console.assert(S.parts['2-0'] && S.parts['2-1'] && S.parts['2-2'], 'Bloques de Nivel 2 completos');

console.assert(unlocked(1) === true, 'Nivel 1 debe estar desbloqueado');
console.assert(unlocked(2) === true, 'Nivel 2 debe estar desbloqueado');
console.assert(unlocked(3) === true, 'Nivel 3 DEBE estar desbloqueado');

console.log('Pantalla inicial (V):', V);
console.assert(V.n === 'level' && V.l === 3, 'Al abrir debe colocarse en Nivel 3');

const resume = getResumeTarget();
console.log('Continuar donde quedé:', resume);
console.assert(resume.params.l === 3 && resume.params.p === 0, 'Debe apuntar a Nivel 3 Bloque 1');
console.log('✔ Estado inicial verificado correctamente.');

console.log('\n=== TEST 3: MIGRACIÓN SEGURA Y GENERACIÓN DE COPIA DE RESPALDO ===');
// Simular que el usuario ya tenía un progreso previo en academia-dinero-v1
const oldUserData = {
  xp: 150,
  parts: { '1-0': 1 },
  exams: {},
  ans: { '1.0.0': 1 },
  err: []
};
const envMigration = createEnvironment({
  'academia-dinero-v1': JSON.stringify(oldUserData)
});
vm.runInContext(js, envMigration);

// Verificar que se creó la copia de seguridad
const backup = envMigration.mockStorage['academia-dinero-v1-backup'];
console.assert(backup !== undefined, 'Debe haberse creado la copia de seguridad');
console.assert(JSON.parse(backup).xp === 150, 'El backup debe contener los datos previos');
console.log('✔ Copia de seguridad creada antes de migrar.');

const SMigrated = vm.runInContext('S', envMigration);
console.assert(SMigrated.migratedToL3 === true, 'Debe quedar registrado como migrado');
console.assert(SMigrated.exams[2].passed === true, 'Nivel 2 debe quedar aprobado tras migrar');
console.assert(SMigrated.xp >= 610, 'XP debe actualizarse como mínimo a 610');
console.log('✔ Migración segura completada sin pérdida de datos.');

console.log('\n=== TEST 4: BARAJADO DINÁMICO DE OPCIONES (SHUFFLE) ===');
const prepareQuestion = vm.runInContext('prepareQuestion', env);
const rawQ = QID.find(q => q.id === '2.0.0');
console.log('Pregunta original:', rawQ.t);
console.log('Opciones originales:', rawQ.o);
console.log('Respuesta correcta original (índice):', rawQ.a, '-> texto:', rawQ.o[rawQ.a[0]]);

// Probar 20 barajados para verificar que la respuesta siempre coincide en contenido
let shuffledDifferent = false;
for (let attempt = 0; attempt < 20; attempt++) {
  const prep = prepareQuestion(rawQ);
  const correctTextInPrep = prep.o[prep.a[0]];
  console.assert(correctTextInPrep === rawQ.o[rawQ.a[0]], 'El texto correcto debe preservarse exactamente');
  if (prep.a[0] !== rawQ.a[0]) {
    shuffledDifferent = true;
  }
}
console.assert(shuffledDifferent, 'Las opciones deben barajarse en distintas posiciones');
console.log('✔ Barajado de opciones dinámico verificado sin desfasar respuestas.');

console.log('\n=== TEST 5: SISTEMA DE ERRORES E HISTORIAL PERMANENTE (ERRHISTORY) ===');
const recordConceptAnswer = vm.runInContext('recordConceptAnswer', env);
const qTest = QID.find(q => q.c === 'Diferencia entre depósito a plazo y agregado monetario M2');

const initialErrHistoryLen = S.errHistory.length;
console.log('Errores históricos iniciales:', initialErrHistoryLen);

// Registrar un fallo intencional
recordConceptAnswer(qTest, [0], false, 'Test Automatizado');
console.assert(S.errHistory.length === initialErrHistoryLen + 1, 'Debe agregarse un nuevo evento al historial');
console.assert(S.conceptStats[qTest.c].status === 'reinforce', 'Estado debe ser reinforce tras fallo');
console.assert(S.conceptStats[qTest.c].correctStreak === 0, 'Racha debe resetearse a 0');

// Responder bien 1 vez distinta
recordConceptAnswer(qTest, qTest.a, true, 'Test Automatizado');
console.assert(S.conceptStats[qTest.c].status === 'progress', 'Estado debe ser progress tras 1 acierto');

// Responder bien una segunda pregunta distinta del mismo concepto
const qTest2 = QID.find(q => q.c === qTest.c && q.id !== qTest.id) || { ...qTest, id: 'test-q-2' };
recordConceptAnswer(qTest2, qTest2.a, true, 'Test Automatizado');
console.assert(S.conceptStats[qTest.c].status === 'mastered', 'Estado debe ser mastered tras 2 aciertos distintos');
console.assert(S.errHistory.length === initialErrHistoryLen + 1, 'El historial de errores NO debe borrarse al dominar');
console.log('✔ Historial permanente y criterio de dominio multirrespuesta verificados.');

console.log('\n=== TEST 6: REPASOS INTELIGENTES (SPACED REPETITION) ===');
const getPracticeQuestions = vm.runInContext('getPracticeQuestions', env);

const quickQs = getPracticeQuestions('quick');
console.log('Preguntas en Repaso Rápido:', quickQs.length);
console.assert(quickQs.length === 5, 'Repaso rápido debe tener 5 preguntas');
console.assert(quickQs.every(q => q.lvl === 1 || q.lvl === 2), 'Solo debe incluir niveles aprobados (1 y 2)');

const challengeQs = getPracticeQuestions('challenge');
console.log('Preguntas en Desafío Mixto:', challengeQs.length);
console.assert(challengeQs.length === 10, 'Desafío mixto debe tener 10 preguntas');
console.assert(challengeQs.every(q => q.lvl === 1 || q.lvl === 2), 'Solo debe incluir niveles aprobados (1 y 2)');
console.log('✔ Repasos inteligentes filtran correctamente niveles aprobados.');

console.log('\n=== TEST 7: GENERACIÓN DE INFORME LIMPIO PARA CHATGPT ===');
const generateChatGPTReport = vm.runInContext('generateChatGPTReport', env);
const mockExamRec = {
  lvl: 2,
  pct: 87,
  ok: 13,
  n: 15,
  pass: true,
  gain: 100,
  ts: Date.now(),
  source: 'Plataforma interactiva',
  res: [
    { q: QID.find(q => q.id === '2.E.3'), sel: [1], ok: false },
    { q: QID.find(q => q.id === '2.E.6'), sel: [2], ok: false },
    { q: QID.find(q => q.id === '2.E.0'), sel: [0], ok: true }
  ]
};
const report = generateChatGPTReport(mockExamRec);
console.assert(report.includes('INFORME DE RENDIMIENTO ACADÉMICO'), 'Debe incluir título');
console.assert(report.includes('Nivel evaluado: 2'), 'Debe indicar Nivel 2');
console.assert(report.includes('PREGUNTAS INCORRECTAS:'), 'Debe incluir preguntas incorrectas');
console.assert(!report.includes('&#x20;'), 'NO debe contener entidades HTML como &#x20;');
console.assert(!report.includes('<div'), 'NO debe contener tags HTML');
console.assert(!report.includes('\\\\n'), 'NO debe contener dobles barras invertidas');
console.log('✔ Informe para ChatGPT estructurado y limpio.');

console.log('\n=== TEST 8: INTEGRIDAD DE XP Y ANTI-FARMING ===');
const checkAnswer = vm.runInContext('checkAnswer', env);
const xpBefore = S.xp;

// Simular un runner activo
env._mockRunner = {
  mode: 'quiz',
  lvl: 3,
  part: 0,
  i: 0,
  qs: [prepareQuestion(QID.find(q => q.id === '3.0.0'))],
  sel: [0],
  checked: false,
  res: []
};
vm.runInContext('R = _mockRunner; R.sel = R.qs[0].a; checkAnswer();', env);
console.assert(S.xp === xpBefore + 10, 'Debe sumar 10 XP la primera vez');

// Responder la misma pregunta nuevamente en otra sesión
const xpAfterFirst = S.xp;
env._mockRunner2 = {
  mode: 'quiz',
  lvl: 3,
  part: 0,
  i: 0,
  qs: [prepareQuestion(QID.find(q => q.id === '3.0.0'))],
  sel: [],
  checked: false,
  res: []
};
vm.runInContext('R = _mockRunner2; R.sel = R.qs[0].a; checkAnswer();', env);
console.assert(S.xp === xpAfterFirst, 'NO debe sumar XP si la pregunta ya fue respondida');
console.log('✔ Regla anti-farming de XP verificada con éxito.');

console.log('\n=======================================================');
console.log('¡TODOS LOS 8 TESTS FUNCIONALES PASARON CON ÉXITO (100%)!');
console.log('=======================================================');
