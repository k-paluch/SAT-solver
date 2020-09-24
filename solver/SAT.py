import functions
from random import randint
import argparse


parser = argparse.ArgumentParser(description='choose heuristic')

parser.add_argument('-S1', '--heur1', help='heur1', action = "store_true")
parser.add_argument('-S2', '--heur2', help='heur1', action = "store_true")
parser.add_argument('-S3', '--heur3', help='heur1', action = "store_true")
parser.add_argument('data', type=str, help='heuristic')

# parser.add_argument('data', type=str, help="path to data")

argc = parser.parse_args()


if __name__ == "__main__":
	true_values = functions.init_result()
	clauses = functions.read_input(f'{argc.data}/rules.txt').clauses
	constants = functions.read_sudokus(f'{argc.data}/sudoku.txt')
	literals = functions.get_literals(clauses)
	
	data = (clauses, literals)


	#pick random sudoku and remove constants from literals
	for constant in constants:
		true_values.append(constant)
		data = functions.simplify_clauses_true(data[0], constant, data[1])
	print(f'{len(constants)}, {constants}')

	#pick heuristic
	# argc.heuristic = 3
	if(argc.heur2):
		literals = functions.heur1(literals,clauses)
	elif(argc.heur3):
		literals = functions.heur2(clauses)

	#define root of a tree and start recursive function
	root = functions.node(literals, clauses)
	c = functions.solve(root)
	
	
	print('unsatisfied')