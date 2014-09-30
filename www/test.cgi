#!/bin/bash
#sleep 50



echo "hello world!." > plik

for i in `seq 1 100`; do
	echo "Iteration: $i" >> plik
	sleep 1
done

exit 0
