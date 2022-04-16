def print_board(board):
    for row in board:
        print(row)  # Press Ctrl+8 to toggle the breakpoint.
    #print(f'Hi, {board}')  # Press Ctrl+8 to toggle the breakpoint.


def find_candidate_list(board, row_no, col_no):
    candidate_list = set(range(1, 10))
    candidate_list = remove_row_candidates(board, row_no, candidate_list)
    candidate_list = remove_col_candidates(board, col_no, candidate_list)
    candidate_list = remove_area_candidates(board, row_no, col_no, candidate_list)
    #print(f'Found {candidate_list} for {row_no}, {col_no}')
    return candidate_list


def remove_area_candidates(board, row_no, col_no, candidate_list):
    area_cells = get_area_cells(board, row_no, col_no)
    for cell in area_cells:
        try:
            candidate_list.remove(cell)
        except KeyError:
            pass
    return candidate_list


def remove_row_candidates(board, row_no, candidate_list):
    row = board[row_no]
    for cell in row:
        try:
            candidate_list.remove(cell)
        except KeyError:
            pass
    return candidate_list


def remove_col_candidates(board, col_no, candidate_list):
    col = [row[col_no] for row in board]
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
