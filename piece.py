class Piece:
    def __init__(self, position, name, color):
        self.position = position
        self.color = color
        self.name = name
        self.has_moved = False