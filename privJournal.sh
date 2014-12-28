#!/usr/bin/env sh
BASELOC="$HOME/privJournal"
ENTRYLOC="$BASELOC/entries"
#check for param
echo "\nPrivJournal -- A simple encrypted journal utility.\n"
if ! [[ -e "$ENTRYLOC" ]]; then
    if ! [[ -e "$BASELOC" ]]; then
        mkdir "$BASELOC"
    fi
    mkdir "$ENTRYLOC"
fi
CMD=$1
case "$CMD" in
    "Read" | "READ" | "read") #read
        ls "$ENTRYLOC"
        echo -n "\nEnter name of the entry you would like to read.\n-> "
        read NAME
        openssl des3 -d -salt -in "$ENTRYLOC/$NAME";;
    "make" | "Make" | "MAKE" | "new" | "NEW" | "New" | "mk") #make
        NAME=`date "+%Y-%m-%d-%H-%M-%S"`
        NAME="$ENTRYLOC/$NAME"
        touch "$NAME"
        echo "Input journal password, confirm, and then input entry."
        openssl des3 -salt -out "$NAME";;
    "list" | "ls" | "LIST" | "List")
        ls "$ENTRYLOC";;
    *) #no command given, show usage
        echo "Usage: privJournal [make | read | list]\n"
        echo "Make - Make a new entry"
        echo "Read - Read a past entry"
        echo "List - List all past entries\n"
        echo "If you have any feature requests, or run into any"
        echo "issues please let me know on the project's Github page.";;
esac
