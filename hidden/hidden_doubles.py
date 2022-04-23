import itertools

import util


def check(board, candidate_board):
    print('######### Checking hidden doubles #########')
    found_any = False

    if check_rows(board, candidate_board):
        found_any = True
    # if check_cols(board, candidate_board):
    #     found_any = True
    # if check_areas(board, candidate_board):
    #     found_any = True
    return found_any


def check_rows(board, candidate_board):
    found_any = False
    for row_index in range(0, 9):
        for col_index in range(0, 9):
            cell = candidate_board[row_index][col_index]
            if len(cell) >= 3:  # 0 is no candidates, 1 is insufficient, 2 could have single hidden or double naked
                for candidate_pair in itertools.combinations(cell, 2):
                    candidate_pair_set = set(candidate_pair)
                    count_repeated = 1
                    exception_cols = {col_index}
                    for searching_repeated_candidate_col_index in range(0, 9):
                        if searching_repeated_candidate_col_index != col_index:
                            possible_repeated_candidate_cell = candidate_board[row_index][searching_repeated_candidate_col_index]
                            if candidate_pair_set.issubset(possible_repeated_candidate_cell):
                                count_repeated += 1
                                exception_cols.add(searching_repeated_candidate_col_index)
                    if count_repeated == 2:
                        found_any = True
                        print(f'Found one hidden double with values {candidate_pair_set} on ({row_index},{col_index}) and ({row_index},{searching_repeated_candidate_col_index})')
                        for hidden_column_index in exception_cols:
                            candidate_board[row_index][hidden_column_index] = candidate_pair_set
                        util.remove_candidate_from_row(candidate_board, candidate_pair_set, row_index, exception_cols)
    return found_any
