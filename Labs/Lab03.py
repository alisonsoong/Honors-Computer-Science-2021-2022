#
# Alison Soong
#
# Lab 03: Operators and Branching
#

# to access all methods in the math library
import math

#
# Outputs four relationships between two points
#
#   parameters:
#       none
#
def points():
    # introductory print statement
    print("Welcome to the Equation Center!!")

    # get user input for two points
    x1, y1 = eval(input("Enter the coordinates of point A as x,y: "))
    x2, y2 = eval(input("Enter the coordinates of point B as x,y: "))

    print("****************************************************")

    # --- slope ---
    # get the rise and run
    rise = y2-y1
    run = x2-x1

    # check if it's a vertical line
    if run == 0:
        # a vertical line, thus the slope is undefined
        print("The slope of the line is undefined")
    else:
        slope = round(rise/run,2) # round to 2 decimal points
        slope = slope + 0.0 # this somehow fixes the negative 0.0 problem!
        # output the slope of the line
        print("The slope of the line is " + str(slope))

    # --- distance ---
    # get the difference in x and y coordinatese
    deltaY = y2-y1
    deltaX = x2-x1
    
    # use the distance formula
    distance = math.sqrt(deltaY*deltaY + deltaX*deltaX)
    distance = round(distance, 2) # round to 2 decimal points
    
    # output the distance
    print("The distance between points is " + str(distance))

    # --- equation ---
    print("The equation of the line is ", end="")

    # check if the equation is for a vertical, horizontal, or regular line
    if deltaX == 0:
        # a vertical line (or two equal points)
        
        if deltaY == 0:
            # then the two points were the same
            print("The two points are the same")
        else:
            # a vertical line: the equation is x = ___
            print("x = " + str(x1) + " (There is no slope).")

    elif deltaY == 0:
        # a horizontal line: the equation is y = ___
        print("y = " + str(y1))

    else: # slope is defined
        # calculate the slope
        slope = round(rise/run,2) # round to 2 decimal points

        # calculate the y-intercept
        yIntercept = y1 - slope * x1
        yIntercept = round(yIntercept, 2) # round to 2 decimal points

        # output formatting
        if yIntercept < 0:
            print("y = " + str(slope) + "x" + " - " + str(abs(yIntercept)))
        elif yIntercept > 0:
            print("y = " + str(slope) + "x" + " + " + str(yIntercept))
        else: # equal to 0
            # I do not like how the 0.0 looks, so I am getting rid of it
            print("y = " + str(slope) + "x")

    # --- angle of rotation ---
    # positive angles mean the rotation from A to B is counterclockwise
    
    # the difference between the arctan of the y-coord/x-coord of pointB
    #   and that of pointA (using atan2, which conserves the angle's quadrant)
    angle = math.degrees(math.atan2(x1, y1) - math.atan2(x2, y2))
    # used math.atan2 to get the correct quadrant
    angle = round(angle,2) # round
    # output the angle
    print("The angle of rotation about the origin from A to B is", angle, "degrees.")

    print("Thanks for visiting!")
    

#
# Determines if a given year is a leap year
#
#   parameters:
#       none
#
def leap():
    # introductory print statement
    print("This program will determine if a given year is a leap year.")
    print("*****************************************")

    # get user input
    year = eval(input("Year (a positive integer): "))

    # determine if user input is invalid (a positive integer)
    if year > 0:
        # valid input
        if year % 400 == 0:
            # a year divisible by 400 is a leap year
            print(year, "is a leap year!")
        elif year % 4 == 0:
            if year % 100 == 0:
                # a year divisible by 4 AND by 100 is NOT a leap year
                print(year, "is NOT a leap year!")
            else:
                # a year divisible by 4 but NOT by 100 is a leap year
                print(year, "is a leap year!")
        else:
            # otherwise, the year is not a leap year
            print(year, "is NOT a leap year.")
    else:
        # invalid input
        print("User input is invalid")

#
# Gives highest, lowest, and average test score
#
#   parameters:
#       none
#
def testScores():
    # introductory print statement
    print("Welcome to the test center!", end=" ")

    # get numbers of tests
    numTests = eval(input("How many tests are there? "))

    print()

    # variables to hold highest score, lowest score, and sum of scores
    maxScore = 0 # start with lowest score possible
    minScore = 100 # start with the highest score possible
    sumScore = 0

    # get score of tests numTests times 
    for i in range(numTests):
        # get user input for score
        curScore = eval(input("Enter the score for test " + str(i+1) + ": "))
        # add to sum
        sumScore = sumScore + curScore
        # check if this is the minimum score
        if curScore < minScore:
            # then this is the new min score
            minScore = curScore
        # check if this is the maximum score
        if curScore > maxScore:
            # then this is the new max score
            maxScore = curScore

    # calculate the average score
    avgScore = round(sumScore/numTests, 2)

    # figure out letter grade
    letterGrade = "F"
    if avgScore >= 90:
        letterGrade = "A"
    elif avgScore >= 80:
        letterGrade = "B"
    elif avgScore >= 70:
        letterGrade = "C"
    elif avgScore >= 60:
        letterGrade = "D"
    else:
        # score below 60 is an F
        letterGrade = "F"

    # output results
    print("\nYour high score was", maxScore)
    print("Your low score was", minScore)
    print("Your test average is", avgScore, "(This is in the", letterGrade, "range)")
    print("\nThanks for visiting!")
    
    

            
            
        
        
    
    




    
