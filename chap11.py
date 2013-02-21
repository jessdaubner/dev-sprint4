#######################################################################
# Name: has_duplicates
# Parameters: 1, a list (l)
# Return: Boolean value 
# Desc: Returns true if any object appears more than once in a list
#######################################################################

def has_duplicates(l):
	d = dict()
	for i in l:
		if i in d:
			return True
		d[i] = True # map item not currently in dictionary to value True
	return False
	
def main():
	num_list = [1, 2, 3, 4, 5, 6, 7]
	print has_duplicates(num_list)
	dup_list = num_list + [3]
	print has_duplicates(dup_list)
main()

#######################################################################
# Name: rotate_pairs
# Parameters: 2 - a string (s) and a dictionary of strings (s)
# Returns: string (s), rotated string (rotated_word), rotation number(i)
# Desc: Finds all the rotated strings (rotated from 1 to 13 places) 
# that correspond to actual words using a dictionary of words from 
# the words.txt file
#######################################################################
import chap8

def make_dictionary():
	fin = open('words.txt')
	d = {}
	for line in fin:
		word = line.strip()
		d[word] = word
	
	return d

def rotated_pairs(s, d):
	for i in range (1, 14):
		rotated_word = chap8.rotate_word(s, i)	
		if rotated_word in d:
			print s, rotated_word, i

def main():
	word_dict = make_dictionary()

	for key in word_dict:
		rotated_pairs(key, word_dict)

main()