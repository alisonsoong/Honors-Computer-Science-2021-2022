#
# Alison Soong
# 
# Die.py
#

from Button import Button 
from graphics import *
from random import randrange

class Die:
    """A Die is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactive() methods. The clicked(p) method
    returns true if the die is active and p is inside it."""

    def __init__(self, win, center, width):
        """ Creates a square button, eg:
        d = Die(myWin, centerPoint, width)"""

        w = width/2.0
        x,y = center.getX(), center.getY()

        # keep track of the value of the die
        self.val = 1

        # create the background rectangle (square)
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+w, y-w
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill('black')
        self.rect.draw(win)

        # create label, start with 1
        self.label = Text(center, "1") # start with value 1
        self.label.setTextColor("white")
        self.label.setFace("courier")
        self.label.setSize(20)
        self.label.draw(win)

        # starts as deactivated, can't be rolled
        self.active = False
        self.deactivate()

    def roll(self):
        """Sets the die to a random value from 1-6 if activated
        Can only roll when the die is active."""
        # only changes value if activated
        if self.active:
            self.val = randrange(1,7) # min <= x < max
            self.label.setText(self.val) # update the die face


    def clicked(self, pt):
        "Returns true if pt is inside the die"
        return (self.xmin <= pt.getX() <= self.xmax
                and self.ymin <= pt.getY() <= self.ymax)

    def setVal(self, newVal):
        "Sets the die to a given integer value."
        self.val = newVal
        self.label.setText(newVal)

    def getValue(self):
        "Get the value of the die."
        return self.val

    def activate(self):
        "Sets this die to 'active'. Can be rolled."
        self.rect.setFill('black')
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'. Can't be rolled."
        self.rect.setFill("darkgrey")
        self.active = False

    def toggle(self):
        "Toggles a die from activated to deactivated, or vice versa"
        # if active, deactivate
        if self.active:
            self.deactivate()
        else:
            # if not active, activate
            self.activate()

    def undraw(self):
        "Undraws the die from the graphics window."
        self.label.undraw()
        self.rect.undraw()

    def __str__(self):
        "returns: is active: (True or False), value: (value)"
        return "is active: " + str(self.active) + ", value: " + str(self.val)


def main():
    # testing out the die class
    win = GraphWin("Dice Testing", 300, 300)

    # create a roll button
    b = Button(win, Point(50, 100), 50, 100, "Roll")
    b.activate()
    
    # create a toggle button
    toggle = Button(win, Point(50, 210), 50, 30, "toggle")
    toggle.activate()

    # crate the die
    die = Die(win, Point(150, 100), 50)

    # quit button
    quitButton = Button(win, Point(250, 100), 50, 100, "Quit")
    quitButton.activate()

    
    # get user click until quit button is pressed
    pt = win.getMouse()
    while not(quitButton.clicked(pt)):
        if b.clicked(pt):
            print("Button is pressed")
            die.roll()
            
        if toggle.clicked(pt):
            print("Toggled button")
            die.toggle()

        if die.clicked(pt):
            die.toggle()
            print("Die has been clicked")
    
        pt = win.getMouse()

    win.close()
    

    
    

# this line calls the test function only when running this module
if __name__ == "__main__": main() # equivalent to main() as long as we are running this modulee


