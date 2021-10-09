#
# Alison Soong
#
# Lab 02: Writing Programs
#


#
# Ouputs nicely formatted personal information as entered by user
#
#     parameters:
#       none
#
def address():
    # introductory print statement 
    print("This program ouputs your personal information in a readable format.")
    print("Please enter your personal information:")
    print("***************************************************************")

    # get user input
    address = input("Enter your street address: ")
    city = input("Enter your city: ")
    state = input("Enter your state abbreviation: ")
    zipCode = input("Enter your zip code: ")
    birthMonth = input("Enter your birth month: ")
    birthDay = input("Enter your birth day: ")
    birthYear = input("Enter your birth year: ")
    areaCode = input("Enter your area code: ")
    phoneNumber = input("Enter your phone number: ")

    print("***************************************************************")
    # output user input in a nice format
    print("Your Address:")
    print(address)
    # a comma and a single space after the city name
    # and three spaces after state and before the zip code
    print(city + ", " + state + "   " + zipCode)
    # dashes in the birthday
    print("Your birthday: " + birthMonth + "-" + birthDay + "-" + birthYear)
    # parentheses around the area code in the phone number
    print("Your phone number: (" + areaCode + ") " + phoneNumber)
    
#
# Converts three measures into the metric system
#
#     parameters:
#       none
#
def metric():
    # introductory print statement 
    print("Welcome to the Metric Conversion Center.")
    
    # get user input
    weight = eval(input("Please enter your weight in pounds: "))
    feet, inches = eval(input("Please enter your height in feet and inches, separated by a comma: "))
    temperature = eval(input("Please enter your body temperature in degrees Fahrenheit: "))

    # converting values into metric system:
    # weight: 1 lb = 0.453592 kg
    metricWeight = weight * 0.453592

    # height: first calculate total height in inches
    totalHeight = feet * 12 + inches
    # 1 in = 0.0254 meters
    metricHeight = totalHeight * 0.0254

    # temperature: C = (F-32) * (5/9)
    metricTemp = (temperature-32) * (5/9)
    
    print("***************************************************************")

    # outputing metric values
    print("Your weight is", metricWeight, "kilograms.")
    print("Your height is", metricHeight, "meters.")
    print("Your body temperature is", metricTemp, "degrees Celsius.")
    print("Thanks for visiting!")
    
    

#
# Prints the triangular numbers up to and including the nth one (using the
#   recursive definition of triangular numbers)
#
#     parameters:
#       n, an integer = the first n triangular numbers will be outputted
#
def triangle(n):
    # introductory print statement 
    print("Prints triangular numbers up to and including the", n, end="")
    print("th/nd/rd one.")
    print("*****************************************************************")

    # holds the current sum of natural numbers
    curSum = 0
    
    # generate 0-nth triangular numbers
    # need to loop n+1 times
    for i in range(n+1):
        # update the current sum by adding the next natural number
        curSum = curSum + i
        # output the current sum
        print(curSum)
        


#
# Finds the vertex of a quadratic function written in standard form
#
#     parameters:
#       none
#
def vertex():
    # introductory print statement 
    print("This program finds the vertex of a quadratic function.")
    print("***************************************************************")

    # get user input for coefficients
    print("Please enter the coefficients of f(x) = ax^2 + bx + c.")
    coefficientA = eval(input("Coefficient a: "))
    coefficientB = eval(input("Coefficient b: "))
    coefficientC = eval(input("Coefficient c: "))
    print("***************************************************************")

    # calculate the vertex
    # x coordinate of vertex is at -b/(2a)
    xCoord = -(coefficientB)/(2*coefficientA)
    
    
    # y coordinate of vertex can be found by plugging in x coord into function
    yCoord = coefficientA * (xCoord**2) + coefficientB * xCoord + coefficientC
    
    # output the vertex
    print("Your vertex is at (", end = "")
    print(xCoord, end = ", ")
    print(yCoord, end = ").")
    
    
    
    
