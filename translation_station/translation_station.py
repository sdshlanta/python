#!/usr/bin/env python
# -*- coding utf8 -*-

import os
import subprocess
import getpass

userprofile = str(os.environ['USERPROFILE'])

def print_logo():
    print(" _____                   _       _       ")
    print("|_   _|                 | |     | |      ")
    print("  | |_ __ __ _ _ __  ___| | __ _| |_ ___ ")
    print("  | | '__/ _` | '_ \/ __| |/ _` | __/ _ |")
    print("  | | | | (_| | | | \__ \ | (_| | ||  __/")
    print("  \_/_|  \__,_|_| |_|___/_|\__,_|\__\___|")
    print("=========================================")
                                         
                                         

def program_map(action):
    dictionary = {
        "1": "caesar_cipher.py",
        "q": "quit"
    }
    return dictionary.get(action, "none")

print_logo()
print("Choose what type of encryption or decryption you desire")
print("1 : Caesar Cipher / Shift Cipher")
print("q : Quit")
action = input(": ")

# Search the dictionary for the program name
action = program_map(action)
# Validation
while(action == "none" or action == None):
    print(action + ", please pick an available number.")
    action = input(": ")
    action = program_map(action)

# Launch the dictonary selected program
if(action != "quit"):
    os.system("python " + userprofile + "/Documents/python/translation_station/" + action)
