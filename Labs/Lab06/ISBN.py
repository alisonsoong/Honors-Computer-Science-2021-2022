#
# Alison Soong
# 
# ISBN.py
#

from graphics import *
from Button import Button

def ISBN():
    print("------This program returns what ISBN values are valid or invalid!------")

    # get the input file name
    fileName = input("Please enter the input file's name (with .py): ")
    # make sure file name ends with .py
    if not(fileName[-3:] == ".py"):
        fileName += ".py"

    # open the file and read the lines, storing it in a list called toCheck
    inputValue = open(fileName, 'r')
    toCheck = inputValue.readlines()
    inputValue.close()
    
    # empty file, end
    if len(toCheck) == 0:
        print("The input file is empty! There is nothing to check. Goodbye!")
        return

    # if the file is not empty, ask for output file name
    outputName = input("Please enter the desired output file's name (with .py): ")
    # make sure file name ends with .py
    if not(outputName[-3:] == ".py"):
        outputName += ".py"

    outputFile = open(outputName, 'w')


    # otherwise if not an empty file, check all values and store them in
    # valid or invalid lists
    
    valid = []
    invalid = []
    invalidReason = [] # reason for string at index i being invalid

    # check each line to see if it's a valid ISBN
    for string in toCheck:
        # slice off the \n
        string = string[:-1]
        
        print(string) # for testing purposes
        
        if len(string) > 10:
            invalid.append(string)
            invalidReason.append("too long to be a valid ISBN!")
            continue
        elif len(string) < 10:
            invalid.append(string)
            invalidReason.append("too short to be a valid ISBN!")
            continue

        # by now, the string has been guaranteed to be 10 characters long
        print("String is 10 long")

        # a flag to tell us if we're done
        flag = False

        # now check: Characters 1-9 must be a digit (0-9)
        counter = 1
        for char in string:
            
            if counter == 10:
                # Character 10 must be a digit or the letter ‘X’ (upper or lowercase)
                if not(char == 'X' or char  == 'x' or "0" <= char <= "9"):
                    invalid.append(string)
                    invalidReason.append("last digit is not x, X, or a value from 0-9.")
                    flag = True
                    break
            else: # checking characters 1-9
                if not("0" <= char <= "9"):
                    invalid.append(string)
                    invalidReason.append("not all of the first 9 characters are digits between 0 and 9.")
                    flag = True
                    break
                
            counter += 1

        # if it didn't pass the above test (constraints on type of characters)
        #   then skip the rest of this body
        if flag:
            continue

        # otherwise, we can continue to do the last check
        
        # (10c1 + 9c2 + 8c3 + 7c4 + 6c5 + 5c6 + 4c7 + 3c8 + 2c9 + c10) % 11 = 0
        # get first part of equation: (10c1 + 9c2 + 8c3 + 7c4 + 6c5 + 5c6 + 4c7 + 3c8 + 2c9 + c10)
        # by now, the string is guaranteed to have integer characters
        #   except for the last character
        part1 = 0
        for i in range(10):
            if string[i] == "x" or string[i] == "X":
                # check if char[i] == "X" or "x"
                part1 += 10 # only happens at the very end, will only add 10
            else: 
                part1 += (10-i) * int(string[i]) # convert the character to an int

        # does not satisfy the formula
        if not(part1 % 11 == 0):
            invalid.append(string)
            invalidReason.append("it does not satisfy the formula, (10c1 + 9c2 + 8c3 + 7c4 + 6c5 + 5c6 + 4c7 + 3c8 + 2c9 + c10) % 11 = 0")
            continue    
                
            
        # if all the above tests are satisfied, add it to the valid list
        valid.append(string)
            

    print("\nThe input file has been read! Calculating...")
    print("...")
    print("...")
    print("...")
    print("...")
    print("...")
    print("\n-------Valid ISBNs-------", file=outputFile)
    for string in valid:
        print(string, file=outputFile)
    print("\n-------------------------", file=outputFile)
    print("\n------Invalid ISBNs------", file=outputFile)
    for i in range(len(invalid)):
        print(invalid[i] + " - Reason for being invalid: " + invalidReason[i], file=outputFile)

    print("\nProgram is complete! See you next time!")

    outputFile.close()



def main():
    ISBN()


# this line calls the test function only when running this module
if __name__ == "__main__": main() # equivalent to main() as long as we are running this modulee
