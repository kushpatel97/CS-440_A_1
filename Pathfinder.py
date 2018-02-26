from random import *
from util import *
from heapq import *
import pygame
import timeit
from AStar import *

# COLORS GO HERE


# DIMENSIONS GO HERE


# Create a 2 dimensional array. A two dimensional array is simply a list of lists.
# Build Maze
# # GENERATE START AND END STATE
#
#
# UNCOMMENT HERE FOR IT TO WORK
ROWS = 50
grid = generateGrid(ROWS)
buildMaze(grid)
grid[0][0] = 2
start_state = (0, 0)
grid[ROWS-1][ROWS-1] = -1
goal_state = (ROWS-1, ROWS-1)




#
# text_file = open('numbers2.txt', 'r')
# lines = text_file.readlines()
# grid = []
# for line in lines:
#     line = line.strip().split(',')
#     line = list(map(int, line))
#     grid.append(line)
#
# print(grid)
# start_state = grid[0][0]
# goal_state = grid[100][100]
# ROWS = len(grid)
#
# print('' + grid[0][0])

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

# regAstar = AStar(ROWS, screen, start_state, goal_state)
# regAstar.show_forwards_astar(grid)
# regAstar.show_backwards_astar(grid)
# regAstar.adaptive(grid)
# print(regAstar.getCloseList())
# print(regAstar.getG())
# print('Distance: ' + str(len(regAstar.show_forwards_astar(grid))))
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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:  # Clear obstacles on screen:
                for row in range(ROWS):
                    for column in range(ROWS):
                        color = WHITE
                        if grid[row][column] != 1:
                            if grid[row][column] != 2:
                                if grid[row][column] != -1:
                                    color = WHITE
                                    grid[row][column] = 0
                                    pygame.draw.rect(screen, color,[(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN,WIDTH, HEIGHT])

                pygame.display.flip()
                time = 0
                distancenum = 0
                print('Path Cleared')
            elif event.key == pygame.K_1:  # Forward A* Low G Value:
                start = timeit.default_timer()
                regAstar = AStar(ROWS, screen,start_state,goal_state)
                regAstar.show_forwards_astar(grid)
                stop = timeit.default_timer()
                pygame.display.flip()
                time = stop - start
                distancenum = regAstar.distance
                algtime = regAstar.time
                print('Running Repeated Forward A* (Low G):', time, 'seconds',', distance: ', distancenum , ', algorithm time: ', algtime)
            elif event.key == pygame.K_2:  # Backwards A* Low G value:
                start = timeit.default_timer()
                regAstar = AStar(ROWS, screen,start_state,goal_state)
                regAstar.show_backwards_astar(grid)
                stop = timeit.default_timer()
                pygame.display.flip()
                time = stop - start
                distancenum = regAstar.distance
                print('Running Repeated Backwards A* (Low G): ', time, 'seconds','distance: ', distancenum, 'algorithm time: ', algtime )




# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()