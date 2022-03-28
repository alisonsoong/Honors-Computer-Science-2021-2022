# Alison
# Lab 10

from time import *
from random import randint

def benchmark():

    n = getInput()
    print("Results (note that all times are milliseconds)\n")

    typeStr = ["Insertion", "Selection", "Bubble\t", "Merge\t", "Quick\t"]
    unTypeStr = ["Insertion", "Selection", "Bubble", "Merge", "Quick"]
    sortResults = []

    results = []
    for type in range(5):
        shuffled = []
        sorted = []
        fastest = 10000000
        slowest = 0
        averageSum = 0
        for run in range(10):
            # make list of size n
            pre = []
            for i in range(n):
                pre.append(randint(0,n-1))
            shuffled.append(pre.copy())

            startTime = time() # source: HCS Lab 10: Recursion and Sorting
            post = trial(type, pre)
            endTime = time()

            sorted.append(post)

            elapsedMS = (endTime - startTime) * 1000 # get elapsed time
            averageSum += elapsedMS
            if (fastest < 1):
                fastest = round(min(fastest, elapsedMS),3)
            else:
                fastest = int(min(fastest, elapsedMS))
            if (slowest < 1):
                slowest = round(max(slowest, elapsedMS),3)
            else:
                slowest = int(max(slowest, elapsedMS))

            print("Completed", unTypeStr[type], "Sort #" + str(run+1))
        
        resultString = typeStr[type]
        result = round(averageSum/10,3)
        if (result > 1):
            result = int(result)
        sortResults.append(typeStr[type] + "\t" + str(fastest) + "\t\t" + str(slowest) + "\t\t" + str(result))
        results.append([resultString, shuffled, sorted])

    print("Sort Method", "\t", "Fastest", "\t", "Slowest", "\t", "Average")
    print("------------", "\t", "-------", "\t", "-------", "\t", "-------")

    for sortResult in sortResults:
        print(sortResult)
    
    if (n <= 10):
        print("\nMore detailed results:")
        # print results
        for type in results:
            print("\n" + type[0] + ":")
            for i in range(10):
                print("original:", type[1][i])
                print("sorted:", type[2][i])
    print("\n------finished-------")

def getInput():
    while True:
        try:
            n = input("Size of list: ")
            if (int(n) > 0):
                return int(n)
            else:
                n = 0/0
        except:
            print("Please enter a valid integer greater than 0.")

def trial(type, lst):

    if type == 0:
        return insertionSort(lst)
    elif type == 1:
        return selectionSort(lst)
    elif type == 2:
        return bubbleSort(lst)
    elif type == 3:
        return mergeSort(lst)
    else:
        return quickSort(lst)

# ---- insertion sort ----

def insertionSort(lst):
    # make a copy
    lst = lst.copy()
    n = len(lst)
    for i in range(n):
        curVal = lst[i]
        curIndex = i-1
        while (curIndex >= 0 and lst[curIndex] > curVal):
            # keep on shifting stuff down
            lst[curIndex + 1] = lst[curIndex]
            curIndex -= 1

        # finally place it
        lst[curIndex + 1] = curVal

    return lst

# ---- selection sort ----

def selectionSort(lst):
    # make a copy
    lst = lst.copy()
    n = len(lst)
    for i in range(n):
        swapInd = i
        for j in range(i+1, n):
            if (lst[swapInd] > lst[j]):
                swapInd = j
        lst[swapInd], lst[i] = lst[i], lst[swapInd]
    
    return lst

# ---- bubble sort ----

def bubbleSort(lst):
    # source: https://www.programiz.com/dsa/bubble-sort
    lst = lst.copy()
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            # don't include the already sorted values
            if (lst[j] > lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

# ---- merge sort ----
    
def mergeSort(lst):
    # source: Python Programming : An Introduction to Computer Science by John Zelle
    lst = lst.copy()
    mergeSortRec(lst)
    return lst

def mergeSortRec(lst):
    n = len(lst)

    if (n>1):
        mid = n//2
        front, back = lst[:mid], lst[mid:]
        mergeSortRec(front)
        mergeSortRec(back)
        merge(front, back, lst)

def merge(lst1, lst2, lst3):
    i1, i2, i3 = 0, 0, 0
    n1 = len(lst1)
    n2 = len(lst2)

    while (i1 < n1 and i2 < n2):
        if (lst1[i1] < lst2[i2]):
            lst3[i3] = lst1[i1]
            i1+=1
        else:
            lst3[i3] = lst2[i2]
            i2+=1
        i3+=1

    while (i1 < n1):
        lst3[i3] = lst1[i1]
        i1 += 1
        i3+=1
    while (i2 < n2):
        lst3[i3] = lst2[i2]
        i2 += 1
        i3+=1
        


# ---- quick sort ----

def quickSort(lst):
    # source: https://www.geeksforgeeks.org/quick-sort/
    lst = lst.copy()
    quickSortRec(0, len(lst)-1, lst)
    return lst

def quickSortRec(start, end, lst):
    if (start < end):
        p = partition(start, end, lst)
        quickSortRec(start, p-1, lst)
        quickSortRec(p+1, end, lst)

def partition(start, end, lst):
    pivotInd = start
    pivotVal = lst[start]
    
    while start < end:
        # start value increses until greater than pivot
        while start < len(lst) and lst[start] <= pivotVal:
            start+=1
        # end value decreases until less than pivot
        while lst[end] > pivotVal:
            end-=1
        if (start < end): # don't cross
            lst[start], lst[end] = lst[end], lst[start]

    lst[pivotInd], lst[end] = lst[end], lst[pivotInd]

    return end


if __name__ == '__main__': benchmark()