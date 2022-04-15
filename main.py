def print_board(board):
    for row in board:
        print(row)  # Press Ctrl+8 to toggle the breakpoint.
    #print(f'Hi, {board}')  # Press Ctrl+8 to toggle the breakpoint.


def create_board():
    #board = [None] * 9
    #board = [board] * 9
    board = [[0, 0, 3, 7, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 4, 3, 2, 0],
             [9, 2, 0, 0, 0, 0, 5, 0, 4],
             [7, 3, 0, 4, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 2, 0, 0, 5],
             [6, 0, 2, 1, 0, 9, 0, 0, 0],
             [2, 0, 4, 0, 3, 8, 1, 5, 7],
             [8, 7, 9, 0, 4, 1, 2, 6, 0],
             [0, 0, 0, 0, 6, 7, 0, 0, 9]]
    # board = [[8, 2, 7, 1, 5, 4, 3, 9, 6],
    #          [9, 6, 5, 3, 2, 7, 1, 4, 8],
    #          [3, 4, 1, 6, 8, 9, 7, 5, 2],
    #          [5, 9, 3, 4, 6, 8, 2, 7, 1],
    #          [4, 7, 2, 5, 1, 3, 6, 8, 9],
    #          [6, 1, 8, 9, 7, 2, 4, 3, 5],
    #          [7, 8, 6, 2, 3, 5, 9, 1, 4],
    #          [1, 5, 4, 7, 9, 6, 8, 2, 3],
    #          [2, 3, 9, 8, 4, 1, 5, 6, 7]]
    # board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
    #          [0, 6, 5, 3, 2, 7, 1, 4, 0],
    #          [0, 4, 1, 6, 8, 9, 7, 0, 2],
    #          [5, 9, 3, 4, 6, 8, 0, 7, 1],
    #          [4, 7, 2, 5, 1, 0, 6, 8, 9],
    #          [6, 1, 8, 9, 0, 0, 0, 0, 0],
    #          [7, 8, 6, 0, 3, 5, 9, 1, 4],
    #          [1, 5, 0, 7, 9, 6, 8, 2, 3],
    #          [2, 0, 9, 8, 4, 1, 5, 6, 7]]
    return board


# def check_singles_in_row(row):
#     candidate_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     for cell in row:
#         if cell != 0:
#             candidate_list.remove(cell)
#             print(f'Removed {cell} from candidates, which are now: {candidate_list}')
#     if len(candidate_list) == 1:
#         for cell in row:
#             if cell == 0:
#                 cell = candidate_list[0]
#                 print(f'Found single candidate {candidate_list[0]} in row. row is now: {row}')
#
#
# def check_singles(board):
#     for row in board:
#         check_singles_in_row(row)
#     pass


def remove_row_candidates(board, row_no, candidate_list):
    row = board[row_no]
    #print(row)
    for cell in row:
        try:
            candidate_list.remove(cell)
        except KeyError:
            pass
    return candidate_list


def remove_col_candidates(board, col_no, candidate_list):
    col = [row[col_no] for row in board]
    #print(col)
    for cell in col:
        try:
            candidate_list.remove(cell)
        except KeyError:
            pass
    return candidate_list


def get_area_cells(board, row_no, col_no):
    area_row_start = row_no - (row_no % 3)
    area_col_start = col_no - (col_no % 3)

    area_cells = set()
    for row_index in range(area_row_start, area_row_start + 3):
        for col_index in range (area_col_start, area_col_start + 3):
            area_cells.add(board[row_index][col_index])

    return area_cells

def remove_area_candidates(board, row_no, col_no, candidate_list):
    area_cells = get_area_cells(board, row_no, col_no)
    for cell in area_cells:
        try:
            candidate_list.remove(cell)
        except KeyError:
            pass
    return candidate_list


def find_candidate_list(board, row_no, col_no):
    candidate_list = set(range(1, 10))
    candidate_list = remove_row_candidates(board, row_no, candidate_list)
    candidate_list = remove_col_candidates(board, col_no, candidate_list)
    candidate_list = remove_area_candidates(board, row_no, col_no, candidate_list)
    print(f'Found {candidate_list} for {row_no}, {col_no}')
    return candidate_list


def find_empty(board):
    for row_no, row in enumerate(board):
        for col_no, cell in enumerate(row):
            if cell == 0:
                return (row_no, col_no)
    return None


def solve_brute_force(board):
    found = find_empty(board)
    if not found:
        return True
    else:
        empty_cell_row, empty_cell_col = found

    candidate_list = find_candidate_list(board, empty_cell_row, empty_cell_col)
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


if __name__ == '__main__':
    board = create_board()
    print('initial board is:')
    print_board(board)

    solve_brute_force(board)

    print('final board is:')
    print_board(board)
    #check_singles(board)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
