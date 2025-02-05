#!/bin/sh

var1="John"
var2=21
var3="Doe"
echo $var1 $var2

unset var1
echo "var2 is now unset"
echo $var1 $var2

readonly var3
unset var3