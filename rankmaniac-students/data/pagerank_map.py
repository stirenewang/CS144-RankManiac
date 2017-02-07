#!/usr/bin/env python

import sys

for line in sys.stdin:
	node_id = int(line[7])
	curr_pr = float(line[9:12])
	prev_pr = float(line[13:16])
	outlinks = line[17:]
	outlinks = outlinks.split(',')
	outlinks = [int(x) for x in outlinks]

	# return list with all outlinked pages as keys
	# corresponding values are pagerank of origin page divided by total num of outlinks
	# from origin page
	# also append to list pair with key the origin page and value 0

	for link in outlinks:
		key = link
		value = curr_pr / len(outlinks)
		sys.stdout.write(key + '\t' + value)











	print node_id
	print curr_pr
	print prev_pr
	for i in outlinks:
		print i
