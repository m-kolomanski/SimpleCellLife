import copy
import random
import time
from random import randint
from Tile import Tile
from Cell import Cell

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

        # cells dict #
        self.cells_dict = {}

        # evolution atributes #
        self.mutation_rate = mutation_rate

        # system atributes #
        self.sleep_time = sleep_time
        self.print_stats = print_stats

    def mapGeneration(self):
        """Generates map"""
        map_tiles = []

        for a in range(self.map_x):
            x_temp = []
            for b in range(self.map_y):

                x_temp.append(Tile(x_pos = a,
                                   y_pos = b))

            map_tiles.append(x_temp)

        self.map = map_tiles

    def printMap(self):
        """Prints map"""
        for i in range(len(self.map)):
            map_row = []
            for j in range(len(self.map[i])):
                map_row.append(self.map[i][j].inhabitant)
            print(map_row)

    def splitCell(self):
        """Splits existing cells"""
        for inhabitant in self.cells_dict.keys():
            inhabitants_local = copy.deepcopy(self.cells_dict)
            if inhabitant != '0':
                for tile in inhabitants_local[inhabitant].inhabited_tiles:
                    x = tile[0]
                    y = tile[1]
                    target = random.choice([[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]])

                    if -1 not in target and 10 not in target and target not in self.cells_dict[inhabitant].inhabited_tiles: ## todo: add flexible bounds detection
                        ## remove current inhabitant ##
                        self.cells_dict[str(self.map[target[0]][target[1]].inhabitant)].inhabited_tiles.remove(target)
                        ## take inhabitantship of the tile ##
                        self.map[target[0]][target[1]].inhabitant = int(inhabitant)
                        ## add owned tile ##
                        self.cells_dict[inhabitant].inhabited_tiles.append(target)


    def mutateCell(self):
        """Mutates existing cells"""
        map_local = copy.deepcopy(self.map)

        for x in range(len(map_local)):
            for y in range(len(map_local[x])):
                if map_local[x][y].inhabitant != 0:
                    if randint(1, 100) in range(1, self.mutation_rate):
                        self.cells_dict[str(self.map[x][y].inhabitant)].inhabited_tiles.remove([x, y])

                        if str(self.map[x][y].inhabitant + 1) in self.cells_dict.keys():
                            self.map[x][y].inhabitant += 1
                            self.cells_dict[str(self.map[x][y].inhabitant)].inhabited_tiles.append([x, y])
                        else:
                            self.cells_dict[str(len(self.cells_dict))] = Cell(species = len(self.cells_dict))
                            self.cells_dict[str(len(self.cells_dict) - 1)].inhabited_tiles.append([x, y])
                            self.map[x][y].inhabitant = len(self.cells_dict) - 1

    def printStats(self):
        """Print simple statistics about tile inhabitantship"""

        for inhabitant in self.cells_dict.keys():
            if len(self.cells_dict[inhabitant].inhabited_tiles) != 0:
                print("Tiles owned by " + str(inhabitant) + ": " + str(len(self.cells_dict[inhabitant].inhabited_tiles)))


    def startSimulation(self):
        """Starts simulation"""
        ## setup initial map ##
        self.mapGeneration()
        self.cells_dict[str(0)] = Cell(species = 0)
        self.cells_dict[str(1)] = Cell(species = 1)
        self.map[1][1].inhabitant = 1

        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                self.cells_dict[str(self.map[x][y].inhabitant)].inhabited_tiles.append([x, y])

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