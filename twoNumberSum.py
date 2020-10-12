def twoNumberSum(array, targetSum):
  array.sort()
  left = 0
  right = len(array) - 1

  while(left < right):
    if(array[left] + array[right] < targetSum):
      left += 1
    elif(array[left] + array[right] > targetSum):
      right += 1
    else:
      return [array[left], array[right]]
  return []


print(twoNumberSum([4, 6, 1, -3], 3))

# -4, -1, 1, 3, 5, 6, 8, 11