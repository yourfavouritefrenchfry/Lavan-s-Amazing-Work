import random
board= [0,1,2,3,4,5,6,7,8]
def show():
    """
    Print the tic-tac-toe grid
    >>>show()
    0 | 1 | 2
    ----------
    3 | 4 | 5
    ----------
    6 | 7 | 8
    """

def check_char(char, spot_1, spot_2, spot_3):
    """
    Return True if char is the same at spot_1, spot_2 and spot_3
    0 | X | O
    ----------
    3 | X | 5
    ----------
    O | X | 8
    >>>check_char(X,1,4,7)
    True
    >>>check_char(O,2,4,6)
    False
    """

def check_line(char):
    """
    Return True if char makes a winning line
    0 | X | O
    ----------
    3 | X | 5
    ----------
    O | X | 8
    >>>check_line(X)
    True
    """
    #Use check_char function

    

#Use input function to input player's character(X) onto grid. If the spot is already taken, have the player choose another spot.
#Use check_line to see if the inputed X makes a winning line
#Randomly input computer's character(O) onto an empty spot on grid.
#Use check_line to see if the inputed O makes a winning line. 
#After the input, show the new board. 
