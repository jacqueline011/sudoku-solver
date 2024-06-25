class boardManager:

    
    #Guys just letting you know that the could should be good, but I plan to add a while to the whole to allow multiple selections of cells
    #as well as reading and maybe writing files to for comparison purposes.
    #Intilize the 2d array
    board = [
        [1,0,0],[0,1,0],[1,0,0],
        [2,0,0],[0,1,0],[1,0,0],
        [3,0,0],[0,1,0],[1,0,0],
        [0,0,0],[0,0,0],[0,5,0],
        [0,1,0],[0,0,0],[0,0,0],
        [0,0,0],[0,2,0],[0,0,0],
        [0,0,0],[0,0,0],[0,0,0],
        [0,9,0],[0,7,0],[0,3,0],
        [0,0,0],[0,0,0],[0,0,0]]
    
 
    #Create a method to display a display teh grid
    def display(board):

        for i in range(0, 27):
            
                print("|",board[i][0], board[i][1], board[i][2],"|", end=" ")
                if (i+1) % 3 == 0:
                    print()
                    if(i+1)%9==0:
                        print("-----------------------------")
                        


    def cellPos(board, choice):
        #index 0 for block choice
        block_index = (choice - 1)
        c_num = int(input("Enter a cell position: "))
        #index 0 for cell number and add a limit to prevent index errors
        cell_index = min(c_num - 1, 8)
        print(f"Changing Cell {c_num}:")

        # Determine the row position within the 3x3 block
        row_in_block = cell_index // 3
        # Determine the column position within the 3x3 block
        col_in_block = cell_index % 3

        # Determine the row position of the block within the grid
        block_row = block_index // 3

        # Determine the column position of the block within the grid
        block_col = block_index % 3
        
        # Calculate the actual row and column on the board
        row = block_row * 3 + row_in_block
        col = block_col * 3 + col_in_block
        
        new_value = int(input("Enter the new value: "))

        # append cell with the new value
        board[row * 3 + col // 3][col % 3] = new_value
    
   #Create an if-else statements that represent the the 9 blocks of the 2d array and when selected
   #call the cellPos method to decided which cell to to use.
        
    display(board)                
    print("Please select a number from 1-9 to choose which block to enter:")

    choice =int(input())
    
    if choice==1:
            print("block 1")
            for i in range(0,9,3):
                    print(board[i][0], board[i][1], board[i][2], end=" ")
                    print()
            cellPos(board, choice)
            display(board)
        
            
            
    elif choice==2:
            print("block 2")
            for i in range(1,9,3):
                    print(board[i][0], board[i][1], board[i][2], end=" ")
                    print()
            cellPos(board, choice)    
            display(board)
            
    elif choice==3:
            print("block 3")
            for i in range(2,9,3):
                    print(board[i][0], board[i][1], board[i][2], end=" ")
                    print()
            cellPos(board, choice)    
            display(board)
            

    elif choice==4:
            print("block 4")
            for i in range(9,18,3):
                    print(board[i][0], board[i][1], board[i][2], end=" ")
                    print()
            cellPos(board, choice)    
            display(board)
            
    elif choice==5:
            print("block 5")
            for i in range(10,18,3):
                    print(board[i][0], board[i][1], board[i][2], end=" ")
                    print()
            cellPos(board, choice)        
            display(board)
            
    elif choice==6:
            print("block 6")
            for i in range(11,18,3):
                    print(board[i][0], board[i][1], board[i][2], end=" ")
                    print()
            cellPos(board, choice)    
            display(board)
            
    elif choice==7:
            print("block 7")
            for i in range(18,27,3):
                    print(board[i][0], board[i][1], board[i][2], end=" ")
                    print()
            cellPos(board, choice)
            display(board)    
            
    elif choice==8:
            print("block 8")
            for i in range(19,27,3):
                    print(board[i][0], board[i][1], board[i][2], end=" ")
                    print()
            cellPos(board, choice)        
            display(board)
            
    elif choice==9:
            print("block 9")
            for i in range(20,27,3):
                    print(board[i][0], board[i][1], board[i][2], end=" ")
                    print()
            cellPos(board, choice)        
            display(board)
            
    else:
            print("Invalid choice pick again")
            
        
                            
        
    
            

        



