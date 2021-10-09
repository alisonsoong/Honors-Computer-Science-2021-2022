#
# Alison Soong
#
# Lab 04: Graphics, AutoDepGUI
#

import math
from graphics import *

#
# Visualizes the depreciated value eof a car over the years
#   according to user input
#
def main():
    # introductory print statement
    print("This program visualizes the depreciated value of a car over the years")

    # the graphics window
    win = GraphWin("Depreciated Value of Car", 800, 600)
    win.setCoords(-50, -50, 850, 700)

    # get user input about car value
    carValueText = Text(Point(10, 650), "Car value:")
    carValueText.draw(win)
    instructionsText = Text(Point(100, 625), "Click once done")
    instructionsText.setSize(9)
    instructionsText.draw(win)
    carValueEntry = Entry(Point(100, 650), 10)
    carValueEntry.draw(win)

    # wait until user clicks, then get input
    win.getMouse()
    initCarValue = int(carValueEntry.getText())
    print("Initial car value: $" + str(initCarValue))


    # get user input about number of years
    yearsText = Text(Point(250, 650), "Number of years:")
    yearsText.draw(win)
    instructionsText.move(260,0)
    numYearsEntry = Entry(Point(360, 650), 10)
    numYearsEntry.draw(win)

    # wait until user clicks, then get input
    win.getMouse()
    numYears = int(numYearsEntry.getText())
    print("Number of years: " + str(numYears))


    # display information: text
    Text(Point(500, 650), "Depreciation rate: 15%").draw(win)

    # create graph

    # y axis and x axis drawing
    Line(Point(0,0), Point(0,600)).draw(win)
    Line(Point(0,0), Point(800,0)).draw(win)

    # create y axis markings
    Text(Point(-25, 600), str(round(initCarValue/1000, 1)) + " K").draw(win)

    incre = (initCarValue/1000)/4 # amount added per interval
    for i in range(4):
        Text(Point(-25, 600/4 * i), str(round(incre*i,1)) + " K").draw(win)
    
    # create x axis markings
    numBars = numYears + 1

    # put 5 pixels between each bar, so
    # ((795 - 5) - 5*numYears) / numBars = width of each bar
    width = (795-5-5*numYears)/numBars
    curX = 5

    # height is value/initCarValue * 600
    value = initCarValue
    for i in range(numBars):
        height = value/initCarValue * 600
        bar = Rectangle(Point(curX, height), Point(curX + width, 0))
        bar.setFill("grey")
        bar.draw(win)
        
        # update curX
        oldX = curX
        curX = curX + width + 5

        # create label for the bar
        Text(Point((oldX + curX - 5)/2, -25), i).draw(win)
        
        # update value of car
        value = value*85/100 # loses 15 percent of value

    # quit button
    quitButton = Rectangle(Point(600, 670), Point(800, 630))
    quitButton.draw(win)
    quitText = Text(Point(700, 650), "Click to quit")
    quitText.draw(win)

    # quit once user clicks
    win.getMouse()
    win.close()
    

main()
