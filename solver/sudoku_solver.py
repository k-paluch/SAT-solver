from pysat.formula import CNF
from pprint import pprint



class node:
	def __init__(self, left, right, values):
		self.right = None
		self.left = None
		values = None

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


# def simplify_clauses(input):
# 	if(value in CONSTANT):
# 		pass
# 	else:
# 		# code
# 		pass

# 	pass
# 	return result

# def is_solved(clauses):
# 	return clauses == True

def solve(input: [], node_input):
	# if(not is_solved(node_input.values)):
	tmp = node(None, None, values)
	node_input.left = tmp
	solve(input, tmp.left)
	node_input.right = tmp
	solve(input, tmp.right)

	return




clauses = read_input('input/sudoku-rules.txt')
values = init_values(clauses)
root = node(None, None, values)
# s_clauses = simplify_clauses(clauses)
solve(clauses, root)
