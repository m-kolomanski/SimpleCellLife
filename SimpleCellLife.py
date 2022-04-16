import copy
import random
import time
from random import randint
from Tile import Tile
from Owner import Owner

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

        # owners dict #
        self.owners_dict = {}

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

                x_temp.append(Tile(x_pos = a,
                                   y_pos = b))

            game_tiles.append(x_temp)

        self.map = game_tiles

    def printMap(self):
        """Prints map"""
        for i in range(len(self.map)):
            map_row = []
            for j in range(len(self.map[i])):
                map_row.append(self.map[i][j].owner)
            print(map_row)
        print('\n')

    def splitCell(self):
        """Splits existing cells"""
        map_local = copy.deepcopy(self.map)

        ## for each cell, check if not empty ##
        for x in range(len(map_local)):
            for y in range(len(map_local[x])):

                ## if not empty, split cell ##
                if map_local[x][y].owner != 0:

                    ## split vertically ##
                    if randint(0, 1) == 1:
                        change = random.choice((-1, 1))

                        ## bounds detection ##
                        if y + change < len(self.map[x]) and y + change >= 0:
                            self.map[x][y + change].owner = map_local[x][y].owner
                            self.owners_dict[str(map_local[x][y].owner)].owned_tiles.append([x, y + change])
                        else:
                            self.map[x][y - change].owner = map_local[x][y].owner
                            self.owners_dict[str(map_local[x][y].owner)].owned_tiles.append([x, y + change])


                    ## split horizontally ##
                    else:
                        change = random.choice((-1, 1))

                        ## bounds detection ##
                        if x + change < len(self.map) and x + change >= 0:
                            self.map[x + change][y].owner = map_local[x][y].owner
                            self.owners_dict[str(map_local[x][y].owner)].owned_tiles.append([x, y + change])
                        else:
                            self.map[x - change][y].owner = map_local[x][y].owner
                            self.owners_dict[str(map_local[x][y].owner)].owned_tiles.append([x, y + change])

    def mutateCell(self):
        """Mutates existing cells"""
        map_local = copy.deepcopy(self.map)

        for x in range(len(map_local)):
            for y in range(len(map_local[x])):
                if map_local[x][y].owner != 0:
                    if randint(1, 100) in range(1, self.mutation_rate):
                        if str(self.map[x][y].owner + 1) in self.owners_dict.keys():
                            self.map[x][y].owner += 1
                            self.owners_dict[str(self.map[x][y].owner)].owned_tiles.append([x, y])
                        else:
                            self.owners_dict[str(len(self.owners_dict) + 1)] = Owner(name = len(self.owners_dict) + 1)
                            self.owners_dict[str(len(self.owners_dict))].owned_tiles.append([x, y])
                            self.map[x][y].owner = len(self.owners_dict)


    def startSimulation(self):
        """Starts simulation"""
        self.mapGeneration()
        self.owners_dict[str(1)] = Owner(name = 1)
        self.map[1][1].owner = 1

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


