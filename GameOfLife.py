import numpy as np
import config

def next_gen(grid: np.ndarray):
    """
    Creates the new generation of the Game Of Life from the previous grid
    Args:
        grid (np.ndarray): previous generation GOL
    """
    new_grid = np.zeros_like(grid)
    grid = grid[:,:,config.CHECK_AXIS]
    grid[grid==255] = 1
    grid = np.pad(grid, 1,constant_values=(0))
    H, W, _ = new_grid.shape
    for i in range(H):
        for j in range(W):
            padded_i = i+1
            padded_j = j+1
            neighborhood = grid[padded_i-1:padded_i+2,padded_j-1:padded_j+2]
            exists = grid[padded_i,padded_j] == 1
            num_elements = np.sum(neighborhood) - grid[padded_i,padded_j]
            if(not exists and num_elements==3): # A cell is born if it has exactly three neighbours, 
                new_grid[i,j] = config.BORN           
            elif(exists and 2<=num_elements<=3):# survives if it has two or three living neighbours, 
                new_grid[i,j] = config.SURVIVED
            elif(exists and not 2<=num_elements<=3):# survives if it has two or three living neighbours, 
                new_grid[i,j] = config.DIED
            # and dies otherwise
    return new_grid