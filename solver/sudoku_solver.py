from pysat.formula import CNF
from pprint import pprint



class node:
	def __init__(self, values):
		self.right = None
		self.left = None
		self.values = None

	def __eq__(self,other):
		return self == other


def init_values(clauses):
	values = {}
	for i in clauses:
		if(len(i) > 2):
			for x in i:
				tmp = {x: False}
				values.update(tmp)
				if(x == clauses.nv):
					return values

def read_input(file):
	return CNF(from_file= file)

def read_DIMACS_sudoku(file):
	pass


def simplify_clauses(input):
	pass
# 	if(value in CONSTANT):
# 		pass
# 	else:
# 		# code
# 		pass

# 	pass
# 	return result

def is_solved(clauses):
	pass
# 	return clauses == True

def move_possible:
	pass

def solve(input: [], node_input):
	# if(not is_solved(node_input.values)):
	node_input.left = node(values)
	solve(input, node_input.left)
	node_input.right = node(values)
	solve(input, node_input.right)

	return

def output(values):
	f = open("demofile3.txt", "w")
	for x in values:
		for i in values[x]:
			if(i==True):
				f.write(f"{x} 0\n")
	f.close()

clauses = read_input('input/sudoku-rules.txt')
values = init_values(clauses)
root = node(values)
# s_clauses = simplify_clauses(clauses)
solve(clauses, root)
