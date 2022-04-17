import naked
import util

candidate_board = []
# Solving order
# Naked: Singles, pairs, triples, quads
# Hidden: Singles, pairs, triples, quads (A hidden pair occurs when a pair of numbers appears in exactly two squares in a row, column, or block, but those two numbers aren't the only ones in their squares)
# Pointing: Pairs, Triples
# X-Wing Family: X-Wing, Swordfish, Jellyfish
# Forced Chains: XY-Wing, XYZ-Wing


def initialize_candidate_board():
    # this way copies references of objects, so changing one changes others
    # candidate_board = [set()] * 9
    # candidate_board = [candidate_board] * 9

    global candidate_board
    candidate_board = [[set() for i in range(9)] for i in range(9)]


def solve(board):
    initialize_candidate_board()

    fill_candidates_board(board)

    while naked.check_naked(board, candidate_board):
        pass

    print('######### Candidates list is ######### ')
    util.print_board(candidate_board)
    return board


def fill_candidates_board(board):
    print('######### Filling full candidate list ######### ')
    for row_no, row in enumerate(board):
        for col_no, cell in enumerate(row):
            if cell == 0:
                candidate_board[row_no][col_no] = util.find_candidate_list(board, row_no, col_no)
    print('######### Candidates list is ######### ')
    util.print_board(candidate_board)
