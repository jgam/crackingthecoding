#1.1
#Implement an algorithm to determine if a string has all unique characters. what if you cannot use additional data structures?

def is_unique(input_str):
	set_input_str = set([i for i in input_str])
	if len(set_input_str) == len(input_str):
		return True
	return False
print(is_unique('abcd'))
#True
print(is_unique('abcc'))
#False

#1.2
#given two strings, write a method to decide if one is a permutaiton of the other
def check_permutation(input_str1,input_str2):
	first = sorted([i for i in input_str1])
	second = sorted([i for i in input_str2])
	if ''.join(first) == ''.join(second):
		return True
	return False

print(check_permutation('abc','acv'))
#False
print(check_permutation('abc','acb'))
#True

#1.3
#write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the true length of the string
def URLify(input_str):
	ret_list = []
	for char in input_str:
		if char == " ":
			ret_list.append("%20")
		else:
			ret_list.append(char)
	return ''.join(ret_list)

print(URLify("Mr John Smith"))
#Mr%20John%20Smith

#1.4
#Function to check if it is a permutation of a palindrome.
def Palindrome_Permutation(input_str):
	cmp_dict = {}
	for char in input_str:
		if char in cmp_dict:
			cmp_dict[char] += 1
		else:
			cmp_dict[char] = 1

	single_char = 0
	even_char = 0
	for key,value in cmp_dict.items():
		if single_char > 1:
			return False
		if value % 2 == 0:
			even_char += 1
		else:
			single_char += 1
	return True

print(Palindrome_Permutation('aaabbbccc'))
#False
print(Palindrome_Permutation('aabbccc'))
#True

#1.5
#three types of edits that can be performed on strings:
#insert a character
#remove a character
#replace a character
#write a function to check if they are one edit (or zero edits) away.
def one_away(input_str1, input_str2):
	index1 = 0
	index2 = 0
	limit = 0
	while index1 < len(input_str1) and index2 < len(input_str2):
		if limit > 1:
			return False
		if input_str1[index1] == input_str2[index2]:
			index1 += 1
			index2 += 1
			continue
		else:
			#this is addition
			if len(input_str1) > len(input_str2):
				index1 += 1
			elif len(input_str2) > len(input_str1):
				index2 += 1
			else:
				limit += 1
				continue
			limit += 1
		#code
	if limit > 1:
		return False
	return True

print(one_away('pale','ple'))
#True
print(one_away('pales','pale'))
print(one_away('pale','bake'))

#1.6
#method to perform basic string compression using the counts of repeated characters
#string aabcccccaaa would become a2b1c5a3
def string_compression(input_str):
	orig_char = input_str[0]
	count = 1
	ret_string = ''
	for char in input_str[1:]:
		if orig_char != char:
			#save the original and numbers
			ret_string += orig_char + str(count)
			orig_char = char
			count = 1
		else:
			count += 1
	ret_string += orig_char + str(count)
	if len(ret_string) == len(input_str):
		return input_str
	return ret_string

print(string_compression('aaabbbccccaaaa'))
print(string_compression('aabbcc'))