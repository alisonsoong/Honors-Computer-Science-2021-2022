#
# Alison Soong
#
# Test01 Responses
#

# for problem 22
import math

#
# prob19()
#

def prob19():
    x = eval(input("Enter a number: "))

    if x % 4 == 0:
        # divisible by four
        y = "a"
    elif x % 2 == 0:
        # otherwise, if only divisible by 2
        y = "b"
    elif x % 2 != 0:
        # if not divisible by 2 nor 4
        y = "c"

    print(y)

#
# prob20()
#

def prob20():
    sumOfSquares = 0 # accumulator variable
    numTerms = 0 # num terms
    curTerm = 0

    # loop through every 
    for num in range(101, 1000, 2):
        numTerms = numTerms+1
        # add the square of current positive triple digit odd number, num
        sumOfSquares = sumOfSquares + (num * num)
    
    average = sumOfSquares/numTerms
    print(average)

#
# prob21()
#

def prob21():
    # get input
    spider = input("Replace spider with: ")
    water = input("Replace water with: ")
    spout = input("Replace spout with: ")
    rain = input("Replace rain with: ")

    print("The Isty-Bitsy", spider, "crawled up the", water, spout + ",")
    print("Down came the", rain, "and washed the", spider, "out!")


#
# prob22()
#

def prob22():
    # heron's formula! yay!
    a,b,c = eval(input("Input the three sides of a triangle (separated with commas): "))

    
    # check triangle inequality
    if a + b <= c:
        # triangle inequality fails
        print("Error: triangle with sides " + str(a) + ", " + str(b) + ", and " + str(c) + " is not valid")
    elif b + c <= a:
        # triangle inequality fails
        print("Error: triangle with sides " + str(a) + ", " + str(b) + ", and " + str(c) + " is not valid")
    elif a + c <= b:
        # triangle inequality fails
        print("Error: triangle with sides " + str(a) + ", " + str(b) + ", and " + str(c) + " is not valid")
    else:
        # passes triangle inequality
        # get the area of the triangle to the hundredths place
        s = (a + b + c)/2 # semiperimeter
        area = math.sqrt(s * (s-a) * (s-b) * (s-c))
        print("Area of the triangle is:", round(area,2))
        
        # classify the triangle
        # assume that the user enters three positive integers from least to greatest
        # base case, the triangle is scalene
        typeOfTriangle = "scalene"

        if a == b:
            if b == c:
                typeOfTriangle = "equilateral"
            else:
                # b!=c, so a!=c
                typeOfTriangle = "isosceles"
        
        if b == c:
            if a == c:
                typeOfTriangle = "equilateral"
            else:
                # a!=c, so a!=b
                typeOfTriangle = "isosceles"

        if c == a:
            if a == b:
                typeOfTriangle = "equilateral"
            else:
                # b!=a, so b!=c
                typeOfTriangle = "isosceles"

        print("The triangle is", typeOfTriangle)
        
            
            
            

            
    

