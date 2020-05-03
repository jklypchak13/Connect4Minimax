from board import Board
MIN_INT: int = -1000000000000000000
MAX_INT: int = 1000000000000000000


class Move:
    """Represents a connect 4 move, and it's associated score
    """

    def __init__(self, score, index):
        self.score = score
        self.index = index

    def __repr__(self):
        return str(self.index)


def minimax(board: Board, player: int, depth: int, alpha: int, beta: int) -> Move:
    """run the minimax algorithm with alpha beta pruning, given the associated board

    Arguments:
        board {Board} -- the current board state
        player {int} -- the active player (1 or 2)
        depth {int} -- how much deeper to go in the minimax tree
        alpha {int} -- the current alpha value (for pruning)
        beta {int} -- the current beta value (for pruning)

    Returns:
        Move -- the optimal move for the active player, containing the score and column to get there.
    """

    # If the game is over or we are done looking
    if board.terminal() or depth == 0:
        return Move(board.score(), None)

    # Max Player
    if player == 1:
        value = Move(MIN_INT, None)
        children = board.generate_neighbors(player)
        for move, child_board in children.items():
            value = max(value, Move(minimax(child_board, 2, depth - 1, alpha, beta).score,
                                    move), key=lambda x: x.score)
            alpha = max(alpha, value.score)
            if(alpha >= beta):
                break
        return value
    # Min Player
    else:
        value = Move(MAX_INT, None)
        children = board.generate_neighbors(player)
        for move, child_board in children.items():
            value = min(value, Move(minimax(child_board, 1, depth - 1, alpha, beta).score,
                                    move), key=lambda x: x.score)
            beta = min(beta, value.score)
            if(alpha >= beta):
                break
        return value
