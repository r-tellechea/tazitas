from dataclasses import dataclass
from direction import Direction
from player import Player

@dataclass(order=True, frozen=True)
class Coords:
	row : int
	col : int

	# Añade una dirección a las coordenadas y devuelve otras coordenadas. 
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

	# Calcula si las coordenadas están en el rango de el tablero.
	def valid(self) -> bool:
		return self.row in range(6) and self.col in range(6)

	# Toma una lista de direcciones y devuelve la suma de esta casilla y cada dirección si el resultado es válido.
	def apply(self, dirs : list[Direction]) -> list:
		return list(filter(
			lambda coords : coords.valid(), 
			(self + dir for dir in dirs)
		))

	# Devuelve todas las casillas a las que es válido moverse desde esta casilla.
	def nesw(self) -> list:
		return self.apply(Direction.nesw())

# Da las coordenadas de las casillas iniciales de uno de los jugadores.
def start_display_coords(player : Player) -> list[Coords]:
	if player == Player():
		return [Coords(i, j) for i in range(4,6) for j in range(1,5)]
	if player == ~Player():
		return [Coords(i, j) for i in range(0,2) for j in range(1,5)][::-1]
