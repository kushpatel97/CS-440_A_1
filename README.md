# CS-440_A_1
This is a CS 440 Rutgers Assign 1
Instructions on how to use the A* star Python environment.

Rows and columns are specified at the beginning of Pathfinder.py, grid is set to be displayed as a square.
Can randomly generate mazes.
(Defined as ROW = x, automatically set to 101x101 grid)

Program can also read in 50 gridworlds .txt files from words folder


Algorithms are defined in AStar.py class except for Adaptive A*

utils.py file contains etc variables and grid building functions

Pathfinder.py is driver program

AdaptiveAStar.py contains Adaptive A* algorithm

worlds folder contains 50 .txt files of pregenerated gridworlds than can be loaded and ran


Start and goal states are hard coded to be in the top left and bottom right respectively.

Walls are black squares that are randomly selected when making the grid (using the 70/30 randomizer)

Code for High G Value tiebreaking is commented out in each A* method

Replace the two following if statements with the commented out if statements to change tiebreaking preference

Key:
-GOAL is GREEN
-START is RED
-OPTIMAL PATH is YELLOW
-NEIGHBOR nodes are BLUE


On program Start:

Pathfinder.py will prompt the user to enter a number between 0 and 49

By doing so, you are selecting a world to run the A* algorithim on

Start and goal squares are chosen and colored, empty and wall squares are chosen randomly and colored



When running the program:

Press 1: Runs Repeated Forward A*, shows path dynamically (g values set to low preference as default)

Press 2: Runs Repeated Backward A*, shows path dynamically (g values set to high preference as default)

Press 3: Runs Adaptive A*, shows pathd dynamically (g values set to low preference as default)

Press c: Clears the board, resets grid to start state


Other:
Time for each algorithm is displayed in console. (Note: time includes color shading for grid building, it does not represent pure algorithm runtime)

Distance is also displayed in console, represents # of grid squares in optimal path (DOES NOT INCLUDE EVERY VISITED NODE)

To generate more worlds run buildmap.py and it will overwrite older maps

There is a research paper submitted in Latex formate with latex source code.

Also, just incase if any information is missing on the latex formate, there is also a Word formate submitted.
