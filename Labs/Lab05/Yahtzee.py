#
# Alison Soong
# 
# yahtzee.py
#

from Button import Button
from Die import Die
from ScoreCell import ScoreCell
from graphics import *

def Yahtzee():
    """A game of Yahtzee!"""

    win = GraphWin("Welcome to Yahtzee", 400, 400, autoflush=False)
    win.setCoords(0,0,400,400)

    # ask for name
    initText = Text(Point(200,270), "Welcome to Yahtzee!").draw(win)
    initText2 = Text(Point(200,255), "Enter your name:").draw(win)

    # entry for name
    nameEntry = Entry(Point(200, 230), 30)
    nameEntry.draw(win)

    # continue button
    continueButton = Button(win, Point(200, 190), 100, 30, "Start")
    continueButton.activate()

    # quit button
    quitButton = Button(win, Point(100, 360), 150, 30, "Quit")
    quitButton.activate()

    # flush
    win.update()

    # get user click
    pt = win.getMouse()
    while True:
        # if the name entry is not empty and the continue button is clicked,
        # can proceed with game
        if (not(nameEntry.getText() == "") and continueButton.clicked(pt)):
            break

        # otherwise, give a reminder!
        Text(Point(200, 150), "Please enter your name to continue.").draw(win)

        # otherwise, if the quit button is clicked, quit.
        if quitButton.clicked(pt):
            win.close()
            # return/quit the program
            return
            
        pt = win.getMouse()

    # get the name of the player
    name = nameEntry.getText()
    print("Player's name: " + name)

    # undraw everything
    initText.undraw()
    initText2.undraw()
    nameEntry.undraw()
    continueButton.undraw()

    # close this window
    win.close()

    # create the new window for the game
    win = GraphWin("Yahtzee", 700, 600, autoflush=False)
    win.setCoords(0,0,700,600)

    # create the scoreboard
    # name
    Text(Point(100, 530), "Player's name: " + name).draw(win)

    # high score
    highScoreLabel = Text(Point(100, 510), "High score: NA")
    highScoreLabel.draw(win)
    highScore = 0

    # num games played
    numGamesLabel = Text(Point(100, 490), "Games played: 0")
    numGamesLabel.draw(win)
    numGames = 0

    # create the dice, and activate them (start as activated beginning of
    # each round
    d1 = Die(win, Point(100, 300), 50)
    d1.activate()
    d2 = Die(win, Point(100+50+15, 300), 50)
    d2.activate()
    d3 = Die(win, Point(100+100+30, 300), 50)
    d3.activate()
    d4 = Die(win, Point(100+150+45, 300), 50)
    d4.activate()
    d5 = Die(win, Point(100+200+60, 300), 50)
    d5.activate()

    # create the scoregrid (all score cells!)
    oneCell = ScoreCell(win, Point(360+212.5, 550), 120, 30, 1)
    twoCell = ScoreCell(win, Point(360+212.5, 550-30), 120, 30, 2)
    threeCell = ScoreCell(win, Point(360+212.5, 550-30*2), 120, 30, 3)
    fourCell = ScoreCell(win, Point(360+212.5, 550-30*3), 120, 30, 4)
    fiveCell = ScoreCell(win, Point(360+212.5, 550-30*4), 120, 30, 5)
    sixCell = ScoreCell(win, Point(360+212.5, 550-30*5), 120, 30, 6)

    # lower sum and bonus cells (for lower scores)
    lowerSumCell = Text(Point(360+212.5, 550-30*6), "Sum: 0")
    lowerSumCell.draw(win)
    bonusLowerCell = Text(Point(360+212.5, 550-30*6-15), "Bonus: 0")
    bonusLowerCell.draw(win)
    
    threeKindCell = ScoreCell(win, Point(360+212.5, 550-30*6-65), 120, 30, 7)
    fourKindCell = ScoreCell(win, Point(360+212.5, 550-30*7-65), 120, 30, 8)
    fullHouseCell = ScoreCell(win, Point(360+212.5, 550-30*8-65), 120, 30, 9)
    smallStraightCell = ScoreCell(win, Point(360+212.5, 550-30*9-65), 120, 30, 10)
    largeStraightCell = ScoreCell(win, Point(360+212.5, 550-30*10-65), 120, 30, 11)
    chanceCell = ScoreCell(win, Point(360+212.5, 550-30*11-65), 120, 30, 12)
    yahtzeeCell = ScoreCell(win, Point(360+212.5, 550-30*12-65), 120, 30, 13)

    # total scores
    totalScoreCell = Text(Point(360+212.5, 550-30*13-65), "Total Score: 0")
    totalScoreCell.draw(win)

    # create the roll button
    rollButton = Button(win, Point(100+100+30, 250), 150, 25, "Roll")
    rollButton.activate()
    
    # create the quit button
    quitButton = Button(win, Point(100, 560), 150, 30, "Quit")
    quitButton.activate()

    # create the prompt (background and label)
    promptBackground = Rectangle(Point(75, 140), Point(360+25, 220))
    promptBackground.setFill("lightgrey")
    promptBackground.setOutline("lightgrey")
    promptBackground.draw(win)
    promptLabel = Text(Point(100+100+30, 200), "PROMPT:")
    promptLabel.draw(win)
    prompt = Text(Point(100+100+30, 175), "Welcome to Yahtzee!\n" +
                  "Press Roll to start.")
    prompt.draw(win)

    # hint!
    Text(Point(100+100+30, 40), "Hint: you can 'hold' dice, or " +
                     "prevent them from rolling, by clicking them to\n" +
                     "toggle before the second or third roll in a round.\n" +
                     "Black = active, dark gray = inactive.").draw(win)

    # game finished boolean (start as falsee)
    finishedGame = False
    
    # counts the current number of rolls so far (once it reaches 3, should reset)
    rollsCount = 0

    # total score
    totalScore = 0
    upperScoresTotal = 0

    numBonusYahtzee = 0 # number of bonus Yahtzees rolled. points from subsequent Yahtzees: 100 per each,
    # provided a first Yahtzee was found and Yahtzee cell is not 0
    seenYahtzee = False # only when seenYahtzee is true will bonus points be added
    bonusFromUpper = 0 # bonus points from upper scores: 63 or more upper -> 35 points extra

    # bonus Yahtzees counter (draw it)
    numBonusYahtzeeCell = Text(Point(360+212.5, 550-30*13-80), "Bonus Yahtzees: 0")
    numBonusYahtzeeCell.draw(win)

    # flush
    win.update()

    pt = Point(0,0) # start with a random point (to start the while loop)
    while not(quitButton.clicked(pt)):

        # update things: upper scores (the sum)
        upperScoresTotal = (oneCell.getScore() +
                            twoCell.getScore() +
                            threeCell.getScore() +
                            fourCell.getScore() +
                            fiveCell.getScore() +
                            sixCell.getScore())

        # update if bonus is applicable
        if upperScoresTotal >= 63:
            bonusFromUpper = 35

        # update total score (sum, and numBonusYahtzee * 100)
        totalScore = (upperScoresTotal +
                      threeKindCell.getScore() +
                      fourKindCell.getScore() +
                      fullHouseCell.getScore() +
                      smallStraightCell.getScore() +
                      largeStraightCell.getScore() +
                      chanceCell.getScore() +
                      yahtzeeCell.getScore() +
                      numBonusYahtzee*100 +
                      bonusFromUpper)

        

        # before even the mouse click, check if done
        finishedGame = (oneCell.isDone() and
                        twoCell.isDone() and
                        threeCell.isDone() and
                        fourCell.isDone() and
                        fiveCell.isDone() and
                        sixCell.isDone() and
                        threeKindCell.isDone() and
                        fourKindCell.isDone() and
                        fullHouseCell.isDone() and
                        smallStraightCell.isDone() and
                        largeStraightCell.isDone() and
                        chanceCell.isDone() and
                        yahtzeeCell.isDone())

        # if the game is finished
        if finishedGame:
            # give finished screen

            # update scores
            lowerSumCell.setText("Sum: " + str(upperScoresTotal))
            bonusLowerCell.setText("Bonus: " + str(bonusFromUpper))
            totalScoreCell.setText("Total Score: " + str(totalScore))

            # update prompt
            prompt.setText("Good Game! Your final score was " + str(totalScore))

            # update scoreboard
            if totalScore > highScore:
                highScore = totalScore
            highScoreLabel.setText("High score: " + str(highScore))
            numGames += 1
            numGamesLabel.setText("Games played: " + str(numGames))

            # show replay button
            replayButton = Button(win, Point(100+100+30, 100), 150, 40, "Click to Replay") 
            replayButton.activate()
            
            pt = win.getMouse()

            # check where user clicks. if replay button, continue.
            # if quit, exit while loop and close window
            endGame = False
            while not(replayButton.clicked(pt)):
                if quitButton.clicked(pt):
                    endGame = True
                    break
                pt = win.getMouse()
                
            if endGame:
                break

            # undraw replay button
            replayButton.undraw()

            # update prompt for a new game!
            prompt.setText("Let's start again! Roll again!")

            # reset the game

            rollsCount = 0
            totalScore = 0
            upperScoresTotal = 0
            numBonusYahtzee = 0 # bonus points from subsequent Yahtzees
            seenYahtzee = False # only when seenYahtzee is true will bonus points be added
            bonusFromUpper = 0 # bonus points from upper scores: 63 or more upper -> 35 points extra
            
            oneCell.resetForGame()
            twoCell.resetForGame()
            threeCell.resetForGame()
            fourCell.resetForGame()
            fiveCell.resetForGame()
            sixCell.resetForGame()
            threeKindCell.resetForGame()
            fourKindCell.resetForGame()
            fullHouseCell.resetForGame()
            smallStraightCell.resetForGame()
            largeStraightCell.resetForGame()
            chanceCell.resetForGame()
            yahtzeeCell.resetForGame()
            d1.activate()
            d2.activate()
            d3.activate()
            d4.activate()
            d5.activate()
            rollButton.activate()

            lowerSumCell.setText("Sum: " + str(upperScoresTotal))
            bonusLowerCell.setText("Bonus: " + str(bonusFromUpper))
            totalScoreCell.setText("Total Score: " + str(totalScore))
            numBonusYahtzeeCell.setText("Bonus Yahtzees: 0")

            # flush
            win.update()
            

        # get mouse click (for the while loop.
        # checking if game is done always comes first before the click)
        pt = win.getMouse()

        if oneCell.clicked(pt):
            oneCell.used()
    
            # reset the round (this is copied and pasted for every single
            # one of the score cells below)
            oneCell.resetForRound()
            twoCell.resetForRound()
            threeCell.resetForRound()
            fourCell.resetForRound()
            fiveCell.resetForRound()
            sixCell.resetForRound()
            threeKindCell.resetForRound()
            fourKindCell.resetForRound()
            fullHouseCell.resetForRound()
            smallStraightCell.resetForRound()
            largeStraightCell.resetForRound()
            chanceCell.resetForRound()
            yahtzeeCell.resetForRound()
            d1.activate()
            d2.activate()
            d3.activate()
            d4.activate()
            d5.activate()
            rollButton.activate()
            rollsCount = 0

            upperScoresTotal = (oneCell.getScore() +
                            twoCell.getScore() +
                            threeCell.getScore() +
                            fourCell.getScore() +
                            fiveCell.getScore() +
                            sixCell.getScore())
            if upperScoresTotal >= 63:
                bonusFromUpper = 35

            totalScore = (upperScoresTotal +
                      threeKindCell.getScore() +
                      fourKindCell.getScore() +
                      fullHouseCell.getScore() +
                      smallStraightCell.getScore() +
                      largeStraightCell.getScore() +
                      chanceCell.getScore() +
                      yahtzeeCell.getScore() +
                      numBonusYahtzee*100 +
                      bonusFromUpper)

            lowerSumCell.setText("Sum: " + str(upperScoresTotal))
            bonusLowerCell.setText("Bonus: " + str(bonusFromUpper))
            totalScoreCell.setText("Total Score: " + str(totalScore))


            prompt.setText("Start of next round! Let's roll!") 
            
           
        if twoCell.clicked(pt):
            twoCell.used()

            # reset the round
            oneCell.resetForRound()
            twoCell.resetForRound()
            threeCell.resetForRound()
            fourCell.resetForRound()
            fiveCell.resetForRound()
            sixCell.resetForRound()
            threeKindCell.resetForRound()
            fourKindCell.resetForRound()
            fullHouseCell.resetForRound()
            smallStraightCell.resetForRound()
            largeStraightCell.resetForRound()
            chanceCell.resetForRound()
            yahtzeeCell.resetForRound()
            d1.activate()
            d2.activate()
            d3.activate()
            d4.activate()
            d5.activate()
            rollButton.activate()
            rollsCount = 0

            upperScoresTotal = (oneCell.getScore() +
                            twoCell.getScore() +
                            threeCell.getScore() +
                            fourCell.getScore() +
                            fiveCell.getScore() +
                            sixCell.getScore())
            if upperScoresTotal >= 63:
                bonusFromUpper = 35

            totalScore = (upperScoresTotal +
                      threeKindCell.getScore() +
                      fourKindCell.getScore() +
                      fullHouseCell.getScore() +
                      smallStraightCell.getScore() +
                      largeStraightCell.getScore() +
                      chanceCell.getScore() +
                      yahtzeeCell.getScore() +
                      numBonusYahtzee*100 +
                      bonusFromUpper)

            lowerSumCell.setText("Sum: " + str(upperScoresTotal))
            bonusLowerCell.setText("Bonus: " + str(bonusFromUpper))
            totalScoreCell.setText("Total Score: " + str(totalScore))


            prompt.setText("Start of next round! Let's roll!") 
            

        if threeCell.clicked(pt):
            threeCell.used()

            # reset the round
            oneCell.resetForRound()
            twoCell.resetForRound()
            threeCell.resetForRound()
            fourCell.resetForRound()
            fiveCell.resetForRound()
            sixCell.resetForRound()
            threeKindCell.resetForRound()
            fourKindCell.resetForRound()
            fullHouseCell.resetForRound()
            smallStraightCell.resetForRound()
            largeStraightCell.resetForRound()
            chanceCell.resetForRound()
            yahtzeeCell.resetForRound()
            d1.activate()
            d2.activate()
            d3.activate()
            d4.activate()
            d5.activate()
            rollButton.activate()
            rollsCount = 0

            upperScoresTotal = (oneCell.getScore() +
                            twoCell.getScore() +
                            threeCell.getScore() +
                            fourCell.getScore() +
                            fiveCell.getScore() +
                            sixCell.getScore())
            if upperScoresTotal >= 63:
                bonusFromUpper = 35

            totalScore = (upperScoresTotal +
                      threeKindCell.getScore() +
                      fourKindCell.getScore() +
                      fullHouseCell.getScore() +
                      smallStraightCell.getScore() +
                      largeStraightCell.getScore() +
                      chanceCell.getScore() +
                      yahtzeeCell.getScore() +
                      numBonusYahtzee*100 +
                      bonusFromUpper)

            lowerSumCell.setText("Sum: " + str(upperScoresTotal))
            bonusLowerCell.setText("Bonus: " + str(bonusFromUpper))
            totalScoreCell.setText("Total Score: " + str(totalScore))


            prompt.setText("Start of next round! Let's roll!") 

        
        if fourCell.clicked(pt):
            fourCell.used()

            # reset the round
            oneCell.resetForRound()
            twoCell.resetForRound()
            threeCell.resetForRound()
            fourCell.resetForRound()
            fiveCell.resetForRound()
            sixCell.resetForRound()
            threeKindCell.resetForRound()
            fourKindCell.resetForRound()
            fullHouseCell.resetForRound()
            smallStraightCell.resetForRound()
            largeStraightCell.resetForRound()
            chanceCell.resetForRound()
            yahtzeeCell.resetForRound()
            d1.activate()
            d2.activate()
            d3.activate()
            d4.activate()
            d5.activate()
            rollButton.activate()
            rollsCount = 0

            upperScoresTotal = (oneCell.getScore() +
                            twoCell.getScore() +
                            threeCell.getScore() +
                            fourCell.getScore() +
                            fiveCell.getScore() +
                            sixCell.getScore())
            if upperScoresTotal >= 63:
                bonusFromUpper = 35

            totalScore = (upperScoresTotal +
                      threeKindCell.getScore() +
                      fourKindCell.getScore() +
                      fullHouseCell.getScore() +
                      smallStraightCell.getScore() +
                      largeStraightCell.getScore() +
                      chanceCell.getScore() +
                      yahtzeeCell.getScore() +
                      numBonusYahtzee*100 +
                      bonusFromUpper)

            lowerSumCell.setText("Sum: " + str(upperScoresTotal))
            bonusLowerCell.setText("Bonus: " + str(bonusFromUpper))
            totalScoreCell.setText("Total Score: " + str(totalScore))


            prompt.setText("Start of next round! Let's roll!") 
            
        
        if fiveCell.clicked(pt):
            fiveCell.used()

            # reset the round
            oneCell.resetForRound()
            twoCell.resetForRound()
            threeCell.resetForRound()
            fourCell.resetForRound()
            fiveCell.resetForRound()
            sixCell.resetForRound()
            threeKindCell.resetForRound()
            fourKindCell.resetForRound()
            fullHouseCell.resetForRound()
            smallStraightCell.resetForRound()
            largeStraightCell.resetForRound()
            chanceCell.resetForRound()
            yahtzeeCell.resetForRound()
            d1.activate()
            d2.activate()
            d3.activate()
            d4.activate()
            d5.activate()
            rollButton.activate()
            rollsCount = 0

            upperScoresTotal = (oneCell.getScore() +
                            twoCell.getScore() +
                            threeCell.getScore() +
                            fourCell.getScore() +
                            fiveCell.getScore() +
                            sixCell.getScore())
            if upperScoresTotal >= 63:
                bonusFromUpper = 35

            totalScore = (upperScoresTotal +
                      threeKindCell.getScore() +
                      fourKindCell.getScore() +
                      fullHouseCell.getScore() +
                      smallStraightCell.getScore() +
                      largeStraightCell.getScore() +
                      chanceCell.getScore() +
                      yahtzeeCell.getScore() +
                      numBonusYahtzee*100 +
                      bonusFromUpper)

            lowerSumCell.setText("Sum: " + str(upperScoresTotal))
            bonusLowerCell.setText("Bonus: " + str(bonusFromUpper))
            totalScoreCell.setText("Total Score: " + str(totalScore))


            prompt.setText("Start of next round! Let's roll!") 
            
        
        if sixCell.clicked(pt):
            sixCell.used()

            # reset the round
            oneCell.resetForRound()
            twoCell.resetForRound()
            threeCell.resetForRound()
            fourCell.resetForRound()
            fiveCell.resetForRound()
            sixCell.resetForRound()
            threeKindCell.resetForRound()
            fourKindCell.resetForRound()
            fullHouseCell.resetForRound()
            smallStraightCell.resetForRound()
            largeStraightCell.resetForRound()
            chanceCell.resetForRound()
            yahtzeeCell.resetForRound()
            d1.activate()
            d2.activate()
            d3.activate()
            d4.activate()
            d5.activate()
            rollButton.activate()
            rollsCount = 0

            upperScoresTotal = (oneCell.getScore() +
                            twoCell.getScore() +
                            threeCell.getScore() +
                            fourCell.getScore() +
                            fiveCell.getScore() +
                            sixCell.getScore())
            if upperScoresTotal >= 63:
                bonusFromUpper = 35

            totalScore = (upperScoresTotal +
                      threeKindCell.getScore() +
                      fourKindCell.getScore() +
                      fullHouseCell.getScore() +
                      smallStraightCell.getScore() +
                      largeStraightCell.getScore() +
                      chanceCell.getScore() +
                      yahtzeeCell.getScore() +
                      numBonusYahtzee*100 +
                      bonusFromUpper)

            lowerSumCell.setText("Sum: " + str(upperScoresTotal))
            bonusLowerCell.setText("Bonus: " + str(bonusFromUpper))
            totalScoreCell.setText("Total Score: " + str(totalScore))


            prompt.setText("Start of next round! Let's roll!") 
            
        
        if threeKindCell.clicked(pt):
            threeKindCell.used()

            # reset the round
            oneCell.resetForRound()
            twoCell.resetForRound()
            threeCell.resetForRound()
            fourCell.resetForRound()
            fiveCell.resetForRound()
            sixCell.resetForRound()
            threeKindCell.resetForRound()
            fourKindCell.resetForRound()
            fullHouseCell.resetForRound()
            smallStraightCell.resetForRound()
            largeStraightCell.resetForRound()
            chanceCell.resetForRound()
            yahtzeeCell.resetForRound()
            d1.activate()
            d2.activate()
            d3.activate()
            d4.activate()
            d5.activate()
            rollButton.activate()
            rollsCount = 0

            upperScoresTotal = (oneCell.getScore() +
                            twoCell.getScore() +
                            threeCell.getScore() +
                            fourCell.getScore() +
                            fiveCell.getScore() +
                            sixCell.getScore())
            if upperScoresTotal >= 63:
                bonusFromUpper = 35

            totalScore = (upperScoresTotal +
                      threeKindCell.getScore() +
                      fourKindCell.getScore() +
                      fullHouseCell.getScore() +
                      smallStraightCell.getScore() +
                      largeStraightCell.getScore() +
                      chanceCell.getScore() +
                      yahtzeeCell.getScore() +
                      numBonusYahtzee*100 +
                      bonusFromUpper)

            lowerSumCell.setText("Sum: " + str(upperScoresTotal))
            bonusLowerCell.setText("Bonus: " + str(bonusFromUpper))
            totalScoreCell.setText("Total Score: " + str(totalScore))


            prompt.setText("Start of next round! Let's roll!") 
            
        
        if fourKindCell.clicked(pt):
            fourKindCell.used()

            # reset the round
            oneCell.resetForRound()
            twoCell.resetForRound()
            threeCell.resetForRound()
            fourCell.resetForRound()
            fiveCell.resetForRound()
            sixCell.resetForRound()
            threeKindCell.resetForRound()
            fourKindCell.resetForRound()
            fullHouseCell.resetForRound()
            smallStraightCell.resetForRound()
            largeStraightCell.resetForRound()
            chanceCell.resetForRound()
            yahtzeeCell.resetForRound()
            d1.activate()
            d2.activate()
            d3.activate()
            d4.activate()
            d5.activate()
            rollButton.activate()
            rollsCount = 0

            upperScoresTotal = (oneCell.getScore() +
                            twoCell.getScore() +
                            threeCell.getScore() +
                            fourCell.getScore() +
                            fiveCell.getScore() +
                            sixCell.getScore())
            if upperScoresTotal >= 63:
                bonusFromUpper = 35

            totalScore = (upperScoresTotal +
                      threeKindCell.getScore() +
                      fourKindCell.getScore() +
                      fullHouseCell.getScore() +
                      smallStraightCell.getScore() +
                      largeStraightCell.getScore() +
                      chanceCell.getScore() +
                      yahtzeeCell.getScore() +
                      numBonusYahtzee*100 +
                      bonusFromUpper)

            lowerSumCell.setText("Sum: " + str(upperScoresTotal))
            bonusLowerCell.setText("Bonus: " + str(bonusFromUpper))
            totalScoreCell.setText("Total Score: " + str(totalScore))


            prompt.setText("Start of next round! Let's roll!") 
            
        
        if fullHouseCell.clicked(pt):
            fullHouseCell.used()

            # reset the round
            oneCell.resetForRound()
            twoCell.resetForRound()
            threeCell.resetForRound()
            fourCell.resetForRound()
            fiveCell.resetForRound()
            sixCell.resetForRound()
            threeKindCell.resetForRound()
            fourKindCell.resetForRound()
            fullHouseCell.resetForRound()
            smallStraightCell.resetForRound()
            largeStraightCell.resetForRound()
            chanceCell.resetForRound()
            yahtzeeCell.resetForRound()
            d1.activate()
            d2.activate()
            d3.activate()
            d4.activate()
            d5.activate()
            rollButton.activate()
            rollsCount = 0

            upperScoresTotal = (oneCell.getScore() +
                            twoCell.getScore() +
                            threeCell.getScore() +
                            fourCell.getScore() +
                            fiveCell.getScore() +
                            sixCell.getScore())
            if upperScoresTotal >= 63:
                bonusFromUpper = 35

            totalScore = (upperScoresTotal +
                      threeKindCell.getScore() +
                      fourKindCell.getScore() +
                      fullHouseCell.getScore() +
                      smallStraightCell.getScore() +
                      largeStraightCell.getScore() +
                      chanceCell.getScore() +
                      yahtzeeCell.getScore() +
                      numBonusYahtzee*100 +
                      bonusFromUpper)

            lowerSumCell.setText("Sum: " + str(upperScoresTotal))
            bonusLowerCell.setText("Bonus: " + str(bonusFromUpper))
            totalScoreCell.setText("Total Score: " + str(totalScore))


            prompt.setText("Start of next round! Let's roll!") 
            
        
        if smallStraightCell.clicked(pt):
            smallStraightCell.used()

            # reset the round
            oneCell.resetForRound()
            twoCell.resetForRound()
            threeCell.resetForRound()
            fourCell.resetForRound()
            fiveCell.resetForRound()
            sixCell.resetForRound()
            threeKindCell.resetForRound()
            fourKindCell.resetForRound()
            fullHouseCell.resetForRound()
            smallStraightCell.resetForRound()
            largeStraightCell.resetForRound()
            chanceCell.resetForRound()
            yahtzeeCell.resetForRound()
            d1.activate()
            d2.activate()
            d3.activate()
            d4.activate()
            d5.activate()
            rollButton.activate()
            rollsCount = 0

            upperScoresTotal = (oneCell.getScore() +
                            twoCell.getScore() +
                            threeCell.getScore() +
                            fourCell.getScore() +
                            fiveCell.getScore() +
                            sixCell.getScore())
            if upperScoresTotal >= 63:
                bonusFromUpper = 35

            totalScore = (upperScoresTotal +
                      threeKindCell.getScore() +
                      fourKindCell.getScore() +
                      fullHouseCell.getScore() +
                      smallStraightCell.getScore() +
                      largeStraightCell.getScore() +
                      chanceCell.getScore() +
                      yahtzeeCell.getScore() +
                      numBonusYahtzee*100 +
                      bonusFromUpper)

            lowerSumCell.setText("Sum: " + str(upperScoresTotal))
            bonusLowerCell.setText("Bonus: " + str(bonusFromUpper))
            totalScoreCell.setText("Total Score: " + str(totalScore))


            prompt.setText("Start of next round! Let's roll!") 
            
        
        if largeStraightCell.clicked(pt):
            largeStraightCell.used()

            # reset the round
            oneCell.resetForRound()
            twoCell.resetForRound()
            threeCell.resetForRound()
            fourCell.resetForRound()
            fiveCell.resetForRound()
            sixCell.resetForRound()
            threeKindCell.resetForRound()
            fourKindCell.resetForRound()
            fullHouseCell.resetForRound()
            smallStraightCell.resetForRound()
            largeStraightCell.resetForRound()
            chanceCell.resetForRound()
            yahtzeeCell.resetForRound()
            d1.activate()
            d2.activate()
            d3.activate()
            d4.activate()
            d5.activate()
            rollButton.activate()
            rollsCount = 0

            upperScoresTotal = (oneCell.getScore() +
                            twoCell.getScore() +
                            threeCell.getScore() +
                            fourCell.getScore() +
                            fiveCell.getScore() +
                            sixCell.getScore())
            if upperScoresTotal >= 63:
                bonusFromUpper = 35

            totalScore = (upperScoresTotal +
                      threeKindCell.getScore() +
                      fourKindCell.getScore() +
                      fullHouseCell.getScore() +
                      smallStraightCell.getScore() +
                      largeStraightCell.getScore() +
                      chanceCell.getScore() +
                      yahtzeeCell.getScore() +
                      numBonusYahtzee*100 +
                      bonusFromUpper)

            lowerSumCell.setText("Sum: " + str(upperScoresTotal))
            bonusLowerCell.setText("Bonus: " + str(bonusFromUpper))
            totalScoreCell.setText("Total Score: " + str(totalScore))


            prompt.setText("Start of next round! Let's roll!") 
            
        
        if chanceCell.clicked(pt):
            chanceCell.used()

            # reset the round
            oneCell.resetForRound()
            twoCell.resetForRound()
            threeCell.resetForRound()
            fourCell.resetForRound()
            fiveCell.resetForRound()
            sixCell.resetForRound()
            threeKindCell.resetForRound()
            fourKindCell.resetForRound()
            fullHouseCell.resetForRound()
            smallStraightCell.resetForRound()
            largeStraightCell.resetForRound()
            chanceCell.resetForRound()
            yahtzeeCell.resetForRound()
            d1.activate()
            d2.activate()
            d3.activate()
            d4.activate()
            d5.activate()
            rollButton.activate()
            rollsCount = 0

            upperScoresTotal = (oneCell.getScore() +
                            twoCell.getScore() +
                            threeCell.getScore() +
                            fourCell.getScore() +
                            fiveCell.getScore() +
                            sixCell.getScore())
            if upperScoresTotal >= 63:
                bonusFromUpper = 35

            totalScore = (upperScoresTotal +
                      threeKindCell.getScore() +
                      fourKindCell.getScore() +
                      fullHouseCell.getScore() +
                      smallStraightCell.getScore() +
                      largeStraightCell.getScore() +
                      chanceCell.getScore() +
                      yahtzeeCell.getScore() +
                      numBonusYahtzee*100 +
                      bonusFromUpper)

            lowerSumCell.setText("Sum: " + str(upperScoresTotal))
            bonusLowerCell.setText("Bonus: " + str(bonusFromUpper))
            totalScoreCell.setText("Total Score: " + str(totalScore))


            prompt.setText("Start of next round! Let's roll!") 
            
        
        if yahtzeeCell.clicked(pt):
            yahtzeeCell.used()

            # chose this cell, check if 50. if so, potential for bonus points
            # later.
            if yahtzeeCell.getScore() == 50: # a Yahtzee was indeed found
                seenYahtzee = True

            # reset the round
            oneCell.resetForRound()
            twoCell.resetForRound()
            threeCell.resetForRound()
            fourCell.resetForRound()
            fiveCell.resetForRound()
            sixCell.resetForRound()
            threeKindCell.resetForRound()
            fourKindCell.resetForRound()
            fullHouseCell.resetForRound()
            smallStraightCell.resetForRound()
            largeStraightCell.resetForRound()
            chanceCell.resetForRound()
            yahtzeeCell.resetForRound()
            d1.activate()
            d2.activate()
            d3.activate()
            d4.activate()
            d5.activate()
            rollButton.activate()
            rollsCount = 0

            upperScoresTotal = (oneCell.getScore() +
                            twoCell.getScore() +
                            threeCell.getScore() +
                            fourCell.getScore() +
                            fiveCell.getScore() +
                            sixCell.getScore())
            if upperScoresTotal >= 63:
                bonusFromUpper = 35

            totalScore = (upperScoresTotal +
                      threeKindCell.getScore() +
                      fourKindCell.getScore() +
                      fullHouseCell.getScore() +
                      smallStraightCell.getScore() +
                      largeStraightCell.getScore() +
                      chanceCell.getScore() +
                      yahtzeeCell.getScore() +
                      numBonusYahtzee*100 +
                      bonusFromUpper)

            lowerSumCell.setText("Sum: " + str(upperScoresTotal))
            bonusLowerCell.setText("Bonus: " + str(bonusFromUpper))
            totalScoreCell.setText("Total Score: " + str(totalScore))


            prompt.setText("Start of next round! Let's roll!") 


        # toggle the die from activated to deactivated
        # and vice versa when clicked
        # can't be toggled before first roll
        if d1.clicked(pt) and not(rollsCount == 0):
            d1.toggle()
            win.update()
        if d2.clicked(pt) and not(rollsCount == 0):
            d2.toggle()
            win.update()
        if d3.clicked(pt) and not(rollsCount == 0):
            d3.toggle()
            win.update()
        if d4.clicked(pt) and not(rollsCount == 0):
            d4.toggle()
            win.update()
        if d5.clicked(pt) and not(rollsCount == 0):
            d5.toggle()
            win.update()

        # roll button clicked
        if rollButton.clicked(pt):

            # increment rolls count and update prompt
            rollsCount += 1
            if rollsCount == 1:
                prompt.setText("You have rolled!\nEither select a score or roll again. (2 more rolls left!)")
            elif rollsCount == 2:
                prompt.setText("You have rolled twice!\nEither select a score or roll once more!")
            elif rollsCount == 3:
                rollsCount = 0
                prompt.setText("You used up all your rolls for this round!\nSelect a score.")
                rollButton.deactivate()
                # end of the round. deactivate roll button
                # and wait for score cell to be pressed (or quit)

            # roll the dice!
            d1.roll()
            d2.roll()
            d3.roll()
            d4.roll()
            d5.roll()
            
            oneCell.update(d1, d2, d3, d4, d5)
            twoCell.update(d1, d2, d3, d4, d5)
            threeCell.update(d1, d2, d3, d4, d5)
            fourCell.update(d1, d2, d3, d4, d5)
            fiveCell.update(d1, d2, d3, d4, d5)
            sixCell.update(d1, d2, d3, d4, d5)
            threeKindCell.update(d1, d2, d3, d4, d5)
            fourKindCell.update(d1, d2, d3, d4, d5)
            fullHouseCell.update(d1, d2, d3, d4, d5)
            smallStraightCell.update(d1, d2, d3, d4, d5)
            largeStraightCell.update(d1, d2, d3, d4, d5)
            chanceCell.update(d1, d2, d3, d4, d5)
            yahtzeeCell.update(d1, d2, d3, d4, d5)

            # if yahtzee has been seen before, can get bonus points
            # if current five dice represent a yahtzee too.
            if (seenYahtzee and
                d1.getValue() == d2.getValue()
                == d3.getValue() == d4.getValue()
                == d5.getValue()):
                # increment num Yahtzees
                numBonusYahtzee += 1
                # update on scoresheet
                numBonusYahtzeeCell.setText("Bonus Yahtzees: " + str(numBonusYahtzee))
            
            # flush
            win.update()
           

    # close the window
    win.close()
    



# run Yahtzee in main.
def main():
    Yahtzee()

# this line calls the test function only when running this module
if __name__ == "__main__": main() # equivalent to main() as long as we are running this modulee


