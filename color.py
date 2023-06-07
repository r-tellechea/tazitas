from dataclasses import dataclass

@dataclass(order=True, frozen=True)
class Color:
	color : str
	
	def __invert__(self):
		return Color('blue') if self.color == 'red' else Color('red')
