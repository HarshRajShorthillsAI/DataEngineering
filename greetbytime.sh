#!/bin/sh
time=$(date +%H)
if [ $time -lt 12 ]
then
echo "Good Morning $(uname -n)"
else
if [ $time -lt 18 ]
then
echo "Good Afternoon $(uname -n)"
else
echo "Good Evening $(uname -n)"
fi
fi