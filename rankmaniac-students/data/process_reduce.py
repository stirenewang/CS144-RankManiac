#!/usr/bin/env python
import sys
tuples = []
iteration = 0
lines = []
for line in sys.stdin:
    if len(sys.argv) == 2 and int(sys.argv[1]) == 50:
            iteration = 50
    else:
        iteration = 0
    #if line[0] == 'i': # READ ITERATION HERE; this will only be on last file
    #    iteration = int(line[1]) + 1

    lines.append(line)
    line_tab = line.split('\t')
    line_info = line_tab[1].split(',')

    node_id = int(line_tab[0])
    pr = float(line_info[0])

    tuples.append((node_id, pr))

sorted_tuples = sorted(tuples, key=lambda x: x[1])
sorted_tuples = sorted_tuples[::-1]

if iteration == 50:
    for i in range(20):
        sys.stdout.write('FinalRank:' + str(sorted_tuples[i][1]) + '\t' + str(sorted_tuples[i][0]) + '\n')
else:
    #sys.stdout.write('i' + str(iteration + 1) + '\n')
    for i in range(len(lines)):
        sys.stdout.write('NodeId:' + lines[i])
