import copy
import random
import time
from random import randint

class SimpleCellLife:
    """
    Simulation class

    Attributes:
        map_x, map_y - map dimensions (default 10)
        mutation_rate - mutation rate in %, 0 < int < 100 (default 20)
        sleep_time - sleep time between turns (default 2)

    """

    def __init__(self, map_x = 10, map_y = 10,
                 mutation_rate = 20,
                 sleep_time = 2):

        # map atributes #
        self.map_x = map_x
        self.map_y = map_y
        self.map = []

        # evolution atributes #
        self.mutation_rate = mutation_rate

        # system atributes #
        self.sleep_time = sleep_time

    def mapGeneration(self):
        """Generates map"""
        game_tiles = []
        for a in range(self.map_x):
            x_temp = []
            for b in range(self.map_y):
                x_temp.append(0)
            game_tiles.append(x_temp)

        self.map = game_tiles

    def printMap(self):
        """Prints map"""
        for i in range(len(self.map)):
            print(self.map[i])
        print('\n')

    def splitCell(self):
        """Splits existing cells"""
        map_local = copy.deepcopy(self.map)

        ## for each cell, check if not empty ##
        for x in range(len(map_local)):
            for y in range(len(map_local[x])):

                ## if not empty, split cell ##
                if map_local[x][y] > 0:

                    ## split vertically ##
                    if randint(0, 1) == 1:
                        change = random.choice((-1, 1))

                        ## bounds detection ##
                        if y + change < len(self.map[x]) and y + change >= 0:
                            self.map[x][y + change] = map_local[x][y]
                        else:
                            self.map[x][y - change] = map_local[x][y]


                    ## split horizontally ##
                    else:
                        change = random.choice((-1, 1))

                        ## bounds detection ##
                        if x + change < len(self.map) and x + change >= 0:
                            self.map[x + change][y] = map_local[x][y]
                        else:
                            self.map[x - change][y] = map_local[x][y]

    def mutateCell(self):
        """Mutates existing cells"""
        map_local = copy.deepcopy(self.map)

        for x in range(len(map_local)):
            for y in range(len(map_local)):
                if map_local[x][y] > 0:
                    if randint(1, 100) in range(1, self.mutation_rate):
                        self.map[x][y] += 1

    def startSimulation(self):
        """Starts simulation"""
        self.mapGeneration()
        self.map[1][1] = 1

        turns = 0
        print('Turn:' + str(turns))
        self.printMap()

        while True:
            time.sleep(self.sleep_time)

            self.splitCell()
            self.mutateCell()

            turns += 1
            print('Turn:' + str(turns))
            self.printMap()


