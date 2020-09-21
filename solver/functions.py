from pysat.formula import CNF
import time
import copy
import random
import timeit
class node:
	def __init__(self, literals, clauses):
		self.right = None
		self.left = None
		self.literals = literals
		self.clauses = clauses

	def __eq__(self,other):
		return self == other


true_values = []
start = timeit.default_timer()
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
	if(node_input.clauses=='not satisfied'):
		return
	c = node_input.clauses
	l = node_input.literals
	data = [c, l]
	if(len(node_input.literals)==0):
		if(len(node_input.clauses)==0):
			print('satisfied')
			exit()
		else:
			return

	literal = node_input.literals[0]

	copy_data = copy.deepcopy(data)

	sat = simplify_clauses_true(copy_data[0],literal,copy_data[1])
	if(sat[0]!='not satisfied'):
		node_input.left = node(sat[1],sat[0])
		true_values.append(literal)
		solve(node_input.left)
	

	sat = simplify_clauses_false(data[0],literal,data[1], False)
	if(sat[0]!='not satisfied'):
		node_input.right = node(sat[1],sat[0])
		if(literal in true_values):
			true_values.pop(true_values.index(literal))
		solve(node_input.right)

	return true_values


def heur1(literal, clauses):
	i =0
	for clause in clauses:
		if literal in clause or -literal in clause:
			i+=1

	return {literal: i}

def heur2(literals):
	return random.sample(literals, len(literals))

def heur3(clauses):
	# [111,112,113]
	heur3 = [[],[],[],[],[],[],[],[],[]]
	for clause in clauses:
		if(clause[0]>0):
			for x in clause:
				if(x not in heur3[len(clause)-1]):
					heur3[len(clause)-1].append(x)

	result = []
	for x in heur3:
		for y in x:
			if(y not in result):
				result.append(y)


	return result


# adjust list of literals
def adjust_literals(literals, literal, value):
	tmp = literals
	if(value == False and literal in tmp):
		tmp.pop(tmp.index(literal))
	if(value == True and literal in tmp):
		cell = int(str(literal)[0:2]+'1')
		cell_values = range(cell,cell+9)
		for x in cell_values:
			if x in tmp:
				tmp.pop(tmp.index(x))
	return tmp


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
def check_single_literal_clauses(clauses, literals):
	tmp_literals = literals
	tmp =(clauses,tmp_literals)
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

	return tmp, tmp_literals

# simplify function to set literal to True
def simplify_clauses_true(clauses, literal, literals):
	tmp_literals = literals
	if(literal in tmp_literals):
		if(tmp_literals == 'satisfied' or tmp_literals == 'not satisfied'):
			print(true_values)
			exit()
		tmp_literals.pop(tmp_literals.index(literal))
	tmp = clauses
	negation = int('-' + str(literal))

	cell = int(str(literal)[0:2]+'1')
	for clause in reversed(range(len(tmp))):
		if(tmp == 'not satisfied'):
			return 'not satisfied', tmp_literals
		if(literal in tmp[clause]):
			tmp.pop(clause)
		if(len(tmp)>clause):
			if (negation in tmp[clause]):
				if len(tmp[clause]) != 1:
					index = int(tmp[clause].index(negation))
					tmp[clause].pop(index)
				else:
					return 'not satisfied', tmp_literals
	if(len(tmp)==0):
		print('satisfied')
		true_values.append(literal)
		print(true_values)
		stop = timeit.default_timer()
		print('Runtime: ', stop - start) 
		exit()

	
		
	cell_values = range(cell,cell+9)
	tmp = (tmp,tmp_literals)
	for value in cell_values:
		if value != literal:
			if(tmp == 'satisfied'):
				print('satisfied')
				true_values.append(literal)
				print(true_values)
				exit()
			tmp = simplify_clauses_false(tmp[0],value, tmp[1] ,True)
	return tmp[0], tmp[1]

# adjust clauses and set literal to False
# clause_value -> 
# 				True -> setting a literal to True and therefore whole clause is True -> can get rid of whole clause -> called only from simplify_clauses_true()
# 				False -> when setting a literal to False and we cannot delete whole clause -> if we do -> return unsatisfied
def simplify_clauses_false(clauses,literal, literals , clause_value):
	tmp_literals = literals
	tmp_literals = adjust_literals(tmp_literals, literal, False)
	tmp = clauses
	negation = int('-' + str(literal))
	if(tmp == 'not satisfied'):
		return 'not satisfied', tmp_literals
	for clause in reversed(range(len(tmp))):
		if(literal in tmp[clause]):
			if (len(tmp[clause]) != 1 or clause_value == True):
				index = int(tmp[clause].index(literal))
				tmp[clause].pop(index)
			elif(len(tmp[clause])==1):
				return 'not satisfied', tmp_literals
		if (negation in tmp[clause]):
			tmp.pop(clause)

		if(len(tmp)==0):
			return 'satisfied'
			exit()
		if(len(tmp[0])==0):
			return 'not satisfied', tmp_literals
	return tmp, tmp_literals


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