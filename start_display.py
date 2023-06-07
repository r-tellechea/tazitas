from dataclasses import dataclass
from piece import Piece
from player import Player
from color import Color

@dataclass
class StartDisplay:
    pieces : tuple[Piece]
    player : Player

    def __init__(self, pieces : tuple[Piece]) -> None:
        self.pieces = pieces

basic_display = StartDisplay(pieces=tuple(
    [Piece(player=Player(1), color=Color('red'))  for _ in range(4)] + 
    [Piece(player=Player(1), color=Color('blue')) for _ in range(4)]
))
