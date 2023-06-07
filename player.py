from dataclasses import dataclass

@dataclass(order=True, frozen=True)
class Player:
	player : int=1

	def __invert__(self):
		return Player(1) if self.player == 2 else Player(2)
