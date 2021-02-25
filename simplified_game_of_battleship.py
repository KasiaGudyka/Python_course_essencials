# try to sank a battleship by guessing it's location (simplified version because it takes one shot to sink it)
from random import randint

board = []

print ("In this 5x5 battlefield there is a hidden battleship.\nTry to sank it by guessing it's location:\n")
for x in range(0, 5):
  board.append(["O "] * 5)

def print_board(board):
  for row in board:
    print ("  ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
# remove the comments if you'd like to see the bettleship location
# print (ship_row)
# print (ship_col)

# 
for turn in range(10):
  print ("Turn", turn + 1)
  guess_row = int(input("Guess the row: ")) - 1
  guess_col = int(input("Guess the column: ")) - 1

  if guess_row == ship_row and guess_col == ship_col:
    print ("Congratulations! You sank the battleship!")
    board[guess_row][guess_col] = "V " 
    print_board(board)
    break  
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print ("You missed the battlefield! The range is 5x5.")
    elif board[guess_row][guess_col] == "X ":
      print( "You guessed that one already." )
    # adding the hint of hitting close from the bettleship
    elif guess_row - 1 == ship_row and guess_col - 1 == ship_col or guess_row + 1 == ship_row and guess_col + 1 == ship_col or guess_row == ship_row and guess_col - 1 == ship_col or guess_row - 1 == ship_row and guess_col == ship_col or guess_row == ship_row and guess_col + 1 == ship_col or guess_row + 1 == ship_row and guess_col == ship_col or guess_row - 1 == ship_row and guess_col + 1 == ship_col or guess_row + 1 == ship_row and guess_col - 1 == ship_col :
      print ("That was close! But you didn't sink the battleship!")
      board[guess_row][guess_col] = "x "
    else:
      print ("You missed the battleship!")
      board[guess_row][guess_col] = "X "
    if (turn == 9):
      print ("Game Over")
    print_board(board)
