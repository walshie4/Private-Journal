#!/usr/bin/env sh
NAME=$1
#check params
if [[ -z "$NAME" ]]; then
    echo "Usage: privJournal <filename>"
    exit;
fi
echo "PrivJournal\n\n"
if [[ -e "$NAME" ]]; then
    echo "Journal found."
else
    echo "Creating journal."
    touch "$NAME"
fi
echo "Input entry now."
CONTENT=$(cat)
echo "$CONTENT" >> "$NAME"
