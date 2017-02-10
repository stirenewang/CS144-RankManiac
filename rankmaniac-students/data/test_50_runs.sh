#!/bin/bash

python2 pagerank_map.py < convertedStanford.txt | sort | python2 pagerank_reduce.py | python2 process_map.py | sort | python2 process_reduce.py > int_output.txt
cat int_output.txt > int_input.txt

for i in {1..49}
do
	echo "iter: ${i}"
	python2 pagerank_map.py < int_input.txt | sort | python2 pagerank_reduce.py | python2 process_map.py | sort | python2 process_reduce.py > int_output.txt

	if grep -q "FinalRank" int_output.txt
	then
		cat int_output.txt > output.txt
		echo "done after ${i} iterations"
		break
	else
		cat int_output.txt > int_input.txt
	fi
done