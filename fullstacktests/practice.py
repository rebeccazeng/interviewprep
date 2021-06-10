# Python, written in Sublime window
def cents(dollars, tax_percent):
	"""
	Given an amount in dollars and a tax percentage. Return an array with the tax amount in cents.
	"""
	# assuming that tax percent is given in format "2.5%" otherwise if the format was in "0.025" then we would multiply answer by 100
	tax_amount_in_cents = dollars * tax_percent
	return [tax_amount_in_cents]

# Python, written in Sublime window
import random
def random_integer(deck):
	"""
	Given the deck ['A',1,2,3,4,5,6,7,8,9,10,'J','K','Q'], write a function that shuffles the deck using the randint function. 
	The random module includes a basic function randint(a, b) that returns a uniformly random integer from a to b (including both endpoints). 

	"""
	# Initiate seen numbers to avoid dupes
	seen_int=[]
	# Initiate new list
	shuffled_deck = []

	for i in range(len(deck)):
		item = deck[i]
		# Solve for the numbers, 1 to 10 inclusive on both
		random = random.randint(1, 10)
		# Replace all ints with another int
		if isinstance(item, int) and random not in seen_int:
			seen_int += random
			deck[i] = random

		# Trying to find a random number that is available
		elif isinstance(item, int) and random in seen_int:
			while random in seen_int:
				# Keep looking for random
				random = random.randint(1, 10)
			seen_int += random
			deck[i] = random

	# After replacing the numbers, shuffle the deck
	return random.shuffle(deck, 0.1)

# Python, written in Sublime window
def total_vowel_weight(s):
	"""
	Given a string s, return the sum of the vowels in the string if each vowel's weight increases by 1 according to the vowels order. 

	"""
	total_weight = 0
	# Loop through the string and add the totals
	for letter in s:
		if letter == "a":
			total_weight += 1
		elif letter == "e":
			total_weight += 2
		elif letter == "i":
			total_weight += 3
		elif letter == "o":
			total_weight += 4
		elif letter == "u":
			total_weight += 5
		# No need else statement b/c else: do nothing
	return total_weight

# Python, written in Sublime
def recursive_total_vowel_weights(s):
	"""
	Write a recursive version of the previous function (or an iterative version if you already did a recursive version).
	"""
	def helper(letter_index, total):
		if letter_index > len(s):
			return total
		letter = s[letter_index]
		if letter == "a":
			return helper(letter_index + 1, total + 1)
		elif letter == "e":
			return helper(letter_index + 1, total + 2)
		elif letter == "i":
			return helper(letter_index + 1, total + 3)
		elif letter == "o":
			return helper(letter_index + 1, total + 4)
		elif letter == "u":
			return helper(letter_index + 1, total + 5)
		else:
			return helper(letter_index + 1, total)
	return helper(0, 0)

























