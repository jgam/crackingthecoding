#list of primes
def list_of_primes(num_list):
	start = 4
	ret_list = [2,3]
	for i in range(start, num_list):
		if i % 2 == 0:
			continue
		else:
			for v in ret_list[1:]:
				print(i,v)
				if i % v != 0:
					if v == ret_list[-1]:
						ret_list.append(i)
					continue
				else:
					break
	return ret_list

#print(list_of_primes(10000))

#번외
def sieve_of_erathosthenese(limit):
	basic_list = [1] * limit
	basic_list[1] = 1
	basic_list[2] = 1
	prime_cond = False
	prime_list = [2,3]
	for i in range(4, limit+1):
		for prime in prime_list:
			if i % prime == 0:
				prime_cond = False
				break
			else:
				prime_cond = True
				continue
		if prime_cond:
			prime_list.append(i)

	return prime_list

print(sieve_of_erathosthenese(150))

#6.1
#You have 20 bottles of pills. 19 bottles have 1.0gram pills, but one has pills of weight 1.1 grams. Given a scale that provdes an exact measurement, how would you find the heavy bottle? you can only use the scale once.
#-> we can number the 20 bottles from 1 to 20. Then, take the number of pills of the number of that bottles. Then we can figure out by the numbers after decimal point to see which bottle.

#6.2
#you have a basketball hoop and someone says that you can play one of two games.
#game1: you get one shot to make the hoop
#game2: you get three shots and you have to make two of three shots
#-> game 1 is P
#-> game 2 is addition of making 3 shots and 2shots -> p^3 + 3(p^2(1-p))
#-> Now compare the value to get the following results
#->  Game 1 for 0<p<.5 and Game 2 for .5 < p < 1

#6.3
#Thsere is an 8x8 chessboard in which two diagonally opposite corners have been cut off. You are given 31 dominos, and a single domino can cover exactly two squares. Cna you use the 31 dominos to cover the entire board? Prove your answer.
#-> my logic is that on chess board, we have 32 whites and 32 blacks. Because the dominoes always get 1 black and 1 white board. 31 dominoes will get 31 blacks and 31 whites rather than 30 blacks and 32 whites or vice versa.