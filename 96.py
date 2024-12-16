s = 0

class sudoku_solver:
    def __init__(self,sudoku):
        self.sudoku = sudoku
    def solve(self,i,j):
        global s
        if self.sudoku[i][j] == 0: 
            for x in range(1,10):
                incorrect = False
                for k in range(9):
                    if self.sudoku[i][k] == x or self.sudoku[k][j] == x:
                        incorrect = True 
                        break
                k = 3*(i//3)
                l = 3*(j//3)
                for m in range(k,k+3):
                    for n in range(l,l+3):
                        if self.sudoku[m][n] == x:
                            incorrect = True
                            break
                if not incorrect:
                    self.sudoku[i][j] = x
                    if i+1 != 9:
                        self.solve(i+1,j)
                    elif j+1 != 9:
                        self.solve(0,j+1)
                    else: 
                        s += 100*self.sudoku[0][0] + 10*self.sudoku[0][1] + self.sudoku[0][2]
                    self.sudoku[i][j] = 0
        else:
            if i+1 != 9:
                self.solve(i+1,j)
            elif j+1 != 9:
                self.solve(0,j+1)
            else: 
                s += 100*self.sudoku[0][0] + 10*self.sudoku[0][1] + self.sudoku[0][2]
                
def read_sudoku_grids(file_name):
    grids = []
    current_grid = []
    
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            if line.startswith("Grid"):  # Skip "Grid" headers
                if current_grid:  # If a grid is being built, append it to grids
                    grids.append(current_grid)
                    current_grid = []
            elif line:  # Add the numeric rows to the current grid
                current_grid.append([int(c) for c in line])
        
        # Add the last grid
        if current_grid:
            grids.append(current_grid)
    
    return grids

# Read grids from the file
sudoku_file = "sudoku.txt"
sudoku_grids = read_sudoku_grids(sudoku_file)

# Print the grids
for i, grid in enumerate(sudoku_grids):
    print(f"Grid {i+1}:")
    sudoku_solver(grid).solve(0,0)
    for row in grid:
        print(row)
    print()

print(s)
