  
'''
Problem Statement 
Given an array of positive numbers and a positive number ‘S’, 
find the length of the smallest contiguous subarray whose sum 
is greater than or equal to ‘S’. Return 0, if no such subarray exists.
Example 1:
Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
Example 2:
Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
Example 3:
Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
'''

# my code
def smallest_subarray_with_given_sum(s, arr):
	window_sum = 0
	min_length = math.inf 
	window_start = 0

	for window_end in range(0, len(arr)):
		window_sum += arr[window_end] #add the next element to start counting the sum within the subarray
		# now we're going to shrink the window as small as possible until the window_sum is smaller than s
		while window_sum >= s:
			min_length = min(min_length, window_end - window_start + 1) # ? possible minimum brackets
			window_sum -= arr[window_start] # erase the one from the back
			window_start += 1 # move the brackets forward
	if min_length == math.inf:
		return 0
	return min_length







