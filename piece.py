from dataclasses import dataclass
from player import Player
from color import Color

@dataclass
class Piece:
    player : Player
    color  : Color