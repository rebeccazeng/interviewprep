'''
Problem Challenge 2
Find the Smallest Missing Positive Number (medium)
Given an unsorted array containing numbers, find the smallest missing positive number in it.
Example 1:
Input: [-3, 1, 5, 4, 2]
Output: 3
Explanation: The smallest missing positive number is '3'
Example 2:
Input: [3, -2, 0, 1, 2]
Output: 4
Example 3:
Input: [3, 2, 5, 1]
Output: 4
'''

# mycode
def find_first_missing_positive(nums):
	nums.sort()
	pointer = 0
	while pointer < len(nums):
		if nums[pointer] < 0:
			pointer += 1
		else:
			break;

	# now the pointer at the positive number
	val = nums[pointer]
	while pointer < len(nums):
		if nums[pointer] != val:
			return val
		else:
			val += 1
			pointer += 1
	return val

print(find_first_missing_positive([-3, 1, 5, 4, 2]))
