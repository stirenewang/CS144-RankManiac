#!/usr/bin/env python

import sys

alpha = 0.85        # page rank calculate

# Dictionary of node page ranks on this iteration
node_pr = {}        # key: nodeID (string)
                    # value: contribution (float)

# Dictionary of graph information (pline), indicated by 'p' before data
# pline are lines that look like 'p',curr_pr,prev_pr, outlinks.....
graph_data = {}     # key: nodeID (string)
                    # value: [pline = curr_pr (str), prev_pr (str), outlinks (str)]


for line in sys.stdin:
    line_tab = line.split('\t')         # get tab separated parts of line: node_id and info (contribution/pline)

    if line_tab[0] == "i" or line_tab[0] == 'c':    # if line tells iteration or convergence counter
        sys.stdout.write(line)
    else:
        line_info = line_tab[1].strip().split(',', 3)          # get contribution/pline
        node_id = line_tab[0]                       # get node ID as string

        if line_info[0] != 'p':                     # if not pline
            cont = float(line_info[0])              # get contribution
            try:                                    # add contribution to dictionary of node's pagerank
                node_pr[node_id] += cont
            except KeyError:
                node_pr[node_id] = cont
        else:                                       # if line is pline
            graph_data[node_id] = line_info[1:]     # store to pline dictionary (get rid of 'p')

for n_id in node_pr.keys():                         # iterate through nodes in pagerank dictionary
    curr_pr = str(alpha*node_pr[n_id]+1.0-alpha)                    # get new page rank
    prev_pr = graph_data[n_id][0]                   # get last 'curr_pr' from pline

    if len(graph_data[n_id]) > 2:                  # if this node has outlinks, print outlinks
        outlinks = graph_data[n_id][2]       # get comma separated outlinks (without curr_pr, prev_pr)
        sys.stdout.write('%s\t%s,%s,%s\n' %(n_id, curr_pr, prev_pr, outlinks))
    else:
        sys.stdout.write('%s\t%s,%s\n' %(n_id, curr_pr, prev_pr))



            # if len(line_info) > 3: 
            #     outlinks = ','.join(line_info[3:])
            #     #sys.stdout.write(node_id + '\t' + str(curr_pr) + ',' + prev_pr + ',' + outlinks)
            #     sys.stdout.write('%s\t%s,%s,%s' %(node_id, str(curr_pr), prev_pr, outlinks))
            # else:
            #     #sys.stdout.write(node_id + '\t' + str(curr_pr) + ',' + prev_pr + '\n')
            #     sys.stdout.write('%s\t%s,%s\n' %(node_id, str(curr_pr), prev_pr))
            #lst_values = 0.0
        