#!/bin/bash

echo "Enter the number of the feature you want to execute: "
read num

if [ "$num" -eq 2 ] ; then
        ls -lS -R ../../CS1XA3* | grep -v '^d' > filesize.txt
	cut -b 28-31,45- filesize.txt
	rm filesize.txt
fi

if [ "$num" -eq 3 ] ; then
        git log -i --grep=merge > file1.txt
        cut -c 8-48 file1.txt > file2.txt
        commit_number=$(head -n 1 file2.txt)
        git checkout "$commit_number"
	rm file1.txt file2.txt
fi

if [ "$num" -eq 4 ] ; then

	echo "Enter an extension to find how many files exist with that extension: "
	read ext_num
	COUNT=$(find .. -name "*.$ext_num" | wc -l)
	echo "The number of files in the repo with this extension are: $COUNT"
fi

if [ "$num" -eq 5 ] ; then

	if [ -f fixme.log ] ; then
		echo "" > fixme.log
	fi

	for file in $(find .. -type f) ; do
		if [ $(tail -1 "$file" | egrep "*#FIXME") ] ; then
			echo "$file"$'\n' >> fixme.log
		fi
	done

fi

if [ "$num" -eq 6 ] ; then

        echo "Enter a tag: "
        read var6

        if [ -f "$var6".log ] ; then
                rm "$var6".log
	fi

        for pythonFile in $(find .. -name "*.py" -type f) ; do
                pythonComment=`cat "$pythonFile" | grep "^#" | grep "$var6"`
		echo "$pythonComment" >> "$var6".log
	done
fi

if [ "$num" -eq 7 ] ; then

	echo "This feature has a Backup and Delete Feature, and a Restore feature"
	echo "To execute the Backup and Delete Feature, enter 1"
	echo "To execute the Restore Feature, enter 2"
	read var7

	if [ "$var7" -eq 1 ] ; then

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

	if [ "$var7" -eq 2 ] ; then

		cd backup

		if [ ! -f restore.log ] ; then
			echo "The file restore.log does not exist. Could not restore files back to their original location."
		else

			for item in $(cat restore.log) ; do
				filename=$(basename "$item")
				mv "$filename" "../$item"
			done
		fi

	fi
fi

if [ "$num" -eq 8 ] ; then

	echo "Welcome to Custom Feature 1"
	echo "For this feature, one of the sub-features is that you can delete all lines in all files that contain a certain string,"
	echo "and the files being searched will be only of a certain file extension that you select."
	echo "Or, you can delete all files containing that string from their original location, and copy them to another directory."
	echo "To select the first feature, enter 1"
	echo "To select the second feature, enter 2"
	read var8


	echo "Enter a certain keyword:"
	read keyword
	echo "Enter a certain file extension:"
	read file_ext

	if [ "$var8" -eq 1 ] ; then

		if [ -d "$keyword" ] ; then
			rm -r "$keyword"
		fi


		find .. -type f -name "*.$file_ext" -print | xargs grep -r "$keyword" > "$keyword".log
		find .. -type f -name "*.$file_ext" -print0 | xargs -0 sed -i /"$keyword"/d

		echo "The occurrences of this string have successfully been deleted from all files of the $file_ext file extension"
		echo "The previous occurrences of this string can be found stored in the file '$keyword'.log"

	fi

	if [ "$var8" -eq 2 ] ; then

		if [ ! -d "$keyword" ] ; then
			mkdir "$keyword"
		else
			cd "$keyword"
			ls | xargs rm
			cd ..
		fi

		cd ..
		grep -lr "$keyword" --include \*."$file_ext" | xargs -I xxx -P 0 mv xxx Project01/"$keyword"/
	fi

fi

if [ "$num" -eq 9 ] ; then

	echo "Welcome to Custom Feature 2"
	echo "For this feature, you will be prompted to select between two features."
	echo "You can either find every occurrence of a string, and replace it with another string, while recording all occurrences of the previous word in another file"
	echo "Or, you can find all files with a certain file extension, that contain a certain string, and append the files by adding the second word to them."
	echo "To select the first sub-feature, enter 1"
	echo "To select the second sub-feature, enter 2"
	read var9

	if [ "$var9" -eq 1 ] ; then

		echo "Welcome to the Find/Replace Feature. Enter a word to find: "
		read fst_word
		echo "Next, enter a file extension :"
		read file_ext
		echo "Now, enter a word that you want to replace it with: "
		read snd_word

		egrep -lRZ "${fst_word}" --include \*."$file_ext" . | xargs -0 -l sed -i -e "s/${fst_word}/${snd_word}/g"
	fi

	if [ "$var9" -eq 2 ] ; then

		echo "Enter the word you want to find: "
		read fst_word
		echo "Enter a file extension: "
		read file_ext
		echo "Enter a second word: "
		read snd_word


		for i in $(find .. -type f -name "*.$file_ext" -print0 | xargs -0 grep -r -l "$keyword") ;
		do
			echo "$snd_word" >> "$i"
		done

	fi

fi
