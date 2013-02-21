# Desc: create a function that imitates ROT13 encryption
# Version 2 -- 21 February 2013

def rotate_word(str, int):
	rotated_words = ''
	for j in range(len(str)):
		character = str[j]
		code = ord(character)
		if code == 32: # keeps spacing the same, if sentence
			new_code = code
		elif code >= (122 - (int-1)): # 122 = ascii value of 'z'
	 		new_code = 97 + (code - (122 - (int-1))) # 97 is ascii value of 'a'
		elif (code >= (90 - (int-1))) and (code <= 90): # 90 = ascii value of 'Z' 
			new_code = 65 + (code - (90 - (int-1))) # 65 = ascii value of 'A'
		else:	
			new_code = code + int
		new_chr = chr(new_code)
		rotated_words = rotated_words + new_chr
	return rotated_words
