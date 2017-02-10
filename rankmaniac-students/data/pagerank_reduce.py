#!/usr/bin/env python

import sys

alpha = 0.85

# key: node_id (str)
# value: pagerank contribution (float)
pr_conts = {}

# key: node_id (str)
# value: [curr_pr (str), prev_pr (str), outlinks (str)]
graph_info = {}

'''
line looks like one of these:
i\t{iteration}\n
c\t{counter}\n
{node_id}\t{pagerank contribution}\n
{node_id}\tp,{curr_pr},{prev_pr},{outlinks}\n
'''

for line in sys.stdin:
    line_tab = line.split('\t')

    if line_tab[0] == "i" or line_tab[0] == 'c':  # if line has iteration/counter
        sys.stdout.write(line)
    else:
        line_info = line_tab[1].strip().split(',', 3) 
        node_id = line_tab[0]

        if line_info[0] != 'p':  # if line has pagerank contribution, adds to pr_cont
            pr_cont = float(line_info[0])
            try:
                pr_conts[node_id] += pr_cont
            except KeyError:
                pr_conts[node_id] = pr_cont
        else: # if line contains p, adds to graph_info
            graph_info[node_id] = line_info[1:]

for n_id in pr_conts.keys():
    curr_pr = str(alpha * pr_conts[n_id] + 1.0 - alpha)  # calculates new pagerank
    prev_pr = graph_info[n_id][0]

    if len(graph_data[n_id]) > 2:  # if node has outlinks
        outlinks = graph_info[n_id][2:]
        outlinks = ','.join(outlinks)
        sys.stdout.write('%s\t%s,%s,%s\n' % (n_id, curr_pr, prev_pr, outlinks))
    else:
        sys.stdout.write('%s\t%s,%s\n' % (n_id, curr_pr, prev_pr))