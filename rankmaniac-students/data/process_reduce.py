#!/usr/bin/env python

import sys
import numpy as np
import heapq
from operator import itemgetter

tuples = []
lines = []
iteration = 0
tolerance = 0.001
converged = True

for line in sys.stdin:
    lines.append(line)
    line_tab = line.strip().split('\t')
    line_info = line_tab[1].split(',')

    if line_tab[0] == "i":
        iteration = int(line_tab[1])
    else:
        node_id = line_tab[0]
        
        pr = map(float, line_info[:2])
        change = abs(pr[0] - pr[1])

        if change > tolerance:
            converged = False

        tuples.append((node_id, pr[0]))

if iteration == 49 or converged:
    top = heapq.nlargest(20, tuples, key=itemgetter(1))

    for tup in top:
        sys.stdout.write('FinalRank:' + tup[0] + '\t' + str(tup[1]) + '\n')
else:
    sys.stdout.write('i' + '\t' + str(iteration + 1) + '\n')

    for lin in lines:
        if not lin.startswith('i'):
            sys.stdout.write('NodeId:' + lin)