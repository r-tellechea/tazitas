from dataclasses import dataclass
from player import Player
from color import Color

@dataclass(order=True, frozen=True)
class Piece:
    player : Player
    color  : Color

    def get_player(self) -> Player:
        return self.player
