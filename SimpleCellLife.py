from random import randint
from Tile import Tile
from Species import Species
import tkinter as tk

class SimpleCellLife:
    """
    Simulation class
    """

    def __init__(self):
        # tiles #
        self.tiles = []

        # cells dict #
        self.species_dict = {}

        self.setupWindow()

    def setupWindow(self):
        self.window = tk.Tk()

        # canvas #
        self.canvas = tk.Canvas(self.window,
                                width = 1000,
                                height = 1000,
                                bd = 0, highlightthickness=0)
        self.canvas.grid(row=1,column=1)
        
        # input widgets #
        self.input_widgets = tk.Frame(master = self.window)
        tk.Label(master = self.input_widgets, text = "Input widgets").grid(row=1,column=1)

        # Map parameters #
        self.map_x = tk.Entry(master = self.input_widgets)
        self.map_x.grid(row=3,column=1)
        self.map_y = tk.Entry(master = self.input_widgets)
        self.map_y.grid(row=4,column=1)

        # sleep time #
        self.sleep_time = tk.Entry(master = self.input_widgets)
        self.sleep_time.grid(row=5,column=1)

        # mutation rate #
        self.mutation_rate = tk.Entry(master = self.input_widgets)
        self.mutation_rate.grid(row=6,column=1)

        # start sim button #
        self.start_sim_btn = tk.Button(master=self.input_widgets, text = "Start simulation")
        self.start_sim_btn.bind('<Button-1>', lambda e:self.startSimulation())
        self.start_sim_btn.grid(row=2,column=1)

        self.input_widgets.grid(row=1,column=2)

        self.window.mainloop()

    def createNewSpecies(self, genes = None, rgb_genes = (0,0,0)):
        species_id = len(self.species_dict)

        if genes == None:
            pass
        elif genes == 'mutate':
            new_genes = list(rgb_genes)
            new_genes[randint(0,2)] -= 10
        elif genes == 'random':
            rgb_genes = (randint(0,255),randint(0,255),randint(0,255))

        self.species_dict[str(species_id)] = Species(species_id = species_id,
                                                    rgb_genes = new_genes)

    def processTurn(self):
        # Tkinter does not allow to make deepcopies of its objects, therefore making a local copy of
        # tiles list is not possible. Hence weird way of iterating over tiles and their inhibitants.
        # TODO: Optimize

        tile_inhabitants = [tile.inhabitant for tile in self.tiles]
        for tile in range(len(self.tiles)):

            if tile_inhabitants[tile] == None:
                continue
            
            ### EXPAND ###
            move = tile_inhabitants[tile].getMove(self.tiles[tile].pos_x, self.tiles[tile].pos_y)

            for new_tile in self.tiles:
                if new_tile.pos_x == move[0] and new_tile.pos_y == move[1]:
                    new_tile.changeInhabitant(tile_inhabitants[tile])
                    break

            ### MUTATE ###
            if randint(1,100) <= int(self.mutation_rate.get()):

                # evolve into existing #
                if str(self.tiles[tile].inhabitant.species_id + 1) in self.species_dict.keys():
                    self.tiles[tile].changeInhabitant(self.species_dict[str(self.tiles[tile].inhabitant.species_id + 1)])

                # declare new species #
                else:
                    self.createNewSpecies(genes = 'mutate',
                                        rgb_genes = self.tiles[tile].inhabitant.getGenes())
                    self.tiles[tile].changeInhabitant(self.species_dict[str(len(self.species_dict) - 1)])   
        
        ### DRAW TILES ###
        for tile in self.tiles:
            tile.draw()

        ## do other stuff

        ## repeat
        self.canvas.after(int(self.sleep_time.get()), self.processTurn)
        
            
    def startSimulation(self):
        """Starts simulation"""
        ## show window ##
        #self.setupWindow()
        
        current_x = 0
        current_y = 0

        while True:
            self.tiles.append(Tile(self.canvas, current_x, current_y))

            current_x += 100

            if current_x >= int(self.map_x.get()) * 100:
                current_y += 100
                if current_y >= int(self.map_y.get()) * 100:
                    break
                current_x = 0

        self.species_dict[str(0)] = Species(species_id = 0,
                                          rgb_genes = [0,0,0])
        
        self.species_dict[str(1)] = Species(species_id = 1,
                                          rgb_genes = [255,255,255])
        
        self.tiles[0].changeInhabitant(self.species_dict[str(1)])

        for tile in self.tiles:
            tile.draw()

        self.processTurn()
        
if __name__ == "__main__":
    SimpleCellLife()