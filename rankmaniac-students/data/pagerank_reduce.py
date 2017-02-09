#!/usr/bin/env python

import sys

alpha = 0.85

lst_values = []

for line in sys.stdin:
    line_tab = line.split('\t')

    if line_tab[0] == "i" or line_tab[0] == 'c':  # check if first line
        sys.stdout.write(line)
    else:  
        line_info = line_tab[1].split(',')
        node_id = int(line_tab[0])

        if line_info[0] == 'p':
            sum_vals = alpha * sum(lst_values) + 1.0 - alpha
            
            curr_pr = sum_vals
            prev_pr = float(line_info[1])


            if len(line_info) > 3:
                outlinks = ','.join(line_info[3:])
                sys.stdout.write(str(node_id) + '\t' + str(curr_pr) + ',' + str(prev_pr) + ',' + outlinks)
            else:
                sys.stdout.write(str(node_id) + '\t' + str(curr_pr) + ',' + str(prev_pr) + '\n')

            lst_values = []
        else:
            lst_values.append(float(line_tab[1]))