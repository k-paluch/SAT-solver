import functions

class node:
	def __init__(self, literals, clauses):
		self.right = None
		self.left = None
		self.literals = values
		self.clauses = clauses
		self.result = []

	def __eq__(self,other):
		return self == other



if __name__ == "__main__":
	true_values = functions.init_true_values()
	clauses = functions.read_input('input/sudoku-rules.txt').clauses
	constants = functions.read_input('input/sudoku_solved.txt').clauses
	literals = functions.get_literals(clauses)
	for constant in constants:
		print(len(clauses))
		true_values.append(constant)
		clauses = functions.simplify_clauses_true(clauses, constant[0])

	print(clauses)
	print(true_values)