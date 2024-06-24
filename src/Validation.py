"""
Validation

This class checks if the new number being inputted into the grid
is valid. (Follows the Sudoku rules)


"""

def is_valid_number(grid, num, row, column):

    """
    Check if number is valid under the Sudoku rules

    Parameters:
    grid: 9x9 Sudoku grid (2D array)
    num: the new number being inputted into grid
    row: the current row being checked
    column: the current column being checked

    Returns:
    bool: True/False, whether the number is valid or not

    
    """
    
    # check if num is valid in 3x3 grid
    srow = 3 * (row // 3) #integer division to check the starting row index of the 3x3 subgrid
    scol = 3 * (column // 3) #integer division to check the starting column index of the 3x3 subgrid

    for i in range(srow, srow + 3):
        for j in range(scol, scol + 3):
            if grid[i][j] == num:
                return False 
            
    # check if num is valid in row
    for i in range(9):
        if grid[row][i] == num:
            return False

    # check if num is valid in column
    for i in range(9):
        if grid[i][column] == num:
            return False
    
    
    
    return True

def found_solution(grid):

    """
    Checks if the the grid is the solution

    Parameters: 
    grid: 2D array, 9x9 Sudoku board

    Returns:
    bool: True/False, whether the grid is the solution
    
    """
    
    # check if the grid is the solution
    
    
    pass
