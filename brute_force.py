import util


def solve_brute_force(board):
    found = find_empty(board)
    if not found:
        return True
    else:
        empty_cell_row, empty_cell_col = found

    candidate_list = util.find_candidate_list(board, empty_cell_row, empty_cell_col)
    if len(candidate_list) == 0:
        return False
    for candidate in candidate_list:
        print(f'Guessing if value {candidate} in cell ({empty_cell_row},{empty_cell_col})')
        board[empty_cell_row][empty_cell_col] = candidate
        if solve_brute_force(board):
            print(f'Found value {candidate} in cell ({empty_cell_row},{empty_cell_col})')
            return True
        else:
            print(f'Discarded value {candidate} in cell ({empty_cell_row},{empty_cell_col})')
            continue
    board[empty_cell_row][empty_cell_col] = 0
    return False #No candidates are valid


def find_empty(board):
    for row_no, row in enumerate(board):
        for col_no, cell in enumerate(row):
            if cell == 0:
                return (row_no, col_no)
    return None


