from pysat.formula import CNF
import time

true_values = []

class node:
	def __init__(self, literals, clauses):
		self.right = None
		self.left = None
		self.literals = values
		self.clauses = clauses
		self.result = []

	def __eq__(self,other):
		return self == other

#read rules
def read_input(file):
	return CNF(from_file= file)

#read constants
def read_DIMACS_sudoku(file):
	return CNF(from_file= file)

#solve sudoku
def solve(node_input):
	for literal in node_input.literals:
			l = adjust_literals(literals)
			clauses = simplify_clauses_true(node_input.clauses,literal)
			node_input.left = node(l,clauses)
			node_input.left.result.append(literal)
			solve(node_input.left)

			clauses = simplify_clauses_false(node_input.clauses,literal, False)
			node_input.right = node(l,clauses)
			solve(input, node_input.right)

	return 'not satisfied'

def adjust_literals(literals, literal,value):
	if(value == False):
		literals.pop(literals.index(literal))
	if(value):
		cell = int(str(literal)[0:2]+'1')
		cell_values = range(cell,cell+9)
		for x in literals:
			if x in cell_values:
				literals.pop(literals.index(x))



def get_literals(clauses):
	literals = []

	for clause in clauses:
		for literal in clause:
			if (not str(literal).startswith('-')) and (literal not in literals):
				literals.append(literal)
	return literals

#generate output file
def output(result):
	f = open("output.txt", "w")
	for literal in result:
		f.write(f"{literal} 0\n")
	f.close()

# if last literal in big clause -> dont pop the clause -> add to solution instead

def check_single_literal_clauses(clauses):
	tmp = clauses

	single_literal_closes = []

	for clause in reversed(range(len(tmp))):
		if len(tmp[clause]) == 1 and tmp[clause][0]<0:
			single_literal_closes.append(int(str(tmp[clause][0])[1:]))

	for literal in single_literal_closes:
		simplify_clauses_false(clauses,literal,False)

	if(len(tmp[0])==0):
		return 'not satisfied'
	return tmp


def simplify_clauses_true(clauses, literal):
	tmp = clauses
	negation = int('-' + str(literal))
	cell = int(str(literal)[0:2]+'1')
	for clause in reversed(range(len(tmp))):
		if(literal in tmp[clause]):
			tmp.pop(clause)
		if(len(tmp)>clause):
			if (negation in tmp[clause]):
				if len(tmp[clause]) != 1:
					tmp[clause].pop(tmp[clause].index(negation))
				else:
					return 'not satisfied'

		if(len(tmp)==0):
			return 'satisfied'


			# make it run :D

	cell_values = range(cell,cell+9)
	for value in cell_values:
		simplify_clauses_false(clauses,value,True)


	return check_single_literal_clauses(tmp)

def simplify_clauses_false(clauses,literal, clause_value):
	tmp = clauses
	negation = int('-' + str(literal))
	for clause in reversed(range(len(tmp))):
		if(literal in tmp[clause]):
			if (len(tmp[clause]) != 1 or clause_value == True):
				tmp[clause].pop(tmp[clause].index(literal))
			if(len(tmp[clause])==1):
				return 'not satisfied'
		if (negation in tmp[clause]):
			tmp.pop(clause)
	
	return tmp

if __name__ == "__main__":
	solution_found = False
	clauses = read_input('input/sudoku-rules.txt').clauses
	constants = read_input('sudoku.txt').clauses
	literals = get_literals(clauses)


	for constant in constants:
		true_values.append(constant[0])
		clauses = simplify_clauses_true(clauses, constant[0])
		if(clauses=='not satisfied'):
			break
	
	print(clauses)
	print(true_values)