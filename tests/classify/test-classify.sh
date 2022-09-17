#!/bin/bash

rm -f expected.out
rm -f actual.out
rm -f classify-copilot.py
rm -f classify-solution.py

cp ../../copilot-solutions/classify/untouched/classify.py classify-copilot.py
cp ../../solutions/classify.py classify-solution.py

while read -r line
do
	./send-arg.exp classify-solution.py $line >> expected.out
	./send-arg.exp classify-copilot.py $line >> actual.out
done < input.txt

diff -y --suppress-common-lines expected.out actual.out | wc -l > failed.txt

rm -f classify-copilot.py
rm -f classify-solution.py
