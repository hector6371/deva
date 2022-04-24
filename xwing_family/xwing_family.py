from xwing_family import xwing


def check(board, candidate_board):
    found_any = False
    while xwing.check(board, candidate_board):
        found_any = True
    # while swordfish.check(board, candidate_board):
    #     found_any = True
    # while jellyfish.check(board, candidate_board):
    #     found_any = True
    return found_any