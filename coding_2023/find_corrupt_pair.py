'''
Problem Challenge 1
Find the Corrupt Pair (easy)
We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. The array originally contained all the numbers from 1 to ‘n’, but due to a data error, one of the numbers got duplicated which also resulted in one number going missing. Find both these numbers.
Example 1:
Input: [3, 1, 2, 5, 2]
Output: [2, 4]
Explanation: '2' is duplicated and '4' is missing.
Example 2:
Input: [3, 1, 2, 3, 6, 4]
Output: [3, 5]
Explanation: '3' is duplicated and '5' is missing.
'''
def find_corrupt_pair(nums):
	i = 0
	while i < len(nums):
		j = nums[i] - 1
		if nums[i] != nums[j]:
			# swap
			nums[i], nums[j] = nums[j], nums[i]
		else:
			i += 1
	# finished sorting

	corrupt = []

	for i in range(len(nums)-1):
		if nums[i] != i + 1:
			# found corrupt
			corrupt.append(nums[i])
			corrupt.append(i + 1)
	return corrupt

print(find_corrupt_pair([3, 1, 2, 5, 2]))

