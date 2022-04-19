import copy
import random
import time
from random import randint
from Tile import Tile
from Owner import Owner

from os import system, name
# clear terminal funtion #
def clearTerminal():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

class SimpleCellLife:
    """
    Simulation class

    Attributes:
        map_x, map_y - map dimensions (default 10)
        mutation_rate - mutation rate in %, 0 < int < 100 (default 20)
        sleep_time - sleep time between turns (default 2)
        print_stats - whether to print stats about the simulation (default False)

    """

    def __init__(self, map_x = 10, map_y = 10,
                 mutation_rate = 20,
                 sleep_time = 2,
                 print_stats = False):

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
        self.print_stats = print_stats

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

    def splitCell(self):
        """Splits existing cells"""
        for owner in self.owners_dict.keys():
            owners_local = copy.deepcopy(self.owners_dict)
            if owner != '0':
                for tile in owners_local[owner].owned_tiles:
                    x = tile[0]
                    y = tile[1]
                    target = random.choice([[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]])

                    if -1 not in target and 10 not in target and target not in self.owners_dict[owner].owned_tiles: ## todo: add flexible bounds detection
                        ## remove current owner ##
                        self.owners_dict[str(self.map[target[0]][target[1]].owner)].owned_tiles.remove(target)
                        ## take ownership of the tile ##
                        self.map[target[0]][target[1]].owner = int(owner)
                        ## add owned tile ##
                        self.owners_dict[owner].owned_tiles.append(target)


    def mutateCell(self):
        """Mutates existing cells"""
        map_local = copy.deepcopy(self.map)

        for x in range(len(map_local)):
            for y in range(len(map_local[x])):
                if map_local[x][y].owner != 0:
                    if randint(1, 100) in range(1, self.mutation_rate):
                        self.owners_dict[str(self.map[x][y].owner)].owned_tiles.remove([x, y])

                        if str(self.map[x][y].owner + 1) in self.owners_dict.keys():
                            self.map[x][y].owner += 1
                            self.owners_dict[str(self.map[x][y].owner)].owned_tiles.append([x, y])
                        else:
                            self.owners_dict[str(len(self.owners_dict))] = Owner(name = len(self.owners_dict))
                            self.owners_dict[str(len(self.owners_dict) - 1)].owned_tiles.append([x, y])
                            self.map[x][y].owner = len(self.owners_dict) - 1

    def printStats(self):
        """Print simple statistics about tile ownership"""

        for owner in self.owners_dict.keys():
            if len(self.owners_dict[owner].owned_tiles) != 0:
                print("Tiles owned by " + str(owner) + ": " + str(len(self.owners_dict[owner].owned_tiles)))


    def startSimulation(self):
        """Starts simulation"""
        ## setup initial map ##
        self.mapGeneration()
        self.owners_dict[str(0)] = Owner(name = 0)
        self.owners_dict[str(1)] = Owner(name = 1)
        self.map[1][1].owner = 1

        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                self.owners_dict[str(self.map[x][y].owner)].owned_tiles.append([x, y])

        turns = 0
        print('Turn:' + str(turns))
        self.printMap()

        while True:
            time.sleep(self.sleep_time)

            self.splitCell()
            self.mutateCell()

            clearTerminal()

            turns += 1
            print('Turn:' + str(turns))
            self.printMap()
            if (self.print_stats):
                self.printStats()