from random import *
from collections import deque


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (135,206,235)


WIDTH = 10
HEIGHT = 10

# This sets the margin between each cell
MARGIN = 1


def generateGrid(ROWS):
    grid = []
    for row in range(ROWS):
        # Add an empty array that will hold each cell in this row
        grid.append([])
        for column in range(ROWS):
            grid[row].append(0)
    return grid

def buildMaze(board):
    length = len(board)
    for i in range(length):
        for j in range(length):
            if (random() < 0.7):
                board[i][j] = 0
            else:
                board[i][j] = 1

def setStart(board):
    x = randint(0,len(board))
    y = randint(0,len(board))
    board[x][y] = 2

def setGoal(board):
    x = randint(0,len(board))
    y = randint(0,len(board))
    board[x][y] = 3