import hidden_singles
import naked_doubles
import naked_quadruples
import naked_singles
import naked_triples
import util


# Hidden: Singles, pairs, triples, quads (A hidden pair occurs when a pair of numbers appears in exactly two squares in a row, column, or block, but those two numbers aren't the only ones in their squares)


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


def check(board, candidate_board):
    found_any = False
    while hidden_singles.check(board, candidate_board):
        found_any = True
    # while hidden_doubles.check(board, candidate_board):
    #     found_any = True
    # while hidden_triples.check(board, candidate_board):
    #     found_any = True
    # while hidden_quadruples.check(board, candidate_board):
    #     found_any = True
    return found_any
