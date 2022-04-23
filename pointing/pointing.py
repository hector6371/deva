import util


def check(board, candidate_board):
    print('######### Pointing pairs and triples #########')
    found_any = False

    for candidate_value in range(1, 10):
        for area in range(1, 10):
            rows_with_value, cols_with_value = search_value_in_area(candidate_board, candidate_value, area)
            if len(rows_with_value) == 1 and (len(cols_with_value) == 2 or len(cols_with_value) == 3):
                row_index = min(rows_with_value)
                if util.remove_candidate_from_row(candidate_board, {candidate_value}, row_index, cols_with_value):
                    print(f'Found pointing pair/triple with value {candidate_value} in row {row_index} and cols {cols_with_value}')
                    found_any = True
            elif len(cols_with_value) == 1 and (len(rows_with_value) == 2 or len(rows_with_value) == 3):
                col_index = min(cols_with_value)
                if util.remove_candidate_from_col(candidate_board, {candidate_value}, col_index, rows_with_value):
                    print(f'Found pointing pair/triple with value {candidate_value} in col {col_index} and rows {rows_with_value}')
                    found_any = True
    return found_any


def search_value_in_area(candidate_board, candidate_value, area):
    rows_with_value = set()
    cols_with_value = set()

    #1 -> 0,0
    #2 -> 0,3
    #3 -> 0,6
    #4 -> 3,0
    #5 -> 3,3
    #6 -> 3,6
    #7 -> 6,0
    #8 -> 6,3
    #9 -> 6,6
    # row (area) = round_down(area-1/3) * 3
    # col (area) = ((area-1)%3) * 3

    row_index = int((area-1)/3) * 3
    col_index = ((area-1) % 3) * 3

    next_index_pair = (row_index, col_index)

    while next_index_pair is not None:
        cell = candidate_board[next_index_pair[0]][next_index_pair[1]]
        if candidate_value in cell:
            rows_with_value.add(next_index_pair[0])
            cols_with_value.add(next_index_pair[1])
        next_index_pair = util.next_area_cell_indexes(next_index_pair[0], next_index_pair[1])

    return rows_with_value, cols_with_value
