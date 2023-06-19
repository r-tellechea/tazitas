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
			raise ValueError('There is not a piece in the selected cell.')
		return self.get_piece(coords).get_player() == player

	def insert_start_display (self, player : Player, start_display : StartDisplay) -> None:
		for coords, piece in zip(start_display_coords(player), start_display.pieces):
			self.set_piece(coords=coords, piece=piece)
		
	def check_victory(self) -> Player:
		# TODO
		# Devuelve None si la partida sigue o un jugador si éste gana.
		pass

	def is_edge_of_player(player : Player, coords : Coords) -> bool:
		if player == Player():
			if coords in [Coords(5,0),Coords(5,5)]:
				return True
			return False
		if player == ~Player():
			if coords in [Coords(0,0),Coords(0,5)]:
				return True
			return False

	def move_piece(self, start_coords : Coords, end_coords : Coords):
		# - Las coordenadas de origen corresponden a una pieza.
		if not self.is_piece(start_coords):
			raise ValueError('There is not a piece in the selected cell.')
		# - Las coordenadas de destino está en la lista de casillas disponibles para la pieza.
		if end_coords not in start_coords.nesw():
			raise Exception('That move is not allowed.')
		# - En caso de que haya una pieza en el destino no puede ser del mismo jugador.
		if not self.is_piece(end_coords) and self.is_piece_of_player(end_coords,self.get_piece(start_coords).get_player()):
			raise Exception('You cannot caputre your own piece.')
		# - Cosas de las esquinas
		if self.is_edge_of_player(self.get_piece(start_coords).get_player(), end_coords):
			raise Exception('You cannot move to the edges of your side of the board.')
		# Copiar pieza en la casilla de destino.
		self.set_piece(end_coords,self.get_piece(start_coords))
		# Poner vacía la casilla de origen.
		self.set_piece(start_coords)
		# TODO
		# Comprobar victorias.
		pass

	def df(self, player : Player=None) -> pd.DataFrame:
		return board_to_dataframe(board=self, player=player)
