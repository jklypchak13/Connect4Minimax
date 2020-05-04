from tkinter import *
import numpy as np
import minimax
from board import Board
import sys
board = Board()
master = Tk()

canvas_width = 800
canvas_height = 600
frame = Frame(master, height=75, width=75 * 7)


buttons = []
turn = 1


def insert(i):

    def partial():
        global turn
        if(turn == 1):
            board.insert_piece(1, i)
            turn = 2
    return partial


for i in range(0, 7):
    temp = Button(frame, text=str(i), command=insert(i), width=10)
    temp.pack(side=LEFT)
    buttons.append(temp)

temp = Button(frame, text="Quit", command=master.destroy, width=10)
temp.pack(side=LEFT)
buttons.append(temp)

w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
frame.pack()
w.pack()


def draw_grid(canvas: Canvas):
    for i in range(1, 9):
        canvas.create_line(i * 75 + 50, 75, i * 75 + 50,
                           canvas_height - 75, fill="#000000")

    for j in range(1, 8):
        canvas.create_line(125, j * 75, canvas_width -
                           150, j * 75, fill="#000000")


def draw_board(board: np.ndarray, canvas: Canvas):
    for i in range(7):
        for j in range(6):
            position_x = 125 + 75 * i
            position_y = 75 + j * 75
            if(board[j, i] == 1):
                w.create_text(position_x + (75 / 2),
                              position_y + (75 / 2),
                              text="X", font=("Purisa", 50))
            elif(board[j, i] == 2):
                w.create_text(position_x + (75 / 2),
                              position_y + (75 / 2),
                              text="O", font=("Purisa", 50))
            # canvas.create_line(position_x, position_y,
            #                    position_x + 75, position_y + 75, fill="#000000")


while True:
    if not board.terminal() and turn == 2:
        board = minimax.take_turn(board, 2)
        turn = 1
    draw_grid(w)
    draw_board(board.data, w)
    master.update_idletasks()
    master.update()
