#
# Alison Soong
#
# SharkRunner.py
#

from graphics import *


def main():
        # Creates the SharkGUI object
        # while True:
        #       call SharkGUI’s update() that returns true or false.
        #       If it’s true, it exits the while loop, says good game, and ends the game.
        #       If false, check SharkGUI’s checkIfStalemate(). If false, keep on going.
        #               If true, end game and say that it is a stalemate, and end

        sharkGUI = SharkGUI()
        while True:
                if sharkGUI.update():
                        print("Thank you for playing Shark Runner")
                        break
                elif sharkGUI.checkIfStalemate():
                        print("Stalemate! Thank you for playing Shark Runner")
                        break


if __name__ == "__main__": main()
