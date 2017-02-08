#!/bin/sh

python pagerank_map.py < input.txt | sort | python pagerank_reduce.py | python process_map.py | sort | python process_reduce.py > int_output.txt
cat int_output.txt > int_input.txt

for i in {1..48}
do
	python pagerank_map.py < int_input.txt | sort | python pagerank_reduce.py | python process_map.py | sort | python process_reduce.py > int_output.txt

	cat int_output.txt > int_input.txt
done

python pagerank_map.py < int_input.txt | sort | python pagerank_reduce.py | python process_map.py | sort | python process_reduce.py 50 > output.txt