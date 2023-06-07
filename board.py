import pandas as pd

from color import Color
from piece import Piece
from player import Player
from coords import Coords, start_display_coords
from start_display import StartDisplay
from board_to_dataframe import board_to_dataframe

class Board:
	"""Tablero del juego. Cuenta con:
	 - insert_piece: Colorcar una pieza concreta en unas coordenadas
	 - insert_display: Colorcar una configuración inicial en el lado de uno de los jugadores.
	"""
	def __init__(self) -> None:
		self.board = [[None for __ in range(6)] for _ in range (6)]

	def __str__(self) -> str:
		text = ''
		for row in self.board:
			for piece in row:
				if piece == None:
					text += '0 '
				else:
					if piece.color == Color('red'):
						text += 'r '
					else:
						text += 'b '
			text += '\n'
		return text
	
	def get_piece(self, coords : Coords) -> Piece:
		return self.board[coords.row][coords.col]
	
	def set_piece(self, coords : Coords, piece : Piece=None) -> None:
		self.board[coords.row][coords.col] = piece
	
	def is_piece(self, coords : Coords) -> bool:
		return isinstance(self.get_piece(coords), Piece)
	
	def is_piece_of_player(self, coords : Coords, player : Player) -> bool:
		if not self.is_piece(coords):
			raise ValueError('There is not piece in the selected cell.')
		return self.get_piece(coords).player == player

	def insert_start_display (self, player : Player, start_display : StartDisplay) -> None:
		for coords, piece in zip(start_display_coords(player), start_display.pieces):
			self.set_piece(coords=coords, piece=piece)
		
	def check_victory(self) -> Player:
		#TODO
		# Devuelve None si la partida sigue o un jugador si éste gana.
		pass

	def move_piece(self, start_coords : Coords, end_coords : Coords):
		#TODO
		# Comprobar:
		# - Las coordenadas de origen corresponden a una pieza.
		# - Las coordenadas de destino está en la lista de casillas disponibles para la pieza.
		# - En caso de que haya una pieza en el destino no puede ser del mismo jugador.
		# - Cosas de las esquinas

		# Copiar pieza en la casilla de destino.
		# Poner vacía la casilla de origen.

		# Comprobar victorias.

		pass

	def df(self, player : Player=None) -> pd.DataFrame:
		return board_to_dataframe(board=self, player=player)
