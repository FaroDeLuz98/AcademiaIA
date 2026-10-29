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

for l in levels:
    q_count = sum(len(p['quiz']) for p in l['parts'])
    e_count = len(l['exam'])
    total_quiz += q_count
    total_exam += e_count
    for p in l['parts']:
        for q in p['quiz']:
            all_concepts.add(q['c'])
    for q in l['exam']:
        all_concepts.add(q['c'])
    print(f"Nivel {l['id']}: {l['name']} -> {q_count} quiz + {e_count} exam = {q_count + e_count} preguntas")

print(f"\nTotal: {total_quiz} quiz + {total_exam} exam = {total_quiz + total_exam} preguntas")
print(f"Conceptos únicos: {len(all_concepts)}")
