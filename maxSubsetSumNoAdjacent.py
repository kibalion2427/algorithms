
#   Write a function that takes in an array of positive integers and returns the
#   maximum sum of non-adjacent elements in the array.

# If a sum can't be generated, the function should return 0

# array = [75, 105, 120, 75, 90, 135]
# output = 330 # 75 + 120 + 135


# 7, 10, 12, 7, 9, 14] -> 33//7 12  14
# 7, 10, 19,19, 28, 33

# maxSums [i] = max(maxSums[i-1],maxSums[i-2]+array[i])

def maxSubsetSumNoAdjacent(array):
    first = max(array[0], array[1])
    second = array[0]
    current = first

    for i in range(2, len(array)):
        print(second, first, current)
        current = max(first, second + array[i])
        second = first
        first = current

    return current


print(maxSubsetSumNoAdjacent([7, 10, 12, 7, 9, 14]))
