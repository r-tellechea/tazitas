#%%
from board import Board
from player import Player
from start_display import basic_display_0, basic_display_1
from color import Color

board = Board()
board.insert_start_display(Player(), basic_display_0)
board.insert_start_display(~Player(), basic_display_1)
print(board)

#%%
board.df()
