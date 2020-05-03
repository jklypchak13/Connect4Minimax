import numpy as np

from board import Board
from minimax import minimax
from time import sleep
board = Board()


player_1 = 1
player_2 = 2

temp = np.array([[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]
                 ])
board.set_board(temp)
while(not board.terminal()):
    # sleep(2)
    print(board)
    # column = input('Choose a column: ')
    move = minimax(board, player_1, 5, -1000000000, 10000000)
    column = move.index
    board.insert_piece(player_1, int(column))
    print(f"1 Score:{move.score}")
    print(f"Move: {move.index}")
    if board.terminal():
        break
    move = minimax(board, player_2, 5, -1000000000, 10000000)
    print(f"2 Score: {move.score}")
    print(f"Move: {move.index}")
    board.insert_piece(player_2, move.index)

print(board)
