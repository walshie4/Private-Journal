#!/usr/bin/env python
#Written by: Adam Walsh
#Written on: 3/29/14
#Maintained @ https://github.com/walshie4/Private-Journal

#Requires pyCrypto
from Crypto.Cipher import AES
import os

LOCATION = '/usr/bin/'

if os.path.isfile(LOCATION): #journal already exists
    os.system("touch " + LOCATION) #create new journal

key = input("Please enter your journals encryption passphrase.")
cipher = AES.new(key)

