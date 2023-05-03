import tkinter as tk
from random import randint

class Tile:
    """
    Tile class

    Attributes:
        x_pos, y_pos - positions on the map
        inhabitant - tile inhabitant (currently just number)

    """
    def __init__(self, canvas, pos_x, pos_y, width, height):
        self.canvas = canvas
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.inhabitant = None

        self.initialized = False

    def draw(self):
        if self.inhabitant == None:
            tile_color = "black"
            species_id = "None"
            species_genes = ""
        else:
            tile_color = "#%02x%02x%02x" % self.inhabitant.getGenes()
            species_id = str(self.inhabitant.species_id)
            species_genes = str(self.inhabitant.getGenes())

        if not self.initialized:
            self.id = self.canvas.create_rectangle(self.pos_x,
                                                   self.pos_y,
                                                   self.pos_x + self.width,
                                                   self.pos_y + self.height,
                                                   fill = tile_color)
            self.text_id = self.canvas.create_text(self.pos_x + 20,
                                                   self.pos_y + 20,
                                                   text = species_id)
            self.text_genes_id = self.canvas.create_text(self.pos_x + 40,
                                                            self.pos_y + 50,
                                                            text = species_genes)
            self.initialized = True
        else:
            self.canvas.itemconfig(self.id, fill=tile_color)
            self.canvas.itemconfig(self.text_id, text=species_id)
            self.canvas.itemconfig(self.text_genes_id, text=species_genes)
            

    def changeInhabitant(self, inhabitant):
        self.inhabitant = inhabitant


    