from dataclasses import dataclass
from direction import Direction
from player import Player

@dataclass(order=True, frozen=True)
class Coords:
	row : int
	col : int

	def __add__(self, dir : Direction) -> None:
		match dir.dir:
			case 0:
				return Coords(self.row - 1, self.col)
			case 1:
				return Coords(self.row, self.col + 1)
			case 2:
				return Coords(self.row + 1, self.col)
			case 3:
				return Coords(self.row, self.col - 1)

	def valid(self) -> bool:
		return self.row in range(6) and self.col in range(6)

	def apply(self, dirs : list[Direction]) -> list:
		return list(filter(
			lambda coords : coords.valid(), 
			(self + dir for dir in dirs)
		))

	def nesw(self) -> list:
		return self.apply(Direction.nesw())

def display_coords(player : Player) -> list[Coords]:
	if player == Player():
		return [Coords(i, j) for i in range(4,6) for j in range(1,5)]
	if player == ~Player():
		return [Coords(i, j) for i in range(0,2) for j in range(1,5)][::-1]
