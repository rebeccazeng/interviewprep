
'''
Problem Statement 
Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.
Example 1:
Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
Example 2:
Input: [-3, -1, 0, 1, 2]
Output: [0 1 1 4 9]
'''

# quick runthrough
def squaring_sorted_array(arr):
	left, right = 0, len(arr) - 1
	squared_sorted = []
	while left < right:
		square = arr[left] ** 2
		if abs(arr[left]) >= abs(arr[right]):
			# means that you can put the left one after the right after you square
			squared_sorted.append(square)
		else: 
			squared_sorted.insert(0, square)
		left += 1
	return squared_sorted

# answer
def make_squares(arr):
  n = len(arr)
  squares = [0 for x in range(n)]
  highestSquareIdx = n - 1
  left, right = 0, n - 1
  while left <= right:
    leftSquare = arr[left] * arr[left]
    rightSquare = arr[right] * arr[right]
    if leftSquare > rightSquare:
      squares[highestSquareIdx] = leftSquare
      left += 1
    else:
      squares[highestSquareIdx] = rightSquare
      right -= 1
    highestSquareIdx -= 1

  return squares