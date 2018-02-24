from random import *

def buildMaze(board):
    length = len(board)
    for i in range(length):
        for j in range(length):
            if (random() < 0.7):
                board[i][j] = 0
            else:
                board[i][j] = -1

def setStart(board):
    x = randint(0,len(board))
    y = randint(0,len(board))
    board[x][y] = 1


def setGoal(board):
    x = randint(0,len(board))
    y = randint(0,len(board))
    board[x][y] = 2