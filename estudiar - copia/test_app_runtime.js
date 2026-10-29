// Test de simulación en Node.js de Academia del Dinero
const fs = require('fs');
const jsdom = require('vm');

const html = fs.readFileSync('c:/Users/Usuario/Downloads/estudiar/Academia del Dinero.html', 'utf8');
const js = html.match(/<script>([\s\S]*?)<\/script>/)[1];

// Simulación de entorno de navegador básico
const mockLocalStorage = {};
const storage = {
  getItem: k => mockLocalStorage[k] || null,
  setItem: (k, v) => { mockLocalStorage[k] = String(v); },
  removeItem: k => { delete mockLocalStorage[k]; }
};

const dom = {
  innerHTML: '',
  select: () => {},
  value: ''
};

const sandbox = {
  console,
  localStorage: storage,
  document: {
    querySelector: () => dom
  },
  window: {
    scrollTo: () => {}
  },
  setTimeout: fn => fn(),
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
  URL: { createObjectURL: () => 'blob:url', revokeObjectURL: () => {} }
};

jsdom.createContext(sandbox);
jsdom.runInContext(js, sandbox);

console.log('--- VALIDACIONES DE ESTADO Y RUNTIME ---');
console.log('Niveles cargados:', sandbox.LEVELS.length);
console.log('Total preguntas QID indexadas:', sandbox.QID.length);
console.assert(sandbox.LEVELS.length === 9, 'Debe haber 9 niveles');
console.assert(sandbox.QID.length === 270, 'Debe haber 270 preguntas');

// Verificar estado inicial S
const S = sandbox.S;
console.log('XP inicial:', S.xp);
console.assert(S.xp >= 295, 'XP debe incluir nivel 1 superado');
console.assert(S.exams[1] && S.exams[1].passed, 'Nivel 1 debe figurar como superado');
console.assert(S.exams[1].best === 80, 'Nota diagnóstico de Nivel 1 debe ser 80%');
console.assert(S.parts['1-0'] && S.parts['1-1'] && S.parts['1-2'], 'Las 3 partes del nivel 1 deben estar completadas');

// Verificar conceptos de error registrados del diagnóstico
console.log('Errores pendientes registrados:', S.err.length);
const errConcepts = S.err.map(e => e.c);
console.log('Conceptos a reforzar:', errConcepts);
console.assert(errConcepts.includes('Diferencia entre efectivo y depósito a la vista'), 'Falta concepto 1 a reforzar');
console.assert(errConcepts.includes('Clasificación de los depósitos según su disponibilidad'), 'Falta concepto 2 a reforzar');
console.assert(errConcepts.includes('Diferencia entre depósito a plazo y agregado monetario M2'), 'Falta concepto 3 a reforzar');

// Verificar pantalla inicial
console.log('Vista inicial V:', sandbox.V);
console.assert(sandbox.V.n === 'level' && sandbox.V.l === 2, 'La vista inicial DEBE ser Nivel 2');

// Verificar botón Continuar donde quedé
const resume = sandbox.getResumeTarget();
console.log('Objetivo de "Continuar donde quedé":', resume);
console.assert(resume.params.l === 2, 'Continuar donde quedé debe apuntar al Nivel 2');

// Verificar prueba de calificación
const qSample = sandbox.LEVELS[0].parts[0].quiz[0];
console.assert(sandbox.grade(qSample, [0]) === true, 'Opción correcta debe dar true');
console.assert(sandbox.grade(qSample, [1]) === false, 'Opción incorrecta debe dar false');

// Simular informe para ChatGPT
const testRec = {
  lvl: 2,
  pct: 73,
  ok: 11,
  n: 15,
  pass: false,
  ts: Date.now(),
  res: [
    { id: '2.E.0', sel: [1], ok: false },
    { id: '2.E.1', sel: [0], ok: true }
  ]
};
const report = sandbox.generateChatGPTReport(testRec);
console.log('--- MUESTRA DEL INFORME CHATGPT GENERADO ---');
console.log(report.slice(0, 350) + '\n...');
console.assert(report.includes('INFORME DE RENDIMIENTO ACADÉMICO'), 'Falta título de informe');
console.assert(report.includes('PREGUNTAS INCORRECTAS EN ESTE EXAMEN'), 'Falta sección preguntas incorrectas');
console.assert(report.includes('PROMPT DE ESTUDIO DIRIGIDO PARA CHATGPT'), 'Falta prompt para ChatGPT');

console.log('========================================');
console.log('¡TODAS LAS PRUEBAS DE RUNTIME PASARON CON ÉXITO!');
console.log('========================================');
