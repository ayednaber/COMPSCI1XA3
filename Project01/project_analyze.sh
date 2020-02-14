#!/bin/bash

echo "Enter the number of the feature you want to execute: "
read fnum

if [ "$fnum" -eq 2 ] ; then
        ls -lS -R ../../CS1XA3* | grep -v '^d' > filesize.txt
	cut -b 28-31,45- filesize.txt
fi

if [ "$fnum" -eq 3 ] ; then
        git log -i --grep=merge > file1.txt
        cut -c 8-48 file1.txt > file2.txt
        commit_number=$(head -n 1 file2.txt)
        git checkout "$commit_number"
fi

if [ "$fnum" -eq 4 ] ; then

	echo "Enter an extension to find how many files exist with that extension: "
	read ext_num
	COUNT=$(find . -name "*.$ext_num" | wc -l)
	echo "The number of files in the repo with this extension are: $COUNT"
fi





