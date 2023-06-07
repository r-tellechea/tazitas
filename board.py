from color import Color
from piece import Piece
from player import Player
from coords import Coords, display_coords
from display import Display

class Board:
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
	
	def insert_piece(self, coords : Coords, piece : Piece) -> None:
		self.board[coords.row][coords.col] = piece

	def insert_display (self, player : Player, display : Display) -> None:
		for coords, piece in zip(display_coords(player), display.pieces):
			self.insert_piece(coords=coords, piece=piece)
