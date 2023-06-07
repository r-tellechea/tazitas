#%%
from board import Board
from player import Player
from start_display import basic_display

board = Board()
board.insert_start_display(Player(), basic_display)
board.insert_start_display(~Player(), basic_display)
print(board)
