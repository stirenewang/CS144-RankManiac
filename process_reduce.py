#!/usr/bin/env python

import sys
import numpy as np
import heapq
from operator import itemgetter

lines = []
iteration = 0
converged = True
currpr = []
prevpr = []

for line in sys.stdin:
    lines.append(line)
    line_tab = line.strip().split('\t')
    line_info = line_tab[1].split(',')

    if line_tab[0] == "i":
        iteration = int(line_tab[1])
    else:
        node_id = line_tab[0]
        
        pr = map(float, line_info[:2])
        # change = abs(pr[0] - pr[1])

        # if change > tolerance:
        #     converged = False

        currpr.append((node_id, pr[0]))
        prevpr.append((node_id, pr[0]))

top_curr = heapq.nlargest(30, currpr, key=itemgetter(1))
top_prev = heapq.nlargest(30, prevpr, key=itemgetter(1))
print top_curr
print top_prev
for i in range(30):
    if top_curr[i][0] != top_prev[i][0]:
        converged = False
        break

if iteration == 49 or converged:
    top = top_curr[:20]

    for tup in top:
        sys.stdout.write('FinalRank:' + str(tup[1]) + '\t' + tup[0] + '\n')
else:
    sys.stdout.write('i' + '\t' + str(iteration + 1) + '\n')

    for lin in lines:
        if not lin.startswith('i'):
            sys.stdout.write('NodeId:' + lin)