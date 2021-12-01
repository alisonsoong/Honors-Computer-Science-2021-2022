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

        def isAlive():
                "Returns if fish is eaten"
                return self.isEaten
        
        def getPosition(self):
                "Returns position of fish, simultaneous assignment"
                if !isAlive():
                        self.x = -1
                        self.y = -1
                        
                return self.x,self.y

        def getTypeFish(self):
                "Returns the type of the fish (1, 2, or 3). 1 has move priority over 2, and 2 has move priority over 3"
                return self.fishNum

        def setPosition(self,newX, newY):
                "Sets position of fish. Expects (newX, newY)"
                self.x = newX
                self.y = newY

        def isFleeing(self):
                "Returns if fish is fleeing (fleeMode)"
                return self.fleeMode

        def setFleeing(self):
                "Sets the fish to flee mode"
                self.fleeMode = True
                
        def move(self,posSharkX, posSharkY, fishA, fishB):
                """Checks if the next position is taken.
                Randomizes move/determines move according to the position of the shark.
                Sets fish to fleeMode = True if fish is within three squares from the shark.
                Possibly passes through the walls if fleeing, but will exit fleeMode once it does.
                -> Updates position, direction, fleeMode
                """
                dx, dy = getDirection()
                x, y = getPosition()
                
                # check if in flee mode
                if ((posSharkX - x)*(posSharkX - x) + (posSharkY - y)*(posSharkY - y) <= 9): # need to check if this is right
                        setFleeing()

                if !isFleeing():
                        # keep in this direction
                        nx, ny = dx+x, dy+y
                        # reverse direction if hitting a wall
                        nx, ny = getAdjustedPos(nx, ny)
                        # check if move is not blocked by others
                        nx, ny = checkMove(nx, ny, x, y)
                        setPosition(nx, ny)
                        
                else:
                        # calculate new direction and new position

                        if posSharkX == x: # if the shark is on the same x axis
                                # figure out and set new direction
                                fleeDirection(posSharkX, posSharkY, fishA, fishB)
                                dx, dy = getDirection()
                                nx, ny = dx+x, dy+y
                                nx, ny = getAdjustedFleeModePos(nx, ny, x, y, fishA, fishB)
                                setPosition(nx, ny)
        
                        if posSharkY == y: # if the shark is on the same y axis
                                # figure out and set new direction
                                fleeDirection(posSharkX, posSharkY, fishA, fishB)
                                dx, dy = getDirection()
                                nx, ny = dx+x, dy+y
                                nx, ny = getAdjustedFleeModePos(nx, ny, x, y, fishA, fishB)
                                setPosition(nx, ny)
                                
                        # if the shark is at a diagonal, there is no "best"
                        # move, so choose a random move that is still good
                        if posSharkX != x and posSharkY != y:
                                nx, ny = figureOutDiag(posSharkX, posSharkY, fishA, fishB)
                                setPosition(nx, ny)

        def checkMove(self, nx, ny, x, y, fishA, fishB):
                """Checks move according to move priority,
                   returns either the new position or the old position"""
                xA, yA = fishA.getPosition()
                xB, yB = fishB.getPosition()
                if (xA == nx and yA == ny) or (xB == nx and yB == ny):
                        return x,y
                return nx, ny

        def getAdjustedFleeModePos(self, nx, ny, x, y, fishA, fishB):
                """Returns the position of the fish in flee mode"""
                passedThroughWall = False
                # If new

                # checks if this new position is valid
                nx, ny = checkMove(nx, ny, x, y, fishA, fishB) # returns original position (x,y) if it doesn't work
                if not(nx == x and ny == y) and passedThroughWall:
                        # has indeed moved through wall, even after check, so it is no longer in flee mode anymore
                        resetFleeing()
                          
                return nx, ny
                
                        
        def figureOutDiag(self, posSharkX, posSharkY, fishA, fishB): # TODO: finish
                """Figures out move for diag, returns new position"""
                # needs to figure out new position
                x1,y1 = -1,-1 # horizontal move
                dirX = ""
                x2,y2 = -1,-1 # vertical move
                numMoves = 0
                x,y = getPosition()
                if posSharkX - x > 0: # the shark is to the right
                        x1,y1 = x-1, y-1
                        checkMove(x1,y1,x1,y1,fishA, fishB)
                        

        def fleeDirection(self, posSharkX, posSharkY):
                """figures out and sets the new direction according
                to shark position if in flee mode"""
                x, y = getPosition()
                if x == posSharkX:
                        if (posSharkX - x > 0): # the shark is to the right of the fish
                                setDirection("L")
                        if (posSharkX - x < 0): # the shark is to the left of the fish
                                setDirection("R")

                if y == posSharkY:
                        if (posSharkY - y > 0): # the shark is below the fish
                                setDirection("U")
                        if (posSharkY - y < 0): # the shark is above the fish
                                setDirection("D")
                
                      
        def getAdjustedPos(self, nx, ny):
                """Returns the adjusted position: specifically checks
                if hitting a wall when NOT in flee mode"""
                if nx > 10:
                        setDirection("L")
                        nx = 9
                elif nx < 1:
                        setDirection("R")
                        nx = 2
                elif ny > 10:
                        setDirection("U")
                        ny = 9
                elif ny < 1:
                        setDirection("D")
                        ny = 2
                return nx, ny

        def resetFleeing(self):
                "Sets the fish to NOT flee mode"
                self.fleeMode = False

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
