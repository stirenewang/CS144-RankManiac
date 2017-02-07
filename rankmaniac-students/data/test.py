from subprocess import call
import os

# Script file to iteratively run 
repeat = " | python pagerank_reduce.py | python process_map.py | sort | python process_reduce.py"
os.system('python pagerank_map.py <input.txt | sort' + repeat + repeat+' > output.txt')
#os.system('python pagerank_map.py <output.txt | sort' + repeat + ' > input.txt')