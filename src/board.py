"""Contains helper code for a Connect 4 AI Game with Mini-max
"""
import numpy as np
from typing import Dict
BOARD_ROWS: int = 6
BOARD_COLUMNS: int = 7


class Board:
    """Represents a board for a game of connect 4
    """

    def __init__(self):
        self.data: np.ndarray[6, 7] = np.zeros((BOARD_ROWS, BOARD_COLUMNS))

    def __repr__(self):

        return str(self.data)

    def column_full(self, i: int) -> bool:
        """check if a given column is full

        Arguments:
            i {int} -- the index of the column

        Returns:
            bool -- if the column is full or not
        """
        return 0 not in self.data[:, i]

    def insert_piece(self, player: int, column: int):
        """insert a piece into a given column

        Arguments:
            player {int} -- the active player token
            column {int} -- the column to insert into
        """
        column_data = self.data[:, column]
        rev_column = column_data[::-1]

        # Get the index of the first 0, then account for reverse
        index = np.argmin(rev_column)
        index = self.data.shape[0] - 1 - index

        self.data[index, column] = player

    def generate_neighbors(self, player: int) -> Dict[int, np.ndarray]:
        """generate all possible outcomes of the given players turn

        Arguments:
            player {int} -- the current player

        Returns:
            Dict[np.ndarray] -- a map of each possible column play and it's associated board
        """
        neighbors: Dict[int, np.ndarray] = {}
        for column in range(self.data.shape[1]):
            if not self.column_full(column):
                new_board: np.ndarray = self.copy()
                new_board.insert_piece(player, column)
                neighbors[column] = new_board
        return neighbors

    def copy(self):
        """get a copy of this board

        Returns:
            Board -- the copied board
        """
        new_board = Board()
        new_board.data = np.copy(self.data)
        return new_board

    def score(self) -> int:
        """generate the score for this board for minimax

        Returns:
            int -- the boards associated score
        """
        score: int = 0
        winner: int = self.winner()
        if winner == 1:
            score += 100000
        elif winner == 2:
            score -= 100000
        one_count: int = np.sum(self.data == 1)
        two_count: int = np.sum(self.data == 2)
        turn: int = 1 if one_count == two_count else 2

        counts: Dict[int, int] = count_lines_of_two(self.data)
        score += counts[1] * 2
        score -= counts[2] * 2

        counts = count_lines_of_three(self.data)
        if turn == 1:
            score += counts[1] * 40
            score -= counts[2] * 400
        else:
            score += counts[1] * 400
            score -= counts[2] * 40

        score += np.sum(self.data[:, 3] == 1) * 12
        score -= np.sum(self.data[:, 3] == 2) * 12
        return score

    def set_board(self, board):
        self.data = board

    def winner(self):
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLUMNS):
                result = check_vertical(self.data, i, j)
                if result != 0:
                    return result
                result = check_horizontal(self.data, i, j)
                if result != 0:
                    return result

                result = check_positive_diagnoal(self.data, i, j)
                if result != 0:
                    return result

                result = check_negative_diagnoal(self.data, i, j)
                if result != 0:
                    return result
        return 0

    def terminal(self):
        return self.winner() > 0 or np.sum(self.data > 0) == BOARD_COLUMNS * BOARD_ROWS


def check_vertical(data, i, j):
    if data[i, j] == 0 or i > 2:
        return 0
    for diff in range(3):
        if(data[i + diff, j] == data[(i + diff) + 1, j]):
            pass
        else:
            return 0
    return data[i, j]


def check_horizontal(data, i, j):
    if data[i, j] == 0 or j > 3:
        return 0
    for diff in range(3):
        if(data[i, j + diff] == data[i, j + 1 + diff]):
            pass
        else:
            return 0
    return data[i, j]


def check_positive_diagnoal(data, i, j):
    if data[i, j] == 0 or i - 3 < 0 or j + 3 >= BOARD_COLUMNS:
        return 0
    for diff in range(3):
        if(data[i - diff, j + diff] == data[i - 1 - diff, j + 1 + diff]):
            pass
        else:
            return 0
    return data[i, j]


def check_negative_diagnoal(data, i, j):
    if data[i, j] == 0 or i + 3 >= BOARD_ROWS or j + 3 >= BOARD_COLUMNS:
        return 0
    for diff in range(3):
        if(data[i + diff, j + diff] == data[i + 1 + diff, j + 1 + diff]):
            pass
        else:
            return 0
    return data[i, j]


def count_lines_of_two(board):
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
