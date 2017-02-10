#!/usr/bin/env python

import sys

'''
line looks like this:
NodeId:{node_id}\t{curr_pr},{prev_pr},{outlinks}\n
'''

for line in sys.stdin:
    line_tab = line.strip().split('\t')

    if line_tab[0] == 'i' or line_tab[0] == 'c':  # if line has iteration/counter data
        sys.stdout.write(line)
    else:  # if line has pagerank data
        line_info = line_tab[1].split(',')
        node_id = line_tab[0][7:]
        
        if len(line_info) > 2:  # if node has outlinks
            outlinks = line_info[2:]
            curr_pr = float(line_info[0])
            value = str(curr_pr / len(outlinks))

            for link in outlinks:
                sys.stdout.write('%s\t%s\n' % (link, value))

            sys.stdout.write('%s\t0\n' % node_id)
        else:  # if node doesn't have outlinks
            sys.stdout.write('%s\t1\n' % node_id)

        sys.stdout.write('%s\tp,%s\n' % (node_id, line_tab[1]))