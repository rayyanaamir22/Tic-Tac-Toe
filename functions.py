# FUNCTIONS

# Modules
import random
import os
import time

def drawBoard(board):
    # This function prints out the board that it was passed.

    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])

def playerOrAI():
  # User determines if he wants to play multiplayer or against AI
  global opponent
  opponent = ''
  # If the user chose single player, the statement directs them to a game against the AI. If not, they will play against someone present with them.
  while True:
    print('How many players? (1 or 2)')
    competition = input()
    if competition == '1' or competition.lower().startswith('o'):
      opponent = 'AI'
      break
    elif competition == '2' or competition.lower().startswith('t'):
      opponent = 'Player 2'
      break
    else:
      print('Invalid input')
  os.system('clear')

def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    os.system('clear')
    # The first element in the list is the player's letter; the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # Randomly choose which player goes first.
    # Depends who the opponent is.
    if opponent == 'AI':
        if random.randint(0, 1) == 0:
            return 'player'
        else:
            return 'computer'
    else:
        if random.randint(0, 1) == 0:
            return 'Player 1'
        else:
            return 'Player 2'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use "bo" instead of "board" and "le" instead of "letter" so we don't have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # Across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # Across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # Across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # Down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # Down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # Down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # Diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # Diagonal

def getBoardCopy(board):
    # Make a copy of the board list and return it.
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    # Return True if the passed move is free on the passed board.
    return board[move] == ' '

def getPlayerMove(board):
    # Let the player enter their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is Player 1\'s move? (1-9)')
        move = input()
    # Replace the previous board with the new one
    os.system('clear')
    return int(move)

def getPlayer2Move(board):
    # Let the player enter their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is Player 2\'s move? (1-9)')
        move = input()
    # Replace the previous board with the new one
    os.system('clear')
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Create delay for computer to take turn
    drawBoard(board) # Show the previous board
    time.sleep(1) # Delay is 1 second
    os.system('clear') # Clear the screen; the board will be replaced when the computer makes its turn

    # Here is the algorithm for our Tic-Tac-Toe AI:
    # First, check if we can win in the next move.
    # For loop has range(1, 10) which creates 9 iterations of 1 to 9 since 10 is exclusive.
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    # Check if the player could win on their next move and block them.
    # This function is the same as the previous but includes playerLetter as a parameter instead of computerLetter. Theoretically, the computer is completing the player's move to win, but really just blocks them from winning.
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

    # Replace the previous board with the new one
    os.system('clear')

def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise, return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

def reuse():
    while True:
      print('Do you want to play again? (yes or no)')
      re = input()
      if re.lower().startswith('y'):
        return True
      elif re.lower().startswith('n'):
        return False
      else:
        print('Invalid input')
