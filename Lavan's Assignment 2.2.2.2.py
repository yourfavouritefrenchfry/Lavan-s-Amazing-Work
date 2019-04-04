import random
import os

board=[0,1,2,
       3,4,5,
       6,7,8]

def show():
    print (board[0],"|",board[1],"|", board[2])
    print ("----------")
    print (board[3],"|",board[4],"|", board[5])
    print ("----------")
    print (board[6],"|",board[7],"|", board[8])

def X_winner(board):
    if (board[0]== "X" and board[1]== "X" and board[2]== "X") or \
        (board[3]== "X" and board[4]== "X" and board[5]== "X") or \
        (board[6]== "X" and board[7]== "X" and board[8]== "X") or \
        (board[0]== "X" and board[3]== "X" and board[6]== "X") or \
        (board[1]== "X" and board[4]== "X" and board[7]== "X") or \
        (board[2]== "X" and board[5]== "X" and board[8]== "X") or \
        (board[0]== "X" and board[4]== "X" and board[8]== "X") or \
        (board[2]== "X" and board[4]== "X" and board[6]== "X"):
        return True
    else:
        return False

def O_winner(board):
    if (board[0]== "O" and board[1]== "O" and board[2]== "O") or \
        (board[3]== "O" and board[4]== "O" and board[5]== "O") or \
        (board[6]== "O" and board[7]== "O" and board[8]== "O") or \
        (board[0]== "O" and board[3]== "O" and board[6]== "O") or \
        (board[1]== "O" and board[4]== "O" and board[7]== "O") or \
        (board[2]== "O" and board[5]== "O" and board[8]== "O") or \
        (board[0]== "O" and board[4]== "O" and board[8]== "O") or \
        (board[2]== "O" and board[4]== "O" and board[6]== "O"):
        return True
    else:
        return False
    
    

while True:
    os.system("clear")
    show()
    choice = input("Select a spot Player X: ")
    choice = int(choice)
    valid_choice_X = False 
    while valid_choice_X == False:
        if board[choice] != "X" and board[choice] != "O":
            board[choice] = "X"
            valid_choice_X = True 
        else: 
            print ("Sorry that spot is taken")
            choice = input("Select a spot Player X: ")
            choice = int(choice) 

    if  X_winner(board): 
        os.system("clear")
        show()
        print ("X wins")
        break

    os.system("clear")
    show()

    full_board = True
    for index in range(0,9):
        if board[index] != "X" and board[index] != "O":
            full_board = False
            break
    if full_board ==True:
        print ("Tie game")
        break










    choice = input("Select a spot Player O: ")
    choice = int(choice)
    valid_choice_O = False
    while valid_choice_O == False:
        if board[choice] != "X" and board[choice] != "O": 
           board[choice] = "O"
           valid_choice_O = True
        else: 
            print ("Sorry that spot is taken")
            choice = input("Select a spot Player O: ")
            choice = int(choice)

    if O_winner(board): 
        os.system("clear")
        show()
        print ("O wins")
        break


    full_board = True
    for index in range(0,9):
        if board[index] != "X" and board[index] != "O":
            full_board = False
            break
    if full_board ==True:
        print ("Tie game")
        break
