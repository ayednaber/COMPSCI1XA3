# CS 1XA3 Project01 - <nabera>

## Usage
   Execute this script from project root with:
   chmod +x CS1XA3/Project01/project_analyze.sh
   ./CS1XA3/Project01/project_analyze.sh

   When this script is executed, it will echo out a message asking the user for a number, and depending on that number will execute the feature corresponding to it.
   This is achieved by reading in a value from the user, and it will be compared to other values in the script, and once it finds a match, then a certain feature inside the if statement will be executed.
   Possible values for the feature number: 
       2, 3, 4


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

## Custom Feature 1: Delete Occurrences of a String

  **Description:** This custom feature prompts the user to select between two features, either deleting all lines that contain a certain keyword, and copying their occurrences to another file, or deleting the
   actual files that contain that string from their original location, and copy them to another directory. The search in the repo is done on a certain file extension that is also entered by the user.

   Regardless of which feature the user selects, the first step will be the same, through which the user will be prompted to enter a file extension, and to enter a keyword.

   If the user selects the first feature,a recursive search will be done through all the files in the repo to delete all the lines that contain it, and deletes them. Also, the occurrences of those strings
   will be documented in another file, which will be named by: '$user_keyword'.log.

   If the user selects the second feature, a recursive search through the repo for files containing that string, and delete them from their original location, and copy those files to another directory.


## Custom Feature 2: Find and Replace Strings in Files

  **Description:** This custom feature will prompt the user to enter 2 keywords, the first one being the word they are looking for, and the second one being the word they want to replace it with.
   Then, the repo will be searched for files containing that string, and will replace the first word with the second word in all occurrences.
