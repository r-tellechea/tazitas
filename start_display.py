from dataclasses import dataclass
from piece import Piece
from player import Player

@dataclass
class StartDisplay:
    pieces : tuple[Piece]
    player : Player

    def __init__(self, pieces : tuple[Piece]) -> None:
        self.pieces = pieces

basic_display = StartDisplay(pieces=tuple(
    [Piece(player=1, color='red')  for _ in range(4)] + 
    [Piece(player=1, color='blue') for _ in range(4)]
))
