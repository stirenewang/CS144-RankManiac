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
		connecting = lines[1][:-1]
		if node not in Graph:
			Graph[node] = [connecting]
		else: Graph[node].append(connecting)
	nodes = sorted(Graph)
	for i in nodes:
		f1.write('NodeId:' + str(i) + '\t1.0,0.0')
		for j in Graph[i]:
			f1.write(',' +j)
		f1.write('\n')
	f1.close()



if __name__ == '__main__':
	filename = sys.argv[1]
	out = sys.argv[2]
	main(filename, out)