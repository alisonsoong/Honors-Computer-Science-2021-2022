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
        shark = Shark((7,2),"Shark.png")
        sharkGUI = SharkGUI(shark)
        shark_img = shark.get_image()
        sharkGUI.add_object(shark_img)

        quitButton = Button()
        quitButton.init(Point(9.5, -0.5), 0.5, 0.5, "QUIT")
        sharkGUI.create_quit_button(quitButton)
        startButton = Button()
        startButton.init(Point(6, -0.5), 2, 1, "START")
        moveButton = Button()
        moveButton.init(Point(7,-0.5), 4, 1, "Move Fish")
        init_list = sharkGUI.valid_input(startButton, moveButton)

        fish_1_list, fish_2_list, fish_3_list = init_list[:2], init_list[2:4], init_list[4:]

        green_fish = Fish(fish_1_list[0],fish_1_list[1],1)
        green_fish_image = sharkGUI.create_a_fish_1(green_fish)
        purple_fish = Fish(fish_2_list[0],fish_2_list[1],2)
        sharkGUI.create_a_fish_2(purple_fish)
        orange_fish = Fish(fish_3_list[0],fish_3_list[1],3)
        sharkGUI.create_a_fish_3(orange_fish)

        while True:
                if sharkGUI.update(moveButton, quitButton):
                        print("Thank you for playing Shark Runner.")
                        break
                elif sharkGUI.check_if_stalemate():
                        # if game is not over after sharkGUI update,
                        # but there is a stalemate detected
                        print("Stalemate! Thank you for playing Shark Runner.")
                        break


if __name__ == "__main__": main()
