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


def remove_candidate_from_col(candidate_value, col_no):
    col = [row[col_no] for row in candidate_board]
    for cell in col:
        try:
            cell.remove(candidate_value)
        except KeyError:
            pass


def remove_candidate_from_area(candidate_value, row_no, col_no):
    area_row_start = row_no - (row_no % 3)
    area_col_start = col_no - (col_no % 3)

    for row_index in range(area_row_start, area_row_start + 3):
        for col_index in range(area_col_start, area_col_start + 3):
            try:
                candidate_board[row_index][col_index].remove(candidate_value)
            except KeyError:
                pass


def remove_candidates(candidate_value, row_no, col_no):
    remove_candidate_from_row(candidate_value, row_no)
    remove_candidate_from_col(candidate_value, col_no)
    remove_candidate_from_area(candidate_value, row_no, col_no)


def remove_candidate_from_row(candidate_value, row_no):
    affected_row = candidate_board[row_no]
    for cell in affected_row:
        try:
            cell.remove(candidate_value)
        except KeyError:
            pass


def check_naked_single(board):
    print('######### Checking naked singles #########')
    found_any = False
    for row_no, row in enumerate(candidate_board):
        for col_no, cell in enumerate(row):
            if len(cell) == 1:
                print(f'Found one naked single with value {cell} on ({row_no},{col_no})')
                board[row_no][col_no] = min(cell)  # retrieve the first element
                candidate_board[row_no][col_no] = set()
                remove_candidates(min(cell), row_no, col_no)
                found_any = True
    return found_any


def solve(board):
    initialize_candidate_board()

    fill_candidates_board(board)

    while check_naked_single(board):
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
