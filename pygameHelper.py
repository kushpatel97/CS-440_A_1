import pygame
from util import *

class pygameHelper():

    def __init__(self, gridSize):
        self.gridSize = gridSize


    def setInitialGrid(self, grid):
        screen = pygame.display.set_mode([(self.gridSize*11)+1,(self.gridSize*11)+1])
        for row in range(self.gridSize):
            for column in range(self.gridSize):
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