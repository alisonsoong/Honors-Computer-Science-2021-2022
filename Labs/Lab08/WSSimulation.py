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
        winner, aScore, bScore = simOneGame(astrosPlayers, bravesPlayers, gameNum, outFile, True)
        if winner: # astros won
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
    bravesScore = 1
    inning = 1
    indexAstrosPlayers = 0
    indexBravesPlayers = 0
    # keep on printing game details to outFile if we are in a single game
    while(inning != 10 or (bravesScore == astrosScore)):
        simOneInning("Astros", astrosPlayers, outFile, singleGame, indexAstrosPlayers, inning)
        simOneInning("Braves", astrosPlayers, outFile, singleGame, indexAstrosPlayers, inning)
        inning += 1
        if (singleGame): # only print to the file if single game only
            print("\nScore: Astros " + str(astrosScore) + " Braves " + str(bravesScore), file = outFile)


    return False, astrosScore, bravesScore


def simOneInning(team, players, outFile, singleGame, indexOfPlayers, inning):
    numPlayers = len(players)
    if (singleGame): # only print to the file if single game only
        print("\nInning " + str(inning) + " - " + team, file = outFile)
  

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
        winner, aScore, bScore = simOneGame(astrosPlayers, bravesPlayers, gameNum, outFile, False)
        if winner: # astros won
            aWins += 1
        else: # braves won
            bWins += 1

    if (bWins > aWins): # false for braves
        whoWonSeries = False
    else: # true for astros
        whoWonSeries = True

    return whoWonSeries, gameNum
    
    
        
if __name__ == '__main__': main()
