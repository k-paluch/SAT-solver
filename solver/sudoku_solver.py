import functions
from random import randint
import argparse


parser = argparse.ArgumentParser(description='choose heuristic')

parser.add_argument('-heur', '--heuristic', help='heuristic', type = int, default=3)
parser.add_argument('-type', '--type', help='type of sudoku', type = str, default='16x16')

argc = parser.parse_args()


if __name__ == "__main__":
	true_values = functions.init_result()
	clauses = functions.read_input(f'input/{argc.type}_rules.txt').clauses
	constants = functions.read_sudokus(f'input/{argc.type}.txt')
	literals = functions.get_literals(clauses)
	
	data = (clauses, literals)


	#pick random sudoku and remove constants from literals
	for constant in constants:
		true_values.append(constant)
		data = functions.simplify_clauses_true(data[0], constant, data[1])
	print(f'{len(constants)}, {constants}')

	#pick heuristic
	# argc.heuristic = 3
	if(argc.heuristic == 1):
		literals = functions.heur1(literals,clauses)
	elif(argc.heuristic == 2):
		literals = functions.heur2(literals)
	elif(argc.heuristic == 3):
		literals = functions.heur3(clauses)

	#define root of a tree and start recursive function
	root = functions.node(literals, clauses)
	c = functions.solve(root)
	
	
	print('unsatisfied')