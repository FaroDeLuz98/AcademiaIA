# -*- coding: utf-8 -*-
"""
Builder para Academia del Dinero v2.0
Genera el archivo completo HTML autónomo e interactivo con:
- 9 niveles completos del PDF oficial «El dinero»
- 270 preguntas originales + 34 preguntas adicionales de razonamiento y cálculo (304 preguntas)
- Migración segura y preservación de progreso existente
- Nivel 1 (80%) y Nivel 2 (87%) superados, posicionando al usuario en Nivel 3 (Agregados monetarios M1, M2 y M3)
- Sistema de errores avanzado con historial permanente e indicadores de dominio multirrespuesta
- Sección «Mi evolución»
- Repasos inteligentes (Repaso rápido, Mis errores, Desafío mixto)
- Barajado aleatorio de opciones (shuffle dinámico sin desfasar respuestas correctas)
- Explicaciones pedagógicas en 4 partes con ejemplos uruguayos
- Temporizador de estudio, modo concentración, atajos de teclado y retoma de quizzes interrumpidos
- Informes pulidos y limpios para ChatGPT
"""

import json
import os
import sys

# Importar niveles y banco extra
import data_l1, data_l2, data_l3, data_l4, data_l5, data_l6, data_l7, data_l8, data_l9, data_extra

LEVELS = [
    data_l1.L1, data_l2.L2, data_l3.L3, data_l4.L4, data_l5.L5,
    data_l6.L6, data_l7.L7, data_l8.L8, data_l9.L9
]

EXTRA_QUESTIONS = data_extra.EXTRA_QUESTIONS

def build_html():
    levels_json = json.dumps(LEVELS, ensure_ascii=False, indent=2)
    extra_json = json.dumps(EXTRA_QUESTIONS, ensure_ascii=False, indent=2)

    template = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Academia del Dinero — Plataforma Educativa</title>
<style>
:root {
  --bg: #0b1026;
  --card: #151b3a;
  --card2: #1d2450;
  --tx: #e8ebff;
  --mu: #9aa3d6;
  --vi: #8b5cf6;
  --tq: #2dd4bf;
  --ok: #22c55e;
  --bad: #f43f5e;
  --ac: #f59e0b;
  box-sizing: border-box;
  padding-top: env(safe-area-inset-top, 0px);
  padding-bottom: env(safe-area-inset-bottom, 0px);
}
* { box-sizing: border-box; }
html, body {
  margin: 0;
  background: var(--bg);
  color: var(--tx);
  font: 16px/1.55 system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  color-scheme: dark;
}
main {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px 16px 100px;
  animation: in .25s ease;
}
@keyframes in {
  from { opacity: 0; transform: translateY(6px); }
  to { opacity: 1; transform: none; }
}

/* Header & Timer */
.top-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 0 14px;
  border-bottom: 1px solid #222a5c;
  margin-bottom: 14px;
}
.timer-pill {
  background: #1e293b;
  border: 1px solid #334155;
  color: var(--tq);
  font-size: 13px;
  font-weight: 600;
  padding: 4px 12px;
  border-radius: 20px;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

/* Navigation bar */
nav {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  justify-content: space-around;
  background: #0e1431f2;
  backdrop-filter: blur(12px);
  border-top: 1px solid #2a3270;
  padding: 6px 4px calc(6px + env(safe-area-inset-bottom, 0px));
  z-index: 50;
  transition: transform .25s ease;
}
nav button {
  background: none;
  border: 0;
  color: var(--mu);
  font: inherit;
  font-size: 11.5px;
  padding: 6px 10px;
  border-radius: 12px;
  cursor: pointer;
  transition: all .2s ease;
}
nav button.on {
  color: var(--tq);
  font-weight: 700;
  background: #2dd4bf15;
}
nav span {
  display: block;
  font-size: 20px;
  margin-bottom: 2px;
}

/* Concentration / Focus mode */
body.focus-mode nav {
  transform: translateY(100%);
  pointer-events: none;
}
body.focus-mode .top-bar,
body.focus-mode .no-focus {
  display: none !important;
}
body.focus-mode main {
  padding-bottom: 30px;
  max-width: 680px;
}

/* Headings */
h1, h2, h3 { line-height: 1.25; }
h1 { font-size: 25px; margin: .25em 0; }
h2 { font-size: 20px; margin: .35em 0; }
h3 { font-size: 17px; margin: .45em 0; }

/* Cards */
.card {
  background: var(--card);
  border: 1px solid #262e63;
  border-radius: 20px;
  padding: 18px;
  margin: 14px 0;
  box-shadow: 0 4px 18px #00000030;
}
.card.highlight {
  border-color: var(--vi);
  background: linear-gradient(135deg, #181d44, #1b214d);
}
.card.diag-box {
  border-color: var(--tq);
  background: #11253e;
}
.card.resume-card {
  border: 2px solid var(--tq);
  background: linear-gradient(135deg, #132e48, #182352);
}
.card.err-card {
  border-left: 4px solid var(--bad);
}
.mu { color: var(--mu); }
.row {
  display: flex;
  gap: 10px;
  align-items: center;
  flex-wrap: wrap;
}
.bar {
  height: 12px;
  background: #222a5c;
  border-radius: 9px;
  overflow: hidden;
}
.bar i {
  display: block;
  height: 100%;
  background: linear-gradient(90deg, var(--vi), var(--tq));
  transition: width .5s ease;
}

/* Buttons */
.btn {
  background: linear-gradient(135deg, var(--vi), #6366f1);
  color: #fff;
  border: 0;
  border-radius: 14px;
  padding: 12px 20px;
  font: inherit;
  font-weight: 600;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  text-decoration: none;
  transition: transform .15s ease, opacity .15s ease;
}
.btn:hover { opacity: .93; transform: translateY(-1px); }
.btn:active { transform: translateY(1px); }
.btn:focus-visible {
  outline: 2px solid var(--tq);
  outline-offset: 2px;
}
.btn.g {
  background: var(--card2);
  border: 1px solid #38418a;
  color: var(--tx);
}
.btn.tq {
  background: linear-gradient(135deg, #0d9488, var(--tq));
  color: #0b1026;
  font-weight: 700;
}
.btn.bad {
  background: linear-gradient(135deg, #be123c, var(--bad));
}
.btn:disabled {
  opacity: .35;
  cursor: not-allowed;
  transform: none;
}
.stat {
  flex: 1;
  min-width: 90px;
  background: var(--card2);
  border-radius: 14px;
  padding: 10px 12px;
  text-align: center;
}
.stat b {
  display: block;
  font-size: 22px;
  color: var(--tq);
}

/* Duolingo style path */
.path {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0;
  margin: 24px 0;
}
.node {
  width: 92px;
  height: 92px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  font-size: 38px;
  background: var(--card2);
  border: 4px solid #38418a;
  cursor: pointer;
  position: relative;
  transition: all .2s ease;
  user-select: none;
}
.node:hover { transform: scale(1.06); }
.node:focus-visible {
  outline: 3px solid var(--tq);
  outline-offset: 4px;
}
.node.available {
  border-color: var(--tq);
  box-shadow: 0 0 0 6px #2dd4bf28;
}
.node.progress {
  border-color: var(--vi);
  box-shadow: 0 0 0 6px #8b5cf638;
}
.node.done {
  background: #14532d;
  border-color: var(--ok);
  box-shadow: 0 0 0 6px #22c55e28;
}
.node.locked {
  opacity: .45;
  filter: grayscale(.7);
  cursor: not-allowed;
}
.node small {
  position: absolute;
  bottom: -4px;
  right: -4px;
  font-size: 20px;
}
.link {
  width: 6px;
  height: 34px;
  background: #2f3878;
  border-radius: 3px;
}
.lbl {
  text-align: center;
  font-size: 13.5px;
  color: var(--tx);
  margin: 6px 0 0;
  max-width: 220px;
  font-weight: 500;
}

/* Options */
.opt {
  display: block;
  width: 100%;
  text-align: left;
  background: var(--card2);
  color: var(--tx);
  border: 2px solid #333c82;
  border-radius: 14px;
  padding: 12px 14px;
  margin: 8px 0;
  font: inherit;
  cursor: pointer;
  transition: all .15s ease;
}
.opt:hover:not(:disabled) {
  border-color: var(--vi);
  background: #232a5a;
}
.opt:focus-visible {
  outline: 2px solid var(--tq);
  outline-offset: 2px;
}
.opt.sel {
  border-color: var(--vi);
  background: #2b2766;
  font-weight: 600;
}
.opt.ok {
  border-color: var(--ok);
  background: #13422a;
  color: #d1fae5;
  font-weight: 600;
}
.opt.bad {
  border-color: var(--bad);
  background: #4c1325;
  color: #ffe4e6;
}

/* Didactic 4-part explanation */
.exp-box {
  background: #0f1c3d;
  border-radius: 14px;
  padding: 14px 16px;
  margin: 14px 0;
  font-size: 14.5px;
  border-left: 4px solid var(--tq);
}
.exp-box.bad {
  border-left-color: var(--bad);
}
.exp-sec {
  margin: 8px 0;
  padding: 6px 0;
  border-bottom: 1px solid #1f2c56;
}
.exp-sec:last-child {
  border-bottom: 0;
  margin-bottom: 0;
  padding-bottom: 0;
}
.exp-sec b {
  color: var(--tq);
}
.exp-sec.err b {
  color: #f87171;
}

/* Badges and tags */
.tag {
  display: inline-block;
  font-size: 11.5px;
  font-weight: 600;
  padding: 2px 9px;
  border-radius: 8px;
  background: #2dd4bf22;
  color: var(--tq);
  margin-right: 6px;
}
.tag.x {
  background: #f59e0b22;
  color: #fbbf24;
}
.tag.ok {
  background: #22c55e22;
  color: var(--ok);
}
.badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 4px 10px;
  border-radius: 12px;
  font-size: 12px;
  font-weight: 600;
}
.badge.done { background: #14532d; color: #86efac; }
.badge.progress { background: #4c1d95; color: #d8b4fe; }
.badge.lock { background: #374151; color: #9ca3af; }
.badge.reinforce { background: #4c1325; color: #fca5a5; }

/* Sub-tabs */
.subtabs {
  display: flex;
  gap: 8px;
  margin: 14px 0;
  overflow-x: auto;
  padding-bottom: 4px;
}
.subtab {
  background: var(--card2);
  border: 1px solid #333c82;
  color: var(--mu);
  padding: 8px 14px;
  border-radius: 12px;
  font-size: 13.5px;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
}
.subtab.on {
  background: linear-gradient(135deg, var(--vi), #4f46e5);
  color: #fff;
  border-color: var(--vi);
}

/* Theory styles */
.th h3 { color: var(--tq); margin-top: 1.2em; }
.th { font-size: 15.5px; }
.th ul, .th ol { padding-left: 22px; }
table { border-color: #343f7c !important; }
textarea {
  width: 100%;
  min-height: 180px;
  background: #0b1026;
  color: var(--tx);
  border: 1px solid #38418a;
  border-radius: 12px;
  padding: 12px;
  font: 13.5px/1.45 ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  resize: vertical;
}
.ok-t { color: var(--ok); }
.bad-t { color: var(--bad); }
.tq-t { color: var(--tq); }
.vi-t { color: var(--vi); }
details {
  background: var(--card2);
  border-radius: 14px;
  padding: 10px 14px;
  margin: 10px 0;
  border: 1px solid #323b78;
}
summary { cursor: pointer; color: var(--tq); font-weight: 600; }
</style>
</head>
<body>

<main id="app"></main>
<nav id="nav"></nav>

<script>
/* ================= DATOS ACADÉMICOS (9 NIVELES + BANCO EXTRA) ================= */
const LEVELS = /* __LEVELS_DATA__ */;
const EXTRA_QS = /* __EXTRA_DATA__ */;

let QID = [];
// Indexar preguntas regulares
LEVELS.forEach(L => {
  if (!L.parts) return;
  L.parts.forEach((p, pi) => {
    p.quiz.forEach((q, n) => {
      q.lvl = L.id;
      q.p = pi;
      q.id = `${L.id}.${pi}.${n}`;
      q.m = Array.isArray(q.a) && q.a.length > 1;
      QID.push(q);
    });
  });
  L.exam.forEach((q, n) => {
    q.lvl = L.id;
    q.id = `${L.id}.E.${n}`;
    q.m = Array.isArray(q.a) && q.a.length > 1;
    q.p = L.parts.findIndex(p => p.quiz.some(z => z.c === q.c));
    if (q.p < 0) q.p = 0;
    QID.push(q);
  });
});

// Indexar banco extra de preguntas
EXTRA_QS.forEach((q, n) => {
  q.id = `${q.lvl}.X.${n}`;
  q.m = Array.isArray(q.a) && q.a.length > 1;
  QID.push(q);
});

/* ================= EJEMPLOS COTIDIANOS URUGUAYOS POR CONCEPTO ================= */
const URUGUAY_EXAMPLES = {
  'Definición de dinero': 'El billete de $100 con la figura de Eduardo Fabini que usás para pagar un alfajor en el almacén de tu barrio.',
  'Funciones del dinero: medio de pago': 'Pagar la cuenta de luz de UTE o el boleto del ómnibus en Montevideo o Canelones con tu tarjeta STM o dinero en efectivo.',
  'Funciones del dinero: unidad de medida (numerario)': 'El cartel en la feria vecinal que marca: «1 kg de manzanas = $80 y 1 kg de naranjas = $40», permitiendo comparar valores en una unidad común.',
  'Funciones del dinero: reserva de valor': 'Guardar $5.000 del aguinaldo en una cuenta para comprarte una campera de abrigo el próximo invierno.',
  'Problemas del trueque: simultaneidad de necesidades': 'Tener una bolsa de zapallos y querer comprar zapatos, pero el zapatero solo busca queso y no acepta tus zapallos.',
  'Problemas del trueque: divisibilidad': 'Tener una vaca entera y necesitar pagar solo una docena de huevos: no podés cortar la vaca viva sin destruirla.',
  'Dinero-mercancía': 'El uso histórico de la sal y los metales preciosos (oro y plata) por su escasez y valor propio intrínseco.',
  'Orfebres y papel moneda': 'Entregar lingotes de oro a los orfebres medievales y pagar en las ferias comerciales entregando directamente los recibos al portador.',
  'Dinero-signo': 'Un billete de $500 pesos uruguayos: no podés ir al Banco Central a exigir que te den oro a cambio, pero todos lo aceptan por confianza social.',
  'Curso legal': 'La ley uruguaya obliga a los comercios a aceptar los pesos uruguayos como medio liberatorio de pago en todo el territorio.',
  'Efectivo como activo más líquido': 'Llevar $1.000 en billetes en la billetera: podés comprar en el acto en cualquier quiosco sin esperar autorizaciones.',
  'Concepto de liquidez': 'La rapidez y facilidad con la que podés usar un activo para pagar en el mostrador sin perder valor.',
  'Emisión del Banco Central del Uruguay (BCU)': 'Los billetes y monedas en pesos que llevan la firma y el sello del Banco Central del Uruguay como única autoridad autorizada.',
  'Diferencia entre efectivo y depósito a la vista': 'El efectivo son los billetes físicos en tu bolsillo; el depósito a la vista es tu saldo en la caja de ahorros del BROU accesible con tarjeta de débito o cajero.',
  'Características de depósitos a la vista': 'Cobrar el sueldo en una cuenta bancaria y poder retirar en cualquier cajero Banred o RedBrou cuando lo necesites.',
  'Características de depósitos a plazo': 'Colocar $20.000 en un plazo fijo a 180 días en el banco: no podés retirar ese dinero hasta que se cumplan los 6 meses pactados.',
  'Clasificación de los depósitos según su disponibilidad': 'Depósitos a la vista (inmediata disponibilidad a demanda) frente a depósitos a plazo (disponibilidad recién al vencimiento del contrato).',
  'Diferencia entre depósito a plazo y agregado monetario M2': 'El depósito a plazo es un componente individual; M2 es la suma total que reúne la emisión pública, depósitos a la vista y depósitos a plazo.',
  'Definición y fórmula de M1 (EMp + DVp)': 'La suma de los billetes en la calle (EMₚ) más el dinero en cuentas corrientes y cajas de ahorro a la vista de los bancos (DVₚ).',
  'Definición y fórmula de M2 (M1 + DPp)': 'M1 más los depósitos a plazo fijo de los particulares en moneda nacional (DPₚ).',
  'Definición y fórmula de M3 (M2 + Dm/e)': 'M2 más los depósitos en dólares estadounidenses que tienen las familias y empresas en los bancos uruguayos.',
  'Dolarización financiera en América Latina y Uruguay': 'La costumbre extendida en Uruguay de comprar autos, inmuebles o abrir cajas de ahorro en dólares estadounidenses.',
  'Capacidad exclusiva de crear dinero del sistema bancario': 'Los bancos comerciales y cooperativas crean dinero al conceder préstamos sucesivos; las AFAPs y aseguradoras no crean dinero.',
  'Fondos de jubilaciones y pensiones (AFAPs en Uruguay)': 'Tu ahorro obligatorio administrado por República AFAP, UniónCapital, etc., para tu jubilación futura: canalizan ahorro pero no crean dinero.',
  'Prestamista en última instancia': 'El BCU otorgando auxilio de liquidez urgente a un banco comercial uruguayo solvente que enfrenta retiros imprevistos.',
  'Agente financiero del Gobierno Central': 'El BCU colocando Bonos del Tesoro o Letras de Regulación Monetaria en el mercado financiero en nombre del Estado.',
  'Spread bancario (ia - ip)': 'Un banco privado cobra 18% anual por un préstamo de auto y paga 4% por un depósito a plazo: su spread o margen financiero es 14%.',
  'Conflicto entre rentabilidad y liquidez': 'Un banco comercial querría prestar todo el dinero para cobrar más intereses, pero debe guardar encajes para devolver dinero a los ahorristas.',
  'Definición formal de Base Monetaria (BM)': 'Todo el dinero legal creado por el BCU: billetes en poder del público más reservas de encaje de los bancos (BM = EMₚ + RTᵦ).',
  'Distinción crucial entre DVp y DVB': 'DVₚ es el dinero de los ciudadanos en los bancos comerciales; DVᵦ es el encaje de los bancos comerciales guardado en la cuenta del Banco Central.',
  'Fórmula del multiplicador bancario: MB = 1 / e': 'Si el encaje legal del BCU es 20% (0.2), el multiplicador bancario es 1 / 0.2 = 5.',
  'Definición de costo de oportunidad del dinero': 'Guardar $50.000 bajo el colchón te da liquidez absoluta, pero renunciás a los intereses que ganarías poniéndolo a plazo fijo.',
  'Efecto de una suba de la tasa de interés (caída de demanda de dinero)': 'Si las tasas suben al 12% anual, la gente prefiere colocar sus ahorros a rendir en lugar de dejar billetes ociosos en el bolsillo.'
};

function getExampleForConcept(concept) {
  return URUGUAY_EXAMPLES[concept] || 'En la vida cotidiana, cada decisión de gastar en efectivo, transferir desde el banco o ahorrar para el futuro refleja este principio económico.';
}

/* ================= BARAJADO DINÁMICO DE OPCIONES ================= */
function shuffle(a) {
  const arr = [...a];
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

function prepareQuestion(q) {
  const indexed = q.o.map((txt, origIdx) => ({ txt, origIdx }));
  const shuffled = shuffle(indexed);
  const newA = [];
  shuffled.forEach((item, newIdx) => {
    if (q.a.includes(item.origIdx)) {
      newA.push(newIdx);
    }
  });
  return {
    ...q,
    rawQ: q,
    o: shuffled.map(item => item.txt),
    a: newA,
    m: newA.length > 1,
    shuffledMap: shuffled.map(item => item.origIdx)
  };
}

/* ================= ESTADO Y MIGRACIÓN SEGURA ================= */
const PASS = 80;
const KEY = 'academia-dinero-v1';
let S;

function createVerifiedInitialState() {
  return {
    xp: 610, // 295 XP (Nivel 1 verificado) + 315 XP (Nivel 2 verificado)
    parts: {
      '1-0': 1, '1-1': 1, '1-2': 1,
      '2-0': 1, '2-1': 1, '2-2': 1
    },
    exams: {
      1: { best: 80, passed: true, bonus: false, source: 'Estudio con ChatGPT' },
      2: { best: 87, passed: true, bonus: false, source: 'Estudio con ChatGPT' }
    },
    ans: {
      '1.0.0': 1, '1.0.1': 1, '1.0.2': 1, '1.0.3': 1,
      '1.1.0': 1, '1.1.1': 1, '1.1.2': 1, '1.1.3': 1, '1.1.4': 1,
      '1.2.0': 1, '1.2.1': 1, '1.2.2': 1, '1.2.3': 1,
      '2.0.0': 1, '2.0.1': 1, '2.0.2': 1, '2.0.3': 1,
      '2.1.0': 1, '2.1.1': 1, '2.1.2': 1, '2.1.3': 1,
      '2.2.0': 1, '2.2.1': 1, '2.2.2': 1, '2.2.3': 1
    },
    // Historial inmutable de errores
    errHistory: [
      {
        id: 'err-chatgpt-1',
        qid: '2.0.4',
        t: 'Rendimiento financiero del efectivo en el bolsillo',
        sel: ['Paga intereses mensuales automáticos'],
        correct: ['No genera intereses ni rendimientos directos'],
        c: 'Costo de mantener efectivo',
        lvl: 2, p: 0,
        src: 'Estudio con ChatGPT',
        ts: Date.now() - 7200000
      },
      {
        id: 'err-chatgpt-2',
        qid: '2.1.3',
        t: 'Retiro anticipado de depósitos a plazo fijo',
        sel: ['Se retira librando cheques en cualquier momento'],
        correct: ['Únicamente a la fecha de su vencimiento'],
        c: 'Diferencia de disponibilidad y vencimiento',
        lvl: 2, p: 1,
        src: 'Estudio con ChatGPT',
        ts: Date.now() - 5400000
      },
      {
        id: 'err-chatgpt-3',
        qid: '2.2.1',
        t: 'Diferencia entre depósito a plazo (DPp) y agregado M2',
        sel: ['Son exactamente la misma magnitud'],
        correct: ['DPp es un componente individual; M2 es el total agregado'],
        c: 'Diferencia entre depósito a plazo y agregado monetario M2',
        lvl: 2, p: 2,
        src: 'Estudio con ChatGPT',
        ts: Date.now() - 4000000
      },
      {
        id: 'err-chatgpt-4',
        qid: '2.E.3',
        t: 'Diferencia fundamental entre efectivo y depósito a la vista',
        sel: ['El efectivo rinde alta tasa de interés'],
        correct: ['Efectivo en mano del público vs depósito a la vista en bancos'],
        c: 'Diferencia entre efectivo y depósito a la vista',
        lvl: 2, p: 1,
        src: 'Estudio con ChatGPT',
        ts: Date.now() - 3600000
      },
      {
        id: 'err-chatgpt-5',
        qid: '2.E.6',
        t: 'Clasificación de depósitos según disponibilidad',
        sel: ['En depósitos estatales y privados únicamente'],
        correct: ['En depósitos a la vista y depósitos a plazo fijo'],
        c: 'Clasificación de los depósitos según su disponibilidad',
        lvl: 2, p: 2,
        src: 'Estudio con ChatGPT',
        ts: Date.now() - 3600000
      }
    ],
    // Fichas conceptuales para evaluar evolución
    conceptStats: {
      'Costo de mantener efectivo': { attempts: 2, errors: 1, correctStreak: 1, distinctCorrectQids: ['2.0.4'], status: 'progress', lastTs: Date.now() - 7200000 },
      'Diferencia de disponibilidad y vencimiento': { attempts: 3, errors: 1, correctStreak: 2, distinctCorrectQids: ['2.1.3', '2.E.4'], status: 'mastered', lastTs: Date.now() - 5400000 },
      'Diferencia entre depósito a plazo y agregado monetario M2': { attempts: 3, errors: 2, correctStreak: 1, distinctCorrectQids: ['2.2.1'], status: 'progress', lastTs: Date.now() - 3600000 },
      'Diferencia entre efectivo y depósito a la vista': { attempts: 3, errors: 1, correctStreak: 2, distinctCorrectQids: ['2.1.0', '2.E.3'], status: 'mastered', lastTs: Date.now() - 3600000 },
      'Clasificación de los depósitos según su disponibilidad': { attempts: 3, errors: 1, correctStreak: 2, distinctCorrectQids: ['2.2.0', '2.E.6'], status: 'mastered', lastTs: Date.now() - 3600000 }
    },
    hist: [
      {
        lvl: 2,
        pct: 87,
        ok: 13,
        n: 15,
        pass: true,
        gain: 100,
        ts: Date.now() - 3600000,
        source: 'Estudio con ChatGPT',
        res: []
      },
      {
        lvl: 1,
        pct: 80,
        ok: 12,
        n: 15,
        pass: true,
        gain: 100,
        ts: Date.now() - 86400000,
        source: 'Estudio con ChatGPT',
        res: []
      }
    ],
    studyTimeSeconds: 1560, // 26 min acumulados de estudio
    migratedToL3: true,
    migrationVersion: 2
  };
}

function load() {
  let raw = null;
  try {
    const item = localStorage.getItem(KEY);
    if (item) raw = JSON.parse(item);
  } catch (e) { raw = null; }

  // Respaldo de seguridad previo antes de modificar nada
  if (raw && !localStorage.getItem(KEY + '-backup')) {
    try { localStorage.setItem(KEY + '-backup', JSON.stringify(raw)); } catch (e) {}
  }

  if (!raw) {
    S = createVerifiedInitialState();
    save();
  } else {
    S = raw;
    S.xp = typeof S.xp === 'number' ? S.xp : 0;
    S.parts = S.parts || {};
    S.exams = S.exams || {};
    S.ans = S.ans || {};
    S.errHistory = S.errHistory || (S.err ? S.err.map(e => ({
      id: 'err-' + (e.ts || Date.now()),
      qid: e.id,
      t: e.c,
      sel: e.sel || [],
      correct: ['Respuesta correcta'],
      c: e.c,
      lvl: e.lvl || 2,
      p: e.p || 0,
      src: e.src || 'Diagnóstico',
      ts: e.ts || Date.now()
    })) : []);
    S.conceptStats = S.conceptStats || {};
    S.hist = S.hist || [];
    S.studyTimeSeconds = S.studyTimeSeconds || 0;

    // Migración segura: incorporar progreso real verificado (Nivel 1 y Nivel 2 aprobados)
    if (!S.migratedToL3) {
      // Guardar copia antes de migrar
      try { localStorage.setItem(KEY + '-backup-v2-' + Date.now(), JSON.stringify(S)); } catch (e) {}

      // Asegurar Nivel 1 superado
      S.parts['1-0'] = 1; S.parts['1-1'] = 1; S.parts['1-2'] = 1;
      S.exams[1] = S.exams[1] || { best: 80, passed: true, bonus: false, source: 'Estudio con ChatGPT' };

      // Asegurar Nivel 2 superado
      S.parts['2-0'] = 1; S.parts['2-1'] = 1; S.parts['2-2'] = 1;
      S.exams[2] = { best: 87, passed: true, bonus: false, source: 'Estudio con ChatGPT' };

      // Preservar y ajustar XP legítimo: 610 XP por Niveles 1 y 2
      if (S.xp < 610) {
        S.xp = 610;
      }

      // Asegurar examen de Nivel 2 en el historial
      if (!S.hist.some(h => h.lvl === 2)) {
        S.hist.unshift({
          lvl: 2,
          pct: 87,
          ok: 13,
          n: 15,
          pass: true,
          gain: 100,
          ts: Date.now() - 3600000,
          source: 'Estudio con ChatGPT',
          res: []
        });
      }

      // Inicializar conceptos si están vacíos
      const initStats = createVerifiedInitialState().conceptStats;
      Object.keys(initStats).forEach(c => {
        if (!S.conceptStats[c]) S.conceptStats[c] = initStats[c];
      });

      S.migratedToL3 = true;
      S.migrationVersion = 2;
      save();
    }
  }
}

function save() {
  try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) {}
}

/* ================= LÓGICA DE ESTADO Y PROGRESO ================= */
const partsDone = l => (LEVELS[l - 1].parts || []).filter((_, i) => S.parts[l + '-' + i]).length;
const unlocked = l => l === 1 || !!(S.exams[l - 1] && S.exams[l - 1].passed);
const status = l => {
  if (!unlocked(l)) return 'locked';
  if (S.exams[l] && S.exams[l].passed) return 'done';
  return partsDone(l) ? 'progress' : 'available';
};
const examOpen = l => partsDone(l) === 3;

function getResumeTarget() {
  // Buscar el primer nivel desbloqueado que no esté completado con examen aprobado
  for (let l = 1; l <= LEVELS.length; l++) {
    if (!unlocked(l)) continue;
    if (!S.exams[l] || !S.exams[l].passed) {
      for (let p = 0; p < 3; p++) {
        if (!S.parts[l + '-' + p]) {
          return { view: 'lesson', params: { l, p }, label: `Nivel ${l}: ${LEVELS[l - 1].name} · Bloque ${p + 1}` };
        }
      }
      return { view: 'level', params: { l }, label: `Nivel ${l}: ${LEVELS[l - 1].name} · 🎓 Examen final` };
    }
  }
  return { view: 'home', params: {}, label: '¡Todos los niveles superados!' };
}

/* ================= UTILIDADES DOM ================= */
const $ = s => document.querySelector(s);
const $$ = s => document.querySelectorAll(s);

/* ================= VISTAS Y NAVEGACIÓN ================= */
// POSICIONAMIENTO AUTOMÁTICO EN NIVEL 3
let V = { n: 'level', l: 3 };
let R = null;
let currentPracticeMode = null;
let activeSubtab = 'weak'; // 'weak', 'evolution', 'history'

function go(n, a = {}) {
  V = { n, ...a };
  R = null;
  render();
  window.scrollTo(0, 0);
}

function render() {
  const tabs = [
    ['home', '🗺️', 'Inicio'],
    ['level', '📖', 'Nivel 3'],
    ['areas', '🎯', 'Mejorar'],
    ['hist', '📜', 'Historial'],
    ['cfg', '⚙️', 'Ajustes']
  ];
  $('#nav').innerHTML = tabs.map(([k, i, t]) => {
    let isAct = V.n === k;
    if (k === 'level' && V.n === 'level' && V.l === 3) isAct = true;
    return `<button class="${isAct ? 'on' : ''}" onclick="${k === 'level' ? `go('level',{l:3})` : `go('${k}')`}"><span>${i}</span>${t}</button>`;
  }).join('');

  const views = { home, level, lesson, exam, results, areas, recov, practice, hist, cfg };
  const fn = views[V.n] || home;
  $('#app').innerHTML = fn();
  if (R && $('#qz')) renderQ();
}

/* ================= TEMPORIZADOR Y MODO CONCENTRACIÓN ================= */
setInterval(() => {
  if (!document.hidden && S) {
    S.studyTimeSeconds = (S.studyTimeSeconds || 0) + 1;
    const el = document.getElementById('studyTimer');
    if (el) {
      const mins = Math.floor(S.studyTimeSeconds / 60);
      el.textContent = `⏱️ ${mins} min de estudio`;
    }
  }
}, 1000);

function toggleFocusMode() {
  document.body.classList.toggle('focus-mode');
  const btn = document.getElementById('focusBtn');
  if (btn) {
    btn.textContent = document.body.classList.contains('focus-mode') ? '✕ Salir de concentración' : '🎯 Modo Concentración';
  }
}

/* ---- VISTA: HOME ---- */
function home() {
  const total = LEVELS.length;
  const done = LEVELS.filter(l => status(l.id) === 'done').length;
  const resume = getResumeTarget();
  const xp = S.xp;
  const rank = Math.floor(xp / 150) + 1;
  const rankNames = [
    '', 'Principiante', 'Aprendiz de Finanzas', 'Analista Monetario',
    'Asistente de Banco Central', 'Operador del Sistema Financiero',
    'Economista Monetario', 'Master en Economía'
  ];
  const rankTitle = rankNames[Math.min(rank, rankNames.length - 1)] || 'Experto Máximo';
  const mins = Math.floor((S.studyTimeSeconds || 0) / 60);

  // Sesión en curso interrumpida
  let resumeSessionHtml = '';
  try {
    const act = JSON.parse(localStorage.getItem('academia-active-session'));
    if (act && act.qs && act.qs.length && act.i < act.qs.length) {
      resumeSessionHtml = `
        <div class="card resume-card">
          <div class="row" style="justify-content:space-between">
            <span class="tag ok">Sesión pendiente guardada</span>
            <span class="mu">Pregunta ${act.i + 1} de ${act.qs.length}</span>
          </div>
          <b style="font-size:16px;display:block;margin:6px 0">Tenés un quiz en curso: ${act.title || 'Evaluación'}</b>
          <div class="row" style="margin-top:10px">
            <button class="btn tq" onclick="resumeActiveSession()">Continuar quiz donde estabas ➔</button>
            <button class="btn g" onclick="discardActiveSession()">Descartar</button>
          </div>
        </div>
      `;
    }
  } catch (e) {}

  const nodes = LEVELS.map((L, i) => {
    const s = status(L.id);
    const ic = { locked: '🔒', done: '✅', progress: '⏳', available: '⭐' }[s];
    const off = [0, -45, 0, 45][i % 4];
    return `${i ? '<div class="link"></div>' : ''}
      <div style="transform:translateX(${off}px);text-align:center">
        <div class="node ${s}" tabindex="0" onclick="${s === 'locked' ? '' : `go('level',{l:${L.id}})`}" onkeydown="if(event.key==='Enter')this.click()">
          ${L.icon}${ic ? `<small>${ic}</small>` : ''}
        </div>
        <div class="lbl">${L.id}. ${L.name}</div>
      </div>`;
  }).join('');

  return `
    <div class="top-bar no-focus">
      <span class="timer-pill" id="studyTimer">⏱️ ${mins} min de estudio</span>
      <button class="btn g" id="focusBtn" style="padding:6px 12px;font-size:12px" onclick="toggleFocusMode()">🎯 Modo Concentración</button>
    </div>

    <h1>Academia del Dinero</h1>
    <p class="mu">Plataforma de estudio adaptativo basada en el documento oficial <b>«El dinero»</b>.</p>

    ${resumeSessionHtml}

    <div class="card highlight no-focus">
      <div class="row" style="justify-content:space-between">
        <div>
          <span class="tag ok">Historial verificado</span>
          <b style="font-size:18px">${rankTitle} (Rango ${rank})</b>
        </div>
        <span class="tq-t"><b>${xp} XP</b></span>
      </div>
      
      <div class="row" style="margin-top:14px">
        <div class="stat"><b>${xp}</b>XP totales</div>
        <div class="stat"><b>${done}/${total}</b>Niveles aprobados</div>
        <div class="stat"><b>${Object.values(S.conceptStats || {}).filter(c => c.status === 'reinforce').length}</b>Por reforzar</div>
      </div>
      
      <p class="mu" style="margin:14px 0 6px;font-size:13px">Progreso al siguiente rango (${xp % 150} / 150 XP)</p>
      <div class="bar"><i style="width:${(xp % 150) / 1.5}%"></i></div>
      
      <div style="margin-top:16px">
        <button class="btn tq" style="width:100%;font-size:16px" onclick="go('${resume.view}', ${JSON.stringify(resume.params)})">
          ▶ Continuar donde quedé (${resume.label})
        </button>
      </div>
    </div>

    <div class="card no-focus" style="display:flex;justify-content:space-between;align-items:center;border-left:4px solid var(--tq)">
      <div>
        <b>⚡ Repasos inteligentes</b>
        <div class="mu" style="font-size:13px">Entrená los conceptos ya vistos de los Niveles 1 y 2.</div>
      </div>
      <button class="btn g" onclick="go('areas')">Practicar ➔</button>
    </div>

    <div class="path">${nodes}</div>
  `;
}

/* ---- VISTA: NIVEL ---- */
function level() {
  const L = LEVELS[V.l - 1];
  const s = status(L.id);
  const ex = S.exams[L.id];
  const pDone = partsDone(L.id);
  const isLvl3 = L.id === 3;

  // Cartel especial para el Nivel 3 (próximo nivel activo)
  const lvl3Intro = isLvl3 ? `
    <div class="card diag-box">
      <div class="row" style="justify-content:space-between">
        <span class="tag ok">Tu frontera de aprendizaje</span>
        <span class="badge progress">Nivel Activo</span>
      </div>
      <h3 style="margin-top:8px">📊 Bienvenido al Nivel 3: Agregados monetarios M1, M2 y M3</h3>
      <p style="font-size:14.5px;margin:6px 0">
        Superaste exitosamente los <b>Niveles 1 y 2</b> (80% y 87%). Ahora aprenderás a clasificar los activos financieros por su grado de liquidez:
      </p>
      <ul style="font-size:14px;padding-left:22px;margin:8px 0">
        <li><b>Bloque 1:</b> Medios de pago (M₁ = EMₚ + DVₚ) — definición más restringida de dinero.</li>
        <li><b>Bloque 2:</b> Cantidad de dinero (M₂ = M₁ + DPₚ) e incorporación de depósitos a plazo.</li>
        <li><b>Bloque 3:</b> Agregado M₃ y el impacto de la dolarización en Uruguay y América Latina.</li>
      </ul>
      <div class="row" style="margin-top:12px">
        <button class="btn tq" onclick="go('lesson',{l:3,p:0})">
          ▶ Iniciar Bloque 1: Medios de pago (M₁)
        </button>
      </div>
    </div>
  ` : '';

  const partRows = L.parts.map((p, i) => {
    const done = !!S.parts[`${L.id}-${i}`];
    const open = i === 0 || !!S.parts[`${L.id}-${i - 1}`];
    return `
      <div class="card" style="display:flex;justify-content:space-between;align-items:center;gap:12px">
        <div>
          <div class="row">
            <b>Bloque ${i + 1}: ${p.title}</b>
            ${done ? '<span class="badge done">✔ Completado</span>' : open ? '<span class="badge progress">Disponible</span>' : '<span class="badge lock">Bloqueado</span>'}
          </div>
          <div class="mu" style="font-size:13px;margin-top:4px">
            Teoría del PDF + Quiz de 5 preguntas (+25 XP por primera vez)
          </div>
        </div>
        <button class="btn ${done ? 'g' : open ? 'tq' : 'g'}" ${open ? '' : 'disabled'} onclick="go('lesson',{l:${L.id},p:${i}})">
          ${done ? 'Repasar' : open ? 'Comenzar' : '🔒'}
        </button>
      </div>
    `;
  }).join('');

  return `
    <button class="btn g" onclick="go('home')">← Volver al Mapa</button>
    
    <div style="margin:16px 0 10px">
      <h1>${L.icon} Nivel ${L.id}: ${L.name}</h1>
      <div class="row" style="justify-content:space-between;margin-bottom:6px">
        <span class="mu">Progreso: ${pDone} de 3 bloques completados</span>
        <span class="tq-t"><b>${Math.round((pDone + (ex && ex.passed ? 1 : 0)) * 25)}%</b></span>
      </div>
      <div class="bar"><i style="width:${(pDone + (ex && ex.passed ? 1 : 0)) * 25}%"></i></div>
    </div>

    ${lvl3Intro}
    ${partRows}

    <div class="card" style="border:1px solid ${examOpen(L.id) ? 'var(--vi)' : '#333c82'};background:${examOpen(L.id) ? '#181e46' : 'var(--card)'}">
      <div class="row" style="justify-content:space-between;align-items:center">
        <div>
          <div class="row">
            <b>🎓 Examen Final del Nivel ${L.id}</b>
            ${ex && ex.passed ? '<span class="badge done">Aprobado</span>' : examOpen(L.id) ? '<span class="badge progress">Habilitado</span>' : '<span class="badge lock">Requiere 3 bloques</span>'}
          </div>
          <div class="mu" style="font-size:13.5px;margin-top:4px">
            ${L.exam.length} preguntas · Sin teoría visible ni pistas · Aprobación con ${PASS}%
            ${ex ? `<br>Mejor nota: <b class="${ex.passed ? 'ok-t' : 'bad-t'}">${ex.best}%</b> (${ex.source || 'Plataforma'})` : ''}
          </div>
        </div>
        <button class="btn ${examOpen(L.id) ? '' : 'g'}" ${examOpen(L.id) ? '' : 'disabled'} onclick="go('exam',{l:${L.id}})">
          ${examOpen(L.id) ? (ex && ex.passed ? 'Repetir Examen' : 'Rendir Examen') : '🔒 Bloqueado'}
        </button>
      </div>
    </div>
  `;
}

/* ---- VISTA: LECCIÓN (TEORÍA + QUIZ DE 5 PREGUNTAS) ---- */
function lesson() {
  const L = LEVELS[V.l - 1];
  const p = L.parts[V.p];
  return `
    <div class="top-bar">
      <button class="btn g" onclick="abandonSession('level',{l:${L.id}})">← Nivel ${L.id}</button>
      <button class="btn g" id="focusBtn" style="padding:6px 12px;font-size:12px" onclick="toggleFocusMode()">🎯 Modo Concentración</button>
    </div>

    <div style="margin:8px 0 14px">
      <span class="tag">Nivel ${L.id} · Bloque ${V.p + 1} de 3</span>
      <h2>${p.title}</h2>
    </div>

    <div class="card th">
      <div class="row" style="justify-content:space-between;margin-bottom:10px">
        <span class="tag ok">Marco Teórico Oficial</span>
        <span class="mu" style="font-size:13px">Fuente: PDF «El dinero»</span>
      </div>
      ${p.theory}
    </div>

    <h2 style="margin-top:24px">Quiz del Bloque ${V.p + 1}</h2>
    <p class="mu">5 preguntas con corrección explicativa detallada. Podés consultar la teoría de arriba.</p>
    <div id="qz"></div>
  ` + (R ? '' : (setTimeout(() => startRun({
    qs: p.quiz,
    mode: 'quiz',
    lvl: L.id,
    part: V.p,
    title: `Nivel ${L.id}: Bloque ${V.p + 1}`
  }), 0), ''));
}

/* ---- VISTA: EXAMEN FINAL ---- */
function exam() {
  const L = LEVELS[V.l - 1];
  return `
    <div class="top-bar">
      <button class="btn g" onclick="abandonSession('level',{l:${L.id}})">← Salir del Examen</button>
      <button class="btn g" id="focusBtn" style="padding:6px 12px;font-size:12px" onclick="toggleFocusMode()">🎯 Modo Concentración</button>
    </div>

    <div style="margin:8px 0 14px">
      <span class="tag">Examen Final Oficial</span>
      <h2>🎓 Examen · Nivel ${L.id}: ${L.name}</h2>
      <p class="mu">${L.exam.length} preguntas sin teoría ni pistas intermedias. Las explicaciones completas se muestran al terminar.</p>
    </div>
    <div id="qz"></div>
  ` + (R ? '' : (setTimeout(() => startRun({
    qs: shuffle(L.exam),
    mode: 'exam',
    lvl: L.id,
    title: `Examen Final Nivel ${L.id}`
  }), 0), ''));
}

/* ---- VISTA: RECUPERACIÓN DIRIGIDA ---- */
function recov() {
  const cTarget = V.c;
  const qs = QID.filter(q => q.c === cTarget);
  const p = LEVELS[V.l - 1].parts[V.p];

  return `
    <button class="btn g" onclick="go('areas')">← Volver a Áreas</button>
    <div style="margin:12px 0 6px">
      <span class="tag x">Práctica adaptativa dirigida</span>
      <h2>Concepto: ${cTarget}</h2>
    </div>

    <details open>
      <summary>📖 Repasar marco teórico relacionado (Nivel ${V.l}, Bloque ${V.p + 1})</summary>
      <div class="th" style="margin-top:10px">
        ${p.theory}
      </div>
    </details>

    <h3 style="margin-top:18px">Ejercicios de consolidación</h3>
    <p class="mu">Respondé correctamente para fortalecer tu racha y dominar este concepto.</p>
    <div id="qz"></div>
  ` + (R ? '' : (setTimeout(() => startRun({
    qs: qs.length ? qs : p.quiz,
    mode: 'recov',
    lvl: V.l,
    part: V.p,
    targetConcept: cTarget,
    title: `Recuperación: ${cTarget}`
  }), 0), ''));
}

/* ---- VISTA: PRÁCTICA ESPACIADA (REPASOS INTELIGENTES) ---- */
function practice() {
  const pMode = V.pMode || 'quick';
  let title = 'Repaso Rápido';
  let desc = '5 preguntas de conceptos de los niveles que ya aprobaste.';
  
  return `
    <button class="btn g" onclick="go('areas')">← Volver a Práctica</button>
    <div style="margin:12px 0 6px">
      <span class="tag ok">Repaso Espaciado</span>
      <h2>${V.title || title}</h2>
      <p class="mu">${desc}</p>
    </div>
    <div id="qz"></div>
  ` + (R ? '' : (setTimeout(() => {
    const qs = getPracticeQuestions(pMode);
    startRun({
      qs,
      mode: 'practice',
      pMode,
      title: V.title || title
    });
  }, 0), ''));
}

function getPracticeQuestions(mode) {
  // Solo incluir preguntas de niveles aprobados
  const approvedLevels = [1, 2, 3, 4, 5, 6, 7, 8, 9].filter(l => S.exams[l] && S.exams[l].passed);
  // Si solo aprobó 1 y 2, los pools son de 1 y 2
  const pool = QID.filter(q => approvedLevels.includes(q.lvl));

  if (mode === 'weak') {
    // Preguntas de conceptos con errores o en estado reinforce
    const weakList = Object.keys(S.conceptStats || {}).filter(c => S.conceptStats[c].status === 'reinforce');
    const weakQs = pool.filter(q => weakList.includes(q.c));
    return shuffle(weakQs.length >= 5 ? weakQs : pool).slice(0, 5);
  } else if (mode === 'challenge') {
    return shuffle(pool).slice(0, 10);
  } else {
    // quick: 5 preguntas aleatorias
    return shuffle(pool).slice(0, 5);
  }
}

/* ---- RUNNER INTERACTIVO Y CONTROL DE SESIÓN ---- */
function startRun(opts) {
  // Preparar preguntas con barajado dinámico de opciones
  const preparedQs = (opts.qs || []).map(q => prepareQuestion(q));
  R = {
    ...opts,
    qs: preparedQs,
    i: 0,
    sel: [],
    checked: false,
    res: []
  };
  saveActiveSession();
  renderQ();
}

function saveActiveSession() {
  if (!R || !R.qs || !R.qs.length) return;
  try {
    const data = {
      mode: R.mode,
      lvl: R.lvl,
      part: R.part,
      i: R.i,
      title: R.title,
      targetConcept: R.targetConcept,
      pMode: R.pMode,
      qs: R.qs.map(q => q.id),
      res: R.res
    };
    localStorage.setItem('academia-active-session', JSON.stringify(data));
  } catch (e) {}
}

function clearActiveSession() {
  try { localStorage.removeItem('academia-active-session'); } catch (e) {}
}

function abandonSession(targetView, params) {
  if (R && R.i > 0 && R.i < R.qs.length) {
    if (!confirm('¿Deseás pausar este cuestionario? Tu avance quedará guardado para retomarlo cuando vuelvas.')) return;
  }
  clearActiveSession();
  go(targetView, params);
}

function resumeActiveSession() {
  try {
    const act = JSON.parse(localStorage.getItem('academia-active-session'));
    if (!act || !act.qs) return;
    const questions = act.qs.map(id => QID.find(q => q.id === id)).filter(Boolean);
    if (!questions.length) return;

    R = {
      ...act,
      qs: questions.map(q => prepareQuestion(q)),
      sel: [],
      checked: false
    };
    if (R.mode === 'quiz') go('lesson', { l: R.lvl, p: R.part });
    else if (R.mode === 'exam') go('exam', { l: R.lvl });
    else if (R.mode === 'practice') go('practice', { pMode: R.pMode });
    else render();
  } catch (e) {}
}

function discardActiveSession() {
  clearActiveSession();
  render();
}

function renderQ() {
  const el = $('#qz');
  if (!el || !R || !R.qs[R.i]) return;
  const q = R.qs[R.i];
  const isExam = R.mode === 'exam';
  const ch = R.checked;
  const isMult = !!q.m;

  let explanationHtml = '';
  if (ch) {
    const ok = R.lastOk;
    const selTexts = R.sel.map(idx => q.o[idx]);
    const okTexts = q.a.map(idx => q.o[idx]);
    const eg = getExampleForConcept(q.c);

    explanationHtml = `
      <div class="exp-box ${ok ? '' : 'bad'}">
        <div style="font-size:16px;font-weight:700;margin-bottom:8px">
          ${ok ? '✅ ¡Respuesta correcta!' : '❌ Tu respuesta no es la adecuada.'}
        </div>
        
        ${!ok ? `
          <div class="exp-sec err">
            <b>1. ¿Por qué tu respuesta no corresponde?</b><br>
            Elegiste: <i>«${selTexts.join(' | ') || 'Sin respuesta'}»</i>. Esta opción contradice las definiciones técnicas del documento.
          </div>
        ` : ''}

        <div class="exp-sec">
          <b>${ok ? '1.' : '2.'} Razonamiento correcto (según el PDF «El dinero»):</b><br>
          ${q.e}
        </div>

        <div class="exp-sec">
          <b>${ok ? '2.' : '3.'} Ejemplo cotidiano uruguayo:</b><br>
          ${eg}
        </div>

        <div class="exp-sec">
          <b>${ok ? '3.' : '4.'} Concepto a reforzar:</b><br>
          <span class="tag">${q.c}</span> (Nivel ${q.lvl})
        </div>
      </div>
    `;
  }

  el.innerHTML = `
    <div class="card" style="border-color:${isExam ? 'var(--vi)' : '#262e63'}">
      <div class="row" style="justify-content:space-between">
        <span class="mu">Pregunta ${R.i + 1} de ${R.qs.length}</span>
        <span class="tag">${isExam ? 'Examen Final' : 'Pregunta de estudio'}</span>
      </div>
      
      <div class="bar" style="margin:10px 0 16px">
        <i style="width:${((R.i + (ch ? 1 : 0)) * 100) / R.qs.length}%"></i>
      </div>

      <h3 style="font-size:18px;margin-bottom:12px">${q.t}</h3>
      ${isMult ? '<p class="mu" style="font-size:13px"><b>Varias opciones correctas:</b> seleccioná todas las que apliquen (usá teclas 1, 2, 3, 4).</p>' : '<p class="mu" style="font-size:12.5px">Podés usar los números del teclado para responder más rápido.</p>'}

      <div>
        ${q.o.map((txt, idx) => {
          let cls = '';
          const isSelected = R.sel.includes(idx);
          if (ch) {
            const isCorrect = q.a.includes(idx);
            if (isCorrect) cls = 'ok';
            else if (isSelected) cls = 'bad';
          } else if (isSelected) {
            cls = 'sel';
          }
          return `
            <button class="opt ${cls}" onclick="pickOpt(${idx})">
              <b>${idx + 1}.</b> ${isMult ? (isSelected ? '☑ ' : '☐ ') : ''}${txt}
            </button>
          `;
        }).join('')}
      </div>

      ${explanationHtml}

      <div style="margin-top:16px">
        <button class="btn tq" ${R.sel.length ? '' : 'disabled'} onclick="${isExam ? 'nextExamQ()' : ch ? 'nextQuizQ()' : 'checkAnswer()'}">
          ${isExam ? (R.i + 1 === R.qs.length ? 'Finalizar Examen ➔' : 'Siguiente Pregunta ➔') : ch ? (R.i + 1 === R.qs.length ? 'Ver Resultado Final ➔' : 'Siguiente Pregunta ➔') : 'Comprobar respuesta (Enter)'}
        </button>
      </div>
    </div>
  `;
}

function pickOpt(idx) {
  if (R.checked) return;
  const q = R.qs[R.i];
  if (q.m) {
    R.sel = R.sel.includes(idx) ? R.sel.filter(x => x !== idx) : [...R.sel, idx];
  } else {
    R.sel = [idx];
  }
  renderQ();
}

/* ---- REGISTRO Y CALIFICACIÓN DE RESPUESTAS ---- */
const grade = (q, sel) => {
  if (!sel || !sel.length) return false;
  const a = Array.isArray(q.a) ? q.a : [q.a];
  return sel.length === a.length && [...sel].sort().every((v, i) => v === [...a].sort()[i]);
};

function recordConceptAnswer(q, selIndices, isCorrect, src) {
  const concept = q.c;
  if (!S.conceptStats[concept]) {
    S.conceptStats[concept] = {
      concept,
      lvl: q.lvl,
      p: q.p,
      attempts: 0,
      errors: 0,
      correct: 0,
      correctStreak: 0,
      distinctCorrectQids: [],
      status: 'reinforce',
      lastTs: Date.now()
    };
  }
  const cs = S.conceptStats[concept];
  cs.attempts++;
  cs.lastTs = Date.now();

  if (isCorrect) {
    cs.correct++;
    cs.correctStreak++;
    if (!cs.distinctCorrectQids.includes(q.id)) {
      cs.distinctCorrectQids.push(q.id);
    }
    // Criterio de Dominio: al menos 2 preguntas distintas respondidas bien y racha >= 2
    if (cs.distinctCorrectQids.length >= 2 && cs.correctStreak >= 2) {
      cs.status = 'mastered';
    } else {
      cs.status = 'progress';
    }
  } else {
    cs.errors++;
    cs.correctStreak = 0;
    cs.status = 'reinforce';

    // Registro inmutable de error histórico
    const selTexts = selIndices.map(i => q.o[i]);
    const okTexts = q.a.map(i => q.o[i]);
    S.errHistory.unshift({
      id: 'err-' + Date.now() + '-' + Math.random().toString(36).substr(2, 4),
      qid: q.id,
      t: q.t,
      sel: selTexts,
      correct: okTexts,
      c: q.c,
      lvl: q.lvl,
      p: q.p,
      src: src || 'Quiz',
      ts: Date.now()
    });
    S.errHistory = S.errHistory.slice(0, 200);
  }
  save();
}

function checkAnswer() {
  const q = R.qs[R.i];
  const ok = grade(q, R.sel);
  R.lastOk = ok;
  R.checked = true;
  R.res.push({ q, sel: R.sel, ok });

  // Anti-farming: solo sumar 10 XP la primera vez que se responde bien
  if (ok && !S.ans[q.id]) {
    S.ans[q.id] = 1;
    S.xp += 10;
  }

  // Registrar evolución conceptual
  recordConceptAnswer(q, R.sel, ok, R.mode === 'quiz' ? `Quiz Nivel ${R.lvl}` : R.mode === 'recov' ? 'Recuperación' : 'Práctica');
  saveActiveSession();
  renderQ();
}

function nextQuizQ() {
  if (R.i + 1 < R.qs.length) {
    R.i++;
    R.sel = [];
    R.checked = false;
    saveActiveSession();
    renderQ();
    return;
  }

  // Fin del cuestionario
  clearActiveSession();
  const ok = R.res.filter(r => r.ok).length;
  const n = R.res.length;
  const pct = Math.round((ok * 100) / n);
  const key = `${R.lvl}-${R.part}`;
  let msg = '';
  const passedBlock = ok >= 3;

  if (R.mode === 'quiz') {
    if (passedBlock) {
      if (!S.parts[key]) {
        S.parts[key] = 1;
        S.xp += 25; // Recompensa de bloque acreditada 1 sola vez
        msg = '🎉 ¡Felicitaciones! Aprobaste este bloque de estudio (+25 XP acreditados).';
      } else {
        msg = '✔ Bloque repasado correctamente. (Los 25 XP ya habían sido ganados previamente).';
      }
    } else {
      msg = 'Alcanzaste ' + ok + ' de ' + n + ' respuestas. Necesitás al menos 3 correctas para completar el bloque.';
    }
  } else {
    msg = `Completaste tu sesión con ${ok} aciertos (${pct}%). Tu progreso se actualizó en «Mi evolución».`;
  }
  save();

  $('#qz').innerHTML = `
    <div class="card" style="text-align:center;padding:26px 18px">
      <h2>Resultado: ${ok}/${n} correctas (${pct}%)</h2>
      <p style="font-size:16px;margin:12px 0 20px">${msg}</p>
      
      <div class="row" style="justify-content:center;gap:12px">
        ${R.mode === 'quiz' && passedBlock && R.part < 2 ? `
          <button class="btn tq" onclick="go('lesson',{l:${R.lvl},p:${R.part + 1}})">
            Siguiente Bloque (${R.part + 2}) ➔
          </button>
        ` : ''}
        <button class="btn" onclick="go('${R.mode === 'quiz' ? 'level' : 'areas'}',${JSON.stringify(R.mode === 'quiz' ? { l: R.lvl } : {})})">
          Volver a ${R.mode === 'quiz' ? `Nivel ${R.lvl}` : 'Áreas de mejora'}
        </button>
        <button class="btn g" onclick="${R.mode === 'recov' ? `go('recov',{l:${R.lvl},p:${R.part},c:'${(R.targetConcept || '').replace(/'/g, "\\'")}'})` : R.mode === 'practice' ? `go('practice',{pMode:'${R.pMode}'})` : `go('lesson',{l:${R.lvl},p:${R.part}})`}">
          Reintentar preguntas
        </button>
      </div>
    </div>
  `;
}

function nextExamQ() {
  const q = R.qs[R.i];
  const ok = grade(q, R.sel);
  R.res.push({ q, sel: R.sel, ok });

  // Registrar respuesta en evolución
  recordConceptAnswer(q, R.sel, ok, `Examen Nivel ${R.lvl}`);

  if (R.i + 1 < R.qs.length) {
    R.i++;
    R.sel = [];
    R.checked = false;
    saveActiveSession();
    renderQ();
    return;
  }
  // Fin del examen
  clearActiveSession();
  finishExam();
}

function finishExam() {
  const ok = R.res.filter(r => r.ok).length;
  const n = R.res.length;
  const pct = Math.round((ok * 100) / n);
  const pass = pct >= PASS;
  const e = S.exams[R.lvl] || { best: 0, passed: false, bonus: false };
  let gain = 0;

  if (pass && !e.passed) {
    gain += 100; // 100 XP por aprobar por primera vez
    e.passed = true;
  }
  if (pct === 100 && !e.bonus) {
    gain += 50; // 50 XP por examen perfecto
    e.bonus = true;
  }
  e.best = Math.max(e.best, pct);
  e.source = 'Plataforma interactiva';
  S.exams[R.lvl] = e;
  S.xp += gain;

  const rec = {
    lvl: R.lvl,
    pct,
    ok,
    n,
    pass,
    gain,
    ts: Date.now(),
    source: 'Plataforma interactiva',
    res: R.res.map(r => ({ id: r.q.id, sel: r.sel, ok: r.ok, q: r.q }))
  };
  S.hist.unshift(rec);
  S.hist = S.hist.slice(0, 30);
  save();

  V = { n: 'results', rec };
  R = null;
  render();
  window.scrollTo(0, 0);
}

/* ---- VISTA: RESULTADOS DE EXAMEN E INFORME PARA CHATGPT ---- */
function generateChatGPTReport(rec) {
  const L = LEVELS[rec.lvl - 1];
  const bad = rec.res.filter(r => !r.ok);
  const weakConcepts = [...new Set(bad.map(b => b.q.c))];
  const masteredConcepts = [...new Set(rec.res.filter(r => r.ok).map(r => r.q.c))].filter(c => !weakConcepts.includes(c));

  // Comparación con intentos anteriores
  const prevAttempts = S.hist.filter(h => h.lvl === rec.lvl && h.ts < rec.ts);
  let evolutionText = 'Primer intento registrado en este nivel.';
  if (prevAttempts.length) {
    const last = prevAttempts[0];
    const diff = rec.pct - last.pct;
    evolutionText = `Intento actual: ${rec.pct}% vs. Intento anterior: ${last.pct}% (${diff >= 0 ? '+' : ''}${diff}%). Total intentos en este nivel: ${prevAttempts.length + 1}.`;
  }

  let badDetails = 'Ninguna. ¡Examen perfecto con 100% de aciertos!';
  if (bad.length) {
    badDetails = bad.map((b, i) => {
      const myAns = b.sel.length ? b.sel.map(x => '"' + b.q.o[x] + '"').join(' | ') : 'Sin respuesta';
      const okAns = b.q.a.map(x => '"' + b.q.o[x] + '"').join(' | ');
      return (i + 1) + '. Pregunta: "' + b.q.t + '"\\n' +
             '   Mi respuesta: ' + myAns + '\\n' +
             '   Respuesta correcta: ' + okAns + '\\n' +
             '   Concepto evaluado: ' + b.q.c + '\\n' +
             '   Fundamento del PDF: ' + b.q.e;
    }).join('\\n\\n');
  }

  const weakStr = weakConcepts.length ? weakConcepts.map(c => '• ' + c).join('\\n') : 'Ninguno. Todos los conceptos evaluados fueron respondidos con éxito.';
  const masteredStr = masteredConcepts.length ? masteredConcepts.map(c => '• ' + c).join('\\n') : 'Pendiente consolidar más conceptos.';
  const targetConcepts = weakConcepts.join(', ') || 'revisión general';
  const nextRec = rec.pass ? `¡Nivel ${L.id} aprobado! Avanzar al Nivel ${L.id + 1} (${LEVELS[L.id] ? LEVELS[L.id].name : 'Fin de programa'})` : `Repasar los conceptos pendientes de Nivel ${L.id} antes de repetir el examen final.`;

  return '=======================================================\\n' +
         'INFORME DE RENDIMIENTO ACADÉMICO — ACADEMIA DEL DINERO\\n' +
         'Documento base: "El dinero" (Bergara, Barretta, Pascale, Haedo)\\n' +
         '=======================================================\\n' +
         'Nivel evaluado: ' + L.id + '. ' + L.name + '\\n' +
         'Resultado: ' + rec.ok + '/' + rec.n + ' aciertos (' + rec.pct + '%) — ' + (rec.pass ? 'APROBADO' : 'NO APROBADO') + '\\n' +
         'Fecha de realización: ' + new Date(rec.ts).toLocaleString('es-UY') + '\\n' +
         'Evolución en este nivel: ' + evolutionText + '\\n\\n' +
         'PREGUNTAS INCORRECTAS:\\n' + badDetails + '\\n\\n' +
         'CONCEPTOS QUE NECESITO REFORZAR:\\n' + weakStr + '\\n\\n' +
         'CONCEPTOS DEMOSTRADOS COMO COMPRENDIDOS:\\n' + masteredStr + '\\n\\n' +
         'RECOMENDACIÓN DE ESTUDIO:\\n' + nextRec + '\\n\\n' +
         '-------------------------------------------------------\\n' +
         'PROMPT PARA ENVIAR A CHATGPT:\\n' +
         '"Hola ChatGPT. Estoy estudiando Economía con el texto oficial «El dinero».\\n' +
         'Acabo de rendir el examen del Nivel ' + L.id + ' (' + L.name + ') y te comparto arriba mi informe de errores.\\n\\n' +
         'Por favor, actúa como mi profesor particular de Economía y asísteme con las siguientes pautas:\\n' +
         '1. Explícame en lenguaje simple por qué la respuesta que elegí en cada fallo era incorrecta y cuál es el razonamiento exacto para llegar a la correcta.\\n' +
         '2. Profundiza exclusivamente en los conceptos que todavía me cuestan (' + targetConcepts + '), utilizando analogías claras y situaciones cotidianas uruguayas (pesos, cajeros Banred/RedBrou, depósitos en BROU, compras del día a día).\\n' +
         '3. NO repitas definiciones de conceptos que ya domino (' + (masteredConcepts.slice(0, 3).join(', ') || 'conceptos previos') + ').\\n' +
         '4. Plantéame 3 preguntas de práctica rápida sobre estos temas difíciles y espera a que yo te responda antes de darme las soluciones, para comprobar si finalmente lo entendí."\\n' +
         '-------------------------------------------------------';
}

function results() {
  const r = V.rec;
  const L = LEVELS[r.lvl - 1];
  const weak = [...new Set(r.res.filter(x => !x.ok).map(x => x.q.c))];
  const reportText = generateChatGPTReport(r);

  return `
    <h1>${r.pass ? '🎉 ¡Examen Aprobado!' : '💪 Todavía no alcanzó'}</h1>
    
    <div class="card highlight">
      <div class="row" style="justify-content:space-around;text-align:center">
        <div><b style="font-size:30px;color:${r.pass ? 'var(--ok)' : 'var(--bad)'}">${r.pct}%</b><br><span class="mu">Calificación</span></div>
        <div><b style="font-size:30px;color:var(--tq)">${r.ok}/${r.n}</b><br><span class="mu">Aciertos</span></div>
        <div><b style="font-size:30px;color:var(--vi)">+${r.gain}</b><br><span class="mu">XP Ganados</span></div>
      </div>
      <p class="mu" style="text-align:center;margin:12px 0 0;font-size:13.5px">
        Exigencia de aprobación: <b>${PASS}%</b> (mínimo 12 respuestas correctas de 15).
      </p>
      
      <div class="row" style="margin-top:16px;justify-content:center;gap:10px">
        ${r.pass && LEVELS[r.lvl] ? `
          <button class="btn tq" onclick="go('level',{l:${r.lvl + 1}})">
            Avanzar al Nivel ${r.lvl + 1}: ${LEVELS[r.lvl].name} ➔
          </button>
        ` : ''}
        <button class="btn g" onclick="go('home')">Ir al Mapa</button>
        <button class="btn g" onclick="go('level',{l:${L.id}})">Volver a Nivel ${L.id}</button>
        <button class="btn g" onclick="go('exam',{l:${L.id}})">Repetir Examen</button>
      </div>
    </div>

    ${weak.length ? `
    <div class="card err-card">
      <b>Conceptos que necesitás reforzar antes del próximo intento:</b>
      <ul style="margin:8px 0 12px;padding-left:22px">
        ${weak.map(c => `<li><b>${c}</b></li>`).join('')}
      </ul>
      <button class="btn tq" onclick="go('areas')">Ir a ejercitarlos en Áreas de Mejora ➔</button>
    </div>` : ''}

    <div class="card">
      <div class="row" style="justify-content:space-between">
        <h3>🤖 Analizar mis errores con ChatGPT</h3>
        <span class="tag">Tutoría Personalizada</span>
      </div>
      <p class="mu" style="font-size:14px;margin:6px 0 12px">
        Copiá este informe generado con tus errores y pegalo en ChatGPT para recibir una explicación adaptada a lo que no entendiste.
      </p>
      <textarea id="repBox" readonly>${reportText.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')}</textarea>
      
      <div class="row" style="margin-top:10px">
        <button class="btn tq" onclick="copyReportText()">📋 Copiar informe completo</button>
        <a class="btn g" target="_blank" rel="noopener" href="https://chatgpt.com">Abrir ChatGPT ↗</a>
      </div>
      <p id="cpyFeedback" class="ok-t" style="font-size:13px;margin-top:6px;font-weight:600"></p>
    </div>

    <h2>Revisión de preguntas del examen</h2>
    ${r.res.map((x, i) => {
      const q = x.q;
      const eg = getExampleForConcept(q.c);
      return `
        <div class="card" style="border-left:4px solid ${x.ok ? 'var(--ok)' : 'var(--bad)'}">
          <div class="row" style="justify-content:space-between">
            <b>${i + 1}. ${q.t}</b>
            <span class="${x.ok ? 'ok-t' : 'bad-t'}">${x.ok ? '✅ Correcta' : '❌ Incorrecta'}</span>
          </div>
          
          <p style="margin:8px 0 4px;font-size:14.5px">
            ${x.ok ? `<span class="ok-t">Tu respuesta:</span> ${x.sel.map(k => q.o[k]).join(' | ')}` : `<span class="bad-t">Tu respuesta:</span> ${x.sel.length ? x.sel.map(k => q.o[k]).join(' | ') : 'Sin respuesta'}`}
          </p>
          ${!x.ok ? `<p style="margin:2px 0 8px;font-size:14.5px"><b>Respuesta correcta:</b> <span class="ok-t">${q.a.map(k => q.o[k]).join(' | ')}</span></p>` : ''}
          
          <div class="exp-box ${x.ok ? '' : 'bad'}">
            ${!x.ok ? `
              <div class="exp-sec err">
                <b>1. Por qué tu respuesta no corresponde:</b><br>
                La alternativa elegida no coincide con las relaciones teóricas descriptas en el documento oficial.
              </div>
            ` : ''}
            <div class="exp-sec">
              <b>${x.ok ? '1.' : '2.'} Fundamento del PDF «El dinero»:</b><br>
              ${q.e}
            </div>
            <div class="exp-sec">
              <b>${x.ok ? '2.' : '3.'} Ejemplo cotidiano uruguayo:</b><br>
              ${eg}
            </div>
            <div class="exp-sec">
              <b>${x.ok ? '3.' : '4.'} Concepto evaluado:</b><br>
              <span class="tag">${q.c}</span> (Nivel ${q.lvl})
            </div>
          </div>
        </div>
      `;
    }).join('')}
  `;
}

function copyReportText() {
  const el = $('#repBox');
  el.select();
  let ok = false;
  try { ok = document.execCommand('copy'); } catch (e) {}
  try {
    if (navigator.clipboard) {
      navigator.clipboard.writeText(el.value);
      ok = true;
    }
  } catch (e) {}
  $('#cpyFeedback').textContent = ok ? '✔ ¡Informe copiado al portapapeles! Ya podés pegarlo en ChatGPT.' : 'Seleccioná el texto del cuadro y copialo con Ctrl+C.';
}

/* ---- VISTA: ÁREAS DE MEJORA, MI EVOLUCIÓN Y REPASOS ---- */
function areas() {
  const allConcepts = [...new Set(QID.map(q => q.c))];
  const stats = S.conceptStats || {};
  const history = S.errHistory || [];

  const weakConcepts = Object.keys(stats).filter(c => stats[c].status === 'reinforce');
  const progressConcepts = Object.keys(stats).filter(c => stats[c].status === 'progress');
  const masteredConcepts = Object.keys(stats).filter(c => stats[c].status === 'mastered');

  return `
    <button class="btn g" onclick="go('home')">← Volver al Mapa</button>
    <h1>🎯 Áreas de mejora y evolución</h1>
    <p class="mu">Seguimiento adaptativo de conceptos que te cuestan, repaso espaciado e historial de evolución.</p>

    <div class="card highlight">
      <div class="row" style="justify-content:space-between">
        <b>Estado de dominio conceptual:</b>
        <span class="tq-t"><b>${masteredConcepts.length} de ${allConcepts.length} dominados</b></span>
      </div>
      <div class="bar" style="margin:8px 0 14px"><i style="width:${Math.round((masteredConcepts.length * 100) / allConcepts.length)}%"></i></div>
      
      <div class="row">
        <div class="stat"><b>${weakConcepts.length}</b>En refuerzo</div>
        <div class="stat"><b>${progressConcepts.length}</b>En progreso</div>
        <div class="stat"><b>${masteredConcepts.length}</b>Dominados</div>
      </div>
    </div>

    <!-- Pestañas secundarias -->
    <div class="subtabs">
      <button class="subtab ${activeSubtab === 'weak' ? 'on' : ''}" onclick="activeSubtab='weak';render()">🎯 Conceptos a Reforzar (${weakConcepts.length})</button>
      <button class="subtab ${activeSubtab === 'evolution' ? 'on' : ''}" onclick="activeSubtab='evolution';render()">📈 Mi Evolución</button>
      <button class="subtab ${activeSubtab === 'practice' ? 'on' : ''}" onclick="activeSubtab='practice';render()">⚡ Práctica Inteligente</button>
      <button class="subtab ${activeSubtab === 'history' ? 'on' : ''}" onclick="activeSubtab='history';render()">📜 Historial de Errores (${history.length})</button>
    </div>

    ${activeSubtab === 'weak' ? renderWeakConceptsTab(weakConcepts, stats) :
      activeSubtab === 'evolution' ? renderEvolutionTab(stats, allConcepts) :
      activeSubtab === 'practice' ? renderPracticeTab() :
      renderHistoryTab(history)}
  `;
}

function renderWeakConceptsTab(weakConcepts, stats) {
  return `
    <h2>Conceptos que necesitás reforzar (${weakConcepts.length})</h2>
    ${weakConcepts.length ? weakConcepts.map(c => {
      const item = stats[c];
      return `
        <div class="card err-card">
          <div class="row" style="justify-content:space-between">
            <b>${c}</b>
            <span class="badge reinforce">${item.errors || 1} fallo(s) históricos</span>
          </div>
          <p class="mu" style="font-size:13.5px;margin:6px 0 10px">
            Ubicación: Nivel ${item.lvl}, Bloque ${(item.p || 0) + 1} · Racha actual: ${item.correctStreak || 0} aciertos (se requieren 2 para dominarlo)
          </p>
          <button class="btn tq" onclick="go('recov',{l:${item.lvl},p:${item.p || 0},c:'${c.replace(/'/g, "\\'")}'})">
            🎯 Practicar y dominar este concepto
          </button>
        </div>
      `;
    }).join('') : `
      <div class="card" style="border-left:4px solid var(--ok);text-align:center;padding:24px">
        <b>🎉 ¡Excelente! No tenés conceptos pendientes en estado de refuerzo.</b>
        <p class="mu" style="font-size:14px;margin-top:6px">Todos los conceptos evaluados están en progreso o dominados.</p>
        <button class="btn tq" style="margin-top:10px" onclick="go('level',{l:3})">Ir al Nivel 3 ➔</button>
      </div>
    `}
  `;
}

function renderEvolutionTab(stats, allConcepts) {
  const keys = Object.keys(stats);
  return `
    <h2>Mi evolución conceptual</h2>
    <p class="mu">Para considerar un concepto <b>Dominado</b> debés responder correctamente al menos 2 preguntas distintas en ese concepto con racha positiva.</p>
    
    ${keys.length ? keys.map(c => {
      const item = stats[c];
      const isM = item.status === 'mastered';
      const isP = item.status === 'progress';
      const badgeCls = isM ? 'done' : isP ? 'progress' : 'reinforce';
      const badgeTxt = isM ? '🟢 Dominado' : isP ? '🟡 En progreso' : '🔴 Requiere refuerzo';
      return `
        <div class="card" style="display:flex;justify-content:space-between;align-items:center">
          <div>
            <b>${c}</b>
            <div class="mu" style="font-size:13px;margin-top:4px">
              Fallos: ${item.errors} · Aciertos distintos: ${item.distinctCorrectQids ? item.distinctCorrectQids.length : 0} · Racha actual: ${item.correctStreak}
            </div>
          </div>
          <span class="badge ${badgeCls}">${badgeTxt}</span>
        </div>
      `;
    }).join('') : '<div class="card mu">Aún no hay estadísticas acumuladas.</div>'}
  `;
}

function renderPracticeTab() {
  return `
    <h2>Práctica espaciada inteligente</h2>
    <p class="mu">Entrená los contenidos ya aprobados (Niveles 1 y 2). Ninguna pregunta de niveles bloqueados aparecerá acá.</p>

    <div class="card" style="border-left:4px solid var(--tq)">
      <b>⚡ Repaso rápido</b>
      <p class="mu" style="font-size:13.5px;margin:4px 0 12px">5 preguntas aleatorias de los Niveles 1 y 2 para mantener la memoria fresca.</p>
      <button class="btn tq" onclick="go('practice',{pMode:'quick',title:'Repaso Rápido'})">Iniciar Repaso Rápido</button>
    </div>

    <div class="card" style="border-left:4px solid var(--ac)">
      <b>🎯 Mis errores</b>
      <p class="mu" style="font-size:13.5px;margin:4px 0 12px">5 ejercicios focalizados en los conceptos donde tuviste errores recientes.</p>
      <button class="btn" style="background:linear-gradient(135deg,var(--ac),#d97706)" onclick="go('practice',{pMode:'weak',title:'Práctica de Mis Errores'})">Practicar Mis Errores</button>
    </div>

    <div class="card" style="border-left:4px solid var(--vi)">
      <b>🏆 Desafío mixto</b>
      <p class="mu" style="font-size:13.5px;margin:4px 0 12px">10 preguntas variadas con ejercicios de cálculo y situaciones reales de los niveles superados.</p>
      <button class="btn" onclick="go('practice',{pMode:'challenge',title:'Desafío Mixto'})">Comenzar Desafío Mixto</button>
    </div>
  `;
}

function renderHistoryTab(history) {
  return `
    <h2>Historial cronológico de errores (${history.length})</h2>
    <p class="mu">Este registro es permanente y no se borra cuando aprendés un concepto, para que veas cuánto has progresado.</p>

    ${history.length ? history.map((e, idx) => `
      <div class="card" style="border-left:4px solid var(--bad)">
        <div class="row" style="justify-content:space-between">
          <span class="tag x">${e.src || 'Evaluación'}</span>
          <span class="mu" style="font-size:12.5px">${new Date(e.ts).toLocaleString('es-UY')}</span>
        </div>
        <b style="display:block;margin:6px 0;font-size:15px">${e.t}</b>
        <p style="font-size:13.5px;margin:4px 0"><span class="bad-t">Tu respuesta:</span> ${Array.isArray(e.sel) ? e.sel.join(' | ') : e.sel}</p>
        <p style="font-size:13.5px;margin:2px 0"><span class="ok-t">Respuesta correcta:</span> ${Array.isArray(e.correct) ? e.correct.join(' | ') : e.correct}</p>
        <span class="mu" style="font-size:12px;margin-top:4px;display:inline-block">Concepto: <b>${e.c}</b> (Nivel ${e.lvl})</span>
      </div>
    `).join('') : '<div class="card mu">No tenés errores registrados en el historial.</div>'}
  `;
}

/* ---- VISTA: HISTORIAL DE EVALUACIONES ---- */
function hist() {
  return `
    <button class="btn g" onclick="go('home')">← Volver al Mapa</button>
    <h1>📜 Historial de Evaluaciones</h1>
    <p class="mu">Registro de exámenes finales rendidos y evaluaciones diagnósticas externas.</p>

    ${S.hist.length ? S.hist.map(h => `
      <div class="card">
        <div class="row" style="justify-content:space-between">
          <div>
            <b>Nivel ${h.lvl}: ${LEVELS[h.lvl - 1].name}</b>
            <div class="mu" style="font-size:13px">${new Date(h.ts).toLocaleString('es-UY')} · <span class="tag">${h.source || 'Plataforma'}</span></div>
          </div>
          <span class="badge ${h.pass ? 'done' : 'lock'}">${h.pct}% ${h.pass ? 'Aprobado' : 'No alcanzado'}</span>
        </div>
        <div class="bar" style="margin:10px 0 8px"><i style="width:${h.pct}%"></i></div>
        <div class="row" style="justify-content:space-between;align-items:center;margin-top:6px">
          <span class="mu" style="font-size:13px">${h.ok} aciertos de ${h.n} preguntas</span>
          ${h.res && h.res.length ? `
            <button class="btn g" style="padding:6px 12px;font-size:13px" onclick="V={n:'results',rec:S.hist[${S.hist.indexOf(h)}]};render();">
              Ver corrección
            </button>
          ` : '<span class="mu" style="font-size:12.5px">Registro externo verificado</span>'}
        </div>
      </div>
    `).join('') : '<div class="card mu">Aún no has rendido exámenes finales.</div>'}
  `;
}

/* ---- VISTA: AJUSTES Y GESTIÓN DE DATOS ---- */
function cfg() {
  return `
    <button class="btn g" onclick="go('home')">← Volver al Mapa</button>
    <h1>⚙️ Configuración y Progreso</h1>

    <div class="card highlight">
      <div class="row" style="justify-content:space-between">
        <b>Puntos de Experiencia (XP):</b>
        <span class="tq-t" style="font-size:22px"><b>${S.xp} XP</b></span>
      </div>
      <p class="mu" style="font-size:13.5px;margin-top:6px">
        Incluye 610 XP legítimos acumulados por la aprobación completa de los Niveles 1 y 2 (quizzes, exámenes finales y recuperación verificada).
      </p>
    </div>

    <div class="card">
      <h3>📥 Exportar Progreso</h3>
      <p class="mu" style="font-size:14px">Descargá tu progreso como archivo JSON para guardarlo en tu computadora o transferirlo a tu celular.</p>
      <div class="row" style="margin-bottom:12px">
        <button class="btn tq" onclick="downloadProgressFile()">📥 Descargar archivo JSON</button>
        <button class="btn g" onclick="copyProgressText()">📋 Copiar JSON al portapapeles</button>
      </div>
      <textarea id="expTxt" readonly>${JSON.stringify(S, null, 2).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')}</textarea>
      <span id="expMsg" class="ok-t" style="font-size:13px;font-weight:600"></span>
    </div>

    <div class="card">
      <h3>📤 Importar Progreso</h3>
      <p class="mu" style="font-size:14px">Cargá tu archivo JSON de respaldo o pegá el texto para restaurar todo tu avance.</p>
      <div style="margin-bottom:12px">
        <input type="file" id="filePicker" accept=".json" style="display:none" onchange="handleFileUpload(event)">
        <button class="btn g" onclick="$('#filePicker').click()">📁 Seleccionar archivo JSON...</button>
      </div>
      <textarea id="impTxt" placeholder="Pegá acá el texto JSON de tu progreso exportado..."></textarea>
      <div style="margin-top:10px">
        <button class="btn tq" onclick="importProgressFromText()">Restaurar Progreso</button>
        <span id="impMsg" style="font-size:13px;font-weight:600;margin-left:8px"></span>
      </div>
    </div>

    <div class="card" style="border-color:#4c1325">
      <h3 class="bad-t">Restaurar Copia de Seguridad</h3>
      <p class="mu" style="font-size:14px">Restaura la copia de seguridad previa que el sistema creó automáticamente antes de la última migración.</p>
      <button class="btn g" onclick="restoreBackupCopy()">Restaurar Copia Previa</button>
    </div>
  `;
}

function downloadProgressFile() {
  const data = JSON.stringify(S, null, 2);
  const blob = new Blob([data], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `progreso_academia_del_dinero_${new Date().toISOString().slice(0, 10)}.json`;
  a.click();
  URL.revokeObjectURL(url);
  $('#expMsg').textContent = '✔ Archivo JSON descargado exitosamente.';
}

function copyProgressText() {
  const t = $('#expTxt');
  t.select();
  let ok = false;
  try { ok = document.execCommand('copy'); } catch (e) {}
  try { if (navigator.clipboard) { navigator.clipboard.writeText(t.value); ok = true; } } catch (e) {}
  $('#expMsg').textContent = ok ? '✔ ¡JSON copiado al portapapeles!' : 'Copiá manualmente el texto del cuadro.';
}

function handleFileUpload(ev) {
  const file = ev.target.files && ev.target.files[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = e => {
    try {
      const d = JSON.parse(e.target.result);
      applyImportData(d);
    } catch (err) {
      $('#impMsg').className = 'bad-t';
      $('#impMsg').textContent = 'Error: el archivo no contiene un JSON válido.';
    }
  };
  reader.readAsText(file);
}

function importProgressFromText() {
  try {
    const val = $('#impTxt').value.trim();
    if (!val) throw new Error();
    const d = JSON.parse(val);
    applyImportData(d);
  } catch (err) {
    $('#impMsg').className = 'bad-t';
    $('#impMsg').textContent = 'Error: formato JSON inválido.';
  }
}

function applyImportData(d) {
  if (typeof d.xp !== 'number' || !d.parts) {
    $('#impMsg').className = 'bad-t';
    $('#impMsg').textContent = 'Estructura de progreso no válida.';
    return;
  }
  S = d;
  save();
  $('#impMsg').className = 'ok-t';
  $('#impMsg').textContent = '✔ ¡Progreso restaurado correctamente!';
  setTimeout(() => go('home'), 700);
}

function restoreBackupCopy() {
  try {
    const b = localStorage.getItem(KEY + '-backup');
    if (!b) {
      alert('No se encontró una copia de seguridad previa en este navegador.');
      return;
    }
    if (confirm('¿Deseás restaurar los datos guardados en la copia de seguridad previa?')) {
      S = JSON.parse(b);
      save();
      alert('Copia de seguridad restaurada.');
      go('home');
    }
  } catch (e) {
    alert('Error al restaurar copia.');
  }
}

/* ================= ACCESIBILIDAD POR TECLADO ================= */
window.addEventListener('keydown', e => {
  if (e.target.tagName === 'TEXTAREA' || e.target.tagName === 'INPUT') return;
  if (R && $('#qz')) {
    if (['1', '2', '3', '4'].includes(e.key)) {
      const idx = parseInt(e.key, 10) - 1;
      const btns = document.querySelectorAll('#qz .opt');
      if (btns[idx]) pickOpt(idx);
    } else if (e.key === 'Enter' || e.key === ' ') {
      const btn = document.querySelector('#qz .btn.tq');
      if (btn && !btn.disabled) {
        e.preventDefault();
        btn.click();
      }
    }
  }
  if (e.key === 'Escape') {
    if (document.body.classList.contains('focus-mode')) {
      toggleFocusMode();
    }
  }
});

/* ================= INICIALIZACIÓN ================= */
load();
render();
</script>
</body>
</html>
"""
    html = template.replace("/* __LEVELS_DATA__ */", levels_json)
    html = html.replace("/* __EXTRA_DATA__ */", extra_json)
    return html

def main():
    print("Construyendo Academia del Dinero v2.0...")
    content = build_html()
    
    path_estudiar = os.path.join(r"c:\Users\Usuario\Downloads\estudiar", "Academia del Dinero.html")
    path_downloads = os.path.join(r"c:\Users\Usuario\Downloads", "Academia del Dinero.html")
    
    with open(path_estudiar, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Guardado exitosamente en: {path_estudiar} ({len(content)} bytes)")
    
    with open(path_downloads, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Guardado exitosamente en: {path_downloads} ({len(content)} bytes)")

if __name__ == "__main__":
    main()
