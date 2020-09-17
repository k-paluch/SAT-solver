from pysat.formula import CNF

true_values = []

def init_true_values():
	return true_values

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

# adjust list of literals
def adjust_literals(literals, literal,value):
	if(value == False):
		literals.pop(literals.index(literal))
	if(value):
		cell = int(str(literal)[0:2]+'1')
		cell_values = range(cell,cell+9)
		for x in literals:
			if x in cell_values:
				literals.pop(literals.index(x))


# get literals from ruleset
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

# look up clauses with single literal in it and adjust clauses accordingly
def check_single_literal_clauses(clauses):
	tmp = clauses

	single_literals = []

	for clause in reversed(range(len(tmp))):
		if len(tmp[clause]) == 1 and tmp[clause][0]<0:
			single_literals.append(int(str(tmp[clause][0])[1:]))

	for literal in single_literals:
		tmp = simplify_clauses_false(tmp,literal,False)

	
	return tmp

# simplify function to set literal to True
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
		return 'satisfied', true_values

	cell_values = range(cell,cell+9)
	for value in cell_values:
		tmp = simplify_clauses_false(tmp,value,True)

	return check_single_literal_clauses(tmp)

# adjust clauses and set literal to False
# clause_value -> 
# 				True -> setting a literal to True and therefore whole clause is True -> can get rid of whole clause -> called only from simplify_clauses_true()
# 				False -> when setting a literal to False and we cannot delete whole clause -> if we do -> return unsatisfied
def simplify_clauses_false(clauses,literal, clause_value):
	tmp = clauses
	negation = int('-' + str(literal))
	for clause in reversed(range(len(tmp))):
		if(literal in tmp[clause]):
			if (len(tmp[clause]) != 1 or clause_value == True):
				tmp[clause].pop(tmp[clause].index(literal))
			elif(len(tmp[clause])==1):
				return 'not satisfied'
		if (negation in tmp[clause]):
			tmp.pop(clause)
	
		if(len(tmp[0])==0):
			print('not satisfied')
			exit()
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
                givens.append(int(str(list_place[i])+str(line[i])))
        
        test.append(givens)
    return test

def sudoku4x4(lines):
    list_place = list(range(11,15)) + list(range(21,25)) + list(range(31,35)) + list(range(41,45))
    test = []
    for line in lines:
        givens=[]
        for i in range(len(line)):
            if line[i] != '.':
                givens.append(int(str(list_place[i])+str(line[i])))
        
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
                   test.append(int(str(col) + str(row) + str(cor[i])))
            col += 1
            if col > 16:
                col =1 
                row +=1
            
        cordinates.append(test)
    return cordinates


def read_sudokus(file):
    sudoku_lines = [line.rstrip() for line in open(file)]
    sudoku_list = 0
    if len(sudoku_lines[0]) == 81:
        sudoku_list = sudoku9x9(sudoku_lines)
    elif len(sudoku_lines[0]) == 16:
        sudoku_list = sudoku4x4(sudoku_lines)
    elif len(sudoku_lines[0]) == 256:
        sudoku_list = sudoku16x16(sudoku_lines)
    
    
    return sudoku_list