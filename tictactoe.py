"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy


X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num_x = sum(row.count(X) for row in board)
    num_o = sum(row.count(O) for row in board)
    return X if num_x <= num_o else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_set = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action_set.add((i, j))
    return action_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] is not EMPTY:
        raise ValueError("Invalid Action")
    
    new_board = deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for player in [X, O]:
        # Check rows, columns, and diagonals
        for i in range(3):
            if all([board[i][j] == player for j in range(3)]) or \
               all([board[j][i] == player for j in range(3)]):
                return player
        if all([board[i][i] == player for i in range(3)]) or \
           all([board[i][2-i] == player for i in range(3)]):
            return player
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(cell != EMPTY for row in board for cell in row)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    def max_value(board):
        if terminal(board):
            return utility(board)
        v = -math.inf
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v

    def min_value(board):
        if terminal(board):
            return utility(board)
        v = math.inf
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v

    current_player = player(board)
    if current_player == X:
        value, move = -math.inf, None
        for action in actions(board):
            action_value = min_value(result(board, action))
            if action_value > value:
                value, move = action_value, action
    else:
        value, move = math.inf, None
        for action in actions(board):
            action_value = max_value(result(board, action))
            if action_value < value:
                value, move = action_value, action
    return move
