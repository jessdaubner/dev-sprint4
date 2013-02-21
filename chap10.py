##########################################################
# Name: is_anagram
# Parameters: two strings
# Return: boolean - True if the two words are anagrams
# Desc: takes two words as arguments and return True if 
# the words are anagrams 
##########################################################

def is_anagram(word1, word2):
	
	for letter in word1:
		if letter not in word2: 
			return False
	return True

def main():
	w1 = raw_input("Enter a word that you think is an anagram: ")
	w2 = raw_input("Enter the anagram of the first word: ")

	if is_anagram(w1, w2) is True:
		print ("The words " + "'" + w1 + "'" + " and "+ "'" + w2 + "'" + " are anagrams!")
	else:
		print ("The words " + "'" + w1 + "'" + " and "+ "'" + w2 + "'" + " are NOT anagrams!")
main()

##########################################################
# Name: interlocked
# Parameters: 2, a list of words and a word
# Return: True, if the specific word is found in the
# word list, False otherwise
# Desc:  
#  
##########################################################
from bisect import *

def make_list():
	word_list = []
	fin = open('words.txt')
	for line in fin:
		word = line.strip()
		word_list.append(word)
	return word_list

def in_list(a_list, value):
	"""Locate the string in word_list that matches word
	"""
	i = bisect_left(a_list, value)
	if i != len(a_list) and a_list[i] == value:
		return True
	else:
		return False 

def interlocked(b_list, word):
	chrs1 = word[::2] # even indices of string
	chrs2 = word[1::2] # odd indices of string
	return in_list(b_list, chrs1) and in_list(b_list, chrs2) 

def interlocked_3way(c_list, word):
	for j in range(3):
		three_way = word[j::3]
		if not in_list(c_list, three_way):
			return False
	return True

def main():
	word_list = make_list()
	
	print "The following are interlocked words: "
	for word in word_list:
		if interlocked(word_list, word):
			print word, word[::2], word[1::2]
	
	print "The following are three-way interlocked words: "
	for word in word_list:
		if interlocked_3way(word_list, word):
			print word, word[0::3], word[1::3], word[2::3]

main()


