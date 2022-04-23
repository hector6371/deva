
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


def remove_candidates(candidate_board, candidate_value, row_no, col_no):
    remove_candidate_from_row(candidate_board, candidate_value, row_no)
    remove_candidate_from_col(candidate_board, candidate_value, col_no)
    remove_candidate_from_area(candidate_board, candidate_value, row_no, col_no)


def remove_candidate_from_row(candidate_board, candidates_values, row_no, exception_cols=None):
    removed_something = False
    if exception_cols is None:
        exception_cols = set()

    affected_row = candidate_board[row_no]
    for col_no, cell in enumerate(affected_row):
        if col_no not in exception_cols:
            for candidate_value in candidates_values:
                try:
                    cell.remove(candidate_value)
                    removed_something = True
                except KeyError:
                    pass
    return removed_something


def remove_candidate_from_col(candidate_board, candidates_values, col_no, exception_rows=None):
    removed_something = False
    if exception_rows is None:
        exception_rows = set()

    affected_col = [row[col_no] for row in candidate_board]
    for row_no, cell in enumerate(affected_col):
        if row_no not in exception_rows:
            for candidate_value in candidates_values:
                try:
                    cell.remove(candidate_value)
                    removed_something = True
                except KeyError:
                    pass
    return removed_something


def remove_candidate_from_area(candidate_board, candidates_value, row_no, col_no, exception_pairs=None):
    removed_something = False
    if exception_pairs is None:
        exception_pairs = set()

    area_row_start = row_no - (row_no % 3)
    area_col_start = col_no - (col_no % 3)

    for row_index in range(area_row_start, area_row_start + 3):
        for col_index in range(area_col_start, area_col_start + 3):
            if (row_index, col_index) not in exception_pairs:
                for candidate_value in candidates_value:
                    try:
                        candidate_board[row_index][col_index].remove(candidate_value)
                        removed_something = True
                    except KeyError:
                        pass
    return removed_something


def get_area_cells(board, row_no, col_no):
    area_row_start = row_no - (row_no % 3)
    area_col_start = col_no - (col_no % 3)

    area_cells = set()
    for row_index in range(area_row_start, area_row_start + 3):
        for col_index in range (area_col_start, area_col_start + 3):
            area_cells.add(board[row_index][col_index])

    return area_cells


def get_area_start_indexes(current_row_index, current_col_index):
    area_row_start = current_row_index - (current_row_index % 3)
    area_col_start = current_col_index - (current_col_index % 3)
    return area_row_start, area_col_start


def next_area_cell_indexes(current_row_index, current_col_index):
    area_row_start, area_col_start = get_area_start_indexes(current_row_index, current_col_index)
    area_row_end = min(3 + area_row_start, 9)
    area_col_end = min(3 + area_col_start, 9)

    next_area_cell_row_index = current_row_index
    next_area_cell_col_index = current_col_index + 1

    if next_area_cell_col_index >= area_col_end:
        next_area_cell_row_index = current_row_index + 1
        next_area_cell_col_index = area_col_start

    if next_area_cell_row_index >= area_row_end:
        return None

    return next_area_cell_row_index, next_area_cell_col_index
