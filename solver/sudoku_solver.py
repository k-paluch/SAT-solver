import functions
from random import randint

if __name__ == "__main__":
	true_values = functions.init_result()
	clauses = functions.read_input('input/16x16_rules.txt').clauses
	constants = functions.read_sudokus('input/16x16.txt')
	literals = functions.get_literals(clauses)
	
	data = (clauses, literals)

	t = randint(0,len(constants)-1)

	#pick random sudoku and remove constants from literals
	for constant in constants[t]:
		for index in reversed(range(len(literals))):
			for literal in literals:
				literals = functions.adjust_literals(literals, literal, True)
		true_values.append(constant)
		data = functions.simplify_clauses_true(data[0], constant, data[1])

	print(constants[t])
	#pick heuristic
	tmp = 3
	if(tmp == 1):
		literals = functions.heur1(literals,clauses)
	elif(tmp == 2):
		literals = functions.heur2(literals)
	elif(tmp == 3):
		literals = functions.heur3(clauses)

	#define root of a tree and start recursive function
	root = functions.node(literals, clauses)
	c = functions.solve(root)
	
	
	print(c)
	print(len(c))
	print('unsatisfied')