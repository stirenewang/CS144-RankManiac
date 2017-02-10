#!/usr/bin/env python

import sys

alpha = 0.85        # page rank calculate

# Dictionary of node page ranks on this iteration
node_pr = {}        # key: nodeID (string)
                    # value: contribution (float)

# Dictionary of graph information (pline), indicated by 'p' before data
# pline are lines that look like 'p',curr_pr,prev_pr, outlinks.....
graph_data = {}     # key: nodeID (string)
                    # value: [curr_pr (str), prev_pr (str), outlinks (str)]


for line in sys.stdin:
    line_tab = line.split('\t')     # Separate line into node_id and info (contribution or pline)

    if line_tab[0] == "i" or line_tab[0] == 'c':    # if line describes iteration or convergence counter
        sys.stdout.write(line)
    else:
        line_info = line_tab[1].strip().split(',', 3)   # get contribution/pline
        node_id = line_tab[0]                           # get node ID (string)

        if line_info[0] != 'p':                     # If line describes contribution to page rank
            cont = float(line_info[0])              # get contribution
            try:                                    # add contribution to dictionary of node's pagerank
                node_pr[node_id] += cont
            except KeyError:
                node_pr[node_id] = cont
        else:                                       # If line is pline
            graph_data[node_id] = line_info[1:]     # Store to pline dictionary (get rid of 'p')

for n_id in node_pr.keys():                         # Iterate through nodes in pagerank dictionary
    curr_pr = str(alpha*node_pr[n_id]+1.0-alpha)    # Calculate new page rank
    prev_pr = graph_data[n_id][0]                   # Get last 'curr_pr' from pline

    if len(graph_data[n_id]) > 2:                   # If this node has outlinks, print outlinks
        outlinks = graph_data[n_id][2]              # Get string of outlinks
        sys.stdout.write('%s\t%s,%s,%s\n' %(n_id, curr_pr, prev_pr, outlinks))
    else:                                           # Otherwise don't print outlinks
        sys.stdout.write('%s\t%s,%s\n' %(n_id, curr_pr, prev_pr))