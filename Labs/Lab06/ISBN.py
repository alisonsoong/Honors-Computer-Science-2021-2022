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
    fileName = input("Please enter the input file's name: ")

    # open the file and read the lines, storing it in a list called toCheck
    inputValue = open(fileName, 'r')
    toCheck = inputValue.readlines()
    
    # empty file, end
    if len(toCheck) == 0:
        print("The input file is empty! There is nothing to check. Goodbye!")
        return

    # otherwise if not an empty file, check all values and store them in
    # valid or invalid lists
    
    valid = []
    invalid = []
    invalidReason = [] # reason for string at index i being invalid

    # check each line to see if it's a valid ISBN
    for string in toCheck:
        # slice off the \n
        string = string[:-1]
        
        # print(string) # for testing purposes
        
        if len(string) > 10:
            invalid.append(string)
            invalidReason.append("This string is too long to be a valid ISBN!")
            continue
        elif len(string) < 10:
            invalid.append(string)
            invalidReason.append("This string is too short to be a valid ISBN!")
            continue

        
        
        

    print("The input file has been read! Calculating...")
    print("...")
    print("...")
    print("...")
    print("...")
    print("...")
    print("\n-------Valid ISBNs-------")
    for string in valid:
        print(string)
    print("\n-------------------------")
    print("\n------Invalid ISBNs------")
    for i in range(len(invalid)):
        print(invalid[i] + " - " + invalidReason[i])

    print("\nProgram is complete! See you next time!")

    

    
        
    
    
    

def main():
    ISBN()


# this line calls the test function only when running this module
if __name__ == "__main__": main() # equivalent to main() as long as we are running this modulee
