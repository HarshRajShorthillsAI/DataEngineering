#/bin/sh

y=1
z=1
echo -n "1 1 "
for x in 1 2 3 4 5 6 7 8 9 10
do
u=$z
z=$(($y + $z))
echo -n "$z "
y=$u
done
echo ""