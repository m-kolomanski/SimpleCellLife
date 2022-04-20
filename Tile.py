class Tile:
    """
    Tile class

    Attributes:
        x_pos, y_pos - positions on the map
        inhabitant - tile inhabitant (currently just number)

    """
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.inhabitant = 0