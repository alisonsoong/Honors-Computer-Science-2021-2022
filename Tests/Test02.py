#
# Alison Soong
# 
# Test02: HCS Python Chap 4 & 10 Test: Part 2
#

from graphics import *

def prob17():
    print("This program draws a completely blue circle in the middle of a window")
          
    win = GraphWin("Prob 17", 500, 400)

    # draw the circle
    cir = Circle(Point(250,200), 50)
    cir.setFill(color_rgb(0,0,255)) # pure blue! no other colors.
    cir.setOutline(color_rgb(0,0,255))
    cir.draw(win)

    # close the window
    win.getMouse()
    win.close()


# Prob 18
class Truck:
    """Truck class represents a Truck object with a specific make and model."""

    def __init__(self, truckMake, truckModel):
        """Constructs a new Truck class
        ie. t = Truck(truckMake, truckModel) """
        self.make = truckMake
        self.model = truckModel

    def setMake(self, newMake):
        """Sets the make of the Truck"""
        self.make = newMake

    def getMake(self):
        """Gets the make of the Truck"""
        return self.make

    def setModel(self, newModel):
        """Sets the model of the Truck"""
        self.model = newModel

    def getModel(self):
        """Gets the model of the Truck"""
        return self.model

    def __str__(self):
        return self.make + " " + self.model
    

def prob18():
    print("Testing out problem 18, the Truck object:\n")
    truck1 = Truck("Toyota", "Tacoma")

    print("Testing the __str__ function: ")
    print(truck1)
    print()

    print("Testing accessors and mutators:")
    print("Init model:", truck1.getModel())
    truck1.setModel("F150") # I don't know any other cars haha
    print("New model:", truck1.getModel())

    print("Init make:",truck1.getMake())
    truck1.setMake("Ford")
    print("New make:",truck1.getMake())

    print("\nUpdated Truck:")
    print(truck1)

    print("\nUsing pydoc to check:")
    help(Truck)
    
    
def prob19():
    print("Target game!")


    win = GraphWin("Try to click on the Target!",400, 400)

    rect = Rectangle(Point(250, 250), Point(350, 350))
    rect.setFill("orange")
    rect.setOutline("orange")
    rect.draw(win)

    txt = Text(Point(300, 300), "Target")
    txt.draw(win)

    # make the scoreboard
    Text(Point(100, 75), "SCOREBOARD").draw(win)
    hitTxt = Text(Point(100, 100), "Hit: 0")
    hitTxt.draw(win)
    missTxt = Text(Point(100, 125), "Miss: 0")
    missTxt.draw(win)

    miss = 0
    hit = 0

    # keep on getting points after user clicks and updating scoreboard
    while not(miss == 10 or hit == 10): # end when hit or miss equals 10
        pt = win.getMouse()
        # check if the pint is in the target
        if (250 <= pt.getX() <= 350 and 250 <= pt.getY() <= 350):
            hit += 1
            hitTxt.setText("Hit: " + str(hit))
        else:
            miss += 1
            missTxt.setText("Miss: " + str(miss))
        

    # finished
    finishTxt = Text(Point(200, 175), "Game Over — click anywhere to quit")
    finishTxt.setSize(20)
    finishTxt.draw(win)

    # finish when clicked
    win.getMouse()
    win.close()




# testing out the programs
#prob17()
#prob18()
prob19()
    
