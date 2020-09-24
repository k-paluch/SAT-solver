import subprocess
import csv



types = ["16x16"]
heurs = ["0","2"]

for t in types:
	for h in heurs:
		with open(f'statistics{h}.csv', mode='w', newline='') as statistics:
			statistics = csv.writer(statistics, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			statistics.writerow(['type','heuristic','n. of constants', 'n. of literals' , 'result','backtracks', 'max_depth', 'runtime'])
		for x in range(10):
			c= subprocess.call(["python3", "sudoku_solver.py", "-heur", h, "-type", t])