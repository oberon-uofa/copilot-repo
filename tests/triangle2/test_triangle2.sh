#!/bin/bash

rm -f expected.out
rm -f actual.out
rm -f solution.py
rm -f copilot.py

cp ../../solutions/triangle2.py solution.py
cp ../../copilot-solutions/triangle2/untouched/triangle2.py copilot.py

python3 "test.py" solution > expected.out
python3 "test.py" copilot > actual.out

diff -y --suppress-common-lines expected.out actual.out | wc -l > failed.txt

rm -f solution.py
rm -f copilot.py

