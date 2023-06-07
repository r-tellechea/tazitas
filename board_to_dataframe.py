#%%
import pandas as pd
import numpy as np
from player import Player
from color import Color

def board_to_dataframe (board, player : Player=None) -> pd.DataFrame:
	data = np.full(shape=(6,6), fill_value='')
	data[0,0] = '⌜'
	data[0,5] = '⌝'
	data[5,0] = '⌞'
	data[5,5] = '⌟'

	list_color = [[
		'background-color: #B5B2B2; ' if (i+j)%2 else 'background-color: #E0E0E0; '
			for j in range(6)]
				for i in range(6)]
	
	for i in range(6):
		for j in range(6):
			piece = board.board[i][j]
			if piece == None:
				list_color[i][j] += 'color: black'
				continue
			
			data[i,j] = '⦿'
			
			color_available = player == None or player == piece.player
			if color_available:
				list_color[i][j] += 'color: blue' if piece.color == Color('blue') else 'color: red'
			else:
				list_color[i][j] += 'color: black'
	
	array_color = np.array(list_color)
	
	df = (
		pd.DataFrame(
			data=data,
			index=[f'{i}' for i in range(6)],
			columns=[f'{j}' for j in range(6)],	
		)
		.style
		.apply(lambda df : array_color, axis=None)
	)
	return df
