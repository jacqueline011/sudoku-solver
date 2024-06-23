"""
DFS Algorithm

This class uses Depth-First Search Algorithm and backtracking to
solve the sudoku puzzle
"""

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

    

