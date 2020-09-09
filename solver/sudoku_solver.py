from pysat.formula import CNF


class node:
	def __init__(self, values):
		self.right = None
		self.left = None
		self.values = values

	def __eq__(self,other):
		return self == other

#initialize False values to every variable 2D hashmap - 1D is 11-99(no. of cell) and 2D variable(eg. 111-999)
# structure of cell 11 {11:{111,112...,119}}
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

#read rules
def read_input(file):
	return CNF(from_file= file)

#read constants
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

#return array of True/False values based on clauses in combination with values from the hashmap 'values'
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

# check satisfiability - AND and OR statement
def is_satisfied(clauses):
	for clause in clauses:
		if(True in clause):
			continue
		else:
			return False
	return True

#solve sudoku
def solve(clauses, node_input):
	for value in node_input.values:
		for variable in node_input.values[value]:
			node_input.left = node(node_input.values)
			solve(input, node_input.left)
			node_input.values[value][variable] = not node_input.values[value][variable]
			node_input.right = node(values)
			solve(input, node_input.right)

	return

#generate output file
def output(values):
	f = open("output.txt", "w")
	for value in values:
		for variable in values[value]:
			if(values[value][variable]==True):
				f.write(f"{variable} 0\n")
	f.close()


if __name__ == "__main__":
	clauses = read_input('input/sudoku-rules.txt')
	constants = read_input('input/sudoku-example.txt')
	values = init_values(clauses)
	tmp = to_bool(clauses.clauses, values, constants.clauses)
	print(tmp[0])
	# s_clauses = simplify_clauses(clauses)
	print(is_satisfied(tmp))
	output(values)