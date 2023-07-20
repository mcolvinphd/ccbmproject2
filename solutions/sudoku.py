from sudoku_class import *
asudoku=sudoku()
asudoku.generate()
ntrials=50
for n in range(30,71,2):
    completed=0
    for i in range(ntrials):
        asudoku.makepuzzle(n)
        asudoku.solve()
        if asudoku.solved():
            completed+=1
    print("For %d initial clues, completion percentage=%5.3f"%(n,completed/ntrials))


                
