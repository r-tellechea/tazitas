#%%
from board import Board
from player import Player
from display import basic_display

b = Board()
b.insert_display(Player(), basic_display)
b.insert_display(~Player(), basic_display)
print(b)