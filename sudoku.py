import time

def solve_sudoku(board):
    """
    Given a sudoku board (as a list of list of numbers, where 0 represents an
    empty square), return a solved version of the puzzle.
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                continue
            #found a 0; try filling it      
            for trial in valid_moves(board, row, col):
                # new_board = [[trial if (r, c) == (row, col) else board[r][c] for c in range(9)]
                #             for r in range(9)] 
                #result = solve_sudoku(new_board)
                board[row][col] = trial
                result = solve_sudoku(board)
                if result is not None:
                    return result
            board[row][col] = 0
            return None
    return board


""" def valid_board(board):
    for row in range(9):
        if(violation(values_in_row(board, row))):
            return False
        
    for col in range(9):
        if(violation(values_in_column(board, col))):
            return False  
    
    for sr in range(3):
        for sc in range(3):
            if(violation(values_in_subgrid(board, sr, sc))):
                return False

    return True

def violation(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] == list[j] and list[i] != 0:
                return True
    return False
                 """

def values_in_row(board, r):
    """
    Given a board, return a set with the values in the row r of the board 
    """
    return set(board[r])

def values_in_column(board, c):
    """
    Given a board, return a set with the values in the column c of the board 
    """
    return set([row[c] for row in board])
     
def values_in_subgrid(board, sr, sc):
    """
    Given a board, return a set with the values in the subgrid[sr][sc] of the board 
    """  
    subgrid = []
    for i in range(3 * sr, 3 * sr + 3):
        for j in range(3 * sc , 3 * sc  + 3):
            subgrid.append(board[i][j])
    return set(subgrid)

def valid_moves(board, row, col):
    return (
        set(range(1, 10))                           # all posible moves
        - values_in_row(board, row)                 # exclude values already in the row
        - values_in_column(board, col)              # exclude values already in the column
        - values_in_subgrid(board, row//3, col//3)  # exclude values already in the subgrid
        )

def format_sudoku(board):
    """
    Format a sudoku board to be printed to the screen
    """
    if not board:
        return 'Failed'
    _divider = '+' + ''.join('-+' if i % 3 == 2 else '-' for i in range(9))
    lines = []
    for i in range(9):
        if i % 3 == 0:
            lines.append(_divider)
        line = '|'
        for j in range(9):
            line += ' ' if board[i][j] == 0 else str(board[i][j])
            if j % 3 == 2:
                line += '|'
        lines.append(line)
    lines.append(_divider)
    return '\n'.join(lines)


def solve(board):
    """
    Given a sudoku board (as a list of list of numbers, where 0 represents an
    empty square), print the initial board and the solution board and the time 
    elapsed to get the solution.
    """
    print(format_sudoku(board))
    t = time.time()
    res = solve_sudoku(board)
    elapsed = time.time() - t
    if res:
        print(format_sudoku(res))
    else:
        print('Failed')
    print(elapsed, 'seconds')
    print()

