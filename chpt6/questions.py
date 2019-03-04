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

print(list_of_primes(10000))