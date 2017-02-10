#!/usr/bin/env python

import sys

alpha = 0.85

lst_values = 0.0

for line in sys.stdin:
    line_tab = line.split('\t')

    if line_tab[0] == "i" or line_tab[0] == 'c':
        sys.stdout.write(line)
    else:
        line_info = line_tab[1].split(',')
        node_id = line_tab[0]

        if line_info[0] == 'p':
            sum_vals = alpha * lst_values + 1.0 - alpha
            
            curr_pr = sum_vals
            prev_pr = line_info[1]

            if len(line_info) > 3:
                outlinks = ','.join(line_info[3:])
                #sys.stdout.write(node_id + '\t' + str(curr_pr) + ',' + prev_pr + ',' + outlinks)
                sys.stdout.write('%s\t%s,%s,%s' %(node_id, str(curr_pr), prev_pr, outlinks))
            else:
                #sys.stdout.write(node_id + '\t' + str(curr_pr) + ',' + prev_pr + '\n')
                sys.stdout.write('%s\t%s,%s\n' %(node_id, str(curr_pr), prev_pr))
            lst_values = 0.0
        else:
            lst_values += float(line_tab[1])