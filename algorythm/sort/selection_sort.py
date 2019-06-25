import timeit

def selection_sort(mass):
	for i in range(len(mass)):
		index_min = i
		for j in range(i+1, len(mass)):
			if mass[j] < mass[index_min]:
				index_min = j
		mass[i], mass[index_min] = mass[index_min], mass[i]
	return mass

print(selection_sort([5,2,3,1,4]))

print('is work time: ', timeit.timeit("selection_sort([5,2,3,1,4])", setup="from __main__ import selection_sort", number=1))
