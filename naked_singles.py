import naked


def check_singles(board, candidate_board):
    print('######### Checking naked singles #########')
    found_any = False
    for row_no, row in enumerate(candidate_board):
        for col_no, cell in enumerate(row):
            if len(cell) == 1:
                print(f'Found one naked single with value {cell} on ({row_no},{col_no})')
                board[row_no][col_no] = min(cell)  # retrieve the first element
                candidate_board[row_no][col_no] = set()
                naked.remove_candidates(candidate_board, cell, row_no, col_no)
                found_any = True
    return found_any
