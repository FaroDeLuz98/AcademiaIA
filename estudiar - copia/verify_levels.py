# -*- coding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import data_l1, data_l2, data_l3, data_l4, data_l5, data_l6, data_l7, data_l8, data_l9

levels = [
    data_l1.L1, data_l2.L2, data_l3.L3, data_l4.L4, data_l5.L5,
    data_l6.L6, data_l7.L7, data_l8.L8, data_l9.L9
]

total_quiz = 0
total_exam = 0
all_concepts = set()

for lvl in levels:
    print(f"Nivel {lvl['id']}: {lvl['name']} ({lvl['icon']})")
    assert len(lvl['parts']) == 3, f"Nivel {lvl['id']} must have 3 parts"
    for pi, p in enumerate(lvl['parts']):
        assert len(p['quiz']) == 5, f"Nivel {lvl['id']} part {pi} must have 5 questions"
        total_quiz += len(p['quiz'])
        for q in p['quiz']:
            all_concepts.add(q['c'])
            assert len(q['o']) >= 2, f"Question options < 2: {q['t']}"
            assert all(0 <= a < len(q['o']) for a in q['a']), f"Invalid answer index in: {q['t']}"
            assert q['c'], f"Missing concept in: {q['t']}"
            assert q['e'], f"Missing explanation in: {q['t']}"
            
    assert len(lvl['exam']) >= 15, f"Nivel {lvl['id']} exam must have at least 15 questions"
    total_exam += len(lvl['exam'])
    for q in lvl['exam']:
        all_concepts.add(q['c'])
        assert len(q['o']) >= 2, f"Exam question options < 2: {q['t']}"
        assert all(0 <= a < len(q['o']) for a in q['a']), f"Invalid exam answer index in: {q['t']}"
        assert q['c'], f"Missing concept in exam: {q['t']}"
        assert q['e'], f"Missing explanation in exam: {q['t']}"

print("========================================")
print(f"VERIFICACIÓN EXITOSA:")
print(f"Total niveles: {len(levels)}")
print(f"Total preguntas de quiz: {total_quiz}")
print(f"Total preguntas de examen: {total_exam}")
print(f"Total general de preguntas: {total_quiz + total_exam}")
print(f"Total de conceptos únicos cubiertos: {len(all_concepts)}")
print("========================================")
