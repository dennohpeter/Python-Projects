# This is a python version of a2q4 in cis 1500

##Write a  program that prompts the user to enter a noun of no more than 25 characters.
##The program should create a new string that is the plural of the noun.
##Use the following rules when creating plurals:
##
##1. If a noun ends in 's', 'ch', or 'sh'  add es to the noun
##2. If a noun ends in 'y', change the 'y' to 'i' and add 'es' to the noun.
##3. In all other cases add an 's' to the noun.

userInput = input("Enter a noun:")

while len(userInput) > 25:
    userInput = input("Enter a noun:")

if ( userInput[len(userInput) - 1] == 's') or ( userInput[len(userInput) - 1] == 'h' and userInput[len(userInput) - 2] == 'c') or ( userInput[len(userInput) - 1] == 's' and userInput[len(userInput) - 2] == 's'  ):
    print(userInput + 'es')
elif userInput[len(userInput) - 1] == 'y':
    print ( userInput[0: len(userInput) - 2] + 'ies')
else:
    print ( userInput + 's')
