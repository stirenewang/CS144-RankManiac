#!/usr/bin/env python

import sys
import heapq
from operator import itemgetter



lines = []
iteration = 0
counter = 0
converged = True
curr_pr = []
prev_pr = []

'''
line looks like one of these:
i\t{iteration}\n
c\t{counter}\n
{node_id}\t{curr_pr},{prev_pr},{outlinks}\n
'''

for line in sys.stdin:
    lines.append(line)
    line_tab = line.strip().split('\t')

    if line_tab[0] == 'i':  # if line has iteration data
        iteration = int(line_tab[1])
    elif line_tab[0] == 'c':  # if line has counter data
        counter = int(line_tab[1])
    else: # line has pagerank data
        line_info = line_tab[1].split(',')
        node_id = line_tab[0]
        
        pr = map(float, line_info[:2])
        curr_pr.append((node_id, pr[0]))
        prev_pr.append((node_id, pr[1]))

# gets nodes with top 30 prev and curr pageranks
top_prev = heapq.nlargest(30, prev_pr, key=itemgetter(1))
top_curr = heapq.nlargest(30, curr_pr, key=itemgetter(1))

# check for convergence, or up counter
i  = 0

while i < len(top_curr) and converged:
    if top_curr[i][0] != top_prev[i][0]:
        counter = 0
        converged = False

    i += 1

if converged == True:
    counter += 1

if iteration == 49 or counter == 2:  # if converged
    top = top_curr[:20]

    for tup in top:
        sys.stdout.write('FinalRank:%s\t%s\n' % (str(tup[1]), tup[0]))
else:
    sys.stdout.write('i\t%s\n' % str(iteration + 1))
    sys.stdout.write('c\t%s\n' % str(counter))

    new_lines = [x for x in lines if not x.startswith('i') and not x.startswith('c')]

    for lin in new_lines:
        sys.stdout.write('NodeId:%s' % lin)