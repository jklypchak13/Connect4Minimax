"""contains functions related to scoring a connect 4 board for minimax
"""
from typing import Dict
import numpy as np
BOARD_ROWS: int = 6
BOARD_COLUMNS: int = 7


def check_vertical(data: np.ndarray, row: int, col: int) -> int:
    """check the vertical direction for a winner at the designated spot

    Arguments:
        data {np.ndarray} -- the board to check
        row {int} -- the row of the current spot to check
        col {int} -- the column of the current spot to check

    Returns:
        int -- the winner (or 0 is no winner)
    """
    if data[row, col] == 0 or row > 2:
        return 0
    for diff in range(3):
        if(data[row + diff, col] == data[(row + diff) + 1, col]):
            pass
        else:
            return 0
    return data[row, col]


def check_horizontal(data: np.ndarray, row: int, col: int) -> int:
    """check the horizontal direction for a winner at the designated spot

    Arguments:
        data {np.ndarray} -- the board to check
        row {int} -- the row of the current spot to check
        col {int} -- the column of the current spot to check

    Returns:
        int -- the winner (or 0 is no winner)
    """
    if data[row, col] == 0 or col > 3:
        return 0
    for diff in range(3):
        if(data[row, col + diff] == data[row, col + 1 + diff]):
            pass
        else:
            return 0
    return data[row, col]


def check_positive_diagonal(data: np.ndarray, row: int, col: int) -> int:
    """check the postive diagonal for a winner at the designated spot

    Arguments:
        data {np.ndarray} -- the board to check
        row {int} -- the row of the current spot to check
        col {int} -- the column of the current spot to check

    Returns:
        int -- the winner (or 0 is no winner)
    """
    if data[row, col] == 0 or row - 3 < 0 or col + 3 >= BOARD_COLUMNS:
        return 0
    for diff in range(3):
        if(data[row - diff, col + diff] == data[row - 1 - diff, col + 1 + diff]):
            pass
        else:
            return 0
    return data[row, col]


def check_negative_diagonal(data: np.ndarray, row: int, col: int) -> np.ndarray:
    """check the negative diagonal for a winner at the designated spot

    Arguments:
        data {np.ndarray} -- the board to check
        row {int} -- the row of the current spot to check
        col {int} -- the column of the current spot to check

    Returns:
        int -- the winner (or 0 is no winner)
    """
    if data[row, col] == 0 or row + 3 >= BOARD_ROWS or col + 3 >= BOARD_COLUMNS:
        return 0
    for diff in range(3):
        if(data[row + diff, col + diff] == data[row + 1 + diff, col + 1 + diff]):
            pass
        else:
            return 0
    return data[row, col]


def count_lines_of_two(board: np.ndarray) -> Dict[int, int]:
    """count of the number of two consecutive characters in the array

    Arguments:
        board {np.ndarray} -- the board state the check

    Returns:
        Dict[int, int] -- a map of integers values to the corresponding counts
    """
    count = {0: 0, 1: 0, 2: 0}
    for i in range(BOARD_ROWS):
        for j in range(BOARD_COLUMNS):
            if i + 1 < BOARD_ROWS:
                if board[i, j] == board[i + 1, j]:
                    count[board[i, j]] += 1
            if j + 1 < BOARD_COLUMNS:
                if board[i, j] == board[i, j + 1]:
                    count[board[i, j]] += 1
            if i + 1 < BOARD_ROWS and j + 1 < BOARD_COLUMNS:
                if board[i, j] == board[i + 1, j + 1]:
                    count[board[i, j]] += 1
            if i - 1 >= 0 and j + 1 < BOARD_COLUMNS:
                if board[i, j] == board[i - 1, j + 1]:
                    count[board[i, j]] += 1
    return count


def count_lines_of_three(board):
    """count of the number of three consecutive characters in the array

    Arguments:
        board {np.ndarray} -- the board state the check

    Returns:
        Dict[int, int] -- a map of integers values to the corresponding counts
    """
    count = {0: 0, 1: 0, 2: 0}
    for i in range(BOARD_ROWS):
        for j in range(BOARD_COLUMNS):
            if i + 2 < BOARD_ROWS:
                if board[i, j] == board[i + 1, j] and board[i, j] == board[i + 2, j]:
                    count[board[i, j]] += 1
            if j + 2 < BOARD_COLUMNS:
                if board[i, j] == board[i, j + 1] and board[i, j] == board[i, j + 2]:
                    count[board[i, j]] += 1
            if i + 2 < BOARD_ROWS and j + 2 < BOARD_COLUMNS:
                if board[i, j] == board[i + 1, j + 1] and board[i, j] == board[i + 2, j + 2]:
                    count[board[i, j]] += 1
            if i - 2 >= 0 and j + 2 < BOARD_COLUMNS:
                if board[i, j] == board[i - 1, j + 1] and board[i, j] == board[i - 2, j + 2]:
                    count[board[i, j]] += 1
    return count
