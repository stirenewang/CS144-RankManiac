#!/usr/bin/env python

import sys
iteration = 0
for line in sys.stdin:

    line_tab = line.strip().split('\t')
    line_info = line_tab[1].split(',')

    if line_tab[0] == "i":  # check if first line
        iteration = int(line_tab[1]) # print iteration
        sys.stdout.write("i" + "\t" + str(iteration) + "\n")
    else:
        assert line_tab[0].startswith("NodeId:")
        node_id = int(line_tab[0][7:])
        curr_pr = float(line_info[0])
        prev_pr = float(line_info[1])

        if len(line_info) > 2:
            outlinks = [int(float(x)) for x in line_info[2:]]

            for link in outlinks:
                key = link
                value = curr_pr / len(outlinks)
                sys.stdout.write(str(key) + '\t' + str(value) + '\n')

            sys.stdout.write(str(node_id) + '\t0\n')
        else:
            sys.stdout.write(str(node_id) + '\t1\n')

        sys.stdout.write(str(node_id) + '\t' + 'p,' + line_tab[1] + '\n')