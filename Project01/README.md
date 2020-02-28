# CS 1XA3 Project01 - <nabera>

## Usage
   Execute this script from project root with:
   chmod +x CS1XA3/Project01/project_analyze.sh
   ./CS1XA3/Project01/project_analyze.sh

   When this script is executed, it will echo out a message asking the user for a number, and depending on that number will execute the feature corresponding to it.
   This is achieved by reading in a value from the user, and it will be compared to other values in the script, and once it finds a match, then a certain feature inside the if statement will be executed.
   Possible values for the feature number: 
       2, 3, 4, 5, 6, 7, 8, 9


## Feature 01

  **Description:** This feature lists all the files in the repo along with their file sizes, where a recursive search is done listing the contents (files only) of each directory, where the files are sorted
in a descending order. One pitfall of this feature is that although it does display the file names and sizes in the repo, it does not indicate to which directory each file belongs.

  **Execution:** Execute this feature by entering 2 as the feature number during the prompt.

  **Reference:** Some code was taken from [[https://askubuntu.com/questions/454564/count-total-number-of-files-in-particular-directory-with-specific-extension]]  



## Feature 02

  **Description:** This feature checks out to the latest commit that has the keyword "merge" in its commit message, where the search would be case insensitive. This is achieved by
    fetching the commit log, and searching through that log for "merge" wihle ignoring case sensitivity. Then, the output of that will be cut only leaving the commit
    id, which is used to checkout to that commit.
    
  **Execution:** Execute this feature by entering 3 as the feature number during the prompt.
    
  **Reference:** Some code was taken from [[https://stackoverflow.com/questions/1337320/how-to-grep-git-commit-diffs-or-contents-for-a-certain-word]]
					[[https://www.commandlinefu.com/commands/view/14425/search-git-logs-case-insensitive]]

## Feature 03
   
  **Description:** This feature reads in a certain file extension from the user, and searches the repo to output the number of files that exist with that file extension. This is achieved by prompting
    the user to enter as input the file extension they wish to search for, and that value is used to recursively search the repo to count the number of files that exist with that file extension and output it.
   
  **Execution:** Execute this feature by entering 4 as the feature number during the prompt. Then, enter any file extension that you want to search for (ex: py, will search for
    python files in the repo).
    
  **Reference:** Some code was taken from [[https://stackoverflow.com/questions/5905054/how-can-i-recursively-find-all-files-in-current-and-subfolders-based-on-wildcard]]

## Feature 04

  **Description:** This feature finds every file in the repo that has the word "#FIXME" in its last line, and if so, then the file names will be stored in a file 'fixme.log'.

  **Execution: ** Execute this feature by entering 5 as the feature number during the prompt.

  **Reference:** Some code was taken from [[https://unix.stackexchange.com/questions/213610/find-last-line-of-a-file-for-matching-string]]
					  [[https://www.experts-exchange.com/questions/28923569/grep-egrep-multiple-words-while-using-tail.html]]

## Feature 05

  **Description:** This feature prompts the user to enter a tag word, and then it searches the repo for all the python files that include a comment '#' and the tag word, while reading every line. If a line
  contains the comment and the tag word, then that line will be placed in a file called 'tag_word'.log, where tag_word is the tag word that the user entered. In the end, this file will contain all occurrences
  of the comment and the tag word that occurred in the repo. One downside to this feature is that it does not show from which file the line was written, but is still able to find each line containing the
  comment and the tag word.

  **Execution: ** Execute this feature by entering 6 as the feature number during the prompt, and then enter any tag word (example: testing).

  **Reference:** Some code was taken from [[https://www.cyberciti.biz/faq/unix-loop-through-files-in-a-directory/]]
					  [[https://stackoverflow.com/questions/16961084/linux-shell-commands-cat-and-grep]]

## Feature 06

  **Description:** This feature has two sub-features, which are the Backup and Delete feature, and the Restore feature. The Backup and Delete sub-feature creates an empty directory called backup, and,
   finds all the files with the "tmp" file extension, and copies them to this backup directory, as well as deleting them from their original location. The previous file paths of these files will be
   stored in a file called restore.log. As for the second sub-feature, then it restores all of the ".tmp" files that are stored in restore.log back to their original location, where if the file restore.log
   does not exist, then an error message will be thrown".

  **Execution:** Execute this feature by entering 7 as the feature number during the prompt, and then enter 1 for executing the Backup and Delete Feature, or enter 2 to execute the Restore Feature.

  **Reference:** Some code was taken from [[https://stackoverflow.com/questions/18153878/how-to-avoid-are-the-same-file-warning-message-when-using-cp-in-linux]]
					  [[https://unix.stackexchange.com/questions/429382/need-to-loop-through-folder-and-move-files-to-different-directory]] 

## Custom Feature 1: Delete Occurrences of a String

  
  **Description:** This custom feature prompts the user to select between two features. For both features, the user is prompted to enter a keyword and a file extension. The first sub-feature searches
   the files in the repo line-by-line, and wherever it finds that string, then it will delete it. The occurrences of that string in all the files will be stored in another file called 'keyword'.log
  (keyword being the keyword entered by the user). The second sub-feature searches for files containing that string, and deletes them from their original location, and copies them to another directory called
  'keyword'.

  **Execution:** Execute this feature by entering 8 as the feature number during the prompt. Then either enter 1 for executing the first sub-feature, or enter 2 to execute the second sub-feature. Lastly,
   when prompted, enter a keyword (example: hello), and a file extension (example: html).

  **References:** Some code was taken from [[https://stackoverflow.com/questions/5410757/delete-lines-in-a-text-file-that-contain-a-specific-string]]
					   [[https://stackoverflow.com/questions/15617016/copy-all-files-with-a-certain-extension-from-all-subdirectories]] 


## Custom Feature 2: Find and Replace Strings in Files
 
  **Description:** This custom feature has two sub-features. When selecting either of the two sub-features, the user will be prompted to enter a word they want to search for, a file extension, and a word
  they want to replace the first one with. When executing the first sub-feature, then all of the files in the repo will be searched line-by-line, and every occurrence of the first word will be replaced with
  the second word. When executing the second sub-feature, then every file that contains the first word entered by the user will be appended by adding the second word to that file.

  **Execution:** Execute this feature by entering 9 as the feature number during the prompt. Then, either enter 1 for executing the first sub-feature, or enter 2 to execute te second sub-feature. Lastly,
   when prompted, enter the first word, then enter the file extension, then enter the second word.

  **References:** Some code was taken from [[https://askubuntu.com/questions/20414/find-and-replace-text-within-a-file-using-commands]]


