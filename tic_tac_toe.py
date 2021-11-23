def print_board(board):
    '''Print the board after chosing a valid row and column.'''
    board_printed = ""
    for r in range(len(board)):
        c_row = "| ".join(f'{x:2}' for x in board[r])
        board_printed += "------------\n" + " " + c_row + "\n"
    return print(board_printed)

def current_player(player):
    '''Asign the symbol for the current player to the selected square and change to the next player.'''
    if player == 0:
        return "X", 1
    else:
        return "O", 0

def win_checker(count_c_x, count_c_o, count_r_x, count_r_o, diagonals_x, diagonals_o):
    '''Check if any player has achieved the three symbols in a row, column or diagonal'''
    if 3 in count_c_x or 3 in count_r_x or 3 in diagonals_x:
        print("Player 1 has won!")
        return True
    elif 3 in count_c_o or 3 in count_r_o or 3 in diagonals_o:
        print("Player 2 has won!")
        return True
    return False

def tic_tac_toe(board):
    '''Ask the players to select a square to add their token and call the other functions'''
    print("The game begins! You have to create three a row, column or diagonal symbols to win. Player one, you start. Good luck!")
    print("Please, use one NUMBER between 1-3 for each row, and column.")
    player = 0
    empty_spaces = 9
    while True:
        input_row = input("What row will you choose?: ")
        input_column = input("What column will you choose?: ")
        if input_row.isdigit() and input_column.isdigit() and len(input_row) == 1 and len(input_column) == 1 and 1 <= int(input_row) <= 3 and 1 <= int(input_column) <= 3:
            input_row, input_column = int(input_row)-1, int(input_column)-1
            if not "X" in board[input_row][input_column] and not "O" in board[input_row][input_column]:
                board[input_row][input_column], player = current_player(player)
                empty_spaces -= 1
                print_board(board)
                count_r_x = []
                count_r_o = []
                count_c_x = []
                count_c_o = []
                for c in range(len(board)):
                    temp_col = []
                    count_r_x.append(board[c].count("X"))
                    count_r_o.append(board[c].count("O"))
                    for r in range(len(board[c])):
                        temp_col.append(board[r][c])
                    count_c_x.append(temp_col.count("X"))
                    count_c_o.append(temp_col.count("O"))
                diagonals_x = [[board[0][0], board[1][1], board[2][2]].count("X"), [board[0][2], board[1][1], board[2][0]].count("X")]
                diagonals_o = [[board[0][0], board[1][1], board[2][2]].count("O"), [board[0][2], board[1][1], board[2][0]].count("O")]
                win_bool = win_checker(count_c_x, count_c_o, count_r_x, count_r_o, diagonals_x, diagonals_o)
                if win_bool == True: break
            else:
                print("Sorry, someone else has previously chosen that square!")
        else:
            print("Please, use one NUMBER between 1-3 for each row, and column.")
        if empty_spaces == 0:
            return print("Ooops! No one has won this game!")

board = [["", "", ""], ["", "", ""], ["", "", ""]]
tic_tac_toe(board)