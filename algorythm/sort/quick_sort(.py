
import timeit

def quick_sort(mass):
	if len(mass) <= 1:
		return mass

	q = mass[len(mass) // 2]
	l_mass = [n for n in mass if q > n]
	q_mass = [q] * mass.count(q)
	r_mass = [n for n in mass if q < n]
	return quick_sort(l_mass) + q_mass + quick_sort(r_mass)
print(quick_sort([5,4,3,2,1]))
print('is work time: ', timeit.timeit('quick_sort([5,4,3,2,1])', setup='from __main__ import quick_sort', number=1))