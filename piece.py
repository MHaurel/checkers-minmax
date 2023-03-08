from color import Color


class Piece:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        if self.color == Color.WHITE:
            return "⚪"
        elif self.color == Color.BLACK:
            return "⚫"
