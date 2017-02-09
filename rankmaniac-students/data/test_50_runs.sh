#!/bin/sh

python pagerank_map.py < p2p-Gnutella08.txt | sort | python pagerank_reduce.py | python process_map.py | sort | python process_reduce.py > int_output.txt
cat int_output.txt > int_input.txt

for i in {1..49}
do
	echo "iter: ${i}"
	python pagerank_map.py < int_input.txt | sort | python pagerank_reduce.py | python process_map.py | sort | python process_reduce.py > int_output.txt

	if grep -q "FinalRank" int_output.txt
	then
		cat int_output.txt > output.txt
		echo "done after ${i} iterations"
		break
	else
		cat int_output.txt > int_input.txt
	fi
done
