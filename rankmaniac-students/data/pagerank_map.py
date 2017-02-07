#!/usr/bin/env python

import sys

for line in sys.stdin:
	node_id = int(line[7])
	curr_pr = float(line[9:12])
	prev_pr = float(line[13:16])
	outlinks = line[17:]
	outlinks = outlinks.split(',')
	outlinks = [int(x) for x in outlinks]











	print node_id
	print curr_pr
	print prev_pr
	for i in outlinks:
		print i
