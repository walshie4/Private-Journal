#!/usr/bin/env python3
#Written by: Adam Walsh
#Written on: 3/29/14
#Maintained @ https://github.com/walshie4/Private-Journal

#Requires pyCrypto
import os
import encrypt#import encrypt.py
import sys
import fileinput
import time
from shutil import move

if __name__ == "__main__":
    print("\nWARNING: Killing execution at any point, (or encountering an error) may cause your journal\n"
        + "to be left on your drive unencrypted. If the program exits before stating the journal was\n"
        + "re-encrypted please check to see if it encrypted. If an error caused the exit please report\n"
        + "it so I can fix it ASAP. Sorry for any inconvience, hope you enjoy this script! :D\n")
    location = input("Please enter the location of the journal (parent directory containing journal)\n"
                    +"the journal will be created if it does not exist\n-> ")
    encrypted = True
    if not location.endswith('/'):
        location += '/'
    location = location + 'journal'
    if not os.path.isfile(location): #journal doesn't exist
        os.system("touch " + location + ".tmp") #create new journal temp
        encrypted = False#no need to decrypt before appending
    iterations = input("Please enter then number of iterations you would like to use when encrypting your\n"
                    +  "journal, or press enter to use 1,000,000\n-> ")
    if iterations == '':
        iterations = 1000000#default iterations = 1 million
    print("Please input your entry (press crtl-d twice on a newline when done)")
    entry = ''
    for line in fileinput.input():
        entry += line
    if encrypted: #decrypt for writing (journal existed before execution)
        print("Decrypting for appending")
        encrypt.main(location, "d", iterations, location + ".tmp")#an error here probably means it's a malformed file
    with open(location + ".tmp", "a") as out:#append the entry
        out.write(time.strftime("%c") + "\n\n")#add timestamp to entry
        out.write(entry + "\n")
    input("If you would like to read your journal open the journal.tmp file, when done just press enter")
    print("Encrypting journal...(Please wait)")
    encrypt.main(location + ".tmp", "e", iterations, location)#re-encrypt journal
    os.remove(location + ".tmp")#delete tmp file
    print("Exiting...")

