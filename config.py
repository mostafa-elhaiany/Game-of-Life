CELL_SIZE = (5, 5)  # Width and height of each cell
GRID_DIMS = (200, 100) # number of cells (rows, columns)


#visualization
############# if these change remember to change the check condition in GAMEOfLife.py ###############
AS_CIRCLES = True
CHECK_AXIS = 1 # this is the axis in the numbers below that is always 255 when the cell is moving to next gen
# Colors
DIED = (255,0,0) # axis 1 is 0 when dead
SURVIVED = (255,255,0) # axis 1 is 255 because cell is alive
BORN = (0,255,0) # axis 1 is 255 because cell is alive


############## CONSTANTS ######################
# Calculate screen dimensions
SCREEN_WIDTH = CELL_SIZE[0] * GRID_DIMS[0]
SCREEN_HEIGHT = CELL_SIZE[1] * GRID_DIMS[1]
SCREEN_DIMS = (SCREEN_WIDTH, SCREEN_HEIGHT)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)