from pysat.formula import CNF
import sys


# Tree try
class Tree():
    def __init__(self, root):
        self.root = root
        self.children = []

    def addNode(self, obj):
        self.children.append(obj)


class Node():
    def __init__(self, data):
        self.data = data
        self.children = []

    def addNode(self, obj):
        self.children.append(obj)


# Set a node to its boolean value for every clause
def to_Boolean(clauses, node, truth_value):
    new_clauses = []
    for clause in clauses:
        new_clause = []
        for literal in clause:
            for x in literal.keys():
                if int(x) == int(node):
                    new_clause.append({x: truth_value})
                elif int(x) == int(-1 * node) and truth_value == 'True':
                    # check if value is false or true
                    new_clause.append({x: 'False'})
                elif int(x) == int(-1 * node) and truth_value == 'False':
                    new_clause.append({x: 'True'})
                else:
                    new_clause.append(literal)
        new_clauses.append(new_clause)
    return new_clauses


def init_values(clauses):
    values = []
    for i in clauses:
        tmpvalue = []
        for x in i:
            tmpvalue.append({x: 'Unkown'})
        values.append(tmpvalue)
    return values


# eliminate satisfied clauses
def satisfaction(clauses):
    for clause in clauses:
        falses = 0
        for literal in clause:
            for value in literal.values():
                if value == 'False':
                    falses += 1
        if falses == len(clause):
            return False
    return True


# read rules
def read_input(file):
    return CNF(from_file=file)


# read constants
def read_DIMACS_sudoku(file):
    return CNF(from_file=file)


# check satisfiability - AND and OR statement
def is_satisfied(clauses):
    for clause in clauses:
        if (True in clause):
            continue
        else:
            return False
    return True


# solve sudoku
def solve(node_input):
    for value in node_input.values:
        for variable in node_input.values[value]:
            if (is_satisfied(node_input.clauses) == False or solution_found == False):

                node_input.values[value][variable] = True
                simplify_clauses(node_input.clauses)
                node_input.left = node(node_input.values, clauses)
                solve(input, node_input.left)

                node_input.values[value][variable] = False
                simplify_clauses(node_input.clauses)
                node_input.right = node(node_input.values, clauses)
                solve(input, node_input.right)
            else:
                salution_found = True
                return

    return


# generate output file
def output(values):
    f = open("output.txt", "w")
    for value in values:
        for variable in values[value]:
            if (values[value][variable] == True):
                f.write(f"{variable} 0\n")
    f.close()


def simplify_clauses(clauses, literal):
    tmp = clauses
    print(literal)
    negation = int('-' + str(literal))
    for clause in reversed(range(len(tmp))):
        if (literal in tmp[clause]) or (negation in tmp[clause]):
            tmp.pop(clause)

    return tmp

def rebool(clauses, cellvalue):
    new_clauses = []
    for clause in clauses:
        new_clause = []
        for literal in clause:
            for x in literal.keys():
                if int(x) == int(node):
                    new_clause.append({x: 'Unknown'})
                elif int(x) == int(-1 * node):
                    new_clause.append({x: 'Unknown'})
                else:
                    new_clause.append(literal)
        new_clauses.append(new_clause)
    return new_clauses


# recursive loop
def check_options(sudoTree, coordinateslist, index, clauses):
    if index > 10:
        exit()
        return False
    sudoTree.addNode(Node(coordinateslist[index]))
    for i in range(1, 10):
        cellvalue = int(str(sudoTree.children[index].data) + str(i))
        print(cellvalue)
        clauses = to_Boolean(clauses, cellvalue, True)
        if satisfaction(clauses) == True:
            print('True is satisfied')
            sudoTree.children[index].addNode(cellvalue)
            index = index + 1
            if check_options(sudoTree, coordinateslist, index, clauses) == True:
                print('its solved')
            else:
                index = index - 1

        else:
            print('else')
            clauses = rebool(clauses, cellvalue)
        # elseif option = False satisfies clauses
        clauses = to_Boolean(clauses, cellvalue, False)
        if satisfaction(clauses) == True:
            print('satisfaction for false')
            sudoTree.children[index].addNode(-cellvalue)
            index = index + 1
        #             if check_options(sudoTree, coordinateslist, index, clauses) == True:
        #                 print('its solved')
        #             else:
        #                 index = index - 1
        #                 continue
        # elseif option doesn't satisfy clauses & = 9
        if i == 9:
            print('There is a mistake somewhere else')
            return False

#
if __name__ == "__main__":
    # make a list of all the possible coordinates in the grid
    coordinateslist = []
    for i in range(11, 20):
        for j in range(0, 90, 10):
            coordinateslist.append(i + j)
    clauses = read_input('C:/Users\Dell\Documents\VU_Uni\Masters\Knowledge Representation/sudoku-rules.txt').clauses
    constants = read_input('C:/Users\Dell\Documents\VU_Uni\Masters\Knowledge Representation/sudoku-example.txt').clauses
    clauses = init_values(clauses)
    for constant in constants:
        clauses = to_Boolean(clauses, constant[0], 'True')
    if satisfaction(clauses) == False:
        print("Something's wrong")
    else:
        print('Everything is fine')

    #Make the base of the tree
    sudoTree = Tree('start')
    childcounter = 0
    index = 0

    #Start the loop
    check_options(sudoTree, coordinateslist, index, clauses)