from pysat.formula import CNF
from copy import deepcopy
from timeit import default_timer
from random import sample

class node:
	def __init__(self, literals, clauses):
		self.right = None
		self.left = None
		self.literals = literals
		self.clauses = clauses

true_values = []
start = default_timer()

def init_result():
	return true_values

#read rules
def read_input(file):
	return CNF(from_file= file)

#solve sudoku
def solve(node_input):
	if(node_input.clauses=='not satisfied'):
		return

	data = [node_input.clauses, node_input.literals]

	if(len(node_input.literals)==0):
		if(len(node_input.clauses)==0):
			print('satisfied')
			exit()
		else:
			return

	literal = node_input.literals[0]
	copy_data = deepcopy(data)

	sat = simplify_clauses_true(copy_data[0],literal,copy_data[1])
	node_input.left = node(sat[1],sat[0])
	true_values.append(literal)
	solve(node_input.left)
	

	sat = simplify_clauses_false(data[0],literal,data[1], False)
	node_input.right = node(sat[1],sat[0])
	true_values.pop(true_values.index(literal))
	solve(node_input.right)

	return true_values


def heur1(literals, clauses):
	tmp = {}
	for literal in literals:
		i =0
		for clause in clauses:
			if literal in clause or -literal in clause:
				i+=1
		if(i!=0):
			tmp.update({literal: i})

	tmp = sorted(tmp.items(), key=lambda kv: kv[1], reverse = True)
	result =[]

	for t in tmp:
		result.append(t[0])

	return result

def heur2(literals):
	return sample(literals, len(literals))

def heur3(clauses):
	heur3 = [[] for x in range(16)]

	for clause in clauses:
		if(clause[0]>0):
			for literal in clause:
				if(literal not in heur3[len(clause)-1]):
					heur3[len(clause)-1].append(literal)

	result = []
	for clause in heur3:
		for literal in clause:
			if(literal not in result):
				result.append(literal)

	return result


# adjust list of literals
def adjust_literals(literals, literal, value):
	if(value == False and literal in literals):
		literals.pop(literals.index(literal))

	if(value == True and literal in literals):
		cell  = literal - (literal%10)
		cell_values = range(cell,cell+9)
		for x in cell_values:
			if x in literals:
				literals.pop(literals.index(x))

	return literals


# get literals from ruleset
def get_literals(clauses):
	literals = []

	for clause in clauses:
		for literal in clause:
			if (literal > 0) and (literal not in literals):
				literals.append(literal)

	return literals

#generate output file
def output(result):
	f = open("output.txt", "w")
	for literal in result:
		f.write(f"{literal} 0\n")
	f.close()

# look up clauses with single literal in it and adjust clauses accordingly
def check_single_literal_clauses(clauses, literals):
	tmp =(clauses,literals)
	single_literals = []

	for clause in reversed(range(len(tmp[0]))):
		if len(tmp[0][clause]) == 1 and tmp[0][clause][0]<0:
			single_literals.append(int(str(tmp[0][clause][0])[1:]))

	
	for literal in single_literals:
		if(tmp=='not satisfied'):
			return tmp, tmp_literals
		if(literal in tmp[1]):
			tmp[1].pop(tmp[1].index(literal))
			tmp = simplify_clauses_false(tmp[0],literal,tmp[1],False)

	return tmp

# simplify function to set literal to True
def simplify_clauses_true(clauses, literal, literals):
	if(literal in literals):
		literals.pop(literals.index(literal))

	for clause in reversed(range(len(clauses))):
		if(clauses == 'not satisfied'):
			return 'not satisfied', literals

		if(literal in clauses[clause]):
			clauses.pop(clause)

		if(len(clauses)>clause):
			if (-literal  in clauses[clause]):
				if len(clauses[clause]) != 1:
					index = int(clauses[clause].index(-literal ))
					clauses[clause].pop(index)
				else:
					return 'not satisfied', literals

	if(len(clauses)==0):
		print('Runtime: ', default_timer() - start)
		print('satisfied')
		true_values.append(literal)
		output(sorted(true_values))
		exit()

	return check_single_literal_clauses(clauses, heur3(clauses))

# adjust clauses and set literal to False
# clause_value -> 
# 				True -> setting a literal to True and therefore whole clause is True -> can get rid of whole clause -> called only from simplify_clauses_true()
# 				False -> when setting a literal to False and we cannot delete whole clause -> if we do -> return unsatisfied
def simplify_clauses_false(clauses,literal, literals , clause_value):
	literals = adjust_literals(literals, literal, False)
	if(clauses == 'not satisfied'):
		return 'not satisfied', literals
	for clause in reversed(range(len(clauses))):
		if(literal in clauses[clause]):
			if (len(clauses[clause]) != 1 or clause_value == True):
				index = int(clauses[clause].index(literal))
				clauses[clause].pop(index)
			elif(len(clauses[clause])==1):
				return 'not satisfied', literals
		if (-literal in clauses[clause]):
			clauses.pop(clause)

		if(len(clauses[0])==0):
			return 'not satisfied', literals

	return check_single_literal_clauses(clauses, literals)


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
        v = 306
        for i in range(len(cor)):
            if cor[i] != '.':
            	test.append(v+int(cor[i]))
            v+=17
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