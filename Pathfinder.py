from random import *
from util import *
from heapq import *
import pygame
import time
from ForwardAStar import *
from AdaptiveAStar import *
from pygameHelper import *
# COLORS GO HERE


# DIMENSIONS GO HERE

ROWS = 50

# Create a 2 dimensional array. A two dimensional array is simply a list of lists.
grid = generateGrid(ROWS)

# Build Maze
buildMaze(grid)


# GENERATE START AND END STATE
xstart = randint(0,ROWS-1)
ystart = randint(0,ROWS-1)
grid[0][0] = 2
start_state = (0, 0)

xend = randint(0,len(grid)-1)
yend = randint(0,len(grid)-1)
grid[ROWS-1][ROWS-1] = -1
goal_state = (ROWS-1, ROWS-1)

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode(((ROWS*11)+1,(ROWS*11)+1))
pygame.display.set_caption("Pathfinder")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# CREATE VISUAL GRID, PLACE START, GOAL AND WALLS
for row in range(ROWS):
    for column in range(ROWS):
        color = WHITE
        # print(row)
        if grid[row][column] == 1:
            color = BLACK
        pygame.draw.rect(screen, color,
                         [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

        if grid[row][column] == 2:
            color = RED
            pygame.draw.rect(screen, color,
                             [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH,
                              HEIGHT])
        if grid[row][column] == -1:
            color = GREEN
            pygame.draw.rect(screen, color,
                             [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH,
                              HEIGHT])

pygame.display.flip()

regAstar = ForwardAStar(ROWS, screen)
regAstar.show_forwards_astar(grid, start_state, goal_state)

print(regAstar.getCloseList())
print(regAstar.getG())
# adaAStar = AdaptiveAStar(ROWS, grid, start_state, goal_state)

# regAstar.setInitialGrid(grid)
# adaAStar.setInitialGrid(grid)






# regAstar.hidden_regular_astar(grid, start_state, goal_state)



# adaAStar.show_adaptive_astar(grid, start_state, goal_state)

# adaptive_Astar(grid, start_state, goal_state)


# -------- Main Program Loop -----------


while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    clock.tick(60)



# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()