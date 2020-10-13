
#   Write a function that takes in two non-empty arrays of integers, finds the
#   pair of numbers (one from each array) whose absolute difference is closest to
#   zero, and returns an array containing these two numbers, with the number from
#   the first array in the first position.


#   Note that the absolute difference of two integers is the distance between
#   them on the real number line. For example, the absolute difference of -5 and 5
#   is 10, and the absolute difference of -5 and -4 is 1.


#   You can assume that there will only be one pair of numbers with the smallest
#   difference.


# arrayOne= [-1, 5, 10, 20, 28, 3]
# arrayTwo  = [26, 134, 135, 15, 17]

# Output = [28,26]

# -1 3 5 10 27 28
# 15 17 26 134 135

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    firstIdx = 0
    secondIdx = 0
    minimumDifference = float("inf")
    smallestPair = []

    while(  firstIdx < len(arrayOne) and secondIdx < len(arrayTwo)):
        firstNum = arrayOne[firstIdx]
        secondNum = arrayTwo[secondIdx]

        currentDifference = abs( firstNum - secondNum )
        
        if currentDifference == 0:
            return [firstNum, secondNum]

        if firstNum < secondNum:
            firstIdx += 1
        elif firstNum > secondNum:
            secondIdx += 1
        
        if(currentDifference < minimumDifference):
            minimumDifference = currentDifference
            smallestPair = [firstNum,secondNum]
    return smallestPair

print(smallestDifference([-1, 5, 10, 27, 28, 3],[26, 134, 135, 15, 17]))

        
        
