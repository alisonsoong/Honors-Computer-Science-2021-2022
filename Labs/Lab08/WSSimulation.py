#
# Alison Soong
#

# I chose to do top-down design, because I suppose that laying out
# approximately what needs to be done before actually implementing the details
# would not overload my brain/cause me to miss certain details.

from WSPlayer import WSPlayer 

def main():
    introduction() # show introduction
    numGames = getUserInput() # get number of games
    simWS(numGames)
    print("\n\nThank you for visiting the World Series Simulator!")

def introduction():
    print("Welcome to the World Series Simulator!")
    print("\nThis program will simulate a World Series match up between the")
    print("Houston Astros and Atlanta Braves.\n")

def getUserInput():
    # input validation
    while True:
        try:
            n = input("Enter the number of World Series you'd like to simulate: ")
            n = int(n) # try casting
            if (n < 1):
                n = n/0 # force an error
            else:
                print("\n==============================================\n")
                return n # return number of games
        except:
            print("Invalid input. Please enter an integer greater than 0.")

def simWS(numGames):
    astrosPlayers = getPlayers("Astros") # a list of WSPlayer objects
    bravesPlayers = getPlayers("Braves") # a list of WSPlayer objects
    
    if numGames == 1:
        outFile = open("WSplaybyplay.py", 'w') # make outFile
        print("Astros-Braves World Series Simulation", file=outFile)
        print("Results of World Series Simulation\n")
        results = simOneWS(astrosPlayers, bravesPlayers, outFile)
    else:
        outFile = open("WSmultseries.py", 'w') # make outFile
        print("Astros-Braves World Series Simulation\n", file=outFile)
        print("Results of", numGames, "World Series Simulations")
        simMultWS(numGames, astrosPlayers, bravesPlayers, outFile)

    outFile.close()
        
        
def getPlayers(team):
    file = team + ".tsv"
    inFile = open(file, 'r') # open the file
    players = []

    # make list of objects
    for line in inFile:
        line = line[:-1]
        values = line.split("\t")
        curPlayer = WSPlayer(values[0], values[1], float(values[2]), int(values[3]), int(values[4]), int(values[5]), int(values[6]))
        players.append(curPlayer)

    inFile.close()
    # for player in players:
        # print(player)
    return players


def simOneWS(astrosPlayers, bravesPlayers, outFile): # one WS
    bWins = 0
    aWins = 0
    gameNum = 0
    while bWins != 4 and aWins != 4:
        gameNum += 1
        aScore, bScore = simOneGame(astrosPlayers, bravesPlayers, gameNum, outFile, True)
        if aScore > bScore: # astros won
            print("Game", str(gameNum) + ":", "Astros", aScore, "Braves", bScore)
            aWins += 1
        else: # braves won
            print("Game", str(gameNum) + ":", "Braves", bScore, "Astros", aScore)
            bWins += 1

    # world series is complete
    if (bWins > aWins): # Braves won
        print("\nBraves win the series " + str(bWins) + "-" + str(aWins))
    else:
        print("\nAstros win the series " + str(aWins) + "-" + str(bWins))

    # print home runs
    printHomeRuns(astrosPlayers, bravesPlayers)
    
    
def printHomeRuns(astrosPlayers, bravesPlayers):
    print("\nHome Runs:")
    # sort the astros and braves players first by name then by homeruns
    astrosPlayers.sort(key=WSPlayer.getFullName)
    astrosPlayers.sort(key=WSPlayer.getHR, reverse=True)
    bravesPlayers.sort(key=WSPlayer.getFullName)
    bravesPlayers.sort(key=WSPlayer.getHR, reverse=True)


    counter = 0
    start = True # print out the astros
    print("Astros - ", end="")
    for player in astrosPlayers:
        if (player.getHR() == 0):
            break
        else:
            counter += 1
            if not(start):
                print(", ", end="")
            else:
                start = False
            print(player.getName(), player.getHR(), end="")

    if counter == 0:
        print("none", end="")

    counter = 0
    start = True # print out the braves
    print("\nBraves - ", end="")
    for player in bravesPlayers:
        if (player.getHR() == 0):
            break
        else:
            counter += 1
            if not(start):
                print(", ", end="")
            else:
                start = False
            print(player.getName(), player.getHR(), end="")
            
    if counter == 0:
        print("none", end="")
        

def simOneGame(astrosPlayers, bravesPlayers, gameNum, outFile, singleGame):
    # returns true if the Astros win, returns false if the Braves win
    # also returns the score
    # given one WS results, print results to file with title of gameNum at top
    if (singleGame): # only print to the file if single game only
        print("\n=========== GAME", gameNum, "===========", file = outFile)

    astrosScore = 0
    bravesScore = 0
    inning = 1
    indexAstrosPlayers = 0
    indexBravesPlayers = 0
    # keep on printing game details to outFile if we are in a single game
    while(inning < 10 or (bravesScore == astrosScore)):
        indexAstrosPlayers, astrosScore = simOneInning("Astros", astrosPlayers, outFile, singleGame, indexAstrosPlayers, inning, astrosScore)
        indexAstrosPlayers, bravesScore = simOneInning("Braves", bravesPlayers, outFile, singleGame, indexAstrosPlayers, inning, bravesScore)
        inning += 1
        if (singleGame): # only print to the file if single game only
            print("\nScore: Astros " + str(astrosScore) + " Braves " + str(bravesScore), file = outFile)
            
    return astrosScore, bravesScore


def simOneInning(team, players, outFile, singleGame, indexOfPlayers, inning, curScore):
    numPlayers = len(players)
    if (singleGame): # only print to the file if single game only
        print("\nInning " + str(inning) + " - " + team, file = outFile)
    bases = [None, None, None] # [1st base, 2nd base, 3rd base]. Empty string means no one is there
    strikeout = 0
    while strikeout != 3:
        player = players[indexOfPlayers]
        result = player.getHit()
        name = player.getName()
        if result == 0:
            if (singleGame):
                print(name + " struck out", end=" ", file=outFile)
            strikeout += 1
        elif result == 1:
            if (singleGame):
                print(name + " singled", end=" ", file=outFile)
            if bases[-1] != None: # someone is on third base
                curScore += 1 # they score
                if (singleGame):
                    print("(" + bases[-1] + " scored)", end=" ", file=outFile)
            firstBase = bases[0]
            secondBase = bases[1]
            bases = [name, firstBase, secondBase]
        elif result == 2: # double
            if (singleGame):
                print(name + " doubled", end=" ", file=outFile)
            counter = 0
            if bases[-1] != None: # someone is on third base
                curScore += 1 # they score
                counter += 1
                if (singleGame):
                    print("(" + bases[-1] + " scored", end="", file=outFile)
            if bases[-2] != None: # someone is on second base
                curScore += 1 # they score
                if (singleGame):
                    if (counter == 0):
                        print("(" + bases[-2] + " scored)", end="", file=outFile)
                    else:
                        print(" and " + bases[-2] + " scored", end="", file=outFile)
            elif counter == 1:
                if singleGame:
                    print(")", end=" ", file=outFile)
            firstBase = bases[0]
            bases = [None, name, firstBase]
        elif result == 3: # triple
            if (singleGame):
                print(name + " tripled", end=" ", file=outFile)
            counter = 0
            for base in bases:
                if base != None: # they score
                    if counter == 0 and singleGame:
                        print("(" + base, end="", file=outFile)
                    elif singleGame:
                        print(" and " + base, end="", file=outFile)
                    counter += 1
            if (counter != 0 and singleGame):
                print(" scored)", end=" ", file=outFile)
            bases = [None, None, name]
        elif result == 4: # homerun
            player.incrHR()
            if (singleGame):
                print(name + " homered", end=" ", file=outFile)
            counter = 0
            curScore += 1
            for i in range(3):
                if bases[i] != None:
                    curScore += 1 # they score
                    if (counter != 0 and singleGame):
                        print(" and " + bases[i], end="", file=outFile)
                    elif singleGame:
                        print("(" + bases[i], end="", file=outFile)
                    counter += 1
            if (singleGame and counter != 0):
                print(" scored)", end=" ", file=outFile)                    
            bases = [None,None,None] # no one on base
            
        indexOfPlayers = (indexOfPlayers + 1) % numPlayers
        if (singleGame):
            print(file=outFile)
            # print(bases, file=outFile)

            
    return indexOfPlayers, curScore
        
  
def simMultWS(numGames, astrosPlayers, bravesPlayers, outFile):
    Braves = [0] * 4
    Astros = [0] * 4
    for gameNum in range(1,numGames+1):
        winner, num = simOneForMult(astrosPlayers, bravesPlayers, outFile)

        if not(winner): # Braves won
            print(str(gameNum) + ":", "Braves win in", num, file=outFile)
            Braves[num-4] += 1
        else: # Astros won
            print(str(gameNum) + ":", "Astros win in", num, file=outFile)
            Astros[num-4] += 1

    # output to shell a summary: Astros/Braves win in 4, 5, 6, 7 games
    for i in range(4):
        print("\nAstros win in " + str(i+4) + ":", str(round(100*(Astros[i])/float(numGames), 1)) + "%", end="") 
    for i in range(4):
        print("\nBraves win in " + str(i+4) + ":", str(round(100*(Braves[i])/float(numGames), 1)) + "%", end="") 
    

def simOneForMult(astrosPlayers, bravesPlayers, outFile):
    bWins = 0
    aWins = 0
    gameNum = 0
    while bWins != 4 and aWins != 4:
        gameNum += 1
        aScore, bScore = simOneGame(astrosPlayers, bravesPlayers, gameNum, outFile, False)
        if aScore > bScore: # astros won
            aWins += 1
        else: # braves won
            bWins += 1

    if (bWins > aWins): # false for braves
        whoWonSeries = False
    else: # true for astros
        whoWonSeries = True

    return whoWonSeries, gameNum
    
        
if __name__ == '__main__': main()
