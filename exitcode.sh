#/bin/sh
x=10
if $1 -le $x
then
echo failed
exit 1
else
echo passed
exit 0
fi