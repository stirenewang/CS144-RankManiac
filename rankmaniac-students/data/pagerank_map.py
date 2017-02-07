#!/usr/bin/env python

import sys

for line in sys.stdin:
	node_id = int(line[7])
	curr_pr = float(line[9:12])
	prev_pr = float(line[13:16])
	outlinks = line[17:]
	outlinks = outlinks.split(',')
	outlinks = [int(x) for x in outlinks]

	for link in outlinks:
		key = link
		value = curr_pr / len(outlinks)
		sys.stdout.write(str(key) + '\t' + str(value) + '\n')

	sys.stdout.write(str(node_id) + '\t0\n')