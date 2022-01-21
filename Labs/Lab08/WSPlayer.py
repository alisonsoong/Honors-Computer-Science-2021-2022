#
# Alison Soong
#

import random

# WSPlayer
class WSPlayer:
    """Represents a player in the World Series."""
    
    def __init__(self, lastName, firstName, batAvg, hits, dou, tr, hr):
        """Initializes a WSPlayer.
            ex) player = WSPlayer(lastName, firstName, batAvg, hits,
                                    doubles, triples, homeRuns)
        """

        self.lastName = lastName
        self.firstName = firstName
        self.batAvg = batAvg
        self.hitsData = hits
        self.doublesData = dou
        self.triplesData = tr
        self.homeRunsData = hr

        self.singlesPercent = float(hits-dou-tr-hr)/hits
        self.doublesPercent = float(dou)/hits
        self.triplesPercent = float(tr)/hits
        self.HRPercent = float(hr)/hits
        #print(self.singlesPercent, self.doublesPercent, self.triplesPercent, self.HRPercent)

        self.homeRuns = 0 # start with zero home runs

    def getName(self):
        "Returns formatted name of player"
        firstInitial = self.firstName[0]
        name = firstInitial + ". " + self.lastName
        return name

    def getFullName(self):
        "Returns full name of player. Last Name then First Name for sorting purposes"
        return self.lastName + " " + self.firstName

    def getHR(self):
        "Returns the number of homeruns"
        return self.homeRuns

    def incrHR(self):
        "Adds onee to HR count"
        self.homeRuns += 1

    def getHit(self):
        """Calculates what kind of hit (if any), and returns:
            0 = miss
            1 = single
            2 = double
            3 = triple
            4 = homerun
        """

        didHitRandom = random.random()
        # print(didHitRandom, self.batAvg)
        if didHitRandom > self.batAvg:
            return 0 # they missed
        else:
            typeHitRandom = random.random()
            # print(typeHitRandom)
            if typeHitRandom < self.singlesPercent:
                # single
                return 1
            elif typeHitRandom < self.singlesPercent + self.doublesPercent:
                # double range
                return 2
            elif typeHitRandom < self.singlesPercent + self.doublesPercent + self.triplesPercent:
                # triple range
                return 3
            else:
                return 4
            
    def __str__(self):
        "Describes the WSPlayer"
        returnVal = self.lastName + ", " + self.firstName + ", batAvg: "
        returnVal += str(self.batAvg) + ", hits: " + str(self.hits)
        returnVal += ", doubles: " + str(self.doubles) + " triples: "
        returnVal += str(self.triples) + ", home runs:" + str(self.homeRuns)
        return returnVal

def main():
    # test out the WSPlayer
    p = WSPlayer("Altuve", "Jose", 0.978, 167, 30, 32, 31)
    a = p.getHit()
    print(a)
    
    print(p.getName())
    
if __name__ == "__main__": main()
