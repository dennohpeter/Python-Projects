#!/usr/bin/python

from cryptography.fernet import Fernet
import csv

def crypt( string ):

    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(str.encode(string))
    plain_text = cipher_suite.decrypt(cipher_text)

    print("key: " + key.decode())
    print("cipher text: " + cipher_text.decode())
    print(plain_text)
    return cipher_text.decode()

def decrypt(string):
        key = Fernet.generate_key()
        cipher_suite = Fernet(str.encode('YFnwBPEtC6owA2qMLtonmXDFl9QIEpqV_zBrqj5S0tk='))
        plain_text = cipher_suite.decrypt(str.encode(string))

        return plain_text


print("Hello Welcome to Dema's Password Vault\nWould you like to:\n\t1. Create a new password vault.\n\t2. Access an existing passworld vault.\n")

userInput = 0

while userInput not in ['1', '2']:
    userInput = input()

if userInput is '1':
    #create a new vault! aka new file
    #ask what they want to name their file!
    filename = input("What would you like to name your vault? ")
    f = open(filename, "w+") #create and open for writing!
    f.write("platform,username,password\n")

    print("Time to crypt those passwords!\nWe will keep going until you hit 'q'")

    password = '\0'
    platform = '\0'
    username = '\0'

    while platform not in ['q', 'Q']:
        platform = input("What is this for: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        enctyped = crypt(password)
        f.write(platform + ','+ username + ',' + enctyped + '\n')

elif userInput is '2':
    filename = input("Enter the existing password vault name: ")
    f = open(filename, "r")
    fileContent = f.read().splitlines()
    parsedContent = csv.reader(fileContent, delimiter=",")
    #print(fileContent)
    list = list(parsedContent)
    print(list)
    print(decrypt(list[1][2]))
