from pysat.formula import CNF
from copy import deepcopy
from timeit import default_timer
from random import sample
import csv
import SAT
from random import randint


class node:
	def __init__(self, literals, clauses):
		self.right = None
		self.left = None
		self.literals = literals
		self.clauses = clauses

true_values = []
start = default_timer()
depth = 0
max_depth = depth
backtracks = 0
n_of_constants =0
n_of_literals = []


def init_result():
	return true_values

#read rules
def read_input(file):
	return CNF(from_file= file)

#solve sudoku
def solve(node_input):
	global backtracks, depth, max_depth, n_of_literals
	n_of_literals.append(len(node_input.literals))
	# print(f'{len(node_input.literals)} in depth of {depth} at backtrack no. {backtracks}')
	if(node_input.clauses=='not satisfied'):
		return

	data = [node_input.clauses, node_input.literals]
	if(len(node_input.literals)==0):
		if(len(node_input.clauses)==0):
			print('satisfied')
			exit()
		else:
			depth-=1
			backtracks+=1
			return

	literal = node_input.literals[0]
	copy_data = deepcopy(data)

	depth+=1
	if(depth > max_depth):
		max_depth = depth

	sat = simplify_clauses_true(copy_data[0],literal,copy_data[1])
	node_input.left = node(sat[1],sat[0])
	true_values.append(literal)
	solve(node_input.left)

	sat = simplify_clauses_false(data[0],literal,data[1], False)
	node_input.right = node(sat[1],sat[0])
	true_values.pop(true_values.index(literal))
	solve(node_input.right)

	depth-=1
	backtracks+=1
	

	return

def heur1(literals, clauses):
	tmp = {}
	for literal in literals:
		i =0
		for clause in clauses:
			if literal in clause or -literal in clause:
				i+=1
		if(i!=0):
			tmp.update({literal: i})

	tmp = sorted(tmp.items(), key=lambda kv: kv[1])
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
		if(SAT.argc.data == '16'):
			cell = (literal - 307) - ((literal - 307)%17)
			cell_values = range(cell,cell+17)
			for x in cell_values:
				print(x)

			exit()
		else:
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
def output(true_values , backtracks, max_depth, runtime):
	global n_of_constants, n_of_literals
	f = open("output.txt", 'w')
	for literal in true_values:
		f.write(f"{literal} 0\n")
	f.close()

	if(SAT.argc.heur1):
		heuristic = 'h1'
	elif(SAT.argc.heur2):
		heuristic = 'h2'
	elif(SAT.argc.heur3):
		heuristic = 'h3'
	else:
		heuristic = 'h4'
	with open(f'statistics{SAT.argc.data}.csv', mode='a', newline='') as statistics:
		statistics = csv.writer(statistics, delimiter=',')
		statistics.writerow([SAT.argc.data, heuristic , n_of_constants, n_of_literals , true_values, backtracks, max_depth, runtime])

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
		print(f'n. of backtracks is {backtracks}')
		print('satisfied')
		true_values.append(literal)
		output(true_values , backtracks, max_depth, default_timer() - start)
		print(len(true_values))
		exit()

	if(SAT.argc.heur4):
		literals = heur3(clauses)
	elif(SAT.argc.heur2):
		literals = heur1(literals, clauses)
	
	return check_single_literal_clauses(clauses, literals)

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
            if(v%289)==0:
            	v+=17

        cordinates.append(test)
    return cordinates


def read_sudokus(file):
	global n_of_constants
	sudoku_lines = [line.rstrip() for line in open(file)]
	sudoku_list = 0
	if len(sudoku_lines[0]) == 81:
 		sudoku_list = sudoku9x9(sudoku_lines)
	elif len(sudoku_lines[0]) == 16:
		sudoku_list = sudoku4x4(sudoku_lines)
	elif len(sudoku_lines[0]) == 256:
		sudoku_list = sudoku16x16(sudoku_lines)

	t = randint(0,len(sudoku_list)-1)

	n_of_constants = len(sudoku_list[t])
	return sudoku_list[t]