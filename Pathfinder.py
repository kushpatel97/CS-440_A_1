import pygame
from random import *
from util import *
from heapq import *
#from A_Star import *


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 10
HEIGHT = 10

# This sets the margin between each cell
MARGIN = 1

ROWS = 50
COLS = 50


# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(ROWS):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(COLS):
        grid[row].append(0)  # Append a cell



# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
# grid[1][5] = 1

#################
# wall = -1
# start = 1
# goal = 2
#

#################


# Build Maze
buildMaze(grid)
#setStart(grid)
#setGoal(grid)

x = randint(0,len(grid))
y = randint(0,len(grid))
grid[x][y] = -1

xend = randint(0,len(grid))
yend = randint(0,len(grid))
grid[xend][yend] = 2

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
# Display + the 1px margins
WINDOW_SIZE = [(ROWS*11)+1,(ROWS*11)+1]
screen = pygame.display.set_mode(WINDOW_SIZE)


# Set title of screen
pygame.display.set_caption("Pathfinder")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

xcoord = []
ycoord = []

def heuristic(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2


def astarFix(array, start, goal):
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    close_set = set()
    came_from = {}
    gscore = {start: 0}
    fscore = {start: heuristic(start, goal)}
    oheap = []

    heappush(oheap, (fscore[start], start))

    while oheap:
        current = heappop(oheap)[1]

        if current == goal:
            data = []
            while current in came_from:
                #print(current[1])
                xcoord.append(current[0])
                ycoord.append(current[1])
                data.append(current)
                current = came_from[current]
            return data

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + heuristic(current, neighbor)
            if 0 <= neighbor[0] < ROWS:
                if 0 <= neighbor[1] < COLS:
                    if array[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue

            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue

            if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                #print(neighbor)
                heappush(oheap, (fscore[neighbor], neighbor))


    return False

print(astarFix(grid, (x, y), (xend, yend)))


# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            # grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)

    # Set the screen background
    screen.fill(BLACK)

    for i in range(1,len(xcoord)):
        x = xcoord[i]
        y = ycoord[i]
        grid[x][y] = 3


    # Draw the grid
    for row in range(ROWS):
        for column in range(COLS):
            color = WHITE

            if grid[row][column] == 1:
                color = BLACK
            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

            if grid[row][column] == 2:
                color = RED
                pygame.draw.rect(screen, color,
                                 [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
            if grid[row][column] == -1:
                color = GREEN
                pygame.draw.rect(screen, color,
                                 [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

            if grid[row][column] == 3:
                color = YELLOW
                pygame.draw.rect(screen, color,
                                 [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)


    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


print(grid)
print(xcoord)
print(ycoord)


# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()