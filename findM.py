##Give the c code for a function called findM that takes a character array (string)
##as a parameterand returns an integer that is the array index of the first occurence of an uppercase 'M'.
##If no 'M' is found the function should return -1.

def findM(string):
    index = 0
    
    for x in string:
        if x == 'M':
            return index
        index = index + 1
    return -1

string = 'DFSGDDMSWAG'
test = findM(string)
print(test)

