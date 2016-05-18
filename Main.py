################################################################################
#
def shiftRight(aList,indexList,listLen):
    lastItem = aList[listLen-1]                 # Copy Last element in the list. pop out
    for shifter in indexList:
        if shifter != 0 :
            aList[shifter] = aList[shifter-1]   # Shift all to the right. Note: negative index is cool but will avoid at this time
    aList[0] = lastItem                         # Put last element at beginning
 

################################################################################
#
def shiftVector(aList, shiftTimes):
    listLen   = len(aList)
    indexList =list(range(listLen-1,-1,-1))  # Build reverse indexer list 4,3,2,1,0  last is always 0
    
    for i in indexList :            # Shift vector many times
        if shiftTimes > 0 :
            shiftRight(aList,indexList,listLen) # Shift vector right one time.
            shiftTimes-=1

################################################################################
#
def main():
    aList = ['a','b','c','d']   # list of items to shift
    shiftTimes = 3              # How many time to shift
    shiftVector(aList, shiftTimes) # Go Shift vector that many times
    print (aList)
    
################################################################################
#
main()

