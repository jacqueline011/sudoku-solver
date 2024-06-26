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