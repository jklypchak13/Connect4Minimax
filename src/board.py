"""Contains Connect 4 AI Game Implementation, such as the Board and other useful functions
"""
import numpy as np
from typing import Dict
import board_utl
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

        # Check for winner
        winner: int = self.winner()
        if winner == 1:
            score += 100000
        elif winner == 2:
            score -= 100000

        # Determine whose turn it is
        one_count: int = np.sum(self.data == 1)
        two_count: int = np.sum(self.data == 2)
        turn: int = 1 if one_count == two_count else 2

        # Assign score based on lines of two
        counts: Dict[int, int] = board_utl.count_lines_of_two(self.data)
        score += counts[1] * 2
        score -= counts[2] * 2

        # Assign score based on lines of three
        counts = board_utl.count_lines_of_three(self.data)
        if turn == 1:
            score += counts[1] * 40
            score -= counts[2] * 400
        else:
            score += counts[1] * 400
            score -= counts[2] * 40

        # Assign score based on number of tiles in center column
        score += np.sum(self.data[:, 3] == 1) * 12
        score -= np.sum(self.data[:, 3] == 2) * 12
        return score

    def set_board(self, board: np.ndarray):
        """set the board state given a numpy array

        Arguments:
            board {np.ndarray} -- the new board state
        """
        self.data = board

    def winner(self) -> int:
        """check to see if a winner exists

        Returns:
            int -- the winner's number (or 0 if no winner exists)
        """
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLUMNS):
                # Check vertical for winner
                result = board_utl.check_vertical(self.data, i, j)
                if result != 0:
                    return result
                # Check horizontal for winner
                result = board_utl.check_horizontal(self.data, i, j)
                if result != 0:
                    return result
                # Check positive diagonal for winner
                result = board_utl.check_positive_diagonal(self.data, i, j)
                if result != 0:
                    return result

                # Check negative diagonal for winner
                result = board_utl.check_negative_diagonal(self.data, i, j)
                if result != 0:
                    return result
        return 0

    def terminal(self) -> bool:
        """check to see if the game is over

        Returns:
            bool -- whether or not the game is over
        """
        return self.winner() > 0 or np.sum(self.data > 0) == BOARD_COLUMNS * BOARD_ROWS
