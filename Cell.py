import random


class Cell:
    """
    Cell class

    Attributes:
        species - name of the cell species
        inhabited_tiles - list of tiles currently inhabited
        color - phenotype denoted by three genes: R, G, B

    """
    def __init__(self, species, rgb_genes):
        self.species = species
        self.inhabited_tiles = []
        self.color = rgb_genes

    def mutateRGB(self):
        print("mutating" + str(self.species))
        gene_to_mutate = random.choice([0, 1, 2])
        mutation_direction = random.choice([50, -50])
        new_mutation = self.color[gene_to_mutate] + mutation_direction
        if new_mutation <= 255 and new_mutation > 0:
            self.color[gene_to_mutate] += mutation_direction
        else:
            self.color[gene_to_mutate] -= mutation_direction

