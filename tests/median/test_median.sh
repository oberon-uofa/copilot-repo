#!/bin/bash

rm -f expected.out
rm -f actual.out
rm -f solution.py
rm -f copilot.py

cp ../../solutions/median.py solution.py
cp ../../copilot-solutions/median/untouched/median.py copilot.py

chmod +x send
while read -r line
do
	./send solution.py $line >> expected.out
	./send copilot.py $line >> actual.out
done < input.txt

diff -y --suppress-common-lines expected.out actual.out | wc -l > failed.txt

rm -f solution.py
rm -f copilot.py
