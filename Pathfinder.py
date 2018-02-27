import pygame
import time, timeit
from AStar import *



num = input('Enter a world from 0 to 49: \n')
if int(num) > 49 or int(num) < 0:
    raise ValueError('Out of Range')
string = 'worlds/world' + str(num) + '.txt'

text_file = open(string, 'r')
lines = text_file.readlines()
grid = []
for line in lines:
    line = line.strip().split(',')
    line = list(map(int, line))
    grid.append(line)

start_state = (0,0)
goal_state = (len(grid)-1, len(grid)-1)
ROWS = len(grid)


# Initialize pygame
pygame.init()
screen = pygame.display.set_mode(((ROWS*11)+1,(ROWS*11)+1))
pygame.display.set_caption("Pathfinder")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
time = 0
distancenum = 0
algtime = 0
# CREATE VISUAL GRID, PLACE START, GOAL AND WALLS
for row in range(ROWS):
    for column in range(ROWS):
        color = WHITE
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
                print('Running Repeated Forward A* (Low G): {}sec, Distance: {}, Time Taken: {}s'.format(time,regAstar.distance,regAstar.time))
            elif event.key == pygame.K_2:  # Backwards A* Low G value:
                start = timeit.default_timer()
                regAstar = AStar(ROWS, screen,start_state,goal_state)
                regAstar.show_backwards_astar(grid)
                stop = timeit.default_timer()
                pygame.display.flip()
                time = stop - start
                print('Running Repeated Backwards A* (Low G): {}sec, Distance: {}, Time Taken: {}s'.format(time,regAstar.distance,regAstar.time))
            elif event.key == pygame.K_3:  # Adaptive A* Low G value:
                start = timeit.default_timer()
                regAstar = AStar(ROWS, screen,start_state,goal_state)
                regAstar.show_adaptive_astar(grid)
                stop = timeit.default_timer()
                pygame.display.flip()
                time = stop - start
                print('Running Adaptive A* (Low G): {}sec, Distance: {}, Time Taken: {}s'.format(time,regAstar.distance,regAstar.time))


    pygame.display.flip()


pygame.quit()