#
# Alison Soong
#
# HCS Lab 01: Python Basics
#

#
# Prints the International Air Transport Association airport code
#   for Sydney Airport in Australia (SYD)
#
#     parameters:
#       none
#
def airport():
    print(" ******  *     *  ****   ")
    print("**        *   *   *   ** ")
    print("***        * *    *    **")
    print(" *****      *     *     *")
    print("    ***     *     *    **")
    print("     **     *     *   ** ")
    print("******      *     ****   ")

#
# Simulates a MadLibs story based on user input
#
#     parameters:
#       none
#
def madLibs():
    # output welcome message and instructions
    print("----------------------- Welcome to MadLibs! -----------------------")
    print(" Answer the following prompts, and we'll generate a ~wild~ story!")
    print("-------------------------------------------------------------------")
    print("      Please do not include articles (like a/an, the, etc).")
    print("-------------------------------------------------------------------")
    
    # getting user inputs and storing them in descriptively named variables
    familyMember = input("A member of your family: ")
    furnitureAdj = input("An adjective: ")
    furniture = input("A piece of furniture: ")
    bodyPart = input("A body part: ")
    celebrity = input("A celebrity: ")
    friendOfCelebrity = input("A movie character: ")
    numberOfFeet = input("A number (ex: write as 'three,' not 3): ")
    emotion  = input("An emotion: ")
    food = input("A food item or dish: ")
    foodAdj = input("Another adjective: ")
        
    # creative element to make it seem like the program is "generating" the story!
    print("-------------------------------------------------------------------")
    print("Generating...")
    print("...")
    print("...")
    print("...")
    print("...")
    print("...done!")
    
    # display the story
    print("--------------------- An Adventure Into IKEA! ---------------------")
    print("One day, I decided to go to IKEA with " + familyMember+ ". We wanted to buy")
    print("a(n)", furnitureAdj, furniture + ", and we decided that IKEA would be the best")
    print("place to look!")
    print() # next paragraph
    print("Right as we entered IKEA, we realized that the store was incredibly")
    print("crowded! While trying to navigate through the crowd, I stubbed")
    print("my", bodyPart,"on a", furniture,"and was caught off balance. I will")
    print("never forget what happened next! As I proceeded to fall, I ")
    print("knocked someone over! And when I looked up, I saw that it was...")
    print(celebrity + "?!")
    print() # next paragraph
    print("Luckily, " + celebrity + "'s friend, " + friendOfCelebrity + ", helped me get back")
    print("onto my " + numberOfFeet + " feet, but I couldn't help but feel " + emotion + ".")
    print("However, even though I was the one who knocked into them, they")
    print("asked if we wanted to join them in eating IKEA's famous " + food)
    print("at the cafeteria. It was absolutely " + foodAdj + "!")
    print() # next paragraph
    print("Though our adventure into IKEA started off rocky, we left with some")
    print("great memories!")
    print() # next paragraph
    print("The End!")


#
# Calculates the sum of the first n even positive integers numbers
#
#     parameters:
#       n, an integer: the number of positive integer numbers summed
#
def sumOfEven(n):
    # holds the sum of the first n even positive integers
    result = 0

    # keeps track of the current even number that will be added
    # starts with 2 because we are not counting 0 as an even number
    #   for this program specifically
    curEvenNum = 2

    # loops n times
    for i in range(n):
        # add the current even positive integer to result
        result = result + curEvenNum
        # update curEvenNum to the next even number
        curEvenNum = curEvenNum + 2
        
    # print message and result
    print("The sum of the first", n, "even numbers is", result)


    

