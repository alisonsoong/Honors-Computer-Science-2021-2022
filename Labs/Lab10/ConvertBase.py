# Alison
# Lab 10

'''
my explanation:
convertToBase10 is a method that illustrates how recursion can imitate a for loop (recursion = more general form)
-> it keeps track of the power (current digit) and raises the source base to that power, adding it to the final result
-> uses a look-up array of sorts (adj, which stands for adjusted values) to easily interpret the values in the source number string
-> source number is treated as a string because of the possibility of A-F digits

convertToBase is a method that takes in the source number as an integer (a base 10 number) and the destination base. 
-> Repeatedly divides the current number by the destBase until there are no more powers of destBase possible 
(so stops at power just beyond the highest that divides into the source number and returns an empty string). 
-> Concatenates the multiple of the power (calculated by finding the remainder of dividing by another power of destBase) 
as adjusted with look-up array.
'''

def getValues():
    sourceBase = input("Source Base: ")
    sourceNum = input("Source Number: ")
    destBase = input("Destination Base: ")
    endMsg = ""
    end = False

    #  check if invalid source base
    try:
        sourceBase = int(sourceBase)
        if (sourceBase < 2 or sourceBase > 16):
            sourceBase /= 0
    except:
        endMsg = "ERROR: Invalid source base" 
        end = True

    # check if invalid source number
    try:
        # blah
        if sourceNum == "":
            sourceNum /= 0
        if (not end):
            for char in sourceNum:
                if ('A' <= char <= 'F'):
                    # check if only acceptable digits
                    if (9+ord(char)-ord('A')+1) > sourceBase:
                        sourceNum /= 0
                elif int(char) > sourceBase or int(char) < 0:
                    sourceNum /= 0
    except:
        if endMsg != "": endMsg += ", invalid source number"
        else: endMsg = "ERROR: Invalid source number"
        end = True

    # check if invalid destination base
    try:
        destBase = int(destBase)
        if (destBase < 2 or destBase > 16):
            destBase /= 0
    except:
        if endMsg != "": endMsg += ", invalid destination base"
        else: endMsg = "ERROR: Invalid destinatin base"
        end = True   

    if end: 
        print("\n" + endMsg)
        return False, 0, 0, 0 # do not go ahead
    return True, sourceBase, sourceNum, destBase # can go ahead

def convertBase():
    print("Welecome To The Convert Base Program!")
    print("-------------------------------------")
    val = ""
    while "quit" not in val and "q" not in val:
        cont, sourceBase, sourceNum, destBase = getValues()
        if cont:
            # do stuff
            if sourceNum == '0': # weird corner case
                result = 0
            else:
                result = convertToBase10(sourceBase, sourceNum, 0)
                if (destBase != 10):
                    result = convertToBase(result, destBase)
            print("\nNEW NUMBER:", result)
        val = input("\nType \"quit\" to end, return to continue: ")
        if "quit" not in val and "q" not in val:
            print("\n******* Another Run *******")
        
    
    print("\nThank you for using this program!")
        
def convertToBase10(sourceBase, sourceNum, power):
    # sourceBase is an int, sourceNum is a string
    # returns the source number in source base into a base 10 number
    if sourceNum == "":
        return 0
    
    adj = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'] # 0-15 adjusteed values, for easy access
    digit = sourceNum[-1:] # get right most value
    mult = adj.index(digit) # index of digit, which is the multiple
    return pow(sourceBase, power)*mult + convertToBase10(sourceBase, sourceNum[:-1], power+1)

def convertToBase(sourceNum, destBase):
    # sourceNum is a string, destBase is an int
    # given a source number in base 10, converting it to destination base and returning the new value
    adj = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'] # 0-15 adjusteed values, for easy access

    if (sourceNum == 0): # base case
        return "" # nothing left to add on

    # recursively divide num by destBase
    newNum = sourceNum//destBase # divide num by destBase, representing another power
    curMult = sourceNum % destBase # multiple of power
    return convertToBase(newNum, destBase) + adj[curMult]

if __name__ == '__main__': convertBase()