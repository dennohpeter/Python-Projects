##For this assignment you will write a rudimentary text editor that allows the user to edit 5 lines of text,
##where each line is no longer than 80 characters.
##The editor should allow the user to continue editing as long as desired
##and should print the current state of the edit buffer after each edit.
##
##The editor is a 'line editor' in that the user must edit one line at a time.
##The user can specify which line should be edited by choosing a line number from a menu.   
##
##The only two editing operations possible are to replace an entire line with a new line,
##or to replace a substring in the line with a new substring.


##This function causes the original string to be modified such that the first occurrence of substring is removed
##from the original string and the contents of replace are inserted in its place.
##replaceInString does not do the replacing of text directly.  It calls findSubString and insertString.
##The function returns 0 if the operation fails and 1 if the operation is successful.
def replaceInString(original, substring, replace):
    return 0

##This function finds the first occurrence of toFind in original
##and returns an integer representing the index of the first element of the toFind substring in original.
##For example if toFind was 'cat'
##and original was 'thundercat' the function would return 7 since the begining of 'cat' in 'thundercat' is position 7.
##If the function does not find a substring it should return -1
##note:  do not use existing substring functions such as strstr as a solution for this function.
##Solve the algorithm yourself. You may use basic string functions such as strlen and strcat.
def findSubString(original, toFind):
    return 0

##This function replaces the contents of original  with the following sequence of characters:  
##1.the characters from original up to position start-1
##2.the characters from toInsert 
##3.the remaining characters of original, excluding the characters of the substring that is being removed.
def insertString(original, start, length, toInsert):
    return 0
    

    
buffer1 = 'dema is the best'
buffer2 = 'what is life'
buffer3 = 'lets see how hard this will be'
buffer4 = 'I like to go longboarding'
buffer5 = 'python is a cool language!'

print("1.",buffer1)
print("2.",buffer2)
print("3.",buffer3)
print("4.",buffer4)
print("5.",buffer5)
    
userChange = int(input("\n\nEnter which number you would like to change:"))

if userChange == 1:
  print("Enter 1 to change the entire sentence\nEnter 2 to change a string")
  userAction = int(input())
  if userAction == 1:
    print("Enter the new sentence:")
    buffer1 = input()

    print("1.",buffer1)
    print("2.",buffer2)
    print("3.",buffer3)
    print("4.",buffer4)
    print("5.",buffer5)
  else:
    print("ugly")
    
elif userChange == 2:
  print("Enter 1 to change the entire sentence\nEnter 2 to change a string\n")
  userAction = int(input())
  if userAction == 1:
    print("Enter the new sentence:\n")
    buffer2 = input()

    
elif userChange == 3:
  print("Enter 1 to change the entire sentence\nEnter 2 to change a string\n")
  userAction = int(input())
  if userAction == 1:
    print("Enter the new sentence:\n")
    buffer3 = input()

    
elif userChange == 4:
  print("Enter 1 to change the entire sentence\nEnter 2 to change a string\n")
  userAction = int(input())
  if userAction == 1:
    print("Enter the new sentence:\n")
    buffer4 = input()

    
elif userChange == 5:
  print("Enter 1 to change the entire sentence\nEnter 2 to change a string\n")
  userAction = int(input())
  if userAction == 1:
    print("Enter the new sentence:\n")
    buffer5 = input()
