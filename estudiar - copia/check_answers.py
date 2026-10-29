# -*- coding: utf-8 -*-
import sys, os, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import data_l1, data_l2, data_l3, data_l4, data_l5, data_l6, data_l7, data_l8, data_l9
levels = [data_l1.L1, data_l2.L2, data_l3.L3, data_l4.L4, data_l5.L5, data_l6.L6, data_l7.L7, data_l8.L8, data_l9.L9]
non_zero = 0
total = 0
for l in levels:
    for p in l['parts']:
        for q in p['quiz']:
            total += 1
            if q['a'] != [0]:
                non_zero += 1
                print("Level %d quiz a=%s t=%s" % (l["id"], q["a"], q["t"][:60]))
    for q in l['exam']:
        total += 1
        if q['a'] != [0]:
            non_zero += 1
            print("Level %d exam a=%s t=%s" % (l["id"], q["a"], q["t"][:60]))
print("\nTotal questions: %d, non-zero answers: %d" % (total, non_zero))
