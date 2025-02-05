#!/bin/bash
x=$1
y=$2
z=$3
echo "Arrange the $# numbers in the argument($1, $2, $3 respectively) in decending order"
if [ $x -gt $y ]
then
if [ $x -gt $z ]
then
if [ $y -gt $z ]
then
echo $x' > '$y' > '$z
else
echo $x' > '$z' > '$y
fi
else
echo $z' > '$x' > '$y
fi
else
if [ $z -gt $y ]
then
echo $z' > '$y' > '$x
else
if [ $x -gt $z ]
then
echo $y' > '$x' > '$z
else
echo $y' > '$z' > '$x
fi
fi
fi