class Owner:
    """
    Owner class

    Attributes:
        name - name of the owner
        owned_tiles - list of tiles currently owned

    """
    def __init__(self, name):
        self.name = name
        self.owned_tiles = []