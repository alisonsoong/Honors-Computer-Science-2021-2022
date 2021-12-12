#
# Alison Soong
#
# Fish.py
#

# un-comment these if you wish to test out the fish class
# import random
# from graphics import * 

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

                # was previously not fleeing and is now fleeing (needed for logic)
                self.nowFleeingWasFine = False

        def isEaten(self):
                "Returns true if fish has been eaten"
                return self.isEaten
        
        def getPosition(self):
                "Returns position of fish, simultaneous assignment: x,y"
                # set coordinates to -1,-1 if it has been eaten
                if self.isEaten:
                        self.x = -1
                        self.y = -1

                return self.x,self.y

        def eaten():
                "Sets fish as eaten"
                self.isEaten = True

        def getTypeFish(self):
                "Returns the type of the fish (1:Green, 2:Purple, or 3:Orange)"
                return self.fishNum

        def setPosition(self,newX, newY):
                "Sets position of fish. Expects (newX, newY)"
                self.x = newX
                self.y = newY

        def isFleeing(self):
                "Returns true if fish is fleeing (flee mode)"
                return self.fleeMode

        def setFleeing(self):
                "Sets the fish to flee mode"
                self.fleeMode = True

        def resetFleeing(self):
                "Resets the fish flee mode to False"
                self.fleeMode = False

        def updateForSharkMove(self, posSharkX, posSharkY):
                """Updates info for fish according to shark move"""
                curFleeMode = self.fleeMode
                x, y = self.getPosition()
                # if within 3 squares of the shark, now in flee mode
                if ((posSharkX - x)*(posSharkX - x) + (posSharkY - y)*(posSharkY - y) <= 9): # need to check if this is right
                        if not(curFleeMode):
                                self.nowFleeingWasFine = True
                        else:
                                self.nowFleeingWasFine = False
                        self.setFleeing() # set to flee mode
                
        def move(self, posSharkX, posSharkY, fishA, fishB):
                """Checks if the next position is taken.
                        Randomizes move/determines move according
                        to the position of the shark.
                        -> Updates position, direction, fleeMode
                """
                dx, dy = self.getDirection() # get current direction and position
                x, y = self.getPosition()

                if self.isEaten: # if already eaten, place fish somewhere else
                        self.setPosition(-1,-1)
                        return # no need to calculate next move
                
                # check if in flee mode
                curFleeMode = self.fleeMode

                # check if just went through wall
                justWentThroughWall = self.throughWall
                self.throughWall = False

                # if within 3 squares of shark, update to flee mode
                if ((posSharkX - x)*(posSharkX - x) + (posSharkY - y)*(posSharkY - y) <= 9): # need to check if this is right
                        self.setFleeing()

                # if not fleeing, continue moving in desired direction
                if not(self.isFleeing()):
                        # keep in this direction
                        nx, ny = dx+x, dy+y
                        # reverse direction if hitting a wall
                        nx, ny = self.getAdjustedPos(nx, ny)
                        # check if move is not blocked by others
                        nx, ny = self.checkMove(nx, ny, x, y, fishA, fishB)
                        self.setPosition(nx, ny) # set position
                        
                else: # calculate new direction and new position
                        if posSharkX == x: # if the shark is on the same x axis
                                # figure out and set new direction if suddenly in flee mode or just went through wall
                                if not(curFleeMode) or justWentThroughWall or self.nowFleeingWasFine:
                                        self.fleeDirection(posSharkX, posSharkY)
                                dx, dy = self.getDirection()
                                dirStr = self.getDirectionString()
                                nx, ny = dx+x, dy+y # get new position
                                # adjust position according to flee mode and walls
                                nx, ny, didPassWall = self.getAdjustedFleeModePos(dirStr, nx, ny, x, y, fishA, fishB)
                                if not(nx == x and ny == y) and didPassWall:
                                        # if the fish did pass through a wall
                                        self.resetFleeing() # reset fleeing
                                        self.throughWall = True
                                self.setPosition(nx, ny)
        
                        if posSharkY == y: # if the shark is on the same y axis
                                # figure out and set new direction
                                if not(curFleeMode) or justWentThroughWall or self.nowFleeingWasFine:
                                        self.fleeDirection(posSharkX, posSharkY)
                                dx, dy = self.getDirection()
                                dirStr = self.getDirectionString()
                                nx, ny = dx+x, dy+y # get new position
                                # adjust position according to flee mode + walls
                                nx, ny, didPassWall = self.getAdjustedFleeModePos(dirStr, nx, ny, x, y, fishA, fishB)
                                if not(nx == x and ny == y) and didPassWall:
                                        # if the fish did pass through a wall, reset fleeing
                                        self.throughWall = True
                                        self.resetFleeing()
                                self.setPosition(nx, ny)
                                
                        # if the shark is at a diagonal, there is no "best"
                        # move, so choose a random move that is still good
                        if posSharkX != x and posSharkY != y:
                                # only figure out direction/randomize move if just entered flee mode
                                if not(curFleeMode) or justWentThroughWall or self.nowFleeingWasFine:
                                        nx, ny = self.figureOutDiag(posSharkX, posSharkY, fishA, fishB)
                                else:
                                        # maintain the same fleeing distance, maintain fleeing
                                        dx, dy = self.getDirection()
                                        dirStr = self.getDirectionString()
                                        nx, ny = dx+x, dy+y # get new position
                                        # update position, accounts for walls
                                        nx, ny, didPassWall = self.getAdjustedFleeModePos(dirStr, nx, ny, x, y, fishA, fishB)
                                        if not(nx == x and ny == y) and didPassWall:
                                                # if the fish did pass through a wall, reset fleeing
                                                self.throughWall = True
                                                self.resetFleeing()

                                self.setPosition(nx, ny) # set new position

                self.nowFleeingWasFine = False   
                x,y = self.getPosition()
                if ((posSharkX - x)*(posSharkX - x) + (posSharkY - y)*(posSharkY - y) <= 9): # need to check if this is right
                        # check if in flee mode
                        if not(self.fleeMode):
                                self.nowFleeingWasFine = True
                        self.setFleeing()

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
                
                # If passed through wall, adjust position
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
                        
                # checks if this new position is valid
                nx, ny = self.checkMove(nx, ny, x, y, fishA, fishB) # returns original position (x,y) if it doesn't work
                if not(nx == x and ny == y) and passedThroughWall:
                        # has indeed moved through wall, even after check, so it is no longer in flee mode anymore
                        resetFlee = True
     
                return nx, ny, resetFlee
                        
        def figureOutDiag(self, posSharkX, posSharkY, fishA, fishB): 
                """Figures out move if the shark is in a diagonal position
                        to the fish, returns new position"""
                x1,y1 = -1,-1 # horizontal move
                passedThroughWall1 = False
                dir1 = ""
                
                x2,y2 = -1,-1 # vertical move
                passedThroughWall2 = False
                dir2 = ""

                numMoves = 0 # number of possible moves
                x,y = self.getPosition()
                
                if posSharkX - x > 0: # the shark is to the right
                        x1,y1 = x-1, y
                        dir1 = "L" # needs to move left
                        x1, y1, passedThroughWall1 = self.getAdjustedFleeModePos(dir1, x1, y1, -1, -1, fishA, fishB)
                else: # shark is to the left
                        x1,y1 = x+1, y
                        dir1 = "R" # neeeds to move right
                        x1, y1, passedThroughWall1 = self.getAdjustedFleeModePos(dir1, x1, y1, -1, -1, fishA, fishB)
                if posSharkY - y > 0: # the shark is above the fish
                        x2,y2 = x, y-1
                        dir2 = "D" # needs to move down
                        x2, y2, passedThroughWall2 = self.getAdjustedFleeModePos(dir2, x2, y2, -1, -1, fishA, fishB)
                else: # shark is below
                        x2,y2 = x, y+1
                        dir2 = "U" # needs to move up
                        x2, y2, passedThroughWall2 = self.getAdjustedFleeModePos(dir2, x2, y2, -1, -1, fishA, fishB)

                if x1 != -1: # the horizontal move is valid
                        numMoves += 1
                if x2 != -1: # the vertical move is valid
                        numMoves += 1

                if numMoves == 0: # if no valid moves
                        randNum = random.randint(1,2) # randomize direction
                        if randNum == 1:
                                self.setDirection(dir1)
                        else:
                                self.setDirection(dir2)
                        return x, y # don't move because no possible moves!
                if numMoves == 1: # if only one valid move
                        if x1 != -1: # the horizontal move is the only valid one
                                if passedThroughWall1:
                                        self.resetFleeing()
                                self.setDirection(dir1)
                                return x1, y1
                        else: # if the other move was invalid, this must be the good move
                                if passedThroughWall2:
                                        self.resetFleeing()
                                self.setDirection(dir2)
                                return x2, y2
                if numMoves == 2: # get random position because both movese are valid
                        randNum = random.randint(1,2) # random integer between 1 and 2
                        if randNum == 1: # if ranNum is 1, choose first move
                                if passedThroughWall1:
                                        self.resetFleeing()
                                self.setDirection(dir1)
                                return x1, y1
                        else: # otherwise if ranNum is 2, choose second move
                                if passedThroughWall2:
                                        self.resetFleeing()
                                self.setDirection(dir2)
                                return x2, y2                

        def fleeDirection(self, posSharkX, posSharkY):
                """Figures out and sets the new direction according
                        to shark position if in flee mode AND
                        the shark is on the same x and y axis as the fish"""
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


        def getDirection(self):
                """Gets current direction of fish, simultaneous assignment: dX, dY"""
                return self.dX, self.dY

        def getDirectionString(self):
                """Returns the current direction of fish as a string: U, D, L, R"""
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

                # create file name string and return image with this file name
                fileName = self.fishColor+fishDir+fishFlee+".png"
                return Image(Point(self.x, self.y), fileName)


def main():
        print("Testing the fish class!")
        win = GraphWin("Testing fish", 800, 800)
        win.setCoords(0, 0, 1200, 1200)
        GreenFish = Fish(2,1,1)
        PurpleFish = Fish(3,4,2)
        OrangeFish = Fish(1,2,3)
        FakeShark = Fish(3,7,1)

        for i in range(11):
                Line(Point(100+i*100, 100), Point(100+i*100, 100+10*100)).draw(win)
                Line(Point(100, 100+i*100), Point(100+10*100, 100+i*100)).draw(win)
        
        GreenFishImage = GreenFish.getImage() # get images and draw them by position
        PurpleFishImage = PurpleFish.getImage()
        OrangeFishImage = OrangeFish.getImage()
        FakeSharkImage = FakeShark.getImage()
        nx, ny = GreenFish.getPosition()
        GreenFishImage.move(50+nx*100, 50+ny*100)
        nx, ny = OrangeFish.getPosition()
        OrangeFishImage.move(50+nx*100, 50+ny*100)
        nx, ny = PurpleFish.getPosition()
        PurpleFishImage.move(50+nx*100, 50+ny*100)
        nx, ny = FakeShark.getPosition()
        FakeSharkImage.move(50+nx*100, 50+ny*100)
        GreenFishImage.draw(win)
        PurpleFishImage.draw(win)
        OrangeFishImage.draw(win)
        FakeSharkImage.draw(win)

        Rectangle(Point(200, 1100),  Point(110, 1200)).draw(win) # quit "button": create fake buttons
        Rectangle(Point(1000, 1100),  Point(1090, 1200)).draw(win) # move "button"
        pt = Point(0,0) # initial point is 0,0. seeding the whiole loop
        while not (110 < pt.getX() < 200 and 1100 < pt.getY() < 1200):                
                pt = win.getMouse()
                if  (110 < pt.getX() < 200 and 1100 < pt.getY() < 1200):
                        break # quit
                if (1000 < pt.getX() < 1090 and 1100 < pt.getY() < 1200):
                        fnx, fny = FakeShark.getPosition()
                        GreenFish.move(fnx, fny, PurpleFish, OrangeFish) # move all fish
                        PurpleFish.move(fnx, fny, GreenFish, OrangeFish)
                        OrangeFish.move(fnx, fny, GreenFish, PurpleFish)
                        GreenFishImage.undraw() # undraw all the fish and redraw with updated images 
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
                        move = input("Move shark: ") # get shark move as input from user
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
                        
                        FakeSharkImage.undraw() # undraw and redraw everything according to new position of shark
                        GreenFishImage.undraw()
                        PurpleFishImage.undraw()
                        OrangeFishImage.undraw()
                        
                        fnx, fny = FakeShark.getPosition()
                        FakeSharkImage = FakeShark.getImage()
                        FakeSharkImage.move(50+fnx*100, 50+fny*100)
                        
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
                        
                        FakeSharkImage.draw(win)
                        GreenFishImage.draw(win)
                        PurpleFishImage.draw(win)
                        OrangeFishImage.draw(win)
        win.close()
        
if __name__ == "__main__": main()
