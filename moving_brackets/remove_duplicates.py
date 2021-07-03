'''
Problem Statement 
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the new length of the array.
Example 1:
Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
Example 2:
Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].
'''

# first attempt
def remove_duplicates(arr):
	left, right = 0, len(arr) - 1
	recent_left, recent_right = None, None
	while left < right:
		if recent_left = arr[left]:
			# duplicate must be removed
			arr = arr.remove(arr[left])
		if recent_right = arr[right]:
			arr = arr.remove(arr[right])
		left += 1
		right -= 1
	return arr

# answer
def remove_duplicates(arr):
  # index of the next non-duplicate element
  next_non_duplicate = 1

  i = 1
  while(i < len(arr)):
    if arr[next_non_duplicate - 1] != arr[i]:
      arr[next_non_duplicate] = arr[i]
      next_non_duplicate += 1
    i += 1

  return next_non_duplicate
