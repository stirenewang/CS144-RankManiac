#!/usr/bin/python

import sys

# Terminal: 
# convert.py inputfile.txt outputfile.txt
def main(filename, out):
	Graph = {}
	f = open(filename, 'r')
	f1 = open(out, 'w')
	for line in f:
		lines = line.strip().split('\t')
		node = int(lines[0])
		outlink = int(lines[1])
		if node not in Graph:
			Graph[node] = [outlink]
		else: Graph[node].append(outlink)
		if outlink not in Graph:
			Graph[outlink] = []
	nodes = sorted(Graph)
	for i in nodes:
		f1.write('NodeId:' + str(i) + '\t1.0,0.0')
		for j in Graph[i]:
			f1.write(',' + str(j))
		f1.write('\n')
	f1.close()



if __name__ == '__main__':
	filename = sys.argv[1]
	out = sys.argv[2]
	main(filename, out)