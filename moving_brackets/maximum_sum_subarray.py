'''
Problem Statement #
Given an array of positive numbers and a positive number ‘k’, 
find the maximum sum of any contiguous subarray of size ‘k’.
Example 1:
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:
Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
'''

# my code
def maximum_sum_subarray(arr, k):
	# initialize the values
	maximum_sum = -math.inf 
	window_start = 0
	# find each of the windows and make comparisons
	for i in range (0, len(arr)):
		window_end = window_start + k - 1 % len(arr)
		maximum_sum = max(maximum_sum, sum(arr[window_start:window_end + 1]))
	return maximum_sum

# answer
def max_sub_array_of_size_k(k, arr):
  max_sum , window_sum = 0, 0
  window_start = 0

  for window_end in range(len(arr)):
    window_sum += arr[window_end]  # add the next element
    # slide the window, we don't need to slide if we've not hit the required window size of 'k'
    if window_end >= k-1:
      max_sum = max(max_sum, window_sum)
      window_sum -= arr[window_start]  # subtract the element going out
      window_start += 1  # slide the window ahead
  return max_sum
