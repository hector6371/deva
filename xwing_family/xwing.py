import util


def check(board, candidate_board):
    #( two single candidates on parallel on different areas)
    print('######### Checking x-wing #########')
    found_any = False

    for row_index in range(0, 9):
        for col_index in range(0, 9):
            cell_candidates = candidate_board[row_index][col_index].copy()
            for candidate_value in cell_candidates:
                fourth_candidate_coordinates = search_right_square(candidate_board, candidate_value, row_index, col_index)
                if fourth_candidate_coordinates is not None:
                    exception_rows = {row_index, fourth_candidate_coordinates[0]}
                    if util.remove_candidate_from_col(candidate_board, {candidate_value}, col_index, exception_rows):
                        found_any = True
                    if util.remove_candidate_from_col(candidate_board, {candidate_value}, fourth_candidate_coordinates[1], exception_rows):
                        found_any = True

    return found_any


#  Search right
#  if found exactly 2 values in row, continue. Otherwise, discard
#  Look down on first column for the third possible value
#    - If found, check right for the cell in the square. If it has the value and, in this row are only two cells
#    with this value, found an xwing
#    - Otherwise, keep looking down and repeat previous step
def search_right_square(candidate_board, candidate_value, row_index, col_index):
    num_candidates_in_first_row = 1
    second_candidate_coordinates = None
    third_candidate_coordinates = None
    fourth_candidate_coordinates = None
    for matching_col_index in range(0, 9):
        cell = candidate_board[row_index][matching_col_index]

        if matching_col_index != col_index and candidate_value in cell:
            # count every candidate on row, but only use if one is on the right. (An x-wing on the left should have
            # been checked in a previous iteration)
            if matching_col_index > col_index:
                second_candidate_coordinates = (row_index, matching_col_index)
            num_candidates_in_first_row += 1
    if num_candidates_in_first_row != 2 or second_candidate_coordinates is None:  # could be None if this search is for the rightmost value
        return None
    else:
        for matching_row_index in range(row_index + 1, 9):
            cell = candidate_board[matching_row_index][col_index]
            if candidate_value in cell:
                # Possible third value, checking if there is a fourth value in square and only two values in row
                third_candidate_coordinates = (matching_row_index, col_index)
                if candidate_value in candidate_board[row_index][second_candidate_coordinates[1]]:
                    # Found square. Checking if only two values in bottom row
                    candidates_in_bottom_row = 0
                    for counting_col_index in range(0, 9):
                        if candidate_value in candidate_board[matching_row_index][counting_col_index]:
                            candidates_in_bottom_row += 1
                    if candidates_in_bottom_row == 2:
                        print(f'Found xwing square for value {candidate_value} '
                              f'in rows {row_index}, {matching_row_index} '
                              f'and cols {col_index}, {second_candidate_coordinates[1]}')
                        fourth_candidate_coordinates = (third_candidate_coordinates[0], second_candidate_coordinates[1])
                        break
        return fourth_candidate_coordinates
