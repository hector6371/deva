import brute_force
import human
import util


def create_board():
    # board = [None] * 9
    # board = [board] * 9
    # Completed
    # board = [[8, 2, 7, 1, 5, 4, 3, 9, 6],
    #          [9, 6, 5, 3, 2, 7, 1, 4, 8],
    #          [3, 4, 1, 6, 8, 9, 7, 5, 2],
    #          [5, 9, 3, 4, 6, 8, 2, 7, 1],
    #          [4, 7, 2, 5, 1, 3, 6, 8, 9],
    #          [6, 1, 8, 9, 7, 2, 4, 3, 5],
    #          [7, 8, 6, 2, 3, 5, 9, 1, 4],
    #          [1, 5, 4, 7, 9, 6, 8, 2, 3],
    #          [2, 3, 9, 8, 4, 1, 5, 6, 7]]
    # Super easy
    # board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
    #          [0, 6, 5, 3, 2, 7, 1, 4, 0],
    #          [0, 4, 1, 6, 8, 9, 7, 0, 2],
    #          [5, 9, 3, 4, 6, 8, 0, 7, 1],
    #          [4, 7, 2, 5, 1, 0, 6, 8, 9],
    #          [6, 1, 8, 9, 0, 0, 0, 0, 0],
    #          [7, 8, 6, 0, 3, 5, 9, 1, 4],
    #          [1, 5, 0, 7, 9, 6, 8, 2, 3],
    #          [2, 0, 9, 8, 4, 1, 5, 6, 7]]
    # Easy
    # board = [[0, 0, 3, 7, 0, 0, 0, 0, 0],
    #          [0, 0, 0, 0, 0, 4, 3, 2, 0],
    #          [9, 2, 0, 0, 0, 0, 5, 0, 4],
    #          [7, 3, 0, 4, 0, 0, 0, 1, 0],
    #          [0, 0, 0, 0, 0, 2, 0, 0, 5],
    #          [6, 0, 2, 1, 0, 9, 0, 0, 0],
    #          [2, 0, 4, 0, 3, 8, 1, 5, 7],
    #          [8, 7, 9, 0, 4, 1, 2, 6, 0],
    #          [0, 0, 0, 0, 6, 7, 0, 0, 9]]
    # Hidden Singles
    board = [[4, 0, 2, 7, 0, 0, 3, 0, 0],
             [0, 0, 8, 0, 0, 6, 4, 0, 0],
             [0, 0, 0, 5, 0, 0, 0, 8, 0],
             [0, 4, 7, 0, 0, 0, 1, 0, 8],
             [0, 1, 0, 0, 0, 0, 0, 4, 0],
             [8, 0, 3, 0, 0, 0, 7, 9, 0],
             [0, 7, 0, 0, 0, 3, 0, 0, 4],
             [0, 0, 4, 2, 0, 0, 8, 0, 0],
             [0, 0, 9, 0, 0, 5, 6, 0, 1]]
    # Naked Triples
    # board = [[5, 0, 0, 7, 0, 6, 9, 0, 2],
    #          [0, 0, 9, 0, 1, 0, 8, 7, 5],
    #          [2, 7, 0, 8, 9, 5, 3, 0, 6],
    #          [3, 4, 7, 6, 8, 9, 0, 0, 1],
    #          [9, 1, 5, 0, 0, 0, 7, 6, 8],
    #          [8, 2, 6, 5, 7, 1, 4, 3, 9],
    #          [0, 0, 2, 1, 0, 0, 0, 0, 7],
    #          [7, 0, 0, 0, 0, 0, 1, 0, 3],
    #          [1, 0, 3, 9, 0, 7, 0, 0, 4]]
    # Extreme
    # board = [[0, 2, 0, 0, 6, 0, 0, 3, 0],
    #          [8, 0, 0, 7, 0, 1, 0, 0, 6],
    #          [0, 0, 5, 0, 0, 0, 1, 0, 0],
    #          [0, 8, 0, 0, 2, 0, 0, 9, 0],
    #          [5, 0, 0, 6, 0, 4, 0, 0, 8],
    #          [0, 1, 0, 0, 8, 0, 0, 6, 0],
    #          [0, 0, 4, 0, 0, 0, 7, 0, 0],
    #          [9, 0, 0, 2, 0, 5, 0, 0, 3],
    #          [0, 3, 0, 0, 4, 0, 0, 5, 0]]

    return board


# def check_singles_in_row(row):
#     candidate_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     for cell in row:
#         if cell != 0:
#             candidate_list.remove(cell)
#             print(f'Removed {cell} from candidates, which are now: {candidate_list}')
#     if len(candidate_list) == 1:
#         for cell in row:
#             if cell == 0:
#                 cell = candidate_list[0]
#                 print(f'Found single candidate {candidate_list[0]} in row. row is now: {row}')
#
#
# def check_singles(board):
#     for row in board:
#         check_singles_in_row(row)
#     pass


if __name__ == '__main__':
    board = create_board()
    print('######### Initial board is ######### ')
    util.print_board(board)

    board = human.solve(board)

    #print('######### Solving board with brute force######### ')
    #brute_force.solve_brute_force(board)

    print('######### Final board is ######### ')
    util.print_board(board)
