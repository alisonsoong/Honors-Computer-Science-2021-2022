#
# Alison Soong
# 
# ScoreCell.py
#

from Button import Button
from Die import Die
from graphics import *

class ScoreCell:
    """A ScoreCell is a cell on the score sheet visible to the
    player on the window. It helps monitor each cell on the
    score sheet that keeps track of the running score.
    Includes the ability to calculate the score for each cell."""

    def __init__(self, win, center, width, height, typeCell):
        """ Creates a rectangular button, starts deactivated. eg:
        sc = ScoreCell(myWin, centerPoint, width, height, 1)
        where typeCell is a number from 1-13 to represent the
        different types of scoring:
        Upper scores:
            1 = specified die face: 1
            2 = specified die face: 2
            3 = specified die face: 3
            4 = specified die face: 4
            5 = specified die face: 5
            6 = specified die face: 6

        Lower scores:
            7 = 3 of a Kind
            8 = 4 of a kind
            9 = Full House: 3 of a kind, and a pair
            Straights: (sequence of consecutive die faces)
                10 = small straight: 4 consecutive face
                11 = large straight: 5 consecutive faces
            12 = Chance: total all the die faces values
            13 = Yahtzee (5 of a kind)
        """

        # a text label (to describe what the cell represents)
        # and a button (the button is the part that gets pressed)

        # 3:1 ratio of label rectangle to score rectangle
        
        # height and width of label rectangle
        wL, hL = 3.0*width/4.0/2.0, height/2.0
        
        # height and width of score rectangle
        wS,hS = width/4.0/2.0, height/2.0

        # center of entire cell, and other info
        x,y = center.getX(), center.getY()
        w,h = width/2.0, height/2.0
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h

        # create the label rectangle
        # center of label rectangle
        xL,yL = self.xmin+wL, y

        # center of score rectangle
        xS,yS = self.xmax-wS, y

        # create the label rectangle
        p1 = Point(xL-wL, yL-hL)
        p2 = Point(xL+wL, yL+hL)
        self.rectLabel = Rectangle(p1, p2)
        self.rectLabel.setFill('white')
        self.rectLabel.draw(win)

        # determine the label for the rectangle
        self.type = typeCell
        if typeCell == 1:
            label = "Ones"
        elif typeCell == 2:
            label = "Twos"
        elif typeCell == 3:
            label = "Threes"
        elif typeCell == 4:
            label = "Fours"
        elif typeCell == 5:
            label = "Fives"
        elif typeCell == 6:
            label = "Sixes"
        elif typeCell == 7:
            label = "3 of a kind"
        elif typeCell == 8:
            label = "4 of a kind"
        elif typeCell == 9:
            label = "Full House"
        elif typeCell == 10:
            label = "Small Straight"
        elif typeCell == 11:
            label = "Large Straight"
        elif typeCell == 12:
            label = "Chance"
        elif typeCell == 13:
            label = "Yahtzee"

        # create the label for the label rectangle
        self.label = Text(Point(xL, yL), label)
        self.label.setFace("courier")
        self.label.setSize(10)
        self.label.draw(win)

        # create the score rectangle
        p1 = Point(xS-wS, yS-hS)
        p2 = Point(xS+wS, yS+hS)
        self.rectScore = Rectangle(p1, p2)
        self.rectScore.setFill('white')
        self.rectScore.draw(win)
        
        # create the label for the score rectangle
        self.scoreLabel = Text(Point(xS, yS), "")
        self.scoreLabel.setFace("courier")
        self.scoreLabel.setSize(10)
        self.scoreLabel.draw(win)

        # create instance variable for score
        self.score = 0

        # start deactivated
        self.active = False
        self.done = False # start as not done
        self.deactivate()

    def resetForRound(self):
        "Resets the cell for every round"
        self.active = False
        if not(self.done):
            self.deactivate()
        self.num1 = 0
        self.num2 = 0
        self.num3 = 0
        self.num4 = 0
        self.num5 = 0
        self.num6 = 0

    def resetForGame(self):
        "Resets the cell for every GAME"
        self.done = False # start as not done
        self.active = False
        self.deactivate() # start as deactivated
        self.num1 = 0
        self.num2 = 0
        self.num3 = 0
        self.num4 = 0
        self.num5 = 0
        self.num6 = 0

    def update(self, d1, d2, d3, d4, d5):
        """Updates the cell, accordingly makes the cell active,
        and calculates and displays the score of the particular cell according
        to type:

        Upper scores:
            1 = specified die face: 1
            2 = specified die face: 2
            3 = specified die face: 3
            4 = specified die face: 4
            5 = specified die face: 5
            6 = specified die face: 6

        Lower scores:
            7 = 3 of a Kind
            8 = 4 of a kind
            9 = Full House: 3 of a kind, and a pair
            Straights: (sequence of consecutive die faces)
                10 = small straight: 4 consecutive face
                11 = large straight: 5 consecutive faces
            12 = Chance: total all the die faces values
            13 = Yahtzee (5 of a kind)

        """
        
        # reset values
        self.num1 = 0
        self.num2 = 0
        self.num3 = 0
        self.num4 = 0
        self.num5 = 0
        self.num6 = 0

        # get the number of values
        self.calculate(d1)
        self.calculate(d2)
        self.calculate(d3)
        self.calculate(d4)
        self.calculate(d5)

        # calculate the value of the cell according to the type cell
        # these functions will update the cell score and make them active
        # ONLY if the cell is not already done
        if not(self.done):
            if self.type == 1:
                self.upper1()
            elif self.type == 2:
                self.upper2()
            elif self.type == 3:
                self.upper3()
            elif self.type == 4:
                self.upper4()
            elif self.type == 5:
                self.upper5()
            elif self.type == 6:
                self.upper6()
            elif self.type == 7:
                self.kind3()
            elif self.type == 8:
                self.kind4()
            elif self.type == 9:
                self.fullHouse()
            elif self.type == 10:
                self.smallStraight()
            elif self.type == 11:
                self.largeStraight()
            elif self.type == 12:
                self.chance()
            elif self.type == 13:
                self.yahtzee()

    def calculate(self, dice):
        """Adds the given dice value to the total count
        (for calculation purposes)"""
        if dice.getValue() == 1:
            self.num1 += 1
        elif dice.getValue() == 2:
            self.num2 += 1
        elif dice.getValue() == 3:
            self.num3 += 1
        elif dice.getValue() == 4:
            self.num4 += 1
        elif dice.getValue() == 5:
            self.num5 += 1
        elif dice.getValue() == 6:
            self.num6 += 1

    def upper1(self):
        """calculates and updates the upper scoring 1 cell"""
        self.activate()
        val = self.num1 * 1
        self.setScore(val)

    def upper2(self):
        """calculates and updates the upper scoring 2 cell"""
        self.activate()
        val = self.num2 * 2
        self.setScore(val)

    def upper3(self):
        """calculates and updates the upper scoring 3 cell"""
        self.activate()
        val = self.num3 * 3
        self.setScore(val)

    def upper4(self):
        """calculates and updates the upper scoring 4 cell"""
        self.activate()
        val = self.num4 * 4
        self.setScore(val)

    def upper5(self):
        """calculates and updates the upper scoring 5 cell"""
        self.activate()
        val = self.num5 * 5
        self.setScore(val)

    def upper6(self):
        """calculates and updates the upper scoring 6 cell"""
        self.activate()
        val = self.num6 * 6
        self.setScore(val)

    def kind3(self):
        """calculates and updates the 3 of a kind cell"""
        self.activate()
        val = 0
        if (self.num1 >= 3
            or self.num2 >= 3
            or self.num3 >= 3
            or self.num4 >= 3
            or self.num5 >= 3
            or self.num6 >= 3):
            val = self.num1*1 + self.num2*2 + self.num3*3 + self.num4*4 + self.num5*5 + self.num6*6 
        self.setScore(val)

    def kind4(self):
        """calculates and updates the 4 of a kind cell"""
        self.activate()
        val = 0
        if (self.num1 >= 4
            or self.num2 >= 4
            or self.num3 >= 4
            or self.num4 >= 4
            or self.num5 >= 4
            or self.num6 >= 4):
            val = self.num1*1 + self.num2*2 + self.num3*3 + self.num4*4 + self.num5*5 + self.num6*6 
        self.setScore(val)
        
    def fullHouse(self):
        """calculates and updates the full house cell"""
        self.activate()
        val = 25 # full houses are 25 points
        
        doubleVal = 0
        if self.num1 == 2:
            doubleVal = 1
        elif self.num2 == 2:
            doubleVal = 2
        elif self.num3 == 2:
            doubleVal = 3
        elif self.num4 == 2:
            doubleVal = 4
        elif self.num5 == 2:
            doubleVal = 5
        elif self.num6 == 2:
            doubleVal = 6


        tripleVal = 0
        if self.num1 == 3:
            tripleVal = 1
        elif self.num2 == 3:
            tripleVal = 2
        elif self.num3 == 3:
            tripleVal = 3
        elif self.num4 == 3:
            tripleVal = 4
        elif self.num5 == 3:
            tripleVal = 5
        elif self.num6 == 3:
            tripleVal = 6

        # if both doubleVal and tripleVal exist (both are not 0)
        if (tripleVal != 0 and
            doubleVal != 0):
            self.setScore(val)
        else:
            self.setScore(0)
        

    def smallStraight(self):
        """calculates and updates the small straight cell"""
        self.activate()
        val = 30 # small straights are 30 points

        # only options: 1234 2345 3456
        achieved = False

        if (self.num1 >= 1 and
            self.num2 >= 1 and
            self.num3 >= 1 and
            self.num4 >= 1):
            achieved = True
        elif (self.num2 >= 1 and
            self.num3 >= 1 and
            self.num4 >= 1 and
            self.num5 >= 1):
            achieved = True
        elif (self.num3 >= 1 and
            self.num4 >= 1 and
            self.num5 >= 1 and
            self.num6 >= 1):
            achieved = True
        
        if achieved:
            self.setScore(val)
        else:
            self.setScore(0)

    def largeStraight(self):
        """calculates and updates the small straight cell"""
        self.activate()
        val = 40 # large straights are 30 points

        # only options: 12345 23456
        achieved = False

        if (self.num1 == 1 and
            self.num2 == 1 and
            self.num3 == 1 and
            self.num4 == 1 and
            self.num5 == 1):
            achieved = True
        elif (self.num2 == 1 and
            self.num3 == 1 and
            self.num4 == 1 and
            self.num5 == 1 and
            self.num6 == 1):
            achieved = True

        if achieved:
           self.setScore(val)
        else:
            self.setScore(0)

    def chance(self):
        """calculates and updates the chance cell"""
        self.activate()
        val = self.num1 + self.num2*2 + self.num3*3 + self.num4*4 + self.num5*5 + self.num6*6
        self.setScore(val)

    def yahtzee(self):
        """calculates and updates the yahtzee cell"""
        self.activate()
        val = 0
        if self.num1 == 5:
            val = 1
        elif self.num2 == 5:
            val = 2
        elif self.num3 == 5:
            val = 3
        elif self.num4 == 5:
            val = 4
        elif self.num5 == 5:
            val = 5
        elif self.num6 == 5:
            val = 6

        if val == 0:
            self.setScore(0)
        else:
            self.setScore(50)
    
        
    def clicked(self, pt):
        "Returns true if cell is active and pt is inside"
        return (self.active
                and not(self.done)
                and self.xmin <= pt.getX() <= self.xmax
                and self.ymin <= pt.getY() <= self.ymax)

    def getLabel(self):
        "Returns the label string of the cell."
        return self.label.getText()

    def setLabel(self, newText):
        "Sets the label string of the cell."
        self.label.setText(newText)

    def getScore(self):
        "Gets the score of the cell."
        return self.score

    def setScore(self, newVal):
        "Sets the score of the cell to given value."
        self.score = newVal
        self.scoreLabel.setText(newVal)

    def activate(self):
        "Sets the cell to 'active'. Makes cell clickable."
        self.scoreLabel.setFill('black')
        self.rectScore.setFill(color_rgb(235, 235, 235))
        self.active = True

    def deactivate(self):
        """Sets the cell to 'inactive'.
        Makes clicks on cell have no effect on the program."""
        self.rectScore.setFill("white")
        self.scoreLabel.setFill("black")
        self.score = 0
        self.scoreLabel.setText("")
        self.active = False

    def used(self):
        """Sets the cell to 'used'.
        Makes clicks on cell have no effect on the program."""
        self.rectScore.setFill(color_rgb(217, 247, 205))
        self.scoreLabel.setFill("black")
        self.active = False
        self.done = True

    def isDone(self):
        """Returns true if the cell is 'done'"""
        return self.done
        
    def toggle(self):
        "Toggles a cell from activated to deactivated, or vice versa"
        if not(self.done):
            if self.active:
                self.deactivate()
            else:
                self.activate()

    def undraw(self):
        "Undraws the cell from the graphics window."
        self.label.undraw()
        self.scoreLabel.undraw()
        self.rectLabel.undraw()
        self.rectScore.undraw()

    def __str__(self):
        """returns: is active: (True or False), score: (score in cell)"""
        return "is active: " + str(self.active) + ", value: " + str(self.score)


def main():
    # testing out the cell class
    win = GraphWin("Button Testing", 300, 300)

    cell = ScoreCell(win, Point(100, 100), 100, 25, 13)
    cell.setScore(5)
    cell.activate()

    toggle = Button(win, Point(50, 210), 50, 30, "toggle")
    toggle.activate()
    
    quitButton = Button(win, Point(250, 200), 50, 100, "Quit")
    quitButton.activate()
    
    
    pt = win.getMouse()
    while not(quitButton.clicked(pt)):
        print(cell)
        if cell.clicked(pt):
            print("cell is pressed")
            cell.used()
        if toggle.clicked(pt):
            if cell.active and not(cell.done): # bad programming convention, but this is to check functionality
                cell.deactivate()
            elif not(cell.done):
                cell.activate()
                cell.setScore(0)
                
        pt = win.getMouse()
        

    win.close()
    
    

# this line calls the test function only when running this module
if __name__ == "__main__": main() # equivalent to main() as long as we are running this modulee


