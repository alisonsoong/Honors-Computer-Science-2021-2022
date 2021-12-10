#
# Alison Soong
#
# Fish.py
#

import random
from graphics import *
# fix imports, place all imports into SharkRunner

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

                # has not initially passed through wall in its previous move
                self.throughWall = False

                self.nowFleeingWasFine = False

        def isAlive(self):
                "Returns true if fish is eaten"
                return self.isEaten
        
        def getPosition(self):
                "Returns position of fish, simultaneous assignment"
                if self.isAlive():
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

        def updateForSharkMove(self, posSharkX, posSharkY):
                """Updates info for fish according to shark move"""
                curFleeMode = self.fleeMode
                x, y = self.getPosition()
                if ((posSharkX - x)*(posSharkX - x) + (posSharkY - y)*(posSharkY - y) <= 9): # need to check if this is right
                        if not(curFleeMode):
                                self.nowFleeingWasFine = True
                        else:
                                self.nowFleeingWasFine = False
                        self.setFleeing()
                        
                        
                
        def move(self, posSharkX, posSharkY, fishA, fishB):
                """Checks if the next position is taken.
                Randomizes move/determines move according to the position of the shark.
                Sets fish to fleeMode = True if fish is within three squares from the shark.
                Possibly passes through the walls if fleeing, but will exit fleeMode once it does.
                -> Updates position, direction, fleeMode
                """
                dx, dy = self.getDirection()
                x, y = self.getPosition()
                
                # check if in flee mode
                
                curFleeMode = self.fleeMode
                justWentThroughWall = self.throughWall
                self.throughWall = False

                if (self.fishColor =="Orange"):
                        print(self.fishColor, ":", x, y, posSharkX, posSharkY, (posSharkX - x)*(posSharkX - x) + (posSharkY - y)*(posSharkY - y))
                
                if ((posSharkX - x)*(posSharkX - x) + (posSharkY - y)*(posSharkY - y) <= 9): # need to check if this is right
                        self.setFleeing()

                if not(self.isFleeing()):
                        # keep in this direction
                        nx, ny = dx+x, dy+y
                        # reverse direction if hitting a wall
                        nx, ny = self.getAdjustedPos(nx, ny)
                        # check if move is not blocked by others
                        nx, ny = self.checkMove(nx, ny, x, y, fishA, fishB)
                        self.setPosition(nx, ny)
                        
                else: # calculate new direction and new position
                        if posSharkX == x: # if the shark is on the same x axis
                                # figure out and set new direction
                                print("------>", curFleeMode)
                                if not(curFleeMode) or justWentThroughWall or self.nowFleeingWasFine:
                                        self.fleeDirection(posSharkX, posSharkY)
                                dx, dy = self.getDirection()
                                dirStr = self.getDirectionString()
                                nx, ny = dx+x, dy+y
                                nx, ny, didPassWall = self.getAdjustedFleeModePos(dirStr, nx, ny, x, y, fishA, fishB)
                                print(nx, ny, x, y)
                                if not(nx == x and ny == y) and didPassWall:
                                        self.resetFleeing()
                                        self.throughWall = True
                                        print("RESET FLEE MODE")
                                self.setPosition(nx, ny)
        
                        if posSharkY == y: # if the shark is on the same y axis
                                # figure out and set new direction
                                if not(curFleeMode) or justWentThroughWall or self.nowFleeingWasFine:
                                        self.fleeDirection(posSharkX, posSharkY)
                                dx, dy = self.getDirection()
                                dirStr = self.getDirectionString()
                                nx, ny = dx+x, dy+y
                                nx, ny, didPassWall = self.getAdjustedFleeModePos(dirStr, nx, ny, x, y, fishA, fishB)
                                if not(nx == x and ny == y) and didPassWall:
                                        self.throughWall = True
                                        self.resetFleeing()
                                self.setPosition(nx, ny)
                                
                        # if the shark is at a diagonal, there is no "best"
                        # move, so choose a random move that is still good
                        if posSharkX != x and posSharkY != y:
                                if not(curFleeMode) or justWentThroughWall or self.nowFleeingWasFine:
                                        nx, ny = self.figureOutDiag(posSharkX, posSharkY, fishA, fishB)
                                else:
                                        dx, dy = self.getDirection()
                                        dirStr = self.getDirectionString()
                                        nx, ny = dx+x, dy+y
                                        nx, ny, didPassWall = self.getAdjustedFleeModePos(dirStr, nx, ny, x, y, fishA, fishB)
                                        if not(nx == x and ny == y) and didPassWall:
                                                self.throughWall = True
                                                self.resetFleeing()

                                self.setPosition(nx, ny)

                self.nowFleeingWasFine = False
                                
                x,y = self.getPosition()
                if ((posSharkX - x)*(posSharkX - x) + (posSharkY - y)*(posSharkY - y) <= 9): # need to check if this is right
                        if not(self.fleeMode):
                                self.nowFleeingWasFine = True
                        self.setFleeing()
                        print("NOW SET FLEEING AH")

                if self.fishColor == "Orange": 
                        print(self.fishColor, ":", x, y, posSharkX, posSharkY, (posSharkX - x)*(posSharkX - x) + (posSharkY - y)*(posSharkY - y))
                        print()
                                

        def checkMove(self, nx, ny, x, y, fishA, fishB):
                """Checks move according to move priority,
                   returns either the new position or the old position"""
                xA, yA = fishA.getPosition()
                xB, yB = fishB.getPosition()
                if (xA == nx and yA == ny) or (xB == nx and yB == ny):
                        return x,y # position is taken by one of the other fish, stay in place
                return nx, ny

        def getAdjustedFleeModePos(self, dirStr, nx, ny, x, y, fishA, fishB):
                """Returns the position of the fish in flee mode"""
                passedThroughWall = False
                resetFlee = False
                
                # If passed through wall
                if nx > 10 and dirStr == "R":
                        passedThroughWall = True
                        nx = 1
                if nx < 1 and dirStr == "L":
                        passedThroughWall = True
                        nx = 10
                if ny > 10 and dirStr == "U":
                        passedThroughWall = True
                        ny = 1
                if ny < 1 and dirStr == "D":
                        passedThroughWall = True
                        ny = 10

                print("Adjusted Flee Mode pos:", nx,ny)

                # checks if this new position is valid
                nx, ny = self.checkMove(nx, ny, x, y, fishA, fishB) # returns original position (x,y) if it doesn't work
                if not(nx == x and ny == y) and passedThroughWall:
                        print("has flee-ed")
                        # has indeed moved through wall, even after check, so it is no longer in flee mode anymore
                        resetFlee = True
                print("Adjusted Flee Mode pos 2:", nx,ny,resetFlee)
                          
                return nx, ny, resetFlee
                
                        
        def figureOutDiag(self, posSharkX, posSharkY, fishA, fishB): 
                """Figures out move if the shark is in a diagonal position to the fish, returns new position"""
                x1,y1 = -1,-1 # horizontal move
                passedThroughWall1 = False
                dir1 = ""
                
                x2,y2 = -1,-1 # vertical move
                passedThroughWall2 = False
                dir2 = ""

                numMoves = 0
                x,y = self.getPosition()
                
                if posSharkX - x > 0: # the shark is to the right
                        x1,y1 = x-1, y
                        dir1 = "L" # needs to move lefet
                        x1, y1, passedThroughWall1 = self.getAdjustedFleeModePos(dir1, x1, y1, -1, -1, fishA, fishB)
                        print("----------------HELLPPPPPPP", x1, y1)
                else: # shark is to the left
                        x1,y1 = x+1, y
                        dir1 = "R" # neeeds to move right
                        x1, y1, passedThroughWall1 = self.getAdjustedFleeModePos(dir1, x1, y1, -1, -1, fishA, fishB)
                if posSharkY - y > 0: # the shark is above the fish
                        x2,y2 = x, y-1
                        dir2 = "D" # needs to move down
                        x2, y2, passedThroughWall2 = self.getAdjustedFleeModePos(dir2, x2, y2, -1, -1, fishA, fishB)
                else: # shark is above
                        x2,y2 = x, y+1
                        dir2 = "U" # needs to move up
                        x2, y2, passedThroughWall2 = self.getAdjustedFleeModePos(dir2, x2, y2, -1, -1, fishA, fishB)

                if x1 != -1: # the move is valid
                        numMoves += 1
                if x2 != -1: # the move is valid
                        numMoves += 1

                if self.fishColor == "Orange":
                        print("Option1:", x1, y1, "Option2:",x2, y2)

                if numMoves == 0: # if no valid moves
                        randNum = random.randint(1,2)# randomize direction
                        if randNum == 1:
                                self.setDirection(dir1)
                        else:
                                self.setDirection(dir2)
                        return x, y # don't move because no possible moves!
                if numMoves == 1: # if only one valid move
                        if x1 != -1: # the move is valid
                                if passedThroughWall1:
                                        self.resetFleeing()
                                        print("HELP1")
                                self.setDirection(dir1)
                                return x1, y1
                        else: # if the other move was invalid, this must be the good move
                                if passedThroughWall2:
                                        self.resetFleeing()
                                        print("HELP2")
                                self.setDirection(dir2)
                                return x2, y2
                if numMoves == 2: # get random position because both movese are valid
                        randNum = random.randint(1,2) # random integer between 1 and 2
                        if randNum == 1: # if ranNum is 1, choose first move
                                if passedThroughWall1:
                                        self.resetFleeing()
                                        print("HELP3")
                                self.setDirection(dir1)
                                return x1, y1
                        else: # otherwise if ranNum is 2, choose second move
                                if passedThroughWall2:
                                        self.resetFleeing()
                                        print("HELP4")
                                self.setDirection(dir2)
                                return x2, y2                

        def fleeDirection(self, posSharkX, posSharkY):
                """figures out and sets the new direction according
                to shark position if in flee mode AND the shark is on the same x and y axis as the fish"""
                x, y = self.getPosition()
                if x == posSharkX:
                        if (posSharkY - y > 0): # the shark is above the fish
                                self.setDirection("D")
                        if (posSharkY - y < 0): # the shark is below the fish
                                self.setDirection("U")

                if y == posSharkY:
                        if (posSharkX - x > 0): # the shark is to the right of the fish
                                self.setDirection("L")
                        if (posSharkX - x < 0): # the shark is to the left of the fish
                                self.setDirection("R")
                
        def getAdjustedPos(self, nx, ny):
                """Returns the adjusted position: specifically checks
                if hitting a wall when NOT in flee mode"""
                if nx > 10:
                        self.setDirection("L")
                        nx = 9
                elif nx < 1:
                        self.setDirection("R")
                        nx = 2
                elif ny > 10:
                        self.setDirection("D")
                        ny = 9
                elif ny < 1:
                        self.setDirection("U")
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
        print(random.randint(1,2))
        print("I am alive")
        win = GraphWin("Testing fish", 800, 800)
        win.setCoords(0, 0, 1200, 1200)
        GreenFish = Fish(2,1,1)
        PurpleFish = Fish(3,4,2)
        OrangeFish = Fish(1,2,3)
        FakeShark = Fish(3,7,1)
        FakeSharkImage = FakeShark.getImage()

        for i in range(11):
                Line(Point(100+i*100, 100), Point(100+i*100, 100+10*100)).draw(win)
                Line(Point(100, 100+i*100), Point(100+10*100, 100+i*100)).draw(win)
        
        GreenFishImage = GreenFish.getImage()
        PurpleFishImage = PurpleFish.getImage()
        OrangeFishImage = OrangeFish.getImage()
        nx, ny = GreenFish.getPosition()
        print("Green Fish:", nx, ny)
        GreenFishImage.move(50+nx*100, 50+ny*100)
        nx, ny = OrangeFish.getPosition()
        print("Orange Fish:", nx, ny)
        OrangeFishImage.move(50+nx*100, 50+ny*100)
        nx, ny = PurpleFish.getPosition()
        print("Purple Fish:", nx, ny)
        PurpleFishImage.move(50+nx*100, 50+ny*100)

        nx, ny = FakeShark.getPosition()
        print("Fake Shark:", nx, ny)
        FakeSharkImage.move(50+nx*100, 50+ny*100)

        GreenFishImage.draw(win)
        PurpleFishImage.draw(win)
        OrangeFishImage.draw(win)
        FakeSharkImage.draw(win)

        
        print(GreenFish.getDirectionString())
        quitRectangle = Rectangle(Point(100, 900),  Point(10, 870))
        quitRectangle.draw(win)
        moveRectangle = Rectangle(Point(900, 900),  Point(990, 870))
        moveRectangle.draw(win)
        pt = Point(0,0)
        while not (10 < pt.getX() < 100 and 870 < pt.getY() < 900):
                

                pt = win.getMouse()
                if  (10 < pt.getX() < 100 and 870 < pt.getY() < 900):
                        break
                
                if (900 < pt.getX() < 990 and 870 < pt.getY() < 900):
                        fnx, fny = FakeShark.getPosition()
                        GreenFish.move(fnx, fny, PurpleFish, OrangeFish)
                        PurpleFish.move(fnx, fny, GreenFish, OrangeFish)
                        OrangeFish.move(fnx, fny, GreenFish, PurpleFish)
                        GreenFishImage.undraw()
                        PurpleFishImage.undraw()
                        OrangeFishImage.undraw()
                        GreenFishImage = GreenFish.getImage()
                        PurpleFishImage = PurpleFish.getImage()
                        OrangeFishImage = OrangeFish.getImage()

                        gnx, gny = GreenFish.getPosition()
                        GreenFishImage.move(50+gnx*100, 50+gny*100)
                        onx, ony = OrangeFish.getPosition()
                        OrangeFishImage.move(50+onx*100, 50+ony*100)
                        pnx, pny = PurpleFish.getPosition()
                        PurpleFishImage.move(50+pnx*100, 50+pny*100)
                        

                        GreenFishImage.draw(win)
                        PurpleFishImage.draw(win)
                        OrangeFishImage.draw(win)
                else:
                        move = input("Move shark: ")
                        if move == "U":
                                fnx, fny = FakeShark.getPosition()
                                FakeShark.setPosition(fnx, fny+1)
                        if move == "D":
                                fnx, fny = FakeShark.getPosition()
                                FakeShark.setPosition(fnx, fny-1)
                        if move == "L":
                                fnx, fny = FakeShark.getPosition()
                                FakeShark.setPosition(fnx-1, fny)
                        if move == "R":
                                fnx, fny = FakeShark.getPosition()
                                FakeShark.setPosition(fnx+1, fny)

                        
                        
                        FakeSharkImage.undraw()
                        fnx, fny = FakeShark.getPosition()
                        FakeSharkImage = FakeShark.getImage()
                        FakeSharkImage.move(50+fnx*100, 50+fny*100)
                        FakeSharkImage.draw(win)

                        GreenFishImage.undraw()
                        PurpleFishImage.undraw()
                        OrangeFishImage.undraw()

                        GreenFish.updateForSharkMove(fnx, fny)
                        PurpleFish.updateForSharkMove(fnx, fny)
                        OrangeFish.updateForSharkMove(fnx, fny)

                        GreenFishImage = GreenFish.getImage()
                        PurpleFishImage = PurpleFish.getImage()
                        OrangeFishImage = OrangeFish.getImage()

                        gnx, gny = GreenFish.getPosition()
                        GreenFishImage.move(50+gnx*100, 50+gny*100)
                        onx, ony = OrangeFish.getPosition()
                        OrangeFishImage.move(50+onx*100, 50+ony*100)
                        pnx, pny = PurpleFish.getPosition()
                        PurpleFishImage.move(50+pnx*100, 50+pny*100)

                        GreenFishImage.draw(win)
                        PurpleFishImage.draw(win)
                        OrangeFishImage.draw(win)
        
        win.close()
        
if __name__ == "__main__": main()
