#!/bin/bash

echo "Enter the number of the feature you want to execute: "
read num

if [ "$num" -eq 2 ] ; then
        ls -lS -R ../../CS1XA3* | grep -v '^d' > filesize.txt
	cut -b 28-31,45- filesize.txt
fi

if [ "$num" -eq 3 ] ; then
        git log -i --grep=merge > file1.txt
        cut -c 8-48 file1.txt > file2.txt
        commit_number=$(head -n 1 file2.txt)
        git checkout "$commit_number"
fi

if [ "$num" -eq 4 ] ; then

	echo "Enter an extension to find how many files exist with that extension: "
	read ext_num
	COUNT=$(find . -name "*.$ext_num" | wc -l)
	echo "The number of files in the repo with this extension are: $COUNT"
fi

if [ "$num" -eq 5 ] ; then

	echo "kjashdk"

fi

if [ "$num" -eq 5 ] ; then

	echo "This feature has a Backup and Delete Feature, and a Restore feature"
	echo "To execute the Backup and Delete Feature, enter 1"
	echo "To execute the Restore Feature, enter 2"
	read var5
	if [ ! -d ../../CS1XA3/Project01/backup ] ; then
		mkdir backup
	else
		cd backup
		ls | xargs rm
		cd ..
	fi

	find .. -type f -name "*.tmp" > backup/restore.log
	find "../../CS1XA3" -type f -name "*.tmp" -not -path "../../CS1XA3/Project01/backup/*" -exec mv {} ../../CS1XA3/Project01/backup \;
fi
