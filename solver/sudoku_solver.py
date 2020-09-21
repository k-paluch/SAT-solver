import functions
import operator
import random

if __name__ == "__main__":
	true_values = functions.init_true_values()
	clauses = functions.read_input('input/sudoku-rules.txt').clauses
	constants = functions.read_sudokus('input/9x9.txt')
	literals = functions.get_literals(clauses)
	
	data = (clauses, literals)

	t = random.randint(0,len(constants)-1)
	#remove constants from literals
	for constant in constants[66]:
		for literalindex in reversed(range(len(literals))):
			if str(literals[literalindex])[:-1] == str(constant)[:-1]:
				literals.remove(literals[literalindex])
		true_values.append(constant)
		data = functions.simplify_clauses_true(data[0], constant, data[1])

	print(constants[66])


	literals = functions.heur3(clauses)

	root = functions.node(literals, clauses)
	c = functions.solve(root)
	
	
	print(c)
	print(len(c))
	print('unsatisfied')