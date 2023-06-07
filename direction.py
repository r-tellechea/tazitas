from dataclasses import dataclass

@dataclass(order=True, frozen=True)
class Direction:
	dir : int

	def __str__(self) -> str:
		match self.dir:
			case 0: 
				return '↑'
			case 1: 
				return '→'
			case 2: 
				return '↓'
			case 3: 
				return '←'

	def nesw() -> list:
		return [Direction(dir) for dir in range(4)]
