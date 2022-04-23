import numpy as np
import numpy as numpy

import naked
import util


def check_doubles(board, candidate_board):
    print('######### Checking naked doubles #########')
    found_any = False

    if check_doubles_in_rows(candidate_board):
        found_any = True
    if check_doubles_in_cols(candidate_board):
        found_any = True
    if check_doubles_in_areas(candidate_board):
        found_any = True
    return found_any


def check_doubles_in_rows(candidate_board):
    found_any = False
    for row_no, row in enumerate(candidate_board):
        for col_no, cell in enumerate(row):
            if len(cell) == 2:
                print(f'Possible naked pair with values {cell} on ({row_no},{col_no})')

                for pairing_candidate_col_no, pairing_candidate_cell in enumerate(row):
                    if len(pairing_candidate_cell) == 2 and pairing_candidate_col_no != col_no and pairing_candidate_cell == cell:
                        print(f'Found naked pair with values {cell} on ({row_no},{col_no}) and ({row_no},{pairing_candidate_col_no})')
                        exception_cols = {col_no, pairing_candidate_col_no}
                        if util.remove_candidate_from_row(candidate_board, cell.copy(), row_no, exception_cols):
                            found_any = True
    return found_any


def check_doubles_in_cols(candidate_board):
    found_any = False

    for col_no in range(0, 9):
        current_col = [row[col_no] for row in candidate_board]
        for row_no, cell in enumerate(current_col):
            if len(cell) == 2:
                print(f'Possible naked pair with values {cell} on ({row_no},{col_no})')

                for pairing_candidate_row_no, pairing_candidate_cell in enumerate(current_col):
                    if len(pairing_candidate_cell) == 2 and pairing_candidate_row_no != row_no and pairing_candidate_cell == cell:
                        print(
                            f'Found naked pair with values {cell} on ({row_no},{col_no}) and ({row_no},{pairing_candidate_row_no})')
                        exception_cols = {row_no, pairing_candidate_row_no}
                        if util.remove_candidate_from_col(candidate_board, cell.copy(), col_no, exception_cols):
                            found_any = True
    return found_any


def check_doubles_in_areas(candidate_board):
    found_any = False

    for row_no, row in enumerate(candidate_board):
        for col_no, cell in enumerate(row):
            if len(cell) == 2:
                print(f'Possible naked pair with values {cell} on ({row_no},{col_no})')

                area_row_start = row_no - (row_no % 3)
                area_col_start = col_no - (col_no % 3)

                for row_index in range(area_row_start, area_row_start + 3):
                    for col_index in range(area_col_start, area_col_start + 3):
                        try:
                            pairing_candidate_cell = candidate_board[row_index][col_index]
                            if len(pairing_candidate_cell) == 2 and (col_index != col_no or row_index != row_no) and pairing_candidate_cell == cell:
                                print(f'Found naked pair with values {cell} on ({row_no},{col_no}) and ({row_index},{col_index})')
                                exception_pairs = {(row_no, col_no), (row_index, col_index)}
                                if util.remove_candidate_from_area(candidate_board, cell.copy(), row_no, col_no, exception_pairs):
                                    found_any = True
                        except KeyError:
                            pass
    return found_any
