from pysat.formula import CNF


class node:
	def __init__(self, values):
		self.right = None
		self.left = None
		self.values = values

	def __eq__(self,other):
		return self == other


def init_values(clauses):
	values = {}
	for i in clauses:
		if(len(i) > 2):
			tmp = int(str(i[0])[:-1])
			values.update({tmp:{}})
			for x in i:
				values[tmp].update({x: False})
				if(x == clauses.nv):
					return values

def read_input(file):
	return CNF(from_file= file)

def read_DIMACS_sudoku(file):
	return CNF(from_file= file)


def simplify_clauses(input):
	pass
# 	if(value in CONSTANT):
# 		pass
# 	else:
# 		# code
# 		pass

# 	pass
# 	return result

def to_bool(clauses, values, constants):
	tmp = []
	for variable in constants:
		values[int(str(variable[0])[:-1])][variable[0]] = True

	for index, clause in enumerate(clauses):
		tmp.append([])
		for literal in clause:
			if(str(literal).startswith('-')):
				tmp[index].append(not values[int(str(literal)[1:-1])][int(str(literal)[1:])])
			else:
				tmp[index].append(values[int(str(literal)[:-1])][literal])

	return tmp,values

def is_satisfied(clauses):
	for x in clauses:
		if(True in x):
			continue
		else:
			return False
	return True


def solve(clauses, node_input):
	for x in node_input.values:
		for i in node_input.values[x]:
			node_input.left = node(node_input.values)
			solve(input, node_input.left)
			node_input.values[x][i] = not node_input.values[x][i]
			node_input.right = node(values)
			solve(input, node_input.right)

	return

def output(values):
	f = open("output.txt", "w")
	for x in values:
		for i in values[x]:
			if(i==True):
				f.write(f"{x} 0\n")
	f.close()

clauses = read_input('input/sudoku-rules.txt')
sudoku = read_input('input/sudoku-example.txt')
values = init_values(clauses)
tmp = to_bool(clauses.clauses, values, sudoku.clauses)
# s_clauses = simplify_clauses(clauses)
print(is_satisfied(tmp))
output(values)