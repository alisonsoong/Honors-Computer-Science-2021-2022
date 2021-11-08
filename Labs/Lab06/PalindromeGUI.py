#
# Alison Soong
# 
# PalindromeGUI.py
#

from graphics import *
from Button import Button


def palindromeGUI():

    print("This program will check at least three inputs and return if\nthey are " +
          "palindromes or not.")

    # creating the objects needed
    win = GraphWin("Palindrome Checker", 800, 400, autoflush = False)
    win.setCoords(0,0,400,400)

    entry = Entry(Point(200,230), 20)
    entry.draw(win)
    
    quitButton = Button(win, Point(200, 280), 100, 30, "Quit")
    quitButton.activate()

    testButton = Button(win, Point(200, 130), 100, 30, "Test")
    testButton.activate()

    anotherButton = Button(win, Point(200, 80), 100, 30, "Try Another")
    anotherButton.deactivate()

    prompt = Text(Point(200, 190), "Welcome to Palindrome Checker!\n" +
                  "Enter something into the box and press Test to try it!")
    prompt.draw(win)

    numFailedConsecutive = 0
    # after 3 consecutive fails, only quit button is active

    win.update()
    
    pt = Point(0,0)
    while not(quitButton.clicked(pt)):
        if numFailedConsecutive == 3:
            prompt.setText("3 consecutive inputs have been non-palindromes.\nPlease quit")
            anotherButton.deactivate()
            testButton.deactivate()
            win.update()
            
        if (testButton.clicked(pt)):
            # checking if this is an empty string  or not
            if not(entry.getText() == ""):
                # check if string is a palindrome
                initVal = entry.getText()
                print("Original string: " + initVal)

                lowerInit = initVal.lower() # make it all lower case

                # only include letters betwen A-Z and a-z (no punctuation)
                noPunct = ""
                for char in lowerInit:
                    if ("A" <= char <= "Z") or ("a" <= char <= "z"):
                        # append to noPunct if char is in correct range
                        noPunct += char
                print("Without punctuation: " + noPunct)
                                
                # split up the string into lists, split at spaces
                listVal = noPunct.split() 

                # join the list without anything between consecutive values
                joinedVal = "".join(listVal)
                print("Joined string: " + joinedVal)
                
                # get the string but in reverse
                backwardsVal = joinedVal[::-1]
                print("Backwards string: " + backwardsVal)

                if (backwardsVal == joinedVal):
                    # if backwards and forwards are the same, this is a palindrome
                    prompt.setText("\"" + initVal + "\" is a palindrome!")
                    numFailedConsecutive = 0
                    
                else:
                    # otherwise, they are not palindromes
                    prompt.setText("\"" + initVal + "\" is NOT a palindrome!")
                    numFailedConsecutive += 1

                if numFailedConsecutive == 3:
                    # number of consecutive fails is 3, disable everything
                    # prompt to quit
                    prompt.setText("\"" + initVal + "\" is NOT a palindrome!\n" +
                                   "3 consecutive inputs have been non-palindromes.\nPlease quit")
                    anotherButton.deactivate()
                    testButton.deactivate()
                else:
                    # otherwise, reset the window to prompt to restart
                    orig = prompt.getText()
                    prompt.setText(orig + "\nPress the \"Try Another\" button to test another string!")
                    testButton.deactivate()
                    anotherButton.activate()

            else:
                # empty string, ask again for a non-empty string to to test
                prompt.setText("Please enter a non-empty string to test")

        # update screen
        win.update()

        # test another
        if (anotherButton.clicked(pt)):
            # reset
            anotherButton.deactivate()
            testButton.activate()
            entry.setText("") # reset the entry box
            prompt.setText("Let's try another string to test!")
            win.update()
            
        # get point where clicked
        pt = win.getMouse()
        
    # close window when quit button is pressed
    win.close()


def main():
    palindromeGUI()


# this line calls the test function only when running this module
if __name__ == "__main__": main() # equivalent to main() as long as we are running this modulee
