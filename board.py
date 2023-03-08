from case import Case
from color import Color
from piece import Piece


class Board:
    def __init__(self):
        self.grid = [
            [Case(Color.WHITE), Case(Color.BLACK), Case(Color.WHITE), Case(Color.BLACK), Case(Color.WHITE), Case(Color.BLACK), Case(Color.WHITE), Case(Color.BLACK)],
            [Case(Color.BLACK), Case(Color.WHITE), Case(Color.BLACK), Case(Color.WHITE), Case(Color.BLACK), Case(Color.WHITE), Case(Color.BLACK), Case(Color.WHITE)],
            [Case(Color.WHITE), Case(Color.BLACK), Case(Color.WHITE), Case(Color.BLACK), Case(Color.WHITE), Case(Color.BLACK), Case(Color.WHITE), Case(Color.BLACK)],
            [Case(Color.BLACK), Case(Color.WHITE), Case(Color.BLACK), Case(Color.WHITE), Case(Color.BLACK), Case(Color.WHITE), Case(Color.BLACK), Case(Color.WHITE)],
            [Case(Color.WHITE), Case(Color.BLACK), Case(Color.WHITE), Case(Color.BLACK), Case(Color.WHITE), Case(Color.BLACK), Case(Color.WHITE), Case(Color.BLACK)],
            [Case(Color.BLACK), Case(Color.WHITE), Case(Color.BLACK), Case(Color.WHITE), Case(Color.BLACK), Case(Color.WHITE), Case(Color.BLACK), Case(Color.WHITE)],
            [Case(Color.WHITE), Case(Color.BLACK), Case(Color.WHITE), Case(Color.BLACK), Case(Color.WHITE), Case(Color.BLACK), Case(Color.WHITE), Case(Color.BLACK)],
            [Case(Color.BLACK), Case(Color.WHITE), Case(Color.BLACK), Case(Color.WHITE), Case(Color.BLACK), Case(Color.WHITE), Case(Color.BLACK), Case(Color.WHITE)],
        ]

        self.init_pieces()

    def __str__(self):
        str_ = ""
        for row in self.grid:
            for case in row:
                str_ += str(case)
                str_ += " "
            str_ += "\n"
        return str_

    def init_pieces(self):
        for i in range(0, 3):
            for case in self.grid[i]:
                if case.get_color() == Color.BLACK:
                    case.set_occupated_piece(Piece(Color.WHITE))

            for case in self.grid[-i-1]:
                if case.get_color() == Color.BLACK:
                    case.set_occupated_piece(Piece(Color.BLACK))