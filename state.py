import numpy as np
import copy

PIECE_X = 'x'
PIECE_O = 'o'
PIECE_N = ' '


class State:

    def __init__(self, board=False):
        if board:
            self.board = np.array(board)
        else:
            self.board = np.array([PIECE_N] * 9)

    def actions(self, piece):
        states = []
        indices = self.null_indices()
        for i in indices:
            states.append(self.copy().place(i, piece))
        return states

    def place(self, i, piece):
        self.board[i] = piece
        return self

    def winning_piece(self):
        b = self.board
        if   (b[0] != PIECE_N) and (b[0] == b[1] == b[2]): return b[0]
        elif (b[3] != PIECE_N) and (b[3] == b[4] == b[5]): return b[3]
        elif (b[6] != PIECE_N) and (b[6] == b[7] == b[8]): return b[6]
        elif (b[0] != PIECE_N) and (b[0] == b[3] == b[6]): return b[0]
        elif (b[1] != PIECE_N) and (b[1] == b[4] == b[7]): return b[1]
        elif (b[2] != PIECE_N) and (b[2] == b[5] == b[8]): return b[2]
        elif (b[4] != PIECE_N) and ((b[0] == b[4] == b[8])
            or (b[2] == b[4] == b[6])): return b[4]
        return PIECE_N

    def is_terminal(self):
        return (len(self.null_indices()) == 0) or (self.winning_piece() != PIECE_N)

    def utility(self):
        winner = self.winning_piece()
        if winner == PIECE_X:
            return 1
        elif winner == PIECE_N:
            return 0
        return -1


    def null_indices(self):
        return np.where(self.board == PIECE_N)[0]

    def print_board(self):
        print('|'.join(self.board[0:3]))
        print('|'.join(self.board[3:6]))
        print('|'.join(self.board[6:9]))

    def copy(self):
        return copy.deepcopy(self)


testState = State()
testState.place(0, 'x')
testState.place(4, 'o')
testState.place(6, 'x')
testState.place(3, 'o')
testState.place(5, 'x')

drawState = testState.actions('x')[0].actions('o')[0].actions('x')[0].actions('o')[0]
winState = testState.copy().place(0, 'x').place(4, 'o').place(3, 'x').place(7, 'o').place(6, 'x')
loseState = testState.copy().place(0, 'x').place(6, 'o').place(8, 'x').place(2, 'o')


assert not testState.is_terminal()
assert 4 == len(testState.actions('o'))
assert 0 == drawState.utility()
assert 1 == winState.utility()
assert -1 == loseState.utility()
