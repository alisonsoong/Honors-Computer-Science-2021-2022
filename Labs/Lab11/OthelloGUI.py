# Alison

# from ctypes.wintypes import RGB
# from this import d
# from turtle import color
from OthelloBoard import Board
from graphics import *
from Button import Button
from OthelloPiece import Piece
from OthelloAI import *
import time
from random import randint

class OthelloGUI:
    def __init__(self):
        """Creates an Othello GUI object"""
        self.curBoard = Board()
        self.curBoard.reset()
        self.prevBoard = Board()
        self.win = GraphWin("Othello", 800, 600, autoflush = False)
        self.win.setBackground("white")
        self.win.setCoords(-15,-17,150+2,150*3/4)
        self.AI = OthelloAI(True)

        self.pieces = []
        for y in range(8):
            row = []
            for x in range(8):
                row.append(Piece(y,x,False))
            self.pieces.append(row)

        # Set up gui
        self.setUpButtons()
        self.setUpScoreboard()
        self.setUpBoard()
        self.setUpPrompt()

        # title
        title = Text(Point(115, 90), "Othello") 
        title.setSize(36)
        title.draw(self.win)

        # choose to be white or black
        self.startPrompt = Text(Point(115, 58), "Choose what color you want\nto play as:") 
        self.startPrompt.setSize(13)
        self.whiteButton = Button(Point(101,48), 22, 8, "White")
        self.whiteButton.setOutlineFillText(color_rgb(255,255,255), color_rgb(98, 150, 100), color_rgb(255,255,255))
        self.blackButton = Button(Point(129,48), 22, 8, "Black")
        self.blackButton.setOutlineFillText(color_rgb(255,255,255), color_rgb(98, 150, 100), color_rgb(255,255,255))

        self.gameStart_ = True
        self.prevGameStart_ = False # state
        self.currentlyGettingColor_ = False # lol my variable names don't flame me

        self.userColor_ = True # color that user chooses at the start of the game
        self.curPlayerColor_ = False # start with white
        self.isDone_ = False
        self.turnSkip_ = False

        self.posMoves = [-1]

        self.pictures = ["memes/meme1.png", "memes/meme2.png", "memes/meme3.png", "memes/meme4.png", "memes/meme5.png"]
        self.prevMeme = randint(0,4)
        self.meme = Image(Point(115, 53),self.pictures[self.prevMeme])
        self.memeDrawn = False
        self.win.update()

    def setUpPrompt(self):
        """Sets up prompt"""
        # prompt box
        promptBox = Rectangle(Point(-5, -5), Point(140, 10))
        promptBox.setOutline(color_rgb(255,255,255))
        promptBox.setFill(color_rgb(60,60,60))
        promptBox.draw(self.win)

        # prompt text
        self.prompt = Text(Point(135/2, 5/2), "PROMPT")
        self.prompt.setTextColor(color_rgb(255,255,255))
        self.prompt.draw(self.win)

    def setPrompt(self, text):
        """Sets prompt text to string passed in"""
        # wrap prompt
        self.prompt.setText(self.wrapPrompt(text))
        self.win.update()

    def wrapPrompt(self, text):
        """Wraps text"""
        adjusted = ""
        index = 0
        for i in range(1,len(text)//130+1):
            adjusted += text[index:130*i]
            if (text[i*130] == " " or text[i*130-1] == " "): adjusted += "\n"
            else: adjusted += "-\n"
            index = i*130
        adjusted += text[index:]
        return adjusted

    def setUpButtons(self):
        """Sets up buttons"""
        self.quitButton = Button(Point(115,30), 50, 8, "Quit")
        self.quitButton.activate()
        self.quitButton.setOutlineFillText(color_rgb(255,255,255), color_rgb(60,60,60), color_rgb(255,255,255))
        self.quitButton.draw(self.win)
        self.replayButton = Button(Point(115,19), 50, 8, "Reset")
        self.replayButton.activate()
        self.replayButton.setOutlineFillText(color_rgb(255,255,255), color_rgb(60,60,60), color_rgb(255,255,255))
        self.replayButton.draw(self.win)

    def setUpScoreboard(self):
        """Sets up scoreboard"""
        self.scoreLabel = Text(Point(115,80), "Score") 
        self.scoreLabel.setSize(25)
        self.scoreLabel.draw(self.win)
        Text(Point(101, 75), "White").draw(self.win)
        Text(Point(129, 75), "Black").draw(self.win)
        self.whiteScoreLabel = Text(Point(101, 80), "2") 
        self.whiteScoreLabel.setSize(20)
        self.whiteScoreLabel.draw(self.win)
        self.blackScoreLabel = Text(Point(129, 80), "2")
        self.blackScoreLabel.setSize(20) 
        self.blackScoreLabel.draw(self.win)

        self.whiteScore = 2
        self.blackScore = 2

    def setUpBoard(self):
        """Sets up board for game"""
        # draw grid
        for y in range(8):
            for x in range(8):
                rec = Rectangle(Point(x*10-5,y*10+10+5), Point(x*10+10-5,y*10+10+10+5))
                rec.setFill(color_rgb(98, 150, 100))
                rec.setOutline(color_rgb(255, 255, 255))
                rec.draw(self.win)

        # draw the text
        for i in range(8):
            Text(Point(10*i, 97.5), chr(i+ord('a'))).draw(self.win)
        for i in range(8):
            Text(Point(77.5, 10*i+20), i+1).draw(self.win)
        
        # draw the pieces
        self.updateBoard()

    def updateBoard(self):
        """Updates board"""
        diff = self.curBoard-self.prevBoard # get difference in boards
        for change in diff: # update the positions of changes
            x,y = change[0], change[1]
            newPiece = self.pieces[x][y]
            newVal = self.curBoard.getValue(x,y)
            if newVal == None:
                newPiece.undraw()
            elif newVal == True:
                newPiece.toggleToColor(True)
                if (self.prevBoard.getValue(x,y) == None): newPiece.draw(self.win)
            elif newVal == False:
                newPiece.toggleToColor(False)
                if (self.prevBoard.getValue(x,y) == None): newPiece.draw(self.win)
        
        # update the scoreboard
        self.whiteScore, self.blackScore = self.curBoard.calcScore()
    
        self.updateScore()
        self.win.update()

    def gameStartLogic(self):
        """Handles the logic for clicks at the beginning of the game"""
        if self.gameStart_:
            if not self.prevGameStart_: 
                self.configForStart()
                self.prevGameStart_ = True
                self.pt = Point(-100,-100)
            else:
                self.pt = self.win.getMouse()
            self.getUserColor(self.pt)
        else:
            if not self.turnSkip_:
                self.pt = self.win.getMouse()
            else:
                time.sleep(2.0)

        self.win.update()

    def printPieces(self):
        """Prints pieces (helper method for testing purposes)"""
        for y in range(8):
            for x in range(8):
                print(self.pieces[x][y].getColor(), end=" ")
            print()

    def isGameEnd(self):
        """Checks if the game has ended"""
        self.stalemate = False
        if (not self.curBoard.simMoves(True)) and (not self.curBoard.simMoves(False)):
            # no more moves for either player
            self.stalemate = True
            return True
        return self.whiteScore + self.blackScore == 64

    def update(self):
        """Runs the entire game"""
        self.gameStartLogic() # get mouse click

        if self.isGameEnd(): # if the game has ended
            self.msg = "The game has ended! "
            if self.stalemate:
                self.msg = " Stalemate! "
            if self.whiteScore > self.blackScore: self.msg += "White has won!"
            else: self.msg += "Black has won!"
            self.msg += " Press reset to play again, or quit to close the game."
            self.setPrompt(self.msg)
            self.turnSkip_ = False

        if self.quitButton.clicked(self.pt): # quit button
            self.isDone_ = True
            print("Thank you for playing Othello!")
            self.win.close()
            quit()

        elif self.replayButton.clicked(self.pt): # reset button
            self.gameStart_ = True
            self.prevGameStart_ = False
            self.curPlayerColor_ = False
            self.turnSkip_  = False
            self.resetBoard()
            self.removeConfigForStart()
            self.setPrompt(self.msg)
            self.updateBoard()
            return

        if self.isGameEnd(): return # stop other logic if the game has ended
        
        self.setPrompt(self.msg)
        if self.gameStart_: return
        # otherwise, if done with getting user color at start...

        curX = self.pt.getX() + 5
        curY = self.pt.getY() - 15
        curPos = (int(curX/10), int(curY/10)) # current tile clicked
        curX, curY = curPos[0], curPos[1]

        self.prevBoard = Board(self.curBoard) # make a copy of the previous board

        self.getUserMoves()

        if self.userColor_ and not self.curPlayerColor_ or self.turnSkip_: # if user color is white, let AI move if cur player is black
            self.makeAIMove()
            self.getUserMoves()
            if self.turnSkip_: 
                self.curPlayerColor_ = not self.curPlayerColor_
        elif self.makeMove(curPos):
            posInStr = str(chr(ord('A')+curPos[0])) + str(curPos[1]+1)
            if self.curPlayerColor_: self.msg = "White made a move at " + posInStr + "!"
            else: self.msg = "Black made a move at " + posInStr + "!"

            # switch color
            self.curPlayerColor_ = not self.curPlayerColor_
            self.updateBoard()
            self.prevBoard = Board(self.curBoard)

            self.makeAIMove()
            self.getUserMoves()
            if self.turnSkip_: 
                self.curPlayerColor_ = not self.curPlayerColor_
        else:
            self.msg = " It is now "
            if self.curPlayerColor_ == True: self.msg += "White's turn to play. "
            else: self.msg += "Black's turn to play. "
            self.msg += "Please press a square with a valid move."

        # change meme!
        if (self.memeDrawn):
            newMeme = randint(0,4)
            while (newMeme != self.prevMeme): newMeme = randint(0,4)
            self.prevMeme = newMeme
            self.meme.undraw()
            self.meme = Image(Point(115, 53),self.pictures[randint(0,4)])
            self.meme.draw(self.win)

        # self.curBoard.printBoard()
        self.setPrompt(self.msg)
        self.updateBoard()

    def getUserMoves(self):
        """Gets the possible moves for the current user"""
        if self.posMoves == [-1]:
            # create new list of possible moves for user
            self.posMoves = self.curBoard.simMoves(self.curPlayerColor_)
            if self.posMoves == []:
                # if it's STILL empty, then move onto the AI
                self.turnSkip_ = True
    
    def makeAIMove(self):
        """Allows the AI to move"""
        # prompt stuff
        if self.turnSkip_:
            if self.userColor_: self.msg += " White's turn was skipped because no valid moves left! It is Black's "
            else: self.msg += " Black's turn was skipped because no valid moves left! It is White's "
            self.turnSkip_ = False
        else:
            if self.userColor_: self.msg += " It is Black's "
            else: self.msg += " It is White's "
        self.msg += "turn to play! The AI is making a move."
        self.setPrompt(self.msg)

        time.sleep(1.5) # a pause

        # for playing against a dumb ai
        # self.posMoves = self.curBoard.simMoves(self.curPlayerColor_)
        # if not(self.posMoves == []): 
        #     aiMove = self.AI.simTurn(Board(self.curBoard)) # self.posMoves[0]
        #     print(aiMove)
        #     self.makeMove(aiMove)
        #     posInStr = str(chr(ord('A')+aiMove[0])) + str(aiMove[1]+1)
        #     if self.curPlayerColor_: self.msg = "The AI made a move at " + posInStr + "!"
        #     else: self.msg = "The AI made a move at " + posInStr + "!"

        # playing against a "smarter" ai
        aiMove = self.AI.simTurn(Board(self.curBoard))
        if aiMove: 
            self.curBoard.placePiece(aiMove, self.curPlayerColor_)
            posInStr = str(chr(ord('A')+aiMove[0])) + str(aiMove[1]+1)
            if self.curPlayerColor_: self.msg = "The AI made a move at " + posInStr + "!"
            else: self.msg = "The AI made a move at " + posInStr + "!"
        else:
            self.msg = "The AI could not make a move, and thus its turn has been skipped!"
        self.posMoves = [-1] # reset

        # switch color
        self.curPlayerColor_ = not self.curPlayerColor_
        self.msg += " It is now "
        if self.curPlayerColor_: self.msg += "White's turn to play."
        else: self.msg += "Black's turn to play."

    def makeMove(self, pos):
        """Given position of move, makes move, but checks with list of possible moves first"""
        if not (pos in self.posMoves): 
            return False
        self.curBoard.placePiece(pos, self.curPlayerColor_)

        return True

    def generateTestBoard(self):
        """Generates a board for testing purposes"""
        board = Board()
        
        board.setValue(2,4,True)
        board.setValue(5,1,False)
        
        return board

    def isDone(self):
        """Returns if the game is done"""
        return self.isDone_

    def updateScore(self):
        """Updates scoreboard"""
        self.whiteScoreLabel.setText(str(self.whiteScore))
        self.blackScoreLabel.setText(str(self.blackScore))

    def resetBoard(self):
        """Resets the board for a new game"""
        for i in range(8):
            for j in range(8):
                self.pieces[i][j].undraw()
        self.prevBoard = Board() # empty
        self.curBoard.reset()

        self.posMoves = [-1]

        self.whiteScore = 2
        self.blackScore = 2
        self.updateScore()

    def configForStart(self):
        """Sets up GUI for start of game (picking color)"""
        curPlayerColor_ = True

        if self.memeDrawn:
            self.meme.undraw()

        self.msg = "Please choose what color you want to play as. Black moves first!"

        self.memeDrawn = False

        self.startPrompt.draw(self.win)
        self.whiteButton.draw(self.win)
        self.blackButton.draw(self.win)
        self.whiteButton.activate()
        self.blackButton.activate()
        self.win.update()
    
    def removeConfigForStart(self):
        """Reset board for after user chooses color"""
        self.startPrompt.undraw()
        self.whiteButton.undraw()
        self.blackButton.undraw()
        self.memeDrawn = True

    def getUserColor(self, pt):
        """Checks which button user clicked when choosing color"""
        if self.whiteButton.clicked(pt):
            self.prevGameStart_ = False
            self.gameStart_ = False
            self.userColor_ = True
            self.removeConfigForStart()
            self.AI = OthelloAI(False)
            return
        elif self.blackButton.clicked(pt):
            self.prevGameStart_ = False
            self.gameStart_ = False
            self.userColor_ = False
            self.AI = OthelloAI(True)
            self.removeConfigForStart()
            return

# testing
if __name__ == '__main__': 
    test = OthelloGUI()
    while not test.isDone():
        test.update()
