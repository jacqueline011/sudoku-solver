"""
DFS Algorithm

This class uses Depth-First Search Algorithm and backtracking to
solve the sudoku puzzle
"""

from Validation import *

def dfs_sudoku_solver(initial_state):
    """
    Solves the sudoku puzzle by using dfs

    Parameters:
    initial_state: A 9x9 grid representing the inital state of the sudoku puzzle (2D array of ints)

    Return:
    goal_state: A 9x9 grid representing the solved sudoku puzzle (2D array of ints)
    """

    #next_move_stack constains the moves that still need to be explored
    next_move_stack = []
    next_move_stack.append(initial_state)

    #visited_moves contains the moves already explored
    visited_moves = set()

    while next_move_stack:
        current_state = next_move_stack.pop()
        visited_moves.add(board_to_tuple(current_state))

        if found_solution(current_state):
            return current_state

        next_moves = get_next_moves(current_state)

        for board in next_moves:
            board_tuple = board_to_tuple(board)
            
            if board_tuple not in visited_moves:
                next_move_stack.append(board)

    return None



def board_to_tuple(board):
    """
    Makes board immutable so that it can be added to set

    Parameters:
    board: A 9x9 grid representing a state of the sudoku puzzle (2D array of ints)
    """
    return tuple(tuple(row) for row in board)

def get_next_moves(board):
    """
    Next possible moves for the solution

    Parameters:
    board: 2D array of ints to represent the game board for Sudoku

    Returns:
    List of moves
    """
    next_empty = find_new_spot(board)

    if not next_empty:
        return[]
    
    row = next_empty
    col = next_empty
    stored_moves =[]

    #Adds new valid board to stored_moves
    for num in range(1, 10):
        if is_valid_number(board, num, row, col):
            new_board = [row[:] for row in board]
            new_board[row][col] = num
            stored_moves.append(new_board)

    return stored_moves

def find_new_spot(board):
    """
    
    Finds next available empty cell

    Parameters:
    board: 2D array of ints that represent the game board for Sudoku

    Returns:
    The tuple of (row, col) if it exists
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None