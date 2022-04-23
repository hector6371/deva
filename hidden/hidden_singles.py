import util


def check(board, candidate_board):
    print('######### Checking hidden singles #########')
    found_any = False

    if check_rows(board, candidate_board):
        found_any = True
    if check_cols(board, candidate_board):
        found_any = True
    if check_areas(board, candidate_board):
        found_any = True
    return found_any


def check_rows(board, candidate_board):
    found_any = False
    for row_index in range(0, 9):
        for col_index in range(0, 9):
            cell = candidate_board[row_index][col_index]
            if len(cell) >= 2:  # 0 is no candidates and 1 is naked
                for candidate_value in cell:
                    is_repeated = False
                    for searching_repeated_candidate_col_index in range(0, 9):
                        if searching_repeated_candidate_col_index != col_index:
                            possible_repeated_candidate_cell = candidate_board[row_index][searching_repeated_candidate_col_index]
                            if candidate_value in possible_repeated_candidate_cell:
                                is_repeated = True
                    if not is_repeated:
                        found_any = True
                        print(f'Found one hidden single with value {candidate_value} on ({row_index},{col_index})')
                        board[row_index][col_index] = candidate_value
                        candidate_board[row_index][col_index] = set()
                        util.remove_candidates(candidate_board, {candidate_value}, row_index, col_index)
    return found_any


def check_cols(board, candidate_board):
    found_any = False
    for col_index in range(0, 9):
        for row_index in range(0, 9):
            cell = candidate_board[row_index][col_index]
            if len(cell) >= 2:  # 0 is no candidates and 1 is naked
                for candidate_value in cell:
                    is_repeated = False
                    for searching_repeated_candidate_row_index in range(0, 9):
                        if searching_repeated_candidate_row_index != row_index:
                            possible_repeated_candidate_cell = candidate_board[searching_repeated_candidate_row_index][col_index]
                            if candidate_value in possible_repeated_candidate_cell:
                                is_repeated = True
                    if not is_repeated:
                        found_any = True
                        print(f'Found one hidden single with value {candidate_value} on ({row_index},{col_index})')
                        board[row_index][col_index] = candidate_value
                        candidate_board[row_index][col_index] = set()
                        util.remove_candidates(candidate_board, {candidate_value}, row_index, col_index)
    return found_any


def check_areas(board, candidate_board):
    found_any = False
    for row_index in range(0, 9):
        for col_index in range(0, 9):
            cell = candidate_board[row_index][col_index]
            if len(cell) >= 2:  # 0 is no candidates and 1 is naked
                for candidate_value in cell:
                    is_repeated = False

                    next_index_pair = util.get_area_start_indexes(row_index, col_index)

                    while next_index_pair is not None:
                        possible_repeated_candidate_cell = candidate_board[next_index_pair[0]][next_index_pair[1]]
                        if candidate_value in possible_repeated_candidate_cell:
                            is_repeated = True
                        next_index_pair = util.next_area_cell_indexes(next_index_pair[0], next_index_pair[1])
                    if not is_repeated:
                        found_any = True
                        print(f'Found one hidden single with value {candidate_value} on ({row_index},{col_index})')
                        board[row_index][col_index] = candidate_value
                        candidate_board[row_index][col_index] = set()
                        util.remove_candidates(candidate_board, {candidate_value}, row_index, col_index)
    return found_any
