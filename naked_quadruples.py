import naked


def check_quadruples(board, candidate_board):
    print('######### Checking naked quadruples #########')
    found_any = False

    if check_quadruples_in_rows(candidate_board):
        found_any = True
    if check_quadruples_in_cols(candidate_board):
        found_any = True
    if check_quadruples_in_areas(candidate_board):
        found_any = True
    return found_any


def check_quadruples_in_rows(candidate_board):
    found_any = False
    for first_candidate_row_index, row in enumerate(candidate_board):
        for first_candidate_col_index, first_candidate_cell in enumerate(row):

            # For each cell
            if len(first_candidate_cell) >= 2 and (len(first_candidate_cell) <= 4):
                print(f'Possible naked quadruple with values {first_candidate_cell} on ({first_candidate_row_index},{first_candidate_col_index})')

                # Iterate on the rest of the row
                for second_candidate_col_index in range(first_candidate_col_index + 1, 9):
                    second_candidate_cell = candidate_board[first_candidate_row_index][second_candidate_col_index]
                    if len(second_candidate_cell) >= 2 and (len(second_candidate_cell) <= 4):
                        two_candidates_sum_values = set.union(second_candidate_cell, first_candidate_cell)
                        if len(two_candidates_sum_values) == 3 or len(two_candidates_sum_values) == 4:
                            print(f'Found pair for possible quadruple with values {first_candidate_cell} on ({first_candidate_row_index},{first_candidate_col_index}) and {second_candidate_cell} on ({first_candidate_row_index},{second_candidate_col_index})')

                            # Search the remaining cells on the row for the third match
                            for third_candidate_col_index in range(second_candidate_col_index + 1, 9):
                                third_candidate_cell = candidate_board[first_candidate_row_index][third_candidate_col_index]
                                if len(third_candidate_cell) >= 2 and (len(third_candidate_cell) <= 4):
                                    three_candidates_sum_values = set.union(third_candidate_cell, two_candidates_sum_values)
                                    if len(three_candidates_sum_values) == 4:

                                        print(f'Found triple for possible quadruple with values {first_candidate_cell} on ({first_candidate_row_index},{first_candidate_col_index}), '
                                              f' and {second_candidate_cell} on ({first_candidate_row_index},{second_candidate_col_index})'
                                              f' and {third_candidate_cell} on ({first_candidate_row_index},{third_candidate_col_index})')

                                        # Search the remaining cells on the row for the fourth match
                                        for fourth_candidate_col_index in range(third_candidate_col_index + 1, 9):
                                            fourth_candidate_cell = candidate_board[first_candidate_row_index][fourth_candidate_col_index]
                                            if len(fourth_candidate_cell) >= 2 and (len(fourth_candidate_cell) <= 4):
                                                four_candidates_sum_values = set.union(fourth_candidate_cell, three_candidates_sum_values)
                                                if len(four_candidates_sum_values) == 4:
                                                    print(
                                                        f'Found naked quadruple with values {first_candidate_cell} on ({first_candidate_row_index},{first_candidate_col_index}), '
                                                        f' and {second_candidate_cell} on ({first_candidate_row_index},{second_candidate_col_index})'
                                                        f' and {third_candidate_cell} on ({first_candidate_row_index},{third_candidate_col_index})'
                                                        f' and {fourth_candidate_cell} on ({first_candidate_row_index},{fourth_candidate_col_index})')
                                                    exception_cols = {first_candidate_col_index, second_candidate_col_index, third_candidate_col_index, fourth_candidate_col_index}
                                                    if naked.remove_candidate_from_row(candidate_board, four_candidates_sum_values, first_candidate_row_index, exception_cols):
                                                        found_any = True
    return found_any


def check_quadruples_in_cols(candidate_board):
    found_any = False
    for first_candidate_row_index, row in enumerate(candidate_board):
        for first_candidate_col_index, first_candidate_cell in enumerate(row):

            # For each cell
            if len(first_candidate_cell) >= 2 and (len(first_candidate_cell) <= 4):
                print(f'Possible naked quadruple with values {first_candidate_cell} on ({first_candidate_row_index},{first_candidate_col_index})')

                # Iterate on the rest of the col
                for second_candidate_row_index in range(first_candidate_row_index + 1, 9):
                    second_candidate_cell = candidate_board[second_candidate_row_index][first_candidate_col_index]
                    if len(second_candidate_cell) >= 2 and (len(second_candidate_cell) <= 4):
                        two_candidates_sum_values = set.union(second_candidate_cell, first_candidate_cell)
                        if len(two_candidates_sum_values) == 3 or len(two_candidates_sum_values) == 4:
                            print(f'Found pair for possible quadruple with values {first_candidate_cell} on ({first_candidate_row_index},{first_candidate_col_index}) and {second_candidate_cell} on ({second_candidate_row_index},{first_candidate_col_index})')

                            # Search the remaining cells on the row for the third match
                            for third_candidate_row_index in range(second_candidate_row_index + 1, 9):
                                third_candidate_cell = candidate_board[third_candidate_row_index][first_candidate_col_index]
                                if len(third_candidate_cell) >= 2 and (len(third_candidate_cell) <= 4):
                                    three_candidates_sum_values = set.union(third_candidate_cell, two_candidates_sum_values)
                                    if len(three_candidates_sum_values) == 4:

                                        print(f'Found triple for possible quadruple with values {first_candidate_cell} on ({first_candidate_row_index},{first_candidate_col_index}), '
                                              f' and {second_candidate_cell} on ({second_candidate_row_index},{first_candidate_col_index})'
                                              f' and {third_candidate_cell} on ({third_candidate_row_index},{first_candidate_col_index})')

                                        # Search the remaining cells on the col for the fourth match
                                        for fourth_candidate_row_index in range(third_candidate_row_index + 1, 9):
                                            fourth_candidate_cell = candidate_board[fourth_candidate_row_index][first_candidate_col_index]
                                            if len(fourth_candidate_cell) >= 2 and (len(fourth_candidate_cell) <= 4):
                                                four_candidates_sum_values = set.union(fourth_candidate_cell, three_candidates_sum_values)
                                                if len(four_candidates_sum_values) == 4:
                                                    print(
                                                        f'Found naked quadruple with values {first_candidate_cell} on ({first_candidate_row_index},{first_candidate_col_index}), '
                                                        f' and {second_candidate_cell} on ({second_candidate_row_index},{first_candidate_col_index})'
                                                        f' and {third_candidate_cell} on ({third_candidate_row_index},{first_candidate_col_index})'
                                                        f' and {fourth_candidate_cell} on ({fourth_candidate_row_index},{first_candidate_col_index})')
                                                    exception_rows = {first_candidate_row_index, second_candidate_row_index, third_candidate_row_index, fourth_candidate_row_index}
                                                    if naked.remove_candidate_from_col(candidate_board, four_candidates_sum_values, first_candidate_col_index, exception_rows):
                                                        found_any = True
    return found_any


def check_quadruples_in_areas(candidate_board):
    found_any = False
    for first_candidate_row_index, row in enumerate(candidate_board):
        for first_candidate_col_index, first_candidate_cell in enumerate(row):

            # For each cell
            if len(first_candidate_cell) >= 2 and (len(first_candidate_cell) <= 4):
                print(f'Possible naked quadruple with values {first_candidate_cell} on ({first_candidate_row_index},{first_candidate_col_index})')

                # Iterate on the whole area
                area_row_start = first_candidate_row_index - (first_candidate_row_index % 3)
                area_row_end = min(3 + area_row_start, 9)
                area_col_start = first_candidate_col_index - (first_candidate_col_index % 3)
                area_col_end = min(3 + area_col_start, 9)
                for second_candidate_row_index in range(area_row_start, area_row_end):
                    for second_candidate_col_index in range(area_col_start, area_col_end):
                        if second_candidate_row_index != first_candidate_row_index or second_candidate_col_index != first_candidate_col_index:
                            second_candidate_cell = candidate_board[second_candidate_row_index][second_candidate_col_index]
                            if len(second_candidate_cell) >= 2 or len(second_candidate_cell) <= 4:
                                two_candidates_sum_values = set.union(second_candidate_cell, first_candidate_cell)
                                if len(two_candidates_sum_values) == 3 or len(two_candidates_sum_values) == 4:
                                    print(f'Found pair for possible quadruple with values {first_candidate_cell} on ({first_candidate_row_index},{first_candidate_col_index}) and {second_candidate_cell} on ({second_candidate_row_index},{second_candidate_col_index})')

                                    # Search the cells on the area for the third match
                                    for third_candidate_row_index in range(area_row_start, area_row_end):
                                        for third_candidate_col_index in range(area_col_end, area_col_end):
                                            if (third_candidate_row_index != first_candidate_row_index or third_candidate_col_index != first_candidate_col_index) \
                                                and (third_candidate_row_index != second_candidate_row_index or third_candidate_col_index != second_candidate_col_index):
                                                third_candidate_cell = candidate_board[third_candidate_row_index][third_candidate_col_index]
                                                if len(third_candidate_cell) >= 2 or len(third_candidate_cell) <= 4:
                                                    three_candidates_sum_values = set.union(third_candidate_cell, two_candidates_sum_values)
                                                    if len(three_candidates_sum_values) == 4:
                                                        print(f'Found threesome for possible quadruple with values {first_candidate_cell} on ({first_candidate_row_index},{first_candidate_col_index}), '
                                                              f' and {second_candidate_cell} on ({second_candidate_row_index},{second_candidate_col_index})'
                                                              f' and {third_candidate_cell} on ({third_candidate_row_index},{third_candidate_col_index})')

                                                        # Search the remaining cells on the area for the fourth match
                                                        for fourth_candidate_row_index in range(third_candidate_row_index + 1, area_row_end):
                                                            for fourth_candidate_col_index in range(third_candidate_col_index, area_col_end):
                                                                fourth_candidate_cell = candidate_board[fourth_candidate_row_index][fourth_candidate_col_index]
                                                                if (fourth_candidate_row_index != first_candidate_row_index or fourth_candidate_col_index != first_candidate_col_index) \
                                                                    and (fourth_candidate_row_index != second_candidate_row_index or fourth_candidate_col_index != second_candidate_col_index)\
                                                                    and (fourth_candidate_row_index != third_candidate_row_index or fourth_candidate_col_index != third_candidate_col_index):
                                                                    if len(fourth_candidate_cell) >= 2 or len(fourth_candidate_cell) <= 4:
                                                                        four_candidates_sum_values = set.union(fourth_candidate_cell, three_candidates_sum_values)
                                                                        if len(four_candidates_sum_values) == 4:
                                                                            print(
                                                                                f'Found naked quadruple with values {first_candidate_cell} on ({first_candidate_row_index},{first_candidate_col_index}), '
                                                                                f' and {second_candidate_cell} on ({second_candidate_row_index},{second_candidate_col_index})'
                                                                                f' and {third_candidate_cell} on ({third_candidate_row_index},{third_candidate_col_index})'
                                                                                f' and {fourth_candidate_cell} on ({fourth_candidate_row_index},{fourth_candidate_col_index})')

                                                                        exception_pairs = {(first_candidate_row_index, first_candidate_col_index),
                                                                                           (second_candidate_row_index, second_candidate_col_index),
                                                                                           (third_candidate_row_index, third_candidate_col_index),
                                                                                           (fourth_candidate_row_index, fourth_candidate_col_index)}
                                                                        if naked.remove_candidate_from_area(candidate_board, four_candidates_sum_values, first_candidate_row_index, first_candidate_col_index, exception_pairs):
                                                                            found_any = True
    return found_any

