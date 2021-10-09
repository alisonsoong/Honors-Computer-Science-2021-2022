#
# Alison Soong
#
# Class Practice Problems and notes
#

# comments from Lab01:
# - be descriptive with code: variable names, print statements, and comments.
#       Explain what the variable you are creating stands for.
#       In comments, include how and why versus what.
# - Carefully follow the assignment specs (what needs params vs not)
#       Also, upper and lower case functions names and parameters.
#       Just follow the instructions, usually camel case
# - 

#
# Converts miles to kilometers
#
#   parameters:
#       none
#
def convert():
    # introduction
    print("This program will convert a value in miles to kilometers")

    # get user input
    miles = eval(input("Enter a value in miles: "))

    # calculate
    conversion = 1.60934
    kilometers = miles * conversion

    # print out result
    print(miles, "miles is equivalent to", kilometers, "kilometers.")


#
# Counts down from x to 1 all in the same line, then prints a statement
#
#   parameters:
#       x, an integer = number of numbers that will be printed
#
def countdown(x):
    # introduction
    print("Starting the countdown!")

    # loop x times
    for i in range(x):
        print(x-i, end=" ")

    # print statement
    print()
    print("Happy new year!")

#
# Calculates the cell phone bill based on user's usage of phone
#
#   parameters:
#       none
#
def phoneBill():
    # introduction
    print("this program will calculate your cell phone bill based on")
    print("the fixed charge of 4 cents per minute for calls and")
    print("5 cents per text message.")

    # get user input
    monthlyRate = eval(input("Flat monthly rate for cell phone carrier plan: "))
    numMinutes = eval(input("Number of minutes used for calls: "))
    numTexts = eval(input("Number of text messages sent: "))

    # calculate result
    result = monthlyRate + (0.04*numMinutes) + (0.05*numTexts)

    # output result
    print("You owe", result, "dollars")


#
# Calculates the cell phone bill based on user's usage of phone and differing
#   text message rate
#
#   parameters:
#       none
#
def phoneBill2():
    # introduction
    print("this program will calculate your cell phone bill based on")
    print("the fixed charge of 4 cents per minute for calls and")
    print("varying rates for text messages sent.")

    # get user input
    monthlyRate = eval(input("Flat monthly rate for cell phone carrier plan: "))
    numMinutes = eval(input("Number of minutes used for calls: "))
    numTexts = eval(input("Number of text messages sent: "))

    # loop through varying text message rates
    rate = 0
    for i in range(10):
        # increment the rate of text messages
        rate = rate+1
        # calculate the result
        result = monthlyRate + (0.04*numMinutes) + (rate/100*numTexts)

        # output result
        print("For a rate of", rate, "cents per text message cent,")
        print("your total cell phone bill is", result,"dollars.")
        print()

#
# Prints the sum of the sum of the squares of the digits of a positive integer
#
#   parameters:
#       none
#
def sumOfDigitsSquared():
     # introduction
    print("this program will calculate the sum of the squares of the digits")
    print("of a positive integer.")

    # get user input and store in n
    curNum = eval(input("Input a positive integer: "))
    originalNum = curNum

    # result will hold the sum of the squares of the digits
    result = 0

    # loop through the digits of the integer
    # assume that the user won't enter a number less than 20 digits long
    for i in range(20):
        # get the rightmost digit
        curDigit = int(curNum % 10)
        # divide n by 10 to shorten the number by one digit
        curNum = int(curNum/10)
        # add the square of the digit to the result
        result = result + curDigit**2

    # print result
    print("The sum of the squares of the digits of", originalNum, "is:")
    print(result)
        

def sumOfDigitsSquaredBetter():
    print("this program will calculate the sum of the squares of the digits")
    print("of a positive integer.")

    # get user input and store in n
    num = str(input("Input a positive integer: "))

    # result will hold the sum of the squares of the digits
    result = 0

    for char in num:
        curDigit = int(char)
        result = result + curDigit * curDigit

    
    # print result
    print("The sum of the squares of the digits of", num, "is:", end=" ")
    print(result)
    
    






