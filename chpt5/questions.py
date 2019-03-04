#5.1
#given 32-bit numbers, N and M, and two bit positions, i and j.
#a method to insert M into N such that M starts at bit j and ends at bit i.
def Insertion(N, M, i, j):
	end = len(str(N)) - i
	start = j-2

	if end < start:
		return "invalid range"
	elif end < 0 or start < 0:
		return "invalid range"

	N = str(N)
	N = N[:start] +str(M) + N[end:]
	return int(N)

print(Insertion(10000000000, 10011, 2, 6))


#5.2
#Given a real number between 0 and 1 that is passed in as a dobule,(ex. 0.72)
#print the binary representation. If the number cannot be represented accurately in binary with at most 32
#characters, print "error"
def Binary_to_string(real_num):
	str_num = str(real_num)
	start_index = str_num.index('.') + 1
	try:
		return '0.'+str(bin(int(str_num[start_index:])))[2:]
	except:
		return "ERROR"
print(Binary_to_string(0.72))

#5.3
#flip one 0 to get longest sequence of 1s and return its length
def flip_bit_to_win(real_num):
	num_to_change = str(bin(real_num))[2:]
	new_str = ''
	count = 0
	#here cange the binary to string with counting number of 1s
	for i in num_to_change:
		if i == '0':
			if count == 0:
				new_str += 'a'
				continue
			new_str += str(count)
			new_str += 'a'
			count = 0
		else:
			count += 1
	if num_to_change[-1] == '1':
		new_str += str(count)

	#here finally calculate the max num adding number of 1s and 0s
	max_num = 1
	for index in range(len(new_str)-1):
		if new_str[index] == 'a':
			if new_str[index-1] == 'a':
				if new_str[index+1] == 'a':
					continue
				cmp_num = int(new_str[index+1]) + 1
			elif new_str[index+1] == 'a':
				cmp_num = int(new_str[index-1]) + 1
			else:
				cmp_num = int(new_str[index-1]) + int(new_str[index+1]) + 1
			if cmp_num > max_num:
				max_num = cmp_num
		else:
			continue
	print(num_to_change)
	print(new_str)
	return max_num

print(flip_bit_to_win(72))
print(flip_bit_to_win(12))
print(flip_bit_to_win(1775))
