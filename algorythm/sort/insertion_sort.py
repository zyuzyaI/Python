import timeit

def insertion_sort(mass):
	for i in range(1, len(mass)):
		item = mass[i]
		j = i -1
		while j >= 0 and (mass[j] > item):
			mass[j + 1] = mass[j]
			j -= 1
		mass[j + 1] = item
	return mass

print(insertion_sort([5,2,3,1,4]))

print('is work time: ', timeit.timeit('insertion_sort([5,2,3,1,4])', setup='from __main__ import insertion_sort', number=1))
