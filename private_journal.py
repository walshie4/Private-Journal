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
    location = input("Please enter the location of the journal (parent directory containing journal,\n"
                    +"it will be created if it does not exist\n-> ")
    encrypted = True
    if not location.endswith('/'):
        location += '/'
    location = location + 'journal'
    if not os.path.isfile(location): #journal doesn't exist
        os.system("touch " + location) #create new journal
        encrypted = False
    input_file = location
    iterations = input("Please enter then number of iterations you would like to use when encrypting your\n"
                    +  "journal, or press enter to use 1,000,000")
    if iterations = '':
        iterations = 1000000
    if encrypted: #decrypt for writing
        print("Decrypting for appending")
        encrypt.main(input_file, "d", iterations, "output")#an error here probably means it's a malformed file
    print("Journal is ready, input your entry (press crtl-d on a newline when done)")
    entry = ''
    for line in fileinput.input():
        entry += line
    with open(input_file, "a") as out:#append the entry
        out.write(time.strftime("%c") + "\n\n")
        out.write(entry + "\n")
    print("Encrypting journal...(Please wait)")
    encrypt.main(input_file, "e", iterations, location + ".tmp")#re-encrypt journal
    os.remove(location)
    move(location + ".tmp", location)#replace location(unencrypted) with location.tmp(encrypted)
    print("Exiting...")

