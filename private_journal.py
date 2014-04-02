#!/usr/bin/env python
#Written by: Adam Walsh
#Written on: 3/29/14
#Maintained @ https://github.com/walshie4/Private-Journal

#Requires pyCrypto
from Crypto.Cipher import AES
from pbkdf2 import crypt
import os

LOCATION = '/usr/bin/' #location where the journal is stored

if __name__ == "__main__":
    if os.path.isfile(LOCATION): #journal already exists
        os.system("touch " + LOCATION) #create new journal

    key = input("Please enter your journals encryption passphrase.")
    cipher = AES.new(key)

def pad_data(data): #add padding to make data divisible by 16 byte (128-bit) blocks
    if len(data) % 16 == 0: #no padding needed
        return data
    padding_required = 15 - (len(data) % 16) #this function is taken from @kisom's cytpo tutorial
                                             #https://github.com/kisom/crypto_intro
    data = '%s\x80' % data                   #See licence for this and following function
    data = '%s%s' % (data, '\x00' * padding_required) #titled 'kisom's Licence'
    return data

def unpad_data(data): #remove padding to original state
    if not data:
        return data

    data = data.rstrip('\x00')
    if data[-1] == '\x80':
        return data[:-1]
    else:
        return data

def isCorrectPassphrase(passphrase):
    hashed = crypt(secret) #need to add logic to keep this hidden
    if hashed == crypt(passphrase, hashed):
        return True
    else
        return False

