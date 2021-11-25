#
# Alison Soong
#
# Fish.py
#

import random
from graphics import *

class Fish:
        """A fish class that describes all movement and states of a fish"""

        def __init__(self, initX, initY, num):
                """Creates a fish class, randomizes initial direction.
                Expects three parameters: Fish(initX, initY, num)
                num depends on the color of the fish:
                        Green = 1
                        Purple = 2
                        Orange = 3

                ex: greenFish = Fish(6, 3, 1), creates a green fish at
                        position x = 6, y = 3."""

                # initialize position and fish num
                self.x, self.y = initX, initY
                self.fishNum = num

                if num == 1:
                        self.fishColor = "Green"
                elif num == 2:
                        self.fishColor = "Purple"
                elif num == 3:
                        self.fishColor = "Orange"

                # create random fish direction
                self.curFishDir = "U"
                dirNum = random.randint(1,4)
                if dirNum == 1:
                        self.setDirection("U")
                elif dirNum == 2:
                        self.setDirection("D")
                elif dirNum == 3:
                        self.setDirection("L")
                else:
                        self.setDirection("R")


                # set fleeMode as false originally
                self.fleeMode = False

                # set isEaten as false originally
                self.isEaten = False

        def getPosition(self):
                "Returns position of fish, simultaneous assignment"
                return self.x,self.y

        def setPosition(self,newX, newY):
                "Sets position of fish. Expects (newX, newY)"
                self.x = newX
                self.y = newY
                
        def move(self,posSharkX, posSharkY, posFish1X, posFish1Y, posFish2X, posFish2Y):
                """Checks if the next position is taken.
                Randomizes move/determines move according to the position of the shark.
                Sets fish to fleeMode = True if fish is within three squares from the shark.
                Possibly passes through the walls if fleeing, but will exit fleeMode once it does.
                -> Updates position, direction, fleeMode
                """


                # check which new position (thus which direction) would
                #       cause the fish to be the farthest from the shark if in fleeMode

                # if not in fleeMode, keep moving in the same direction
                #       until hit a wall, then go opposite direction

                

        def isFleeing(self):
                "Returns if fish is fleeing (fleeMode)"
                return self.fleeMode

        def setFleeing(self):
                "Sets the fish to flee mode"
                self.fleeMode = True

        def resetFleeing(self):
                "Sets the fish to NOT flee mode"
                self.fleeMode = False

        def isAlive():
                "Returns if fish is eaten"
                return self.isEaten

        def eaten():
                "Sets fish as eaten"
                self.isEaten = True

        def getDirection(self):
                """Gets current direction of fish, simultaneous assignment: dX, dY"""
                return self.dX, self.dY

        def getDirectionString(self):
                """returns the current direction of fish as a string"""
                return self.curFishDir

        def setDirection(self,dire):
                """Sets direction of fish"""
                self.curFishDir = dire
                # set change of x and change of y!
                if dire == "U":
                        self.dX = 0
                        self.dY = 1
                elif dire == "D":
                        self.dX = 0
                        self.dY = -1
                elif dire == "L":
                        self.dX = -1
                        self.dY = 0
                elif dire == "R":
                        self.dX = 1
                        self.dY = 0
        def getImage(self):
                """Based on direction and flee mode, returns the image to use for a particular fish"""
                # check direction and get appropriate label string
                if self.curFishDir == "U":
                        fishDir = "Up"
                elif self.curFishDir == "D":
                        fishDir = "Down"
                elif self.curFishDir == "L":
                        fishDir = "Left"
                elif self.curFishDir == "R":
                        fishDir = "Right"

                # check if in fleeMode, change accordingly
                if self.fleeMode:
                        fishFlee = "Flee"
                else:
                        fishFlee = ""
                
                fileName = self.fishColor+fishDir+fishFlee+".png"
                return Image(Point(self.x, self.y), fileName)



def main():
        print("I am alive")
        win = GraphWin("Testing fish", 1000, 1000)
        win.setCoords(-1000, -1000, 1000, 1000)
        GreenFish = Fish(0,0,1)
        GreenFish.setFleeing()
        fishImage = GreenFish.getImage()
        fishImage.draw(win)
        print(GreenFish.getDirectionString())
        win.getMouse()
        win.close()
        
if __name__ == "__main__": main()
