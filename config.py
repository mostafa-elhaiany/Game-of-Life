CELL_SIZE = (2, 2)  # Width and height of each cell
GRID_DIMS = (200, 200) # number of cells (rows, columns)


# Calculate screen dimensions
SCREEN_WIDTH = CELL_SIZE[0] * GRID_DIMS[1]
SCREEN_HEIGHT = CELL_SIZE[1] * GRID_DIMS[0]
SCREEN_DIMS = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)