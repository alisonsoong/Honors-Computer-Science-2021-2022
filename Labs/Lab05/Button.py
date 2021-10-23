#
# Alison Soong
# 
# Button.py
# 
from graphics import *

class Button:
    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactive() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label):
        """ Creates a rectangular button, starts deactivated. eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit')"""

        # height and width of rectangle
        w,h = width/2.0, height/2.0

        # position of rectangle
        x,y = center.getX(), center.getY()

        # create the rectangle
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)

        #create the label
        self.label = Text(center, label)
        self.label.draw(win)

        # start deactivated
        self.active = False
        self.deactivate()

    def clicked(self, pt):
        "Returns true if button active and p is inside"
        return (self.active and self.xmin <= pt.getX() <= self.xmax
                and self.ymin <= pt.getY() <= self.ymax)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def setLabel(self, newText):
        "Sets the label string of this button."
        self.label.setText(newText)

    def activate(self):
        "Sets this button to 'active'. Makes button clickable."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        """Sets this button to 'inactive'.
        Makes clicks on button have no effect on the program."""
        self.label.setFill("darkgrey")
        self.rect.setWidth(1)
        self.active = False
        
    def toggle(self):
        "Toggles a button from activated to deactivated, or vice versa"
        if self.active:
            self.deactivate()
        else:
            self.activate()

    def undraw(self):
        "Undraws the button from the graphics window."
        self.label.undraw()
        self.rect.undraw()

    def __str__(self):
        """returns: is active: (True or False)"""
        return "is active: " + str(self.active)


def main():
    # testing out the button class
    win = GraphWin("Button Testing", 300, 300)

    b = Button(win, Point(50, 100), 50, 100, "Button")
    b.activate()
    toggle = Button(win, Point(50, 210), 50, 30, "toggle")
    toggle.activate()
    quitButton = Button(win, Point(250, 100), 50, 100, "Quit")
    quitButton.activate()
    

    pt = win.getMouse()
    while not(quitButton.clicked(pt)):
        print(b)
        if b.clicked(pt):
            print("Button is pressed")
        if toggle.clicked(pt):
            print("Toggled button")
            b.toggle()
        

        pt = win.getMouse()

    win.close()
    
    

# this line calls the test function only when running this module
if __name__ == "__main__": main() # equivalent to main() as long as we are running this modulee


