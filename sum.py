##Give the code for a loop that computes
##and displays a sum of numbers that the user enters.
##The loop should prompt the user for input until the user enters -335
##and then exit and display the final sum.
##Do not provide the entire c program, just a working loop.
total = 0
userInput = 0
while userInput != -335:
    userInput = input("Enter a number (to quit enter -335):")
    userInput = int(userInput) #convert to int
    if userInput != -335:
        total = total + userInput
print("The sum:", total)
