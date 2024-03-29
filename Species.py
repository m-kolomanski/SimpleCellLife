from random import randint

class Species:
    """
    Species class

    Attributes:
        species - name of the cell species
        inhabited_tiles - list of tiles currently inhabited
        color - phenotype denoted by three genes: R, G, B

    """
    def __init__(self, species_id, rgb_genes):
        self.species_id = species_id
        self.inhabited_tiles = []
        self.genes = rgb_genes

    def getGenes(self):
        return tuple(self.genes)
    
    def getMove(self, current_x, current_y, offset_x, offset_y):
        move = randint(0,3)

        match move:
            case 0: current_x += offset_x
            case 1: current_x -= offset_x
            case 2: current_y += offset_y
            case 3: current_y -= offset_y
        
        return (current_x, current_y)

