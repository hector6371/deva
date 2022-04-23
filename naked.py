import naked_doubles
import naked_quadruples
import naked_singles
import naked_triples
import util


# Naked is where, in a row, col or area, there are the same 1, 2, 3 or 4 candidates on 1,2,3 or 4 cells respectively


def check(board, candidate_board):
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
