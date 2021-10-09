#
# Alison Soong
#
# Lab 04: Graphics, QuadraticGUI
#

import math
from graphics import *

#There should be a “button” that the user clicks in order to perform
#   the calculation. The result of the calculation should either be
#   “no real solutions” or one or two solutions in the form “x = ”.
#   Solutions should be rounded to two decimal places.
#After the results are displayed on the window, the previous “button”
#   should now say “Quit” and close the window when it is clicked.

#
# Calcualtes the solution(s) to a quadratic equation in standard form
#   as entered by user in graphics window
#
def main():
    # introductory print statement
    print("This program calculates the solution(s) to a quadratic equation in standard" +
          " form according to coefficients entered by the user.")

    # create window and set coords
    win = GraphWin("Quadratic Equation Solver", 500, 500)
    win.setCoords(0,0,500,500)

    # set up the title
    title = Text(Point(250, 450), "Quadratic Equation Solver!")
    title.setSize(20)
    title.setFace("courier")
    title.setStyle("bold italic")
    title.draw(win)


    # standard form of quadratic equation
    standardForm = Text(Point(250, 400), "Standard form of a quadratic equation:\n"+
                        "Ax^2 + Bx + C")
    print("Standard form of a quadratic equation: Ax^2 + Bx + C")
    standardForm.setSize(15)
    standardForm.setFace("courier")
    standardForm.setStyle("italic")
    standardForm.draw(win)

    # get coefficients by user input
    # enter A
    promptA = Text(Point(250, 370), "Enter A:") # label to input coefficient A
    promptA.setFace("courier")
    promptA.setStyle("italic")
    promptA.draw(win)
    coefAEntry = Entry(Point(250, 350), 8)
    coefAEntry.draw(win)
    instructionsA = Text(Point(250, 330), "Click when done")
    instructionsA.setFace("courier")
    instructionsA.setStyle("italic")
    instructionsA.draw(win)
    win.getMouse()
    coefA = int(coefAEntry.getText()) # cast to integer
    print("A:", coefA)

    # enter B
    promptB = Text(Point(250, 310), "Enter B:") # label to input coefficient A
    promptB.setFace("courier")
    promptB.setStyle("italic")
    promptB.draw(win)
    coefBEntry = Entry(Point(250, 290), 8)
    coefBEntry.draw(win)
    instructionsB = Text(Point(250, 270), "Click when done")
    instructionsB.setFace("courier")
    instructionsB.setStyle("italic")
    instructionsB.draw(win)
    win.getMouse()
    coefB = int(coefBEntry.getText()) # cast to integer
    print("B:", coefB)
    
    # enter C
    promptC = Text(Point(250, 250), "Enter C:") # label to input coefficient A
    promptC.setFace("courier")
    promptC.setStyle("italic")
    promptC.draw(win)
    coefCEntry = Entry(Point(250, 230), 8)
    coefCEntry.draw(win)
    # calculate button
    button = Rectangle(Point(50, 50), Point(450, 100)) # create the box for button
    button.setFill("black")
    button.draw(win) # draw quit button's background
    buttonText = Text(Point(250,75), "Click Here to Calculate!") # create text for button
    buttonText.setTextColor("white")
    buttonText.setFace("courier")
    buttonText.setStyle("bold italic")
    buttonText.draw(win) # draw quit button's text
    
    win.getMouse()
    coefC = int(coefCEntry.getText()) # cast to integer
    print("C:", coefC)

    # solution label
    solLabel = Text(Point(250, 170), "Quadratic Equation Solver!")
    solLabel.setSize(16)
    solLabel.setFace("courier")
    solLabel.setStyle("bold italic")
    solLabel.draw(win)

    # calculate solutions, and output the solutions along with:
    #   if two solutions, if one solution, if no solutions
    
    disc = coefB * coefB - 4*coefA*coefC
    if disc < 0:
        # no solutions
        solution = Text(Point(250, 150), "No real solutions!")
        solution.draw(win)
    elif disc == 0:
        # one solution
        solution = Text(Point(250, 150), "x = " + str(round(-coefB/(2*coefA),2)))
        solution.draw(win)
    else:
        # two solutions
        solution1 = Text(Point(250, 150), "x = " + str(round((-coefB + math.sqrt(disc))/(2*coefA) + 0.0, 2)))
        solution1.draw(win)
        solution2 = Text(Point(250, 130), "x = " + str(round((-coefB - math.sqrt(disc))/(2*coefA) + 0.0, 2)))
        solution2.draw(win)
    
    # edit button to say quit
    buttonText.setText("Click here to quit")

    # close window once user clicks anywhere on window 
    win.getMouse()
    win.close()
    # quit message on shell
    print(".\n.\nProgram has quit")


main()
    

    


          
