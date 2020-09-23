import subprocess
import csv

with open('statistics.csv', mode='w', newline='') as statistics:
		statistics = csv.writer(statistics, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		statistics.writerow(['type','heuristic','n. of constants', 'n. of literals' , 'result','backtracks', 'max_depth', 'runtime'])

types = ["4x4", "9x9", "16x16"]
heurs = ["0","1","2","3"]

for t in types:
	# for h in heurs:
	for x in range(10):
		c= subprocess.call(["python", "sudoku_solver.py", "-heur", '3', "-type", t])