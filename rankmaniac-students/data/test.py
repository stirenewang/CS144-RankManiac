from subprocess import call
import os

# Script file to iteratively run 
repeat = " | python2 pagerank_reduce.py | python process_map.py | sort | python process_reduce.py"
os.system('python2 pagerank_map.py <int_output.txt | sort' + repeat + ' > int_input.txt')
#os.system('python2 pagerank_map.py <int_input.txt | sort' + repeat + ' > int_output.txt')
#os.system('python pagerank_map.py <output.txt | sort' + repeat + ' > input.txt')