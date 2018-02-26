from util import *
from heapq import *
import pygame


class ForwardAStar:


    def __init__(self, gridSize, screen, start_state, goal_state):
        self.gridSize = gridSize
        self.screen = screen
        self.start_state = start_state
        self.goal_state = goal_state
        self.f = {}
        self.h = None
        self.g = set()
        self.cl = set()


    def manhattanDistance(self, a, b):
        return (abs(a[0] - b[0]) + abs(a[1] - b[1]))

    def show_forwards_astar(self, array):
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        close_set = set()

        came_from = {}

        gscore = {self.start_state: 0}

        fscore = {self.start_state: self.manhattanDistance(self.start_state, self.goal_state)}

        oheap = []

        heappush(oheap, (fscore[self.start_state], self.start_state))

        while oheap:
            # print(oheap)
            current = heappop(oheap)[1]
            # print(current)
            if current == self.goal_state:
                total_path = []

                while current in came_from:
                    pygame.draw.rect(self.screen, YELLOW,
                                     [(MARGIN + WIDTH) * current[1] + MARGIN, (MARGIN + HEIGHT) * current[0] + MARGIN,
                                      WIDTH, HEIGHT])
                    pygame.display.update()
                    total_path.append(current)
                    current = came_from[current]

                return total_path

            close_set.add(current)
            self.cl.add(current)

            for i, j in neighbors:
                neighbor = current[0] + i, current[1] + j

                tentative_g_score = gscore[current] + self.manhattanDistance(current, neighbor)


                self.h = self.manhattanDistance(current, self.goal_state)


                if 0 <= neighbor[0] < self.gridSize:
                    if 0 <= neighbor[1] < self.gridSize:
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

                    self.g.add(tentative_g_score)

                    came_from[neighbor] = current
                    gscore[neighbor] = tentative_g_score
                    fscore[neighbor] = tentative_g_score + self.manhattanDistance(neighbor, self.goal_state)
                    pygame.draw.rect(self.screen, BLUE,
                                     [(MARGIN + WIDTH) * neighbor[1] + MARGIN, (MARGIN + HEIGHT) * neighbor[0] + MARGIN,
                                      WIDTH, HEIGHT])
                    pygame.display.update()
                    # print(neighbor)
                    heappush(oheap, (fscore[neighbor], neighbor))
            # print(AdaptiveFscore)
        print('Path not found: Visible Regular A Star')
        return False


    def show_backwards_astar(self, array):
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        close_set = set()

        came_from = {}

        gscore = {self.goal_state: 0}

        fscore = {self.goal_state: self.manhattanDistance(self.goal_state, self.start_state)}

        oheap = []

        heappush(oheap, (fscore[self.goal_state], self.goal_state))

        while oheap:
            # print(oheap)
            current = heappop(oheap)[1]
            # print(current)
            if current == self.start_state:
                total_path = []

                while current in came_from:
                    pygame.draw.rect(self.screen, YELLOW,
                                     [(MARGIN + WIDTH) * current[1] + MARGIN, (MARGIN + HEIGHT) * current[0] + MARGIN,
                                      WIDTH, HEIGHT])
                    pygame.display.update()
                    total_path.append(current)
                    current = came_from[current]

                return total_path

            close_set.add(current)
            self.cl.add(current)

            for i, j in neighbors:
                neighbor = current[0] + i, current[1] + j

                tentative_g_score = gscore[current] + self.manhattanDistance(current, neighbor)


                self.h = self.manhattanDistance(current, self.start_state)


                if 0 <= neighbor[0] < self.gridSize:
                    if 0 <= neighbor[1] < self.gridSize:
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

                    self.g.add(tentative_g_score)

                    came_from[neighbor] = current
                    gscore[neighbor] = tentative_g_score
                    fscore[neighbor] = tentative_g_score + self.manhattanDistance(neighbor, self.start_state)
                    pygame.draw.rect(self.screen, BLUE,
                                     [(MARGIN + WIDTH) * neighbor[1] + MARGIN, (MARGIN + HEIGHT) * neighbor[0] + MARGIN,
                                      WIDTH, HEIGHT])
                    pygame.display.update()
                    # print(neighbor)
                    heappush(oheap, (fscore[neighbor], neighbor))
            # print(AdaptiveFscore)
        print('Path not found: Visible Regular A Star')
        return False

    def getF(self):
        return self.f

    def getH(self):
        return self.h

    def getG(self):
        return self.h

    def getCloseList(self):
        return self.cl

    def adaptive(self):
        for i in self.cl:
            self.h



    def hidden_regular_astar(self, array, start, goal):
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        close_set = set()

        came_from = {}

        gscore = {start: 0}

        fscore = {start: self.manhattanDistance(start, goal)}

        oheap = []

        heappush(oheap, (fscore[start], start))

        while oheap:
            # print(oheap)
            current = heappop(oheap)[1]
            # print(current)
            if current == goal:
                total_path = []

                while current in came_from:
                    total_path.append(current)
                    current = came_from[current]
                return total_path

            close_set.add(current)
            for i, j in neighbors:
                neighbor = current[0] + i, current[1] + j

                tentative_g_score = gscore[current] + self.manhattanDistance(current, neighbor)
                if 0 <= neighbor[0] < self.gridSize:
                    if 0 <= neighbor[1] < self.gridSize:
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
                    fscore[neighbor] = tentative_g_score + self.manhattanDistance(neighbor, goal)
                    heappush(oheap, (fscore[neighbor], neighbor))

            self.f = fscore
        print('Path not found: Hidden Regular A star')
        return False