#Author: Soumen Nath


'''
This is theinstuc function responsible for providing instructions to the user.
@params         none
@return         none
'''
def instruc():
    print('This program models a chess game in progress and will assess (numerically) who is winning using the relative value system.\nFirst you must enter the current state of the board by entering the pieces in each row seperately. \nYou must use lowercase letters for the white pieces and uppercase letters for the black pieces.\nYou must enter the hyphen "-" for an empty space and the following abbreviations – (K)ing, (Q)ueen, (B)ishop, k(N)ight, (R)ook, and (P)awn.')
    print('Once a proper board is entered, one can either move a piece on the current board, enter a new board from scratch, or quit.\n')
    print('When moving a piece, you are required to enter the row and column. In this program the coordinate system for the rows anc columns look like this: ')
    print(' ',0, 1, 2, 3, 4, 5, 6, 7)
    for i in range(0, 8):
        print(i)
    print('For instnce, the top left position is indicated by row 0 and column 0.\n')

'''
This is the current_state function responsible for allowing the user to enter the state of the board from scratch.
@params         none
@return         The return value is the state of the board entered by the user.
'''
def current_state():
    #string that stores they abbreviations pf the chess peices as characters
    abr = 'KQRNBP-kqrnbp'
    #variable that serves as the outer list for the chess board
    board = []
    #counters that keep track of how many kings that have been entered by the user for each side
    whiteKingCheck = 0
    blackKingCheck = 0
    #flags that change the first time a single king is entered for their respective side
    wf = False
    bf = False
    for i in range(3):
        #Variable that serves as the inner list for the chesss board
        row = []
        while True:
            #Get input from the user for the pieces in each row
            print('\nPlease enter the state of row', i+1, end=': ')
            uInput = input()
            #counter to check if any invalid characters were entered
            counter = 0
            for char in uInput:
                #checking if more than one king was entered per side
                if char == 'k':
                    whiteKingCheck +=1
                elif char == 'K':
                    blackKingCheck +=1
                if whiteKingCheck >1:
                    if wf == False:
                        whiteKingCheck = 0
                    else:
                        whiteKingCheck -= 1
                    print("Error, there can be one king on each team (white/black).\n")
                    break
                elif blackKingCheck>1:
                    if bf == False:
                        blackKingCheck = 0
                    else:
                        blackKingCheck -= 1
                    print("Error, there can be one king on each team (white/black).\n")
                    break
                else:
            #if valid characters were entered, the counter increases to 8
                    if char in abr:
                        counter+=1
            if counter == 8:
                #append each character to the inner list and break the loop
                for char in uInput:
                    if char == 'k':
                        wf = True
                    elif char == 'K':
                        bf = True
                    row.append(char)
                break
        #append the row to the outer list
        board.append(row)
    print()
    #return the board variable
    return board
'''
This is the move_piece function responsible for allowing the user to move a piece on the board from one location to another.
@params         board, this variable contains current state of the board.
@return         The return value is the state of the board entered by the user.
'''
def move_piece(board):
    #if a valid board has  not been entered yet an error message will be displayed to the user
    if board == '':
        print('\nError! A proper board must be entered before being able to move a piece!\n')
    else:
        #string that contains valid character representations of row and column numbers
        nums = '01234567'
        #r and c contain the a valid row and column number entered by the user
        r = 0
        c = 0
        piece = ''
        #while loops to ensure user enters valid numbers
        flag = True
        while flag:
            row1 = input("Please enter the row where the piece you want to move is located at: ")
            for i in range(len(nums)):
                if row1 == nums[i]:
                    flag = False
            if flag != False:
                print("Error you have entered an invalid number!")
        flag = True
        while flag:
            col1 = input("Please enter the column where the piece you want to move is located at: ")
            for i in range(len(nums)):
                if col1 == nums[i]:
                    flag = False
            if flag != False:
                print("Error you have entered an invalid number!")
        #if the numbers entered by the user equals to one of the numbers in nums, then the index of nums is used to store the interger version of the number entered.
        for i in range(8):
            if nums[i] == row1:
                r = i
            if nums[i] == col1:
                c = i
        #if the is no piece at that postion, an error message is displayed to the user
        if board[r][c] == '-':
            print("Error, there is no piece at the specified location.\n")
        else:
            #the piece that was at that postion is stored in a variable and the and hyphen is placed int that location
            piece = board[r][ c]
            board[r][c] = '-'
            flag = True
            while flag:
                row2 = input("Please enter the row where this piece should move to: ")
                for i in range(len(nums)):
                    if row2 == nums[i]:
                        flag = False
                if flag != False:
                    print("Error you have entered an invalid number!")
            flag = True
            while flag:
                col2 = input("Please enter the column where this piece should move to: ")
                for i in range(len(nums)):
                    if col2 == nums[i]:
                        flag = False
                if flag != False:
                    print("Error you have entered an invalid number!")
            for i in range(8):
                #if the numbers entered by the user equals to one of the numbers in nums, then the index of nums is used to store the interger version of the number entered.
                if nums[i] == row2:
                    r = i
                if nums[i] == col2:
                    c = i
            #set the piece that was moved to the new location
            board[r][c] = piece
    #return the new state of the board
    return board
'''
This is the compute_scores function responsible for computing and displaying the current scores of the players.
@params         board, this variable contains current state of the board.
@return         none
'''
def compute_scores(board):
    #if a valid board has been entered
    if board != '':
        #string containing the abbreviations of the pieces for both sides
        upper = 'KQRNBP'
        lower = 'kqrnbp'
        #list that contains the scores in the relative value system
        score = [0, 10, 5, 3.5, 3, 1]
        #counters to keepp teack of the score of each side
        whiteScore = 0
        blackScore = 0
        for row in board:
            for char in row:
                # By using the index value of the strings containing the abbreviations
                #the counters are increasedby the number located at the same index value in the score variable
                for i in range(len(upper)):
                    if upper[i] == char:
                        blackScore+=score[i]
                    elif lower[i] == char:
                        whiteScore+=score[i]
        print('Player 1 (White) Score:',whiteScore, 'Player 2 (Black) Score: ', blackScore)
        if whiteScore>blackScore:
            print('Player 1 is currently winning.')
        elif whiteScore<blackScore:
            print('Player 2 is currently winning.')
        else:
            print('Both players are currently tied.')
    print('\n\n')
'''
This is the display_board function responsible for displaying the current state of the board.
@params         board, this variable contains current state of the board.
@return         none
'''
def display_board(board):
    if board != '':
        for row in board:
            for char in row:
                print(char+' ', end='')
            print()
    print('\n\n')
'''
This is the main function responsible for user interface.
@params         none
@return         none
'''
def main():
    print("\t\t\t-----------------------------------\n\t\t\tWelcome to Soumen's Chess Simulator\n\t\t\t-----------------------------------\n\n")
    board = ''
    #while loop to keep the program running
    while True:
        #display the following and run the correct funtion depending on what option was chosen.
        print("Current Board State: ")
        display_board(board)
        print('Current Player Scores:')
        compute_scores(board)
        print("Please Choose an option:\n1-View Instructions\n2-Enter the State of the Board From Scratch\n3-Move a Piece\n4-Quit")
        selection = input('Please enter your selection: ')
        print()
        if selection == '1':
            instruc()
        elif selection == '2':
            board = current_state()
        elif selection == '3':
            board = move_piece(board)
        elif selection == '4':
            #break the loop if this option was selected
            print("Thank you for using this prpgram!")
            break
        else:
            print("Error!\n")
#run the main function
main()
