import os
import string

def print_logo():
    print('\033[0;30m\]' + '\033[47m' + "                                                               " + '\033[0m')
    print('\033[0;30m\]' + '\033[47m' + "  ██████░  ████░ ████████░  ██░     ██░ ████████░ ████████░    " + '\033[0m')
    print('\033[0;30m\]' + '\033[47m' + " ██░    ██░ ██░  ██░     ██░██░     ██░ ██░       ██░     ██░  " + '\033[0m')
    print('\033[0;30m\]' + '\033[47m' + " ██░        ██░  ██░     ██░██░     ██░ ██░       ██░     ██░  " + '\033[0m')
    print('\033[0;30m\]' + '\033[47m' + " ██░        ██░  ████████░  ██████████░ ██████░   █████████░   " + '\033[0m')
    print('\033[0;30m\]' + '\033[47m' + " ██░        ██░  ██░        ██░     ██░ ██░       ██░   ██░    " + '\033[0m')
    print('\033[0;30m\]' + '\033[47m' + " ██░    ██░ ██░  ██░        ██░     ██░ ██░       ██░    ██░   " + '\033[0m')
    print('\033[0;30m\]' + '\033[47m' + "  ██████░  ████░ ██░        ██░     ██░ ████████░ ██░     ██░  " + '\033[0m')
    print('\033[0;30m\]' + '\033[47m' + "                                                               " + '\033[0m')
    print()

def encrypt():
    """Encrypts a string by shifting ascii chars"""
    print ("This program will encode your messages using a Caesar Cipher")
    print ()
    try:
        key = int(input("Enter the key: "))
    except ValueError:
        key = int(input("Your key must be a number: "))
    if key > 26:
        print("That's a pretty large key! Let me ajust for that...")
        while key > 26:
            key -= 26
    message = input("Enter the message: ").lower()
    codedMessage = ""
    for ch in message:
        if int(ord(ch)) < 97 or int(ord(ch)) > 122:
            codedMessage = codedMessage + ch
        else:
            if (ord(ch) + key - 96) > 26:
                codedMessage = codedMessage + chr(ord(ch) - 26 + key)
            else:
                codedMessage = codedMessage + chr(ord(ch) + key)
    print ("The coded message is:",'\033[33m' + codedMessage + '\033[0m')
    addToClipBoard(codedMessage)
    print("Copied to Clipboard")

def decrypt():
    """Decrypts a string by shifting ascii chars"""
    print ("This program will decrypt your messages using a Caesar Cipher")
    print ()
    try:
        key = int(input("Enter the key: "))
    except ValueError:
        key = int(input("Your key must be a number: "))
    if key > 26:
        print("That's a pretty large key! Let me ajust for that...")
        while key > 26:
            key -= 26
    message = input("Enter the coded message: ").lower()
    codedMessage = ""
    for ch in message:
        if int(ord(ch)) < 97 or int(ord(ch)) > 122:
            codedMessage = codedMessage + ch
        else:
            if (ord(ch) - key - 96) < 1:
                codedMessage = codedMessage + chr(ord(ch) + 26 - key)
            else:
                codedMessage = codedMessage + chr(ord(ch) - key)
    print ("The decoded message is:",'\033[33m' + codedMessage + '\033[0m')
    addToClipBoard(codedMessage)

def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)
     
##### LET THE MAIN CODE BEGIN #####
os.system("cls")
print_logo()
print("Encrypt or Decrypt? (e/d)")
method_select = input(":")
while True:
    if method_select == "e":
        os.system("cls")
        encrypt()
        break
    elif method_select == "d":
        os.system("cls")
        decrypt()
        break
    else:
        print("Please just type e or d")
        method_select = input(":")
os.system("pause")