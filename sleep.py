#!/usr/bin/python
##display a message based to the user based on
##the number of hours of sleep the user enters for the previous night.
##Use the following values as the basis for the decisions:
##0-4 hours of sleep- Sleep deprived!,
##more than 4 but less than 6- You need more sleep,
##6 or more but less than 8- Not quite enough,
##more than 8- Well Done!

userInput = input("Enter the number of hours of sleep you got the previous night:")
userInput = int(userInput) #Converts string to int for comparrasion ;-)
if userInput >= 0 and userInput <= 4:
    print("Sleep deprived!")
elif userInput > 4 and userInput < 6:
    print("You need more sleep")
elif userInput >= 6 and userInput < 8:
    print("You need more sleep")
elif userInput > 8:
    print("Well Done")
