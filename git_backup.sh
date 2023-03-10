#!/usr/bin/env bash
#

USAGE='git_backup.sh [-h] ["commit message"]\n
	This scripts automatically commits changes in project_dir;\n
	Make sure that project_dir is a git repository.\n\n

	Options:\n
	-h or -help - prints this message\n
	"commit message" - message for git commit; default: date and project name'


if [ "$1" == "-h" ]; then
	echo -e $USAGE
	exit 0
fi


project_dir=$(pwd)
echo "...Backing up $project_dir"


## optional commit message argument
commit_message=${1:-"backed up changes from $(date) in the project $project_dir"}


## check if .gitignore exists in the project dir
if [[ -f .gitignore ]]; then
        echo "...Found .gitignore -> untracked files will be ignored"
else
        echo "...No .gitignore found in this dir -> every file will be added to the commit"
fi


## commit changes
git add .
git commit -m "$commit_message"
git push


## check if successful
if [[ $? == 0  ]]; then
	echo "Backup DONE!"
else
	echo "Backup FAILED!"
fi
