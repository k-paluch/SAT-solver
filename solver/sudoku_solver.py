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

def sudoku9x9(lines):
    list_place = list(range(11,100))
    unwanted_num = {20, 30, 40, 50, 60, 70, 80, 90} 
    list_place = [cor for cor in list_place if cor not in unwanted_num]
    
    test = []
    for line in lines:
        givens=[]
        for i in range(len(line)):
            if line[i] != '.':
                givens.append(str(list_place[i])+str(line[i]) +' 0')
        
        test.append(givens)
    return test

def sudoku4x4(lines):
    list_place = list(range(11,15)) + list(range(21,25)) + list(range(31,35)) + list(range(41,45))
    test = []
    for line in lines:
        givens=[]
        for i in range(len(line)):
            if line[i] != '.':
                givens.append(str(list_place[i])+str(line[i]) +' 0')
        
        test.append(givens)
    return test

def sudoku16x16(lines):
    given=[]
    for line in lines:
        test=[]

        for i in range(len(line)):
            test.append(str(line[i]))
        test = [item.replace("A", "10") for item in test]
        test = [item.replace("B", "11") for item in test]
        test = [item.replace("C", "12") for item in test]
        test = [item.replace("D", "13") for item in test]
        test = [item.replace("E", "14") for item in test]
        test = [item.replace("F", "15") for item in test]
        test = [item.replace("G", "16") for item in test]
        given.append(test)
    
    cordinates=[]
    for cor in given:
        test=[]
        row = 1
        col = 1
        for i in range(len(cor)):
            if col <= 16 and cor[i] != '.':
                   test.append(int(cor[i]) + 17*col + 17*17*row)
            col += 1
            if col > 16:
                col =1 
                row +=1
            
        cordinates.append(test)
    return cordinates


def read_sudokus():
    sudoku_lines = [line.rstrip() for line in open('input/16x16.txt')]
    sudoku_list = 0
    if len(sudoku_lines[0]) == 81:
        sudoku_list = sudoku9x9(sudoku_lines)
    elif len(sudoku_lines[0]) == 16:
        sudoku_list = sudoku4x4(sudoku_lines)
    elif len(sudoku_lines[0]) == 256:
        sudoku_list = sudoku16x16(sudoku_lines)
    
    
    return sudoku_list

if __name__ == "__main__":
    solution_found = False
    clauses = read_input('input/sudoku-rules.txt').clauses
    constants = read_input('input/sudoku-example.txt').clauses
    sudokus = read_sudokus()
	#print(constants)
	#for constant in constants:
	#	clauses = simplify_clauses(clauses, constant[0])