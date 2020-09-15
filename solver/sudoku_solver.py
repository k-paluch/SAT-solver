from pysat.formula import CNF

class node:
	def __init__(self, variables, clauses):
		self.right = None
		self.left = None
		self.variables = variables
		self.clauses = clauses

	def __eq__(self,other):
		return self == other

#read rules
def read_input(file):
	return CNF(from_file= file)

#read constants
def read_DIMACS_sudoku(file):
	return CNF(from_file= file)

# check satisfiability - AND and OR statement
def is_satisfied(clauses):
	for clause in clauses:
		if(True in clause):
			continue
		else:
			return False
	return True

#solve sudoku
def solve(node_input):
	for value in node_input.values:
		for variable in node_input.values[value]:
			if(is_satisfied(node_input.clauses)==False or solution_found == False):

				node_input.values[value][variable] = True
				simplify_clauses(node_input.clauses)
				node_input.left = node(node_input.values,clauses)
				solve(input, node_input.left)

				node_input.values[value][variable] = False
				simplify_clauses(node_input.clauses)
				node_input.right = node(node_input.values,clauses)
				solve(input, node_input.right)
			else:
				salution_found = True
				return

	return

#generate output file
def output(values):
	f = open("output.txt", "w")
	for value in values:
		for variable in values[value]:
			if(values[value][variable]==True):
				f.write(f"{variable} 0\n")
	f.close()

def simplify_clauses(clauses, literal):
	tmp = clauses
	print(literal)
	negation = int('-' + str(literal))
	for clause in reversed(range(len(tmp))):
		if(literal in tmp[clause]) or (negation in tmp[clause]):
			tmp.pop(clause)

	return tmp

def sudoku9x9():
    list_place = list(range(11,100))
    unwanted_num = {20, 30, 40, 50, 60, 70, 80, 90} 
    list_place = [cor for cor in list_place if cor not in unwanted_num]
    return list_place

def sudoku4x4():
    list_place = list(range(11,15)) + list(range(21,25)) + list(range(31,35)) + list(range(41,45))
    return list_place

def sudoku16x16():
    return

def read_sudokus():
    sudoku_lines = [line.rstrip() for line in open('input/16x16.txt')]
    list_place = 0
    if len(sudoku_lines[0]) == 81:
        list_place = sudoku9x9()
    elif len(sudoku_lines[0]) == 16:
        list_place = sudoku4x4()
    elif len(sudoku_lines[0]) == 256:
        list_place = sudoku16x16()
    
   
    test = []
    for lines in sudoku_lines:
        givens=[]
        for i in range(len(lines)):
            if lines[i] != '.':
                givens.append(str(list_place[i])+str(lines[i]) +' 0')
        
        test.append(givens)
    return test

if __name__ == "__main__":
    solution_found = False
    clauses = read_input('input/sudoku-rules.txt').clauses
    constants = read_input('input/sudoku-example.txt').clauses
    sudokus = read_sudokus()
	#print(constants)
	#for constant in constants:
	#	clauses = simplify_clauses(clauses, constant[0])