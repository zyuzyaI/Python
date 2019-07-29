# Решето Ератосфена
n = int(input())
arr = [i for i in range(n+1)]
prime_list = []
i = 2
while i <= n:
	if arr[i] != 0:
		prime_list.append(arr[i])
		for j in range(i, n+1, i):
			arr[j] = 0
	i += 1
print(len(prime_list))
