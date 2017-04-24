from state import *
import numpy as np
from os import system


def main():
    while True:
        state = State()
        while not state.is_terminal():
            system('clear')
            state.print_board()
            pos = int(input('x: ')) % 9
            state = state.place(pos, PIECE_X)

            utilities = []
            actions = state.actions(PIECE_O)

            for action in actions:
                utilities.append(max_play(action))
            if state.is_terminal():
                break
            state = actions[np.argmin(utilities)]
        state.print_board()
        if state.winning_piece() == PIECE_O:
            print('        you lose!')
        else:
            print('        draw!')
        input()


def min_play(state):
    if state.is_terminal():
        return state.utility()

    utilities = []
    actions = state.actions(PIECE_O)
    for action in actions:
        # returning -1 early speeds up min
        _max = max_play(action)
        if _max == -1:
            return -1
        utilities.append(_max)

    return min(utilities)


def max_play(state):
    if state.is_terminal():
        return state.utility()

    utilities = []
    actions = state.actions(PIECE_X)
    for action in actions:
        # returning 1 early speeds up max
        _min = min_play(action)
        if _min == 1:
            return 1
        utilities.append(_min)

    return max(utilities)



main()