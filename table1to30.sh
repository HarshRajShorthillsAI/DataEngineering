#!/bin/sh
x=1
y=1
for y in 1 2 3 4 5 6
do
for x in 1 2 3 4 5
do
./while.sh $(($x + $(($y - 1)) * 5)) >> multiplicationtable.txt
done
echo "" >> multiplicationtable.txt
done