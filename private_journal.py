#!/usr/bin/env python
#Written by: Adam Walsh
#Written on: 3/29/14
#Maintained @ https://github.com/walshie4/Private-Journal

#Requires pyCrypto
import os

LOCATION = '/usr/bin/' #location where the journal is stored


if __name__ == "__main__":
    if os.path.isfile(LOCATION): #journal already exists
        os.system("touch " + LOCATION) #create new journal

