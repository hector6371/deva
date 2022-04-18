import naked_doubles
import naked_quadruples
import naked_singles
import naked_triples
import util


# Naked is where, in a row, col or area, there are the same 1, 2, 3 or 4 candidates on 1,2,3 or 4 cells respectively


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


def check_naked(board, candidate_board):
    found_any = False
    while naked_singles.check_singles(board, candidate_board):
        found_any = True
    while naked_doubles.check_doubles(board, candidate_board):
        found_any = True
    while naked_triples.check_triples(board, candidate_board):
        found_any = True
    while naked_quadruples.check_quadruples(board, candidate_board):
        found_any = True
    return found_any
