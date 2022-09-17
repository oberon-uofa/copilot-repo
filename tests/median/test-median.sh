#!/bin/bash

rm -f expected.out
rm -f actual.out
rm -f median-copilot.py
rm -f median-solution.py

cp ../../copilot-solutions/median/untouched/median.py median-copilot.py
cp ../../solutions/median.py median-solution.py

while read -r line
do
	./send-arg.exp median-solution.py $line >> expected.out
	./send-arg.exp median-copilot.py $line >> actual.out
done < input.txt

diff -y --suppress-common-lines expected.out actual.out | wc -l > failed.txt

rm -f median-copilot.py
rm -f median-solution.py
