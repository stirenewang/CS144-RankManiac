#!/usr/bin/env python

import sys
import heapq
from operator import itemgetter

lines = []
iteration = 0
converged = True
counter = 0
curr_pr = []
prev_pr = []

for line in sys.stdin:
    lines.append(line)
    line_tab = line.strip().split('\t')
    line_info = line_tab[1].split(',')

    if line_tab[0] == "i":
        iteration = int(line_tab[1])
    elif line_tab[0] == 'c':
        counter = int(line_tab[1])
    else:
        node_id = line_tab[0]
        
        pr = map(float, line_info[:2])

        curr_pr.append((node_id, pr[0]))
        prev_pr.append((node_id, pr[1]))

top_curr = heapq.nlargest(30, curr_pr, key=itemgetter(1))
top_prev = heapq.nlargest(30, prev_pr, key=itemgetter(1))

for i in range(len(top_curr)):
    if top_curr[i][0] != top_prev[i][0]:
        counter = 0
        converged = False
        break
if converged == True:
    counter += 1

if iteration == 49 or counter == 3:
    top = top_curr[:20]

    for tup in top:
        sys.stdout.write('FinalRank:' + str(tup[1]) + '\t' + tup[0] + '\n')
else:
    sys.stdout.write('i' + '\t' + str(iteration + 1) + '\n')
    sys.stdout.write('c' + '\t' + str(counter) + '\n')

    for lin in lines:
        if not lin.startswith('i') and not lin.startswith('c'):
            sys.stdout.write('NodeId:' + lin)