#!/usr/bin/env python

import sys
for line in sys.stdin:
    line_tab = line.strip().split('\t')
    line_info = line_tab[1].split(',')

    if line_tab[0] == "i":          # If line has iteration data
        sys.stdout.write(line)
    elif line_tab[0] == 'c':
        sys.stdout.write(line)
    else:                           # If line has graph data
        assert line_tab[0].startswith("NodeId:")
        node_id = line_tab[0][7:]
        
        if len(line_info) > 2:      # if node has outlinks
            outlinks = line_info[2:]    # Get out-links as strings
            curr_pr = float(line_info[0])

            value = str(curr_pr / len(outlinks))
            for link in outlinks:
                sys.stdout.write(link + '\t' + value + '\n')

            sys.stdout.write(node_id + '\t0\n')
        else:                       # if node doesn't have outlinks
            sys.stdout.write(node_id + '\t1\n')

        # Print graph data
        sys.stdout.write(node_id + '\t' + 'p,' + line_tab[1] + '\n')