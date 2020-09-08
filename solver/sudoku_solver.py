read_input [and(
		[or(0,1,2,3)],
		[],
		[])
	]

clauses[[]]

# def sudoku_init(n):
# 	if(n==999):
# 		return [[0 for n in range(10)] for i in range(10)]

values = []

class node:
	def __init__(self, left, right):
		self.right = None
		self.left = None

def output(values):
	file = open('output/output.txt', 'w')
	#111, 112
	for output in values:
		for n in values[output]:
			if(n==True):
				print(f'{n} 0\n')

def read_input(file):
	file = open('sudoku_rules.txt', 'r')
	lines = file.readlines()

	q=0
	for line in lines:
		if(line == lines[0]):
			tmp = line.split(sep=' ')
			dimensions = tmp[2]
			n_of_lines = tmp[3]

		tmp = line.split(sep=' ')
		clauses.append([])
		for t in tmp:
			if(i != 0):
				clauses[len(clauses)].append(t)

		if(q%((n*(n-1))/2)==0):
			for i in tmp:
				if(i != 0):
					values.append(i:False)

		elif(line == lines[0]):
			pass
		else:
  			q+=1

	for index, clause in enumerate(clauses):
		disjunction = or(clause)
	conjuction = and(clauses)


def simplify_input(input):
	if(value in CONSTANT):
		pass
	else:
		# code

	return result

def solve(input: [], node_input):
	
	node = tree(None, None)
	node_input.left = node
	solve(input, node.left)
	node_input.left = node
	solve(input, node.right)

return


if '__name__' == '__main__':
	root = tree(None, None)

