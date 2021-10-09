# class 211007
# Chap10DogClass

#
# Name: Alison
#
# This module contains the Dog class (first class in HCS)
#

class Dog:
    """Dog class
       all typical accessor methods"""
    def __init__(self,name,breed,owner):
        self.dogName = name
        self.dogBreed = breed
        self.owner = owner

    def getName(self):
        return self.dogName

    ### ADD OTHER ACCESSOR METHODS AND MUTATOR METHOD HERE ###

    def setOwner(self, newOwner): # mutator
        self.owner = newOwner

    def __str__(self):
        "returns: name of dog (owner)"
        return self.dogName + " (" + self.owner + ")"


########## END OF DOG CLASS (TEST BELOW) ##########
    
# this function tests the Dog class
def main():
    dog1 = Dog("Chimmy","Whippet","Shin")
    dog2 = Dog("Onyx","Mixed breed","Richardson")
    dog3 = Dog("Chloe","Westie","Kashiwada")

    # expect this to print "Chimmy (Shin)"
    print(dog1)
    dog1.setOwner("Alison")
    print(dog1)

    # CALL YOUR MUTATOR METHOD ON ONE OF THE DOG OBJECTS AND TEST IT

    
# this line calls the test function only when running this module
if __name__ == "__main__": main() # equivalent to main() as long as we are running this modulee
