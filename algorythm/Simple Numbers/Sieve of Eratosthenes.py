def Sieve of Eratosthenes(n):
	list_erat = [True] * n
	list_erat[0] = list_erat[1] = False
	for i in range(2, 10001):
		for j in range(2 * i, 100001, i):
			list_erat[j] = False
	return list_erat
