import numpy as np

N = 10
ON = 1
OFF = 0

grid = np.full((N,N), OFF)

def update(grid):
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] + 
                     grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                     grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                     grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N]))
            if grid[i, j] == ON:
                if (total<2) or (total>3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i,j] = ON

    return newGrid

