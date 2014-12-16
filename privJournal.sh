#!/usr/bin/env sh
NAME=$1
#check for param
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
echo "Input journal password and entry."
openssl des3 -salt -out "$NAME"
openssl des3 -d -salt -in "$NAME"
