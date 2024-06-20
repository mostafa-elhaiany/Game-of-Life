import sys
import pygame
import config
import numpy as np

# Initialize Pygame
pygame.init()

# Initialize screen
screen = pygame.display.set_mode(config.SCREEN_DIMS)
pygame.display.set_caption("Conway's Game of Life")


grid = np.zeros((config.GRID_DIMS[0], config.GRID_DIMS[1],3))


def draw_grid():
    for r_idx, r in enumerate(grid):
        for c_idx, c in enumerate(r):
            rect = pygame.Rect(r_idx * config.CELL_SIZE[0], c_idx * config.CELL_SIZE[1], config.CELL_SIZE[0], config.CELL_SIZE[1])
            pygame.draw.rect(screen, c, rect)

def draw():
     # Fill screen with black
    screen.fill(config.BLACK)

    # draw grid        
    draw_grid()

    # Update display
    pygame.display.flip()

def add_point(x,y):
    global grid
    center_col = x // config.CELL_SIZE[0]
    center_row = y // config.CELL_SIZE[1]
    grid[center_row][center_col] = np.array(config.WHITE)

def handle_event(event):
    """
    handling clicks and drags
    """
    if event.type == pygame.MOUSEBUTTONDOWN:
        y, x = event.pos
        add_point(x,y)


running = True
simulating = False
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            handle_event(event)
    
    draw()

    clock.tick(60)




pygame.quit()
sys.exit()