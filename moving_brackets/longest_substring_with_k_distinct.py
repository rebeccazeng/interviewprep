'''
Problem Statement #
Given a string, find the length of the longest substring 
in it with no more than K distinct characters.
Example 1:
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than 
'2' distinct characters is "araa".
Example 2:
Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than 
'1' distinct characters is "aa".
Example 3:
Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than 
'3' distinct characters are "cbbeb" & "bbebi".
'''


# unneeded
# def letters_check(str, k):
# 	"""
# 	Check through the string to see if the letter has been seen yet.
# 	Returns: True if there are k distinct
# 	"""

# my code before 15 mins ran out
def longest_substring_length(str, k):
	substrings = {}
	letters_seen = []
	window_start = 0

	for window_end in reversed(range(0, len(arr))):
		letter = str[window_start]
		while k > 0:
			if letter not in letters_seen:
				k -= 1
				# treat this as a set, though, for better runtime
				letters_seen.append(letter)
# answer
def longest_substring_with_k_distinct(str, k):
  window_start = 0
  max_length = 0
  char_frequency = {}

  # in the following loop we'll try to extend the range [window_start, window_end]
  for window_end in range(len(str)):
    right_char = str[window_end]
    if right_char not in char_frequency:
      char_frequency[right_char] = 0
    char_frequency[right_char] += 1

    # shrink the sliding window, until we are left with 'k' distinct characters in the char_frequency
    while len(char_frequency) > k:
      left_char = str[window_start]
      char_frequency[left_char] -= 1
      if char_frequency[left_char] == 0:
        del char_frequency[left_char]
      window_start += 1  # shrink the window
    # remember the maximum length so far
    max_length = max(max_length, window_end-window_start + 1)
  return max_length

