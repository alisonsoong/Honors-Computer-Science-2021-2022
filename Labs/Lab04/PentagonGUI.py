#
# Alison Soong
#
# Lab 04: Graphics, PentagonGUI
#

import math
from graphics import *


#
# Finds the area of a pentagon, in square pixels, as drawn
#   by user in a graphics window
#
def main():
    # introductory statement
    print("This program finds the area, in square pixels,\n"
          + "of a pentagon as drawn by the user.")
    
    # create the window
    win = GraphWin("Area of Pentagon", 800,600)
    win.setCoords(0,0,800,600) 

    # set up the title
    title = Text(Point(400, 575), "Draw a pentagon, and we'll calculate its area!")
    title.setSize(20)
    title.setFace("courier")
    title.setStyle("bold italic")
    title.draw(win)

    # total area
    totalArea = 0
    
    # get points and draw points
    p1 = win.getMouse()
    p1.draw(win)
    
    p2 = win.getMouse()
    p2.draw(win)
    # draw line
    Line(p1, p2).draw(win)
    
    p3 = win.getMouse()
    p3.draw(win)
    # draw line
    Line(p2, p3).draw(win)
    
    p4 = win.getMouse()
    p4.draw(win)
    # draw line
    Line(p3, p4).draw(win)
    
    p5 = win.getMouse()
    p5.draw(win)
    # draw line
    Line(p4, p5).draw(win)

    # draw line
    Line(p5, p1).draw(win)

    # make polygon
    pentagon = Polygon(p1, p2, p3, p4, p5)
    pentagon.setFill(color_rgb(100, 140, 140))
    pentagon.draw(win)

    # get side lengths
    # side 1 is from p1 to p2
    s1 = math.sqrt(abs(p1.getX() - p2.getX())**2 + abs(p1.getY() - p2.getY())**2)

    # side 2 is from p2 to p3
    s2 = math.sqrt(abs(p2.getX() - p3.getX())**2 + abs(p2.getY() - p3.getY())**2)

    # side 3 is from p3 to p4
    s3 = math.sqrt(abs(p3.getX() - p4.getX())**2 + abs(p3.getY() - p4.getY())**2)

    # side 4 is from p4 to p5
    s4 = math.sqrt(abs(p4.getX() - p5.getX())**2 + abs(p4.getY() - p5.getY())**2)

    # side 5 is from p5 to p1
    s5 = math.sqrt(abs(p5.getX() - p1.getX())**2 + abs(p5.getY() - p1.getY())**2)

    # diagonal 1 is from p3 to p1
    d1 = math.sqrt(abs(p3.getX() - p1.getX())**2 + abs(p3.getY() - p1.getY())**2)

    # diagonal 2 is from p4 to p1
    d2 = math.sqrt(abs(p4.getX() - p1.getX())**2 + abs(p4.getY() - p1.getY())**2)
    
    # get the area of the entire pentagon by finding area of three triangles
    #   using heron's formula:
    # get the area of triangle s1-s2-d1
    semi = (s1 + s2 + d1)/2 # semiperimeter
    area1 = math.sqrt(semi * (semi - s1) * (semi - s2) * (semi - d1))
    
    # get the area of triangle d1-d2-s3
    semi = (d1 + d2 + s3)/2 # semiperimeter
    area2 = math.sqrt(semi * (semi - d1) * (semi - d2) * (semi - s3))
    
    # get the area of triangle s4-s5-d2
    semi = (s4 + s5 + d2)/2 # semiperimeter
    area3 = math.sqrt(semi * (semi - s4) * (semi - s5) * (semi - d2))

    # add all areas
    totalArea = area1 + area2 + area3
    

    # create the label that will show the area of the pentagon
    areaLabelBox = Rectangle(Point(50, 550), Point(250, 500)) # create label box
    areaLabelBox.setFill("gray")
    areaLabelBox.draw(win) # draw area text background
    
    areaLabel = Text(Point(150, 525), "Area:") # create label that will show final ans
    areaLabel.setTextColor("white")
    areaLabel.setFace("courier")
    areaLabel.setSize(10)
    areaLabel.draw(win) # draw area text label
    
    # update the area label
    areaLabel.setText("Area: " + str(round(totalArea,2)) + " square pixels") 

    # display a ”quit button” and have the window close after a mouse click
    quitButton = Rectangle(Point(300, 550), Point(500, 500)) # create the box for button
    quitButton.setFill("black")
    quitButton.draw(win) # draw quit button's background
    quitText = Text(Point(400,525), "Click Here to Quit") # create text for button
    quitText.setTextColor("white")
    quitText.setFace("courier")
    quitText.setStyle("bold italic")
    quitText.draw(win) # draw quit button's text

    # legend
    legendBox = Rectangle(Point(550, 550), Point(750, 500))
    pentagonColor = Rectangle(Point(560, 540), Point(620, 510))
    pentagonColor.setFill(color_rgb(100, 140, 140))
    legendText = Text(Point(680, 525), " = your pentagon!")
    legendText.setFace("courier")
    legendText.setStyle("bold italic")

    # draw legend
    legendText.draw(win)
    pentagonColor.draw(win)
    legendBox.draw(win)
    

    # print info (for debugging purposes)
    print("--------------------------------------------------------------")
    print("P1: (" + str(p1.getX()) + ", " + str(p1.getY()) + ")")
    print("P2: (" + str(p2.getX()) + ", " + str(p2.getY()) + ")")
    print("P3: (" + str(p3.getX()) + ", " + str(p3.getY()) + ")")
    print("P4: (" + str(p4.getX()) + ", " + str(p4.getY()) + ")")
    print("P5: (" + str(p5.getX()) + ", " + str(p5.getY()) + ")")
    print("--------------------------------------------------------------")    
    print("side 1 (P1->P2): " + str(s1))
    print("side 2 (P2->P3): " + str(s2))
    print("side 3 (P3->P4): " + str(s3))
    print("side 4 (P4->P5): " + str(s4))
    print("side 5 (P5->P1): " + str(s5))
    print("--------------------------------------------------------------")
    print("diagonal 1 (P3->P1): " + str(d1))
    print("diagonal 2 (P4->P1): " + str(d2))
    print("--------------------------------------------------------------")
    print("area 1 (s1-s2-d1): " + str(area1))
    print("area 2 (d1-d2-s3): " + str(area2))
    print("area 3 (s4-s5-d2): " + str(area3))
    print("--------------------------------------------------------------")
    print("total area: " + str(totalArea))
    print("--------------------------------------------------------------")
    
    # wait until user clicks, and then close the graphics window
    win.getMouse()
    win.close()

    # quit message on shell
    print(".\n.\nProgram has quit")

main()
    
