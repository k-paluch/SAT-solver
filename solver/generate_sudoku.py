f = open("sudoku.txt", "w")
values = [20,30,40,50,60,70,80,90]
for literal in range(11,100):
	if(literal not in values):
		f.write(f"{literal} 0\n")
f.close()