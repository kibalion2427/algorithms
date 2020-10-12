#
#   Write a function that takes in a sorted array of integers as well as a target
#   integer. The function should use the Binary Search algorithm to determine if
#   the target integer is contained in the array and should return its index if it
#   is, otherwise -1

#  array =  = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
# target = 33


# METHOD 1  O(log(N)) T  -  O(1) S
# def binarySearch(array, target):
#     left = 0
#     right = len(array) - 1
#     middle = 0

#     while(left <= right):
#         middle = (right + left) // 2

#         if(array[middle] > target):
#             right = middle - 1
#         elif(array[middle] < target):
#             left = middle + 1
#         else:
#             return middle
#     return -1

# print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73],10))

# METHOD 2  O(log(N))T   -   O(log(N))S

def binarySearchHelper(array, left, right, target):
    if(left > right):
        return -1

    middle = (right + left) // 2
    potentialMatch = array[middle]

    if(potentialMatch == target):
        return middle
    if(potentialMatch > target):
        return binarySearchHelper(array, left, middle - 1, target)
    if(potentialMatch < target):
        return binarySearchHelper(array, middle + 1, right, target)


def binarySearch(array, target):
    return binarySearchHelper(array, 0, len(array) - 1, target)


print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 0))
