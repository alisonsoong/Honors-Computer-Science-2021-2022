#
# Alison Soong
#
# Practice problems for chapter 1 (class)
#

#
# a function that prints out a personal greeting to name
#
#   parameters:
#       string name
#
def greeting(name):
    # NOTE: can use + instead of comma to get rid of the extra spaces 
    print("Hello earthling named " + name + ". Nice to meet you~")

def greeting2():
    # get string input from user
    name = input("My name is: ")
    
    # output
    print("Hello earthling named", name)

#
# a function that prints out the first n even natural numbers
#
#   parameters:
#       int n
#
def even(n):
    # for i in range(n):
    #    print(i*2)
    
    # variable to hold current even natural number to print
    numToPrint = 0

    # repeat n timese
    for i in range(n):
        # print value in numToPrint
        print(numToPrint)
        # update numToPrint to get the next even natural number
        numToPrint = numToPrint + 2

def even2():
    # get integer input from user.
    # input means that it is waiting for the user to enter something
    # eval converts the string input to an integer
    n = eval(input("How many even natural numbers do you want?: "))
    # can also do:
    #   userInput = input("How many even natural numbers do you want?: ")
    #   n = eval(userInput)

    # variable to hold current even natural number to print
    numToPrint = 0

    # repeat n timese
    for i in range(n):
        # print value in numToPrint
        print(numToPrint)
        # update numToPrint to get the next even natural number
        numToPrint = numToPrint + 2

