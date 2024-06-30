import os

class boardManager:
    '''
    This class manages and displays a sudoku board

    Attributes:
    board : A 2D array of integers that represent the sudoku board
    '''

    def __init__(self, file_name):
        """
        Converts the text from file_name into a sudoku board 2D array

        Parameters:
        file_name: a string that is the name of the file containing the initial sudoku board
        """
        self.board = [] 
        input_file_path = os.path.join(os.path.dirname(__file__), file_name)

        with open(input_file_path, 'r') as textFile:
            for line in textFile:
                #Scan each line and add to the board as a 2d array
                self.board.append([int(num) for num in line.strip().split(",")])

    def get_initial_board(self):
        """
        Method that gives the initial sudoku board state

        Returns:
        board: The initial sudoku board (2D array)
        """
        return self.board  

    @staticmethod
    def display(board):
        """
        Print out the sudoku board

        Parameters:
        board: A 2D array that is to be printed
        """
        for i in range(len(board)):
            #Print a row divider after every 3 rows
            if i > 0 and i % 3 == 0:
                print("---------------------")
            for j in range(len(board[i])):
                #Print a cloumn divider after every 3 columns
                if j > 0 and j % 3 == 0:
                    print("|", end=" ")
                print(board[i][j], end=" ")
            print()
            
#Only the code above will be used in the final program


# def cellPos(board, choice):
##index 0 for block choice
#         block_index = (choice - 1)
#         c_num = int(input("Enter a cell position: "))
#         if c_num==0:
#                 run(board)
                
##index 0 for cell number and add a limit to prevent index errors
#         cell_index = min(c_num - 1, 8)
#         print(f"Changing Cell {c_num}:")

##Determine the row position within the 3x3 block
#         row_in_block = cell_index // 3
##Determine the column position within the 3x3 block
#         col_in_block = cell_index % 3

##Determine the row position of the block within the grid
#         block_row = block_index // 3

##Determine the column position of the block within the grid
#         block_col = block_index % 3
        
##Calculate the actual row and column on the board
#         row = block_row * 3 + row_in_block
#         col = block_col * 3 + col_in_block
        
#         new_value = int(input("Enter the new value: "))

##append cell with the new value
#         board[row * 3 + col // 3][col % 3] = new_value
        
        
    
##Create an if-else statements that represent the the 9 blocks of the 2d array and when selected
##Call the cellPos method to decided which cell to to use.
# def run(board):      
#         display(board)                
#         print("Please select a number from 1-9 to choose which block to enter:")

#         choice =int(input())
#         while True:
#                 if choice==1:
#                         print("block 1")
#                         for i in range(0,9,3):
#                                 print(board[i][0], board[i][1], board[i][2], end=" ")
#                                 print()
#                         cellPos(board, choice)
#                         display(board)
                        
                        
                        
#                 elif choice==2:
#                         print("block 2")
#                         for i in range(1,9,3):
#                                 print(board[i][0], board[i][1], board[i][2], end=" ")
#                                 print()
#                         cellPos(board, choice)    
#                         display(board)
                        
#                 elif choice==3:
#                         print("block 3")
#                         for i in range(2,9,3):
#                                 print(board[i][0], board[i][1], board[i][2], end=" ")
#                                 print()
#                         cellPos(board, choice)    
#                         display(board)
                        

#                 elif choice==4:
#                         print("block 4")
#                         for i in range(9,18,3):
#                                 print(board[i][0], board[i][1], board[i][2], end=" ")
#                                 print()
#                         cellPos(board, choice)    
#                         display(board)
                        
#                 elif choice==5:
#                         print("block 5")
#                         for i in range(10,18,3):
#                                 print(board[i][0], board[i][1], board[i][2], end=" ")
#                                 print()
#                         cellPos(board, choice)        
#                         display(board)
                        
#                 elif choice==6:
#                         print("block 6")
#                         for i in range(11,18,3):
#                                 print(board[i][0], board[i][1], board[i][2], end=" ")
#                                 print()
#                         cellPos(board, choice)    
#                         display(board)
                        
#                 elif choice==7:
#                         print("block 7")
#                         for i in range(18,27,3):
#                                 print(board[i][0], board[i][1], board[i][2], end=" ")
#                                 print()
#                         cellPos(board, choice)
#                         display(board)    
                        
#                 elif choice==8:
#                         print("block 8")
#                         for i in range(19,27,3):
#                                 print(board[i][0], board[i][1], board[i][2], end=" ")
#                                 print()
#                         cellPos(board, choice)        
#                         display(board)
                        
#                 elif choice==9:
#                         print("block 9")
#                         for i in range(20,27,3):
#                                 print(board[i][0], board[i][1], board[i][2], end=" ")
#                                 print()
#                         cellPos(board, choice)        
#                         display(board)
#                 elif choice==0:
#                         print("Ending program")
#                         break
                        
#                 else:
#                         print("Invalid choice pick again")

# run(board)