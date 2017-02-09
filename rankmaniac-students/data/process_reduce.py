#!/usr/bin/env python

import sys
import heapq
from operator import itemgetter

lines = []
iteration = 0
converged = True
curr_pr = []
prev_pr = []

for line in sys.stdin:
    lines.append(line)
    line_tab = line.strip().split('\t')
    line_info = line_tab[1].split(',')

    if line_tab[0] == "i":
        iteration = int(line_tab[1])
    else:
        node_id = line_tab[0]
        
        pr = map(float, line_info[:2])

        curr_pr.append((node_id, pr[0]))
        prev_pr.append((node_id, pr[0]))

top_curr = heapq.nlargest(30, currpr, key=itemgetter(1))
top_prev = heapq.nlargest(30, prevpr, key=itemgetter(1))

for i in range(len(top_curr)):
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