from pysat.formula import CNF
import time

class node:
	def __init__(self, values,clauses):
		self.right = None
		self.left = None
		self.values = values
		self.clauses = clauses

	def __eq__(self,other):
		return self == other

# #initialize False values to every variable 2D hashmap - 1D is 11-99(no. of cell) and 2D variable(eg. 111-999)
# # structure of cell 11 {11:[False, False,]] - 1-9 [0-8]}
# def init_values(clauses):
# 	values = {}
# 	for i in clauses:
# 		if(len(i) > 2):
# 			tmp = int(str(i[0])[:-1])
# 			values.update({tmp:{}})
# 			for x in i:
# 				values[tmp].update({x: 0})
# 				if(x == clauses.nv):
# 					return values

#read rules
def read_input(file):
	return CNF(from_file= file)

#read constants
def read_DIMACS_sudoku(file):
	return CNF(from_file= file)




# #return array of True/False values based on clauses in combination with values from the hashmap 'values'
# def to_bool(clauses, values, constants):
# 	tmp = []
# 	for variable in constants:
# 		values[int(str(variable[0])[:-1])][variable[0]] = True

# 	for index, clause in enumerate(clauses):
# 		tmp.append([])
# 		for literal in clause:
# 			if(str(literal).startswith('-')):
# 				tmp[index].append(not values[int(str(literal)[1:-1])][int(str(literal)[1:])])
# 			else:
# 				tmp[index].append(values[int(str(literal)[:-1])][literal])

# 	return tmp,values

# check satisfiability - AND and OR statement
def is_satisfied(clauses):
	for clause in clauses:
		if(True in clause):
			continue
		else:
			return False
	return True

solution_found = False
#solve sudoku
def solve(node_input):
	for value in node_input.values:
		for variable in node_input.values[value]:
			if(is_satisfied(node_input.clauses)==False or solution_found == False):

				node_input.values[value][variable] = True
				simplify_clauses(node_input.clauses)
				node_input.left = node(node_input.values,clauses)
				solve(input, node_input.left)

				node_input.values[value][variable] = False
				simplify_clauses(node_input.clauses)
				node_input.right = node(node_input.values,clauses)
				solve(input, node_input.right)
			else:
				salution_found = True
				return

	return

#generate output file
def output(values):
	f = open("output.txt", "w")
	for value in values:
		for variable in values[value]:
			if(values[value][variable]==True):
				f.write(f"{variable} 0\n")
	f.close()

def simplify_clauses(clauses, literal):
	tmp = clauses
	print(literal)
	negation = int('-' + str(literal))
	for clause in reversed(range(len(tmp))):
		if(literal in tmp[clause]) or (negation in tmp[clause]):
			tmp.pop(clause)

	return tmp

if __name__ == "__main__":
	solution_found = False
	clauses = read_input('input/sudoku-rules.txt').clauses
	constants = read_input('input/sudoku-example.txt').clauses
	print(constants)
	for constant in constants:
		clauses = simplify_clauses(clauses, constant[0])
	# root = node(values, clauses)
	# solve(root)
	# output(values)

