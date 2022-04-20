class Cell:
    """
    Cell class

    Attributes:
        species - name of the cell species
        inhabited_tiles - list of tiles currently inhabited

    """
    def __init__(self, species):
        self.species = species
        self.inhabited_tiles = []