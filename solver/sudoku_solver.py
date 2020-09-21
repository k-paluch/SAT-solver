import functions
import operator

if __name__ == "__main__":
	true_values = functions.init_true_values()
	clauses = functions.read_input('input/sudoku-rules.txt').clauses
	constants = functions.read_sudokus('input/9x9.txt')
	literals = functions.get_literals(clauses)
	
	data = (clauses, literals)
	

	# heur1 [15: 111, 13: 132 ... etc]
	# sort [189: 111, 137: 112 etc]


	#remove constants from literals
	for constant in constants[0]:
		for literalindex in reversed(range(len(literals))):
			if str(literals[literalindex])[:-1] == str(constant)[:-1]:
				literals.remove(literals[literalindex])

	for constant in constants[0]:
		true_values.append(constant)
		data = functions.simplify_clauses_true(data[0], constant, data[1])


	#heuristic 1

	heur1 = {}
	for literal in literals:
		heur1.update(functions.heur1(literal, clauses))

	print(heur1)
	sorted_heur1 = sorted(heur1.items(), key=lambda x: x[1], reverse=True)

	#end heuristic 1

	#heuristic 2

	# heur2 = []
	# for literal in literals:
	# 	heur2.append(functions.heur1(literal, clauses))
	# sorted_heur2 = {k: v for k, v in sorted(heur1.items(), key=lambda item: item[1])}

	#end heuristic 2

	literals = []
	for x in range(len(sorted_heur1)):
		literals.append(sorted_heur1[x][0])

	print(literals)

	# literals = functions.heur2(literals)

	root = functions.node(literals, clauses)
	c = functions.solve(root)
	
	
	print(c)
	print(len(c))
	print('unsatisfied')