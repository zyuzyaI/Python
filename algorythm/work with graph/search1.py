'''Знаходить всі шляхи на графі із початкової точки
в кінцеву за допомогою рекурсії.
'''
Graph = {'A': ['B', 'E', 'G'],
		'B':['C'],
		'C':['D', 'E'],
		'D':['F'],
		'E':['C', 'F','G'],
		'F':[],
		'G':['A']
}

def tests(searcher):
	print(searcher('E', 'D', Graph))
	for x in ['AG', 'GF', 'BA', 'DA']:
		print(x, searcher(x[0], x[1], Graph))

def search(start, goal, graph):
	solns = []
	generate([start], goal, solns, graph)
	solns.sort(key=lambda x: len(x))
	return solns

def generate(path, goal, solns, graph):
	state = path[-1]
	if state == goal:
		solns.append(path)
	else:
		for arc in graph[state]:
			if arc not in path:
				generate(path + [arc], goal, solns, graph)

if __name__ == '__main__':
	tests(search)
