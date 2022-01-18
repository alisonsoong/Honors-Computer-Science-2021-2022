#
# Alison Soong
#

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

    def __str__(self):
        "Describes the WSPlayer"
        returnVal = self.lastName + ", " + self.firstName + ", batAvg: "
        returnVal += str(self.batAvg) + ", hits: " + str(self.hits)
        returnVal += ", doubles: " + str(self.doubles) + " triples: "
        returnVal += str(self.triples) + ", home runs:" + str(self.homeRuns)
        return returnVal

def main():
    # test out the WSPlayer
    p = WSPlayer("Altuve", "Jose", 0.278, 167, 32, 1, 31)
    print(p.getName())
    
if __name__ == "__main__": main()
