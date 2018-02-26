from random import *
import numpy as np





for world in range(0, 50):
	grid = []
	for row in range(101):
		grid.append([])
		for col in range(101):
			grid[row].append(0)
	gridLength = len(grid)
	for i in range(gridLength):
		for j in range(gridLength):
			if (random() < 0.7):
				grid[i][j] = 0
			else:
				grid[i][j] = 1
	grid[0][0] = 2
	grid[gridLength-1][gridLength-1] = -1

	filename = 'world' + str(world) + '.txt'
	np.savetxt(filename, grid, delimiter=",", newline = "\n", fmt='%i')


print('Done')