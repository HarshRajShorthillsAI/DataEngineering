#!/bin/sh

ls ~/Tutorial ~/ABC > mytext.txt 2>&1
echo "listed files... 2>&1 means message from 2 is merged with current output 1"

ls ~/Tutorial nonexistent_file > mytext.txt 2<&1