#!/usr/bin/env python

import sys

tuples = []
lines = []
iteration = 0
tolerance = 0.00001
converged = True

for line in sys.stdin:
    #if len(sys.argv) == 2 and int(sys.argv[1]) == 50:
    #        iteration = 50
    #else:
    #    iteration = 0

    lines.append(line)
    line_tab = line.split('\t')
    line_info = line_tab[1].split(',')

    if line_tab[0] == "i": # first line
        iteration = int(line_tab[1]) 
    else:
        node_id = int(line_tab[0])
        
        # Check for convergence: 
        # check prev_pr and curr_pr changes. If they are 
        # greater than the tolerance, there is no convergence
        curr_pr = float(line_info[0])
        prev_pr = float(line_info[1])

        change = abs(curr_pr - prev_pr)
        if change > tolerance:
            converged = False
        tuples.append((node_id, curr_pr))

sorted_tuples = sorted(tuples, key=lambda x: x[1])
sorted_tuples = sorted_tuples[::-1]

if iteration == 50 or converged:
    for i in range(20):
        sys.stdout.write('FinalRank:' + str(sorted_tuples[i][1]) + '\t' + str(sorted_tuples[i][0]) + '\n')
else:
    sys.stdout.write("i" + "\t" + str(iteration + 1) + "\n")
    for i in range(len(lines)):
        # don't concatenate iteration
        if not lines[i].startswith('i'):            
            #print node IDs
            sys.stdout.write('NodeId:' + lines[i])
