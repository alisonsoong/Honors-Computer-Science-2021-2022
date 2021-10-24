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
    nameEntry = Entry(Point(200, 230), 30)
    nameEntry.draw(win)
    continueButton = Button(win, Point(200, 190), 100, 30, "Start")
    continueButton.activate()
    pt = win.getMouse()
    
    while True:
        if (not(nameEntry.getText() == "") and continueButton.clicked(pt)):
            break
        Text(Point(200, 150), "Please enter your name to continue.").draw(win)
        pt = win.getMouse()

    win.close()

    win = GraphWin("Yahtzee", 700, 600, autoflush=False)
    win.setCoords(0,0,700,600)

    name = nameEntry.getText()
    print("Player's name: " + name)

    initText.undraw()
    initText2.undraw()
    nameEntry.undraw()
    continueButton.undraw()

    # create the scoreboard
    Text(Point(100, 530), "Player's name: " + name).draw(win)
    highScoreLabel = Text(Point(100, 510), "High score: NA")
    highScoreLabel.draw(win)
    highScore = 0
    numGamesLabel = Text(Point(100, 490), "Games played: 0")
    numGamesLabel.draw(win)
    numGames = 0
    

    # create the dice
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

    # create the scoregrid
    oneCell = ScoreCell(win, Point(360+212.5, 550), 120, 30, 1)
    twoCell = ScoreCell(win, Point(360+212.5, 550-30), 120, 30, 2)
    threeCell = ScoreCell(win, Point(360+212.5, 550-30*2), 120, 30, 3)
    fourCell = ScoreCell(win, Point(360+212.5, 550-30*3), 120, 30, 4)
    fiveCell = ScoreCell(win, Point(360+212.5, 550-30*4), 120, 30, 5)
    sixCell = ScoreCell(win, Point(360+212.5, 550-30*5), 120, 30, 6)
    threeKindCell = ScoreCell(win, Point(360+212.5, 550-30*6), 120, 30, 7)
    fourKindCell = ScoreCell(win, Point(360+212.5, 550-30*7), 120, 30, 8)
    fullHouseCell = ScoreCell(win, Point(360+212.5, 550-30*8), 120, 30, 9)
    smallStraightCell = ScoreCell(win, Point(360+212.5, 550-30*9), 120, 30, 10)
    largeStraightCell = ScoreCell(win, Point(360+212.5, 550-30*10), 120, 30, 11)
    chanceCell = ScoreCell(win, Point(360+212.5, 550-30*11), 120, 30, 12)
    yahtzeeCell = ScoreCell(win, Point(360+212.5, 550-30*12), 120, 30, 13)

    # create the roll button
    rollButton = Button(win, Point(100+100+30, 250), 150, 25, "Roll")
    rollButton.activate()
    
    # create the quit button
    quitButton = Button(win, Point(100, 560), 150, 30, "Quit")
    quitButton.activate()

    # create the prompt
    promptLabel = Text(Point(100+100+30, 200), "PROMPT:")
    promptLabel.draw(win)
    prompt = Text(Point(100+100+30, 175), "Welcome to Yahtzee! Press Roll to start.")
    prompt.draw(win)

    # draw the screen
    win.update()

    # is the game finished
    finishedGame = False

    
    pt = Point(0,0)

    # counts the current number of rolls so far (once it reaches 3, should reset)
    rollsCount = 0


    # total score
    totalScore = 0
    upperScoresTotal = 0

    bonusFromYahtzee = 0 # bonus points from subsequent Yahtzees. 100 per each,
    # provided a first Yahtzee was found and Yahtzee cell is not 0
    seenYahtzee = False # only when seenYahtzee is true will bonus points be added
    bonusFromUpper = 0 # bonus points from upper scores: 63 or more upper -> 35 points extra
    

    
    while not(quitButton.clicked(pt)):

        # update things:
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
                      bonusFromYahtzee +
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
                        
        if finishedGame:
            # give finished screen
            prompt.setText("Good Game! Your final score was " + str(totalScore))
            if totalScore > highScore:
                highScore = totalScore
            highScoreLabel.setText("High score: " + str(highScore))
            numGames += 1
            numGamesLabel.setText("Games played: " + str(numGames))
            
            replayButton = Button(win, Point(100+100+30, 130), 150, 40, "Click to Replay") 
            replayButton.activate()
            
            pt = win.getMouse()

            endGame = False
            while not(replayButton.clicked(pt)):
                if quitButton.clicked(pt):
                    endGame = True
                    break
                pt = win.getMouse()
                
            if endGame:
                break

            replayButton.undraw()

            prompt.setText("Let's start again! Roll again!")
            
            # reset the game
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

            
            win.update()
            
            rollsCount = 0
            totalScore = 0
            upperScoresTotal = 0
            bonusFromYahtzee = 0 # bonus points from subsequent Yahtzees
            seenYahtzee = False # only when seenYahtzee is true will bonus points be added
            bonusFromUpper = 0 # bonus points from upper scores: 63 or more upper -> 35 points extra
            

        # get mouse click
        pt = win.getMouse()

        if oneCell.clicked(pt):
            oneCell.used()
    
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

            prompt.setText("Start of next round! Let's roll!") 
            
           
        if twoCell.clicked(pt):
            twoCell.used()
            

        if threeCell.clicked(pt):
            threeCell.used()

        
        if fourCell.clicked(pt):
            fourCell.used()
            
        
        if fiveCell.clicked(pt):
            fiveCell.used()
            
        
        if sixCell.clicked(pt):
            sixCell.used()
            
        
        if threeKindCell.clicked(pt):
            threeKindCell.used()
            
        
        if fourKindCell.clicked(pt):
            fourKindCell.used()
            
        
        if fullHouseCell.clicked(pt):
            fullHouseCell.used()
            
        
        if smallStraightCell.clicked(pt):
            smallStraightCell.used()
            
        
        if largeStraightCell.clicked(pt):
            largeStraightCell.used()
            
        
        if chanceCell.clicked(pt):
            chanceCell.used()
            
        
        if yahtzeeCell.clicked(pt):
            yahtzeeCell.used()
            
        
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
        
        if rollButton.clicked(pt):
            rollsCount += 1
            if rollsCount == 1:
                prompt.setText("You have rolled! Either select a score or roll again. (2 more rolls left!)")
            elif rollsCount == 2:
                prompt.setText("You have rolled twice! Either select a score or roll once more!")
            elif rollsCount == 3:
                rollsCount = 0
                prompt.setText("You used up all your rolls for this round! Select a score.")
                rollButton.deactivate()

            
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
            win.update()
           

    win.close()
    




def main():
    Yahtzee()

# this line calls the test function only when running this module
if __name__ == "__main__": main() # equivalent to main() as long as we are running this modulee

