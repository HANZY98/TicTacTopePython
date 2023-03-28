# Firstly the program must select an O or an X to go first, X being the computer and O being the user.
# Once selected, the O or an X must go first, after the first try, the program must check for a win.
# if the win is false then continue to the next go.
# if win is true then display winner, computer or player.

import random as rd
import time

players = ["O", "X"]
gameBoard = [0, 1, 2, 3, 4, 5, 6, 7, 8]

physicalBoard = """

      |     |     
   {}` |  {}  |  {}  
 _____|_____|_____
      |     |     
   {}  |  {}  |  {}  
 _____|_____|_____
      |     |     
   {}  |  {}  |  {}  
      |     |     

""".format(gameBoard[0], gameBoard[1], gameBoard[2], gameBoard[3], gameBoard[4], gameBoard[5], gameBoard[6], gameBoard[7],
           gameBoard[8])

print('Welcome to TicTacToe, the aim of the game is to get three consecutive rows, diagonally, horizontally or vertically\n')

print('Choosing random player')
time.sleep(3)




what_player_first = rd.choice(players)

if what_player_first == "O":
    print("You go first!")
elif what_player_first == "X":
    print("Computer goes first")

print(physicalBoard)


#while win == False:



