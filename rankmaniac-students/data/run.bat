ECHO OFF
FOR /L %%A IN (1,1,10) DO (
ECHO run
python pagerank_map.py <output.txt | sort | python pagerank_reduce.py | python process_map.py | sort | python process_reduce.py > output.txt
)
PAUSE