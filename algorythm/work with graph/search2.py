'''Знаходить всі шляхи на графі із початкової точки
в кінцеву за допомогою стека.
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
	solns = generate( ([start], []), goal, graph)
	solns.sort(key=lambda x: len(x))
	return solns

def generate(paths, goal, graph):
	solns = []
	while paths:
		front, paths = paths
		state = front[-1]
		if state == goal:
			solns.append(front)
		else:
			for arc in graph[state]:
				if arc not in front:
					paths = (front + [arc]), paths
	return solns

if __name__ == '__main__':
	tests(search)
