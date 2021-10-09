#
# Alison Soong
#
# My cool solution for problem 3 of lab02
#

#
# Returns the nth triangular number
#
#     parameters:
#       n, an integer = the nth triangular number will be generated
#
def generateTriangular(n):
    # base case. if looking for the 0th triangular number, it should be 0.
    if (n==0):
        return 0
    
    # otherwise, get the sum of the current index and
    #   the sum of the previous triangular number
    return n + generateTriangular(n-1)

#
# Recursively prints the triangular numbers up to and including the nth one
#
#     parameters:
#       n, an integer = the first n triangular numbers will be outputted
#
def triangle(n):
    # introductory print statement 
    print("Recursively prints the triangular numbers up to and including the nth one.")
    print("***************************************************************")

    # generate 0-nth triangular numbers
    for i in range(n+1):
        # call the recursive function to generate the ith triangular number
        print(generateTriangular(i))
