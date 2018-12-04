# complete the example and description for this function
# then test it
def init_board() -> list:
    """
    Return list to make the board
    >>>initialize_board
    [" 1 1 1 1","1 1 1 1 "," 1 1 1 1","0 0 0 0 "," 0 0 0 0","2 2 2 2 "," 2 2 2 2","2 2 2 2 "]
    """
    b= ' 1 1 1 1', '1 1 1 1 ', ' 1 1 1 1', '0 0 0 0 ', ' 0 0 0 0', '2 2 2 2 ', ' 2 2 2 2', '2 2 2 2 '
    return b
>>> init_board()
(' 1 1 1 1', '1 1 1 1 ', ' 1 1 1 1', '0 0 0 0 ', ' 0 0 0 0', '2 2 2 2 ', ' 2 2 2 2', '2 2 2 2 ')

 # write this function according to the function design recipe
def display_board(board) -> list:
    """
    Return board
    >>>display_board
    [" 1 1 1 1","1 1 1 1 "," 1 1 1 1","0 0 0 0 "," 0 0 0 0","2 2 2 2 "," 2 2 2 2","2 2 2 2 "]
    """
    b= [" 1 1 1 1","1 1 1 1 "," 1 1 1 1","0 0 0 0 "," 0 0 0 0","2 2 2 2 "," 2 2 2 2","2 2 2 2 "]
    return b
>>> b=' 1 1 1 1', '1 1 1 1 ', ' 1 1 1 1', '0 0 0 0 ', ' 0 0 0 0', '2 2 2 2 ', ' 2 2 2 2', '2 2 2 2 '
>>> display_board(b)
[' 1 1 1 1', '1 1 1 1 ', ' 1 1 1 1', '0 0 0 0 ', ' 0 0 0 0', '2 2 2 2 ', ' 2 2 2 2', '2 2 2 2 ']
    
 # write this function according to the function design recipe
def valid_piece(board, piece) -> bool:
    """
    Return True if piece holds a valid spot in board
    >>>vaild_piece(b, 24)
    True
    >>>valid_piece(b, 14)
    False
    """
    row= board[piece//8]
    if row[(piece)%8]== "1" or row[(piece)%8]=="2": 
        return True
    else:
        return False
>>> valid_piece(b, 0)
False
>>> valid_piece(b, 1)
True
>>> valid_piece(b, 2)
False
>>> valid_piece(b, 10)
True
>>> valid_piece(b, 20)
False
>>> valid_piece(b, 21)
True

 # write this function according to the function design recipe
def valid_move(board, move, piece) -> bool:
    """
    Return True if moving piece to move on board is a valid checkers move
    >>>valid_move(b, 30, 21):
    True
    >>>valid_move(b, 32, 22):
    False 
    """
    new_row= board[move//8]
    difference= move-piece
    if new_row(move%8)== "0": 
        difference= 7, -7, 9, -9
        return True
    # I know the next part is completely wrong and the part before
    jump_row= board[move/2//8]
    sec_jump_row= board[move//8]
    if jump_row(move/2%8)== opp_player:
        sec_jump_row(move%8)== 0
        return True
    else:
        return False
    #I can't add my test because the code is wrong but I don't know what is wrong
    
 # write examples for this function, then complete the code body
# and test it.
def update_board(board : list, move : str, piece : str, player : int) -> bool:
    """
    Update board by moving piece to move. Return True if and only if
    the opposing player (the one that is not moving a piece) has no valid
    moves after updating the game.
    """
    new_board=[]
    for rows_added in board:
        if not row:
            new_board.append(rows-added)
        else:
            row[(piece)%8].remove(player)
            new_board.append(row[(piece)%8].append("0"))
    #I can't add my test because the code is wrong. 
            
 # write this function according to the function design recipe.
def update_player(player) -> int:
    """
    Return player as the oppsoing player
    >>>update_player(1):
    2
    >>>update_player(2):
    1
    """
    if player==1:
        player=2
        opp_player=1
    else: 
        player=1
        opp_player=2
    
    if __name__ == "__main__":
        board = init_board()
    player = 1
    gameover = False
    while not gameover:
        print(display_board(board))
        piece = input("Player {}, which piece would you like to move?".format(player))
        while not valid_piece(board, piece):
            piece = input("Player {}, pick a valid piece".format(player))
        move = input("Player {}, where would you like to move the piece at {}?".format(player, piece))
        while not valid_move(board, move, piece):
            move = input("Player {}, pick a valid move for the piece at {}.".format(player, piece))
        gameover = update_board(board, move, piece, player)
        player = update_player(player)
    player = update_player(player)
    print("Game over, player {} wins!".format(player))

