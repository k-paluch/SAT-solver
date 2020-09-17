import functions
import timeit
class node:
	def __init__(self, literals, clauses):
		self.right = None
		self.left = None
		self.literals = literals
		self.clauses = clauses

	def __eq__(self,other):
		return self == other



if __name__ == "__main__":
	true_values = functions.init_true_values()
	clauses = functions.read_input('input/sudoku-rules.txt').clauses
	constants = functions.read_input('input/sudoku-example.txt').clauses
	literals = functions.get_literals(clauses)
	start = timeit.default_timer()
	data = (clauses, literals)
	for constant in constants:
		print(len(clauses))
		true_values.append(constant[0])
		data = functions.simplify_clauses_true(data[0], constant[0], data[1])


	root = node(literals, clauses)
	c = functions.solve(root)
	stop = timeit.default_timer()
	print('Runtime: ', stop - start) 
	print(c)