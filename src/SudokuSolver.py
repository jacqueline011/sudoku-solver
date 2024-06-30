"""
This is the main module for our Sudoku Solver

The code takes in the initial sudoku puzzle through a txt file, runs a dfs algorithm on it, and displays the solved sudoku puzzle.
"""

from boardManager import *
from DFSAlgorithm import dfs_sudoku_solver

#retrive the starting state of the sudoku puzzle from input
file_name = "input.txt"
board_manager = boardManager(file_name)
initial_state = board_manager.get_initial_board()

#display the initial state of the sudoku puzzle
print("Initial Sudoku Puzzle: ")
board_manager.display(initial_state)
print()

#run the dfs algorithm
solved_board = dfs_sudoku_solver(initial_state)

#check if sudoku puzzle has been solved. If so display the solved puzzle
if solved_board is not None:
    print("Solved Sudoku Puzzle: ")
    board_manager.display(solved_board)
else:
    print("There is no valid solution for the sudoku board given")