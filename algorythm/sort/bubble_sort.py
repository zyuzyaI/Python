import timeit

def bubble_sort(mass):
	tmp = True
	while  tmp:
		tmp = False
		for i in range(len(mass) - 1):
			if mass[i] > mass[i+1]:
				mass[i], mass[i+1] = mass[i+1], mass[i]
				tmp = True
	return mass

print(bubble_sort([5,2,3,1,4]))

print('is work time: ', timeit.timeit("bubble_sort([5,2,3,1,4])", setup="from __main__ import bubble_sort", number=1))
