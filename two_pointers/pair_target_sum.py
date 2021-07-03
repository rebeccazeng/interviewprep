'''
Problem Statement 
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is 
equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they 
add up to the given target.

Example 1:
Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
Example 2:
Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
'''
# first approach
def _pair_target_sum(sorted):
	# don't have to go through each one because it is sorted
	for i in range(len(sorted)/2):
		left = i
		if sorted[left]:
			return [left]
		elif sorted[right]:
			return [right]
		elif sorted[left] + sorted[right] == target:
			return [left, right]

# answer
def pair_with_targetsum(arr, target_sum):
  left, right = 0, len(arr) - 1
  while(left < right):
    current_sum = arr[left] + arr[right]
    if current_sum == target_sum:
      return [left, right]

    if target_sum > current_sum:
      left += 1  # we need a pair with a bigger sum
    else:
      right -= 1  # we need a pair with a smaller sum
  return [-1, -1]