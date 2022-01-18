# Alison
# Test03


# Problem 1, Collatz sequence
def collatz(start):
    # starting value start, assume it is a positive integer
    result = []
    a = start
    result.append(a) # add the start value

    while a != 1:
        if a % 2 == 0:
            # if a is even, next is a/2
            a = a//2 # can use integer division because guaranteed
            # a is even
            result.append(a)
        else:
            # if a is odd, next is 3a+1
            a = 3*a+1
            result.append(a)

    return result 
        
        
    

# Problem 2, Day of Year
def dayOfYear(month,day):
    # we may assume that the year is NOT a leap year
    # we can assume the inputs will be positive integers, but may not actually be valid dates
    # however, we CAN'T assume that the inputs will be valid dates (like 15,15)

    # 4, 6, 9, 11 have 30
    # 2 has 28, the rest have 31
    daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # NOTE indexing is backwards
    
    try:
        # check if invalid dates
        # invalid month:
        getDaysInMonth = daysInMonth[month-1]

        # invalid days
        if not(1<=day<=getDaysInMonth):
            day = 5/0 # forces an error

        # both are valid, continue on!
        result = 0

        if month == 1:
            result = day
        else:
            result += day
            for curMonth in range(month-1):
                result += daysInMonth[curMonth]

        return result, ""

    except:
        return -1, "The numbers entered do not represent a valid date."


# Problem 3, Compute GPA
def computeGPA():
    # get user input
    try:
        # get file name and open it 
        fileName = input("What is the file name?: ")
        inFile = open(fileName, 'r')

        result = 0
        count = 0
        for line in inFile:

            # only remove the \n if there is an entry on this line
            if line[-1] == "\n":
                line = line[:-1]
                
            adjustment = 0 # adjustment. 0 if regular, +0.3 for +, -0.3 for -
            if len(line) == 2:
                # there is a minus or a plus
                if line[1] == "-":
                    adjustment = -0.3
                else:
                    adjustment = 0.3

            # add adjustment
            result += adjustment

            # add to GPA
            if line[0] == "A":
                result += 4.0
            elif line[0] == "B":
                result += 3.0
            elif line[0] == "C":
                result += 2.0
            elif line[0] == "D":
                result += 1.0
            else:
                result += 0.0 # it's an F

            # number of grades increment by one
            count += 1

        # divide result by number of grades
        result = result/count

        # close file
        inFile.close()

        # reutrn result rounded to two decimal values
        return round(result,2)

    except:
        print("Something went wrong (ex: the file was empty)")
        return -1


def main():
    # testing collatz
    print(collatz(7))

    # testing dayOfYear
    days, result = dayOfYear(15,15)
    print(days,result)
    days, result = dayOfYear(10,15)
    print(days,result)
    days, result = dayOfYear(1,31)
    print(days,result)
    days, result = dayOfYear(1,32)
    print(days,result)
    days, result = dayOfYear(12,31)
    print(days,result)

    # testing computeGPA
    print(computeGPA())


main()
