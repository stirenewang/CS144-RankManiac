#!/usr/bin/env python

import sys

alpha = 0.85

prev = -1
lst_values = []

for line in sys.stdin:
    temp = line.split('\t')

    if prev == -1:
    	prev = int(temp[0])

    if prev == int(temp[0]):
    	lst_values.append(alpha * float(temp[1]) + 1.0 - alpha)
    else:
    	sum_vals = sum(lst_values)
    	sys.stdout.write(str(prev) + '\t' + str(sum(lst_values)) + '\n')

    	lst_values = [float(temp[1])]
    	prev = int(temp[0])

if len(lst_values) == 1:
	sys.stdout.write(str(prev) + '\t' + str(sum(lst_values)) + '\n')