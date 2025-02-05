#/bin/sh

x=$1
y=1

while [ $y -le 10 ]
do
echo "$x x $y = $(($x*$y))"
y=$(($y+1))
done