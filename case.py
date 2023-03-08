from color import Color

class Case:
    def __init__(self, color):
        self.color = color
        self.occupated_piece = None

    def __str__(self):
        if self.occupated_piece is not None:
            return str(self.occupated_piece)
        else:
            if self.color == Color.WHITE:
                return "⬜"
            elif self.color == Color.BLACK:
                return "⬛"

    def set_occupated_piece(self, piece):
        self.occupated_piece = piece

    def get_occpated_piece(self):
        return self.occupated_piece

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color