#
# Alison Soong
#
# Lab 04: Graphics, BookmarkGUI
#

import math
from graphics import *

#
# A bookmark that utilizes all elements of the graphics.py library!
#
def main():
    # introductory print statement
    print("I hope you enjoy my bookmark!")

    # create graphics window and set coords
    win = GraphWin("Alison's Bookmark", 250, 600)
    win.setCoords(0,0,250,600)

    # a beach!

    # the sky
    # ------Rectangle-------
    sky = Rectangle(Point(0,600), Point(250, 0))
    sky.setFill(color_rgb(230, 242, 242))
    sky.setOutline(color_rgb(230, 242, 242))
    sky.draw(win)
    
    # waves, circles
    for j in range(8):
        if j % 2 == 0:
            for i in range(11):
                # ------Circle-------
                wave = Circle(Point(i*25, 300-30*j), 25)
                if i % 2 == 0: # to "randomize" the colors!
                    wave.setFill(color_rgb(196, 239, 245))
                    wave.setOutline(color_rgb(196, 239, 245))
                elif i % 3 == 0:
                    wave.setFill(color_rgb(168, 220, 227))
                    wave.setOutline(color_rgb(168, 220, 227))
                else:
                    wave.setFill(color_rgb(143, 209, 217))
                    wave.setOutline(color_rgb(143, 209, 217))
                wave.draw(win)
        else:
            for i in range(11):
                wave = Circle(Point(250-i*25, 300-30*j), 25)
                if i % 2 == 0: # to "randomize" the colors!
                    wave.setFill(color_rgb(168, 220, 227))
                    wave.setOutline(color_rgb(168, 220, 227))
                    
                elif i % 3 == 0:
                    wave.setFill(color_rgb(143, 209, 217))
                    wave.setOutline(color_rgb(143, 209, 217))
                else:
                    wave.setFill(color_rgb(196, 239, 245))
                    wave.setOutline(color_rgb(196, 239, 245))
                wave.draw(win)
        
    
    # sand, a rectangle
    # ------Rectangle-------
    sand = Rectangle(Point(0,100), Point(350, 0))
    sand.setFill(color_rgb(224, 209, 146))
    sand.setOutline(color_rgb(224, 209, 146))
    sand.draw(win)

    # I used this to "draw" and find the points for the umbrella
    #for i in range(20):
    #   p = win.getMouse()
    #   p.draw(win)
    #   print("("+str(p.getX())+","+str(p.getY()))

    # creating the umbrella!
    # outer umbrella
    # ------Point-------
    p1 = Point(43.17269076305221,169.2821368948247)
    p2 = Point(39.1566265060241,93.15525876460771)
    p3 = Point(121.48594377510041,128.21368948247078)
    p4 = Point(140.56224899598394,182.30383973288815)
    p5 = Point(101.40562248995984,197.32888146911517)
    p6 = Point(55.22088353413655,198.330550918197)
    p7 = Point(1.0040160642570282,172.2871452420701)
    p8 = Point(-20.0040160642570282,110.21368948247078)
    p1.setFill("grey")
    p2.setFill("grey")
    p3.setFill("grey")
    p4.setFill("grey")
    p5.setFill("grey")
    p6.setFill("grey")
    p7.setFill("grey")
    p8.setFill("grey")
    p1.draw(win)
    p2.draw(win)
    p3.draw(win)
    p4.draw(win)
    p5.draw(win)
    p6.draw(win)
    p7.draw(win)
    
    # draw the shapeso of the umbrella using polygons
    # ------Polygon-------
    # base of the umbrella
    base = Polygon(p2, p3, p4, p5, p6, p7, p8)
    base.setFill("white")
    base.setOutline("white")
    base.draw(win)
    # create the shadow
    # ------Clone-------
    shadow = base.clone()
    shadow.move(20, -100)
    shadow.setFill(color_rgb(201, 187, 135))
    shadow.setOutline(color_rgb(201, 187, 135))
    shadow.draw(win)
    
    # ------Line-------
    # draw umbrella stick
    stick = Line(p1, Point(80, 60))
    stick.setFill("grey")
    stick.setWidth(3)
    stick.draw(win)
    
    # draw outer lines of umbrella
    outer1 = Line(p2, p3)
    outer2 = Line(p3, p4)
    outer3 = Line(p4, p5)
    outer4 = Line(p5, p6)
    outer5 = Line(p6, p7)
    outer6 = Line(p7, p8)
    outer7 = Line(p8, p2)
    outer1.setFill("white")
    outer2.setFill("white")
    outer3.setFill("white")
    outer4.setFill("white")
    outer5.setFill("white")
    outer6.setFill("white")
    outer7.setFill("white")
    outer1.draw(win)
    outer2.draw(win)
    outer3.draw(win)
    outer4.draw(win)
    outer5.draw(win)
    outer6.draw(win)
    outer7.draw(win)

    # inner lines of umbrella
    inner1 = Line(p1, p2)
    inner2 = Line(p1, p3)
    inner3 = Line(p1, p4)
    inner4 = Line(p1, p5)
    inner5 = Line(p1, p6)
    inner6 = Line(p1, p7)
    inner7 = Line(p1, p8)

    # draw the inner polygons
    section1 = Polygon(p1, p2, p3)
    section1.setFill(color_rgb(222, 126, 106))
    section1.setOutline(color_rgb(222, 126, 106))
    section2 = Polygon(p1, p3, p4)
    section2.setFill("white")
    section2.setOutline("white")
    section3 = Polygon(p1, p4, p5)
    section3.setFill(color_rgb(245, 183, 118))
    section3.setOutline(color_rgb(245, 183, 118))
    section4 = Polygon(p1, p5, p6)
    section4.setFill(color_rgb(222, 126, 106))
    section4.setOutline(color_rgb(222, 126, 106))
    section5 = Polygon(p1, p6, p7)
    section5.setFill("white")
    section5.setOutline("white")
    section6 = Polygon(p1, p7, p8)
    section6.setFill(color_rgb(245, 183, 118))
    section6.setOutline(color_rgb(245, 183, 118))
    section7 = Polygon(p1, p8, p2)
    section7.setFill("white")
    section7.setOutline("white")
    section1.draw(win)
    section2.draw(win)
    section3.draw(win)
    section4.draw(win)
    section5.draw(win)
    section6.draw(win)
    section7.draw(win)

    # beach ball, ovals and circles
    ball = Circle(Point(50, 50), 25)
    ball.setFill("white")
    ball.setOutline("white")
    ball.draw(win)
    # ------Oval-------
    outerStripe = Oval(Point(30, 75), Point(70,25))
    outerStripe.setFill(color_rgb(168, 224, 153))
    outerStripe.setOutline(color_rgb(168, 224, 153))
    outerStripe.draw(win)
    middleStripe = Oval(Point(40, 75), Point(60,25))
    middleStripe.setFill("white")
    middleStripe.setOutline("white")
    middleStripe.draw(win)


    # second beach ball, clone
    # ------Clone-------
    secondBall = ball.clone()
    secondBall.move(-30, -15)
    secondBall.setFill(color_rgb(168, 224, 153))
    secondBall.setOutline(color_rgb(168, 224, 153))
    secondBall.draw(win)
    secondStripe = outerStripe.clone()
    secondStripe.move(-30, -15)
    secondStripe.setFill("white")
    secondStripe.setOutline("white")
    secondStripe.draw(win)
    secondMiddle = middleStripe.clone()
    secondMiddle.move(-30, -15)
    secondMiddle.setFill(color_rgb(168, 224, 153))
    secondMiddle.setOutline(color_rgb(168, 224, 153))
    secondMiddle.draw(win)
    overlap = Oval(Point(60, 75), Point(50,25))
    overlap.move(-30, -15)
    overlap.setFill("white")
    overlap.setOutline("white")
    overlap.draw(win)



    # close the window after user clicks
    win.getMouse()
    win.close()
    


main()
