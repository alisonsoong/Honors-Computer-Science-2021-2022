#
# Alison Soong
#
# SharkRunner.py
#

from graphics import *
import random
from Button import *
from Fish import *
from Shark import *
from SharkGUI import *

def main():
        # intro
        print("Welcome to Shark Runner!")
        
        # create the objects
        shark = Shark()
        greenFish = Fish(0,0,1)
        purpleFish = Fish(0,0,2)
        orangeFish = Fish(0,0,3)
        quitButton = Button()
        moveButton = Button()
        sharkGUI = SharkGUI(quitButton, moveButton, greenFish, purpleFish, orangeFish, shark)

        while True:
                if sharkGUI.update():
                        # update sharkGUI. if it returns true, then the game is over
                        print("Thank you for playing Shark Runner")
                        break
                elif sharkGUI.checkIfStalemate(): # if sharkGUI update returns false...
                        # the game is not over, but check if stalemate detected
                        print("Stalemate! Thank you for playing Shark Runner.")
                        break


if __name__ == "__main__": main()


