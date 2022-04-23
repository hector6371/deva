import util
from naked import naked


def check_triples(board, candidate_board):
    print('######### Checking naked triples #########')
    found_any = False

    if check_triples_in_rows(candidate_board):
        found_any = True
    if check_triples_in_cols(candidate_board):
        found_any = True
    if check_triples_in_areas(candidate_board):
        found_any = True
    return found_any


def check_triples_in_rows(candidate_board):
    found_any = False
    for first_candidate_row_index, row in enumerate(candidate_board):
        for first_candidate_col_index, first_candidate_cell in enumerate(row):

            # For each cell
            if len(first_candidate_cell) == 2 or (len(first_candidate_cell) == 3):
                print(f'Possible naked triple with values {first_candidate_cell} on ({first_candidate_row_index},{first_candidate_col_index})')

                # Iterate on the rest of the row
                for second_candidate_col_index in range(first_candidate_col_index + 1, 9):
                    second_candidate_cell = candidate_board[first_candidate_row_index][second_candidate_col_index]
                    if (len(second_candidate_cell) == 2 or len(second_candidate_cell) == 3) \
                            and second_candidate_col_index != first_candidate_col_index:
                        two_candidates_sum_values = set.union(second_candidate_cell, first_candidate_cell)
                        if len(two_candidates_sum_values) == 3:
                            print(f'Found pair for possible triple with values {first_candidate_cell} on ({first_candidate_row_index},{first_candidate_col_index}) and {second_candidate_cell} on ({first_candidate_row_index},{second_candidate_col_index})')

                            # Search the remaining cells on the row for the third match
                            for third_candidate_col_index in range(second_candidate_col_index + 1, 9):
                                third_candidate_cell = candidate_board[first_candidate_row_index][third_candidate_col_index]
                                if len(third_candidate_cell) == 2 or len(third_candidate_cell) == 3:
                                    three_candidates_sum_values = set.union(third_candidate_cell, two_candidates_sum_values)
                                    if len(three_candidates_sum_values) == 3:
                                        print(f'Found naked triple with values {first_candidate_cell} on ({first_candidate_row_index},{first_candidate_col_index}), '
                                              f' and {second_candidate_cell} on ({first_candidate_row_index},{second_candidate_col_index})'
                                              f' and {third_candidate_cell} on ({first_candidate_row_index},{third_candidate_col_index})')
                                        exception_cols = {first_candidate_col_index, second_candidate_col_index, third_candidate_col_index}
                                        if util.remove_candidate_from_row(candidate_board, three_candidates_sum_values, first_candidate_row_index, exception_cols):
                                            found_any = True
    return found_any


def check_triples_in_cols(candidate_board):
    found_any = False
    for first_candidate_row_index, row in enumerate(candidate_board):
        for first_candidate_col_index, first_candidate_cell in enumerate(row):

            # For each cell
            if len(first_candidate_cell) == 2 or (len(first_candidate_cell) == 3):
                print(f'Possible naked triple with values {first_candidate_cell} on ({first_candidate_row_index},{first_candidate_col_index})')

                # Iterate on the rest of the col
                for second_candidate_row_index in range(first_candidate_row_index + 1, 9):
                    second_candidate_cell = candidate_board[second_candidate_row_index][first_candidate_col_index]
                    if (len(second_candidate_cell) == 2 or len(second_candidate_cell) == 3) \
                            and second_candidate_row_index != first_candidate_row_index:
                        two_candidates_sum_values = set.union(second_candidate_cell, first_candidate_cell)
                        if len(two_candidates_sum_values) == 3:
                            print(f'Found pair for possible triple with values {first_candidate_cell} on ({first_candidate_row_index},{first_candidate_col_index}) and {second_candidate_cell} on ({second_candidate_row_index},{first_candidate_col_index})')

                            # Search the remaining cells on the col for the third match
                            for third_candidate_row_index in range(second_candidate_row_index + 1, 9):
                                third_candidate_cell = candidate_board[third_candidate_row_index][first_candidate_col_index]
                                if len(third_candidate_cell) == 2 or len(third_candidate_cell) == 3:
                                    three_candidates_sum_values = set.union(third_candidate_cell, two_candidates_sum_values)
                                    if len(three_candidates_sum_values) == 3:
                                        print(f'Found naked triple with values {first_candidate_cell} on ({first_candidate_row_index},{first_candidate_col_index}), '
                                              f' and {second_candidate_cell} on ({second_candidate_row_index},{first_candidate_col_index})'
                                              f' and {third_candidate_cell} on ({third_candidate_row_index},{first_candidate_col_index})')
                                        exception_rows = {first_candidate_row_index, second_candidate_row_index, third_candidate_row_index}
                                        if util.remove_candidate_from_col(candidate_board, three_candidates_sum_values, first_candidate_col_index, exception_rows):
                                            found_any = True
    return found_any


def check_triples_in_areas(candidate_board):
    found_any = False
    for first_candidate_row_index, row in enumerate(candidate_board):
        for first_candidate_col_index, first_candidate_cell in enumerate(row):

            # For each cell
            if len(first_candidate_cell) == 2 or (len(first_candidate_cell) == 3):
                print(f'Possible naked triple with values {first_candidate_cell} on ({first_candidate_row_index},{first_candidate_col_index})')

                # Iterate on the whole area
                area_row_start = first_candidate_row_index - (first_candidate_row_index % 3)
                area_row_end = min(3 + area_row_start, 9)
                area_col_start = first_candidate_col_index - (first_candidate_col_index % 3)
                area_col_end = min(3 + area_col_start, 9)
                for second_candidate_row_index in range(area_row_start, area_row_end):
                    for second_candidate_col_index in range(area_col_start, area_col_end):
                        if second_candidate_row_index != first_candidate_row_index or second_candidate_col_index != first_candidate_col_index:
                            second_candidate_cell = candidate_board[second_candidate_row_index][second_candidate_col_index]
                            if len(second_candidate_cell) == 2 or len(second_candidate_cell) == 3:
                                two_candidates_sum_values = set.union(second_candidate_cell, first_candidate_cell)
                                if len(two_candidates_sum_values) == 3:
                                    print(f'Found pair for possible triple with values {first_candidate_cell} on ({first_candidate_row_index},{first_candidate_col_index}) and {second_candidate_cell} on ({second_candidate_row_index},{second_candidate_col_index})')

                                    # Search the cells on the area for the third match
                                    for third_candidate_row_index in range(area_row_start, area_row_end):
                                        for third_candidate_col_index in range(area_col_start, area_col_end):
                                            if (third_candidate_row_index != first_candidate_row_index or third_candidate_col_index != first_candidate_col_index) \
                                                and (third_candidate_row_index != second_candidate_row_index or third_candidate_col_index != second_candidate_col_index):
                                                third_candidate_cell = candidate_board[third_candidate_row_index][third_candidate_col_index]
                                                if len(third_candidate_cell) == 2 or len(third_candidate_cell) == 3:
                                                    three_candidates_sum_values = set.union(third_candidate_cell, two_candidates_sum_values)
                                                    if len(three_candidates_sum_values) == 3:
                                                        print(f'Found naked triple with values {first_candidate_cell} on ({first_candidate_row_index},{first_candidate_col_index}), '
                                                              f' and {second_candidate_cell} on ({second_candidate_row_index},{second_candidate_col_index})'
                                                              f' and {third_candidate_cell} on ({third_candidate_row_index},{third_candidate_col_index})')
                                                        exception_pairs = {(first_candidate_row_index, first_candidate_col_index),
                                                                           (second_candidate_row_index, second_candidate_col_index),
                                                                           (third_candidate_row_index, third_candidate_col_index)}
                                                        if util.remove_candidate_from_area(candidate_board, three_candidates_sum_values, first_candidate_row_index, first_candidate_col_index, exception_pairs):
                                                            found_any = True
    return found_any

