import functions
import timeit

if __name__ == "__main__":
	true_values = functions.init_true_values()
	clauses = functions.read_input('input/sudoku-rules.txt').clauses
	constants = functions.read_sudokus('input/9x9.txt')
	literals = functions.get_literals(clauses)
	start = timeit.default_timer()
	data = (clauses, literals)
	
	for constant in constants[55]:
		true_values.append(constant)
		data = functions.simplify_clauses_true(data[0], constant, data[1])

	
	root = functions.node(literals, clauses)
	c = functions.solve(root)
	stop = timeit.default_timer()
	print('Runtime: ', stop - start) 
	print(c)
	print(len(c))