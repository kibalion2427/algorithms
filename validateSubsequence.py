# array = [5, 1, 22, 25, 6, -1, 8, 10,11,17]
# sequence = [1, 6, -1, 10]
def isValidSubsequence(array, sequence):
    pointerSequence = 0
    pointerArray = array.index(sequence[0])
    while(pointerSequence < len(sequence) and pointerArray < len(array)):
        if (sequence[pointerSequence] == array[pointerArray]):
            pointerSequence += 1
        pointerArray += 1
    return pointerSequence == len(sequence)


print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10],
                         [5, 1, 22, 25, 6, -1, 8, 10, 10]))
