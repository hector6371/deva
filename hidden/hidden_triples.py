import itertools

import util


def check(board, candidate_board):
    print('######### Checking hidden triples #########')
    found_any = False

    if check_in_rows(board, candidate_board):
        found_any = True
    if check_in_cols(board, candidate_board):
        found_any = True
    if check_in_areas(board, candidate_board):
        found_any = True
    return found_any


def check_in_rows(board, candidate_board):
    found_any = False
    for row_index in range(0, 9):
        for col_index in range(0, 9):
            cell_candidates = candidate_board[row_index][col_index].copy()
            # 0 is no candidates,
            # 1 is insufficient,
            # 2 could have single hidden or double naked
            # 3 could have double hidden or triple naked
            if len(cell_candidates) >= 4:
                for candidate_threesome in itertools.combinations(cell_candidates, 3):
                    candidate_threesome_set = set(candidate_threesome)
                    count_repeated = 1
                    exception_cols = {col_index}
                    for searching_repeated_candidate_col_index in range(0, 9):
                        if searching_repeated_candidate_col_index != col_index:
                            possible_repeated_candidate_cell = candidate_board[row_index][searching_repeated_candidate_col_index]
                            if not candidate_threesome_set.isdisjoint(possible_repeated_candidate_cell):
                                count_repeated += 1
                                exception_cols.add(searching_repeated_candidate_col_index)
                    if count_repeated == 3:
                        found_any = True
                        print(f'Found one hidden triple with values {candidate_threesome_set} on row ({row_index} and cols {exception_cols})')
                        for hidden_column_index in exception_cols:
                            candidate_board[row_index][hidden_column_index] = candidate_threesome_set.copy()
                        util.remove_candidate_from_row(candidate_board, candidate_threesome_set, row_index, exception_cols)
    return found_any


def check_in_cols(board, candidate_board):
    found_any = False
    for row_index in range(0, 9):
        for col_index in range(0, 9):
            cell_candidates = candidate_board[row_index][col_index].copy()
            # 0 is no candidates,
            # 1 is insufficient,
            # 2 could have single hidden or double naked
            # 3 could have double hidden or triple naked
            if len(cell_candidates) >= 4:
                for candidate_threesome in itertools.combinations(cell_candidates, 3):
                    candidate_threesome_set = set(candidate_threesome)
                    count_repeated = 1
                    exception_rows = {row_index}
                    for searching_repeated_candidate_row_index in range(0, 9):
                        if searching_repeated_candidate_row_index != row_index:
                            possible_repeated_candidate_cell = candidate_board[searching_repeated_candidate_row_index][col_index]
                            if not candidate_threesome_set.isdisjoint(possible_repeated_candidate_cell):
                                count_repeated += 1
                                exception_rows.add(searching_repeated_candidate_row_index)
                    if count_repeated == 3:
                        found_any = True
                        print(f'Found one hidden triple with values {candidate_threesome_set} on rows ({exception_rows} and col {col_index})')
                        for hidden_row_index in exception_rows:
                            candidate_board[hidden_row_index][col_index] = candidate_threesome_set.copy()
                        util.remove_candidate_from_col(candidate_board, candidate_threesome_set, col_index, exception_rows)
    return found_any


def check_in_areas(board, candidate_board):
    found_any = False
    for row_index in range(0, 9):
        for col_index in range(0, 9):
            cell_candidates = candidate_board[row_index][col_index].copy()
            # 0 is no candidates,
            # 1 is insufficient,
            # 2 could have single hidden or double naked
            # 3 could have double hidden or triple naked
            if len(cell_candidates) >= 4:
                for candidate_threesome in itertools.combinations(cell_candidates, 3):
                    candidate_threesome_set = set(candidate_threesome)
                    count_repeated = 1
                    exception_pairs = {(row_index, col_index)}

                    next_index_pair = util.get_area_start_indexes(row_index, col_index)

                    while next_index_pair is not None:
                        possible_repeated_candidate_cell = candidate_board[next_index_pair[0]][next_index_pair[1]]
                        if next_index_pair != (row_index, col_index):
                            if not candidate_threesome_set.isdisjoint(possible_repeated_candidate_cell):
                                count_repeated += 1
                                exception_pairs.add(next_index_pair)
                        next_index_pair = util.next_area_cell_indexes(next_index_pair[0], next_index_pair[1])

                    if count_repeated == 3:
                        found_any = True
                        print(f'Found one hidden triple with values {candidate_threesome_set} on {exception_pairs}')
                        for hidden_pair in exception_pairs:
                            candidate_board[hidden_pair[0]][hidden_pair[1]] = candidate_threesome_set.copy()
                        util.remove_candidate_from_area(candidate_board, candidate_threesome_set, row_index, col_index, exception_pairs)
    return found_any