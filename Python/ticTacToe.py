'''
Name: Rayyan Aamir
Date: May 15, 2022
Program: Tic-Tac-Toe (modified for 1 or 2 players)
'''

# Modules
import functions as f

# Program begins
while True:
    print('Welcome to Tic-Tac-Toe!\n')
  
    f.playerOrAI()
    if f.opponent == 'AI':
        # Reset the board.
        theBoard = [' '] * 10
        playerLetter, computerLetter = f.inputPlayerLetter()
        turn = f.whoGoesFirst()
        print(f'The {turn} will go first.')
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'player':
                # Player's turn
                f.drawBoard(theBoard)
                move = f.getPlayerMove(theBoard)
                f.makeMove(theBoard, playerLetter, move)

                if f.isWinner(theBoard, playerLetter):
                    f.drawBoard(theBoard)
                    print('Hooray! You have won the game!')
                    gameIsPlaying = False
                else:
                    if f.isBoardFull(theBoard):
                        f.drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'computer'

            else:
                # Computer's turn
                move = f.getComputerMove(theBoard, computerLetter)
                f.makeMove(theBoard, computerLetter, move)
                if f.isWinner(theBoard, computerLetter):
                    f.drawBoard(theBoard)
                    print('You lose.')
                    gameIsPlaying = False
                else:
                    if f.isBoardFull(theBoard):
                        f.drawBoard(theBoard)
                        print('Draw.')
                        break
                    else:
                        turn = 'player'
    # If user selects 2-player option, run this code
    elif f.opponent == 'Player 2':
        # Reset the board.
        theBoard = [' '] * 10
        playerLetter, player2Letter = f.inputPlayerLetter()
        turn = f.whoGoesFirst()
        print(f'{turn} will go first.')
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'Player 1':
                # Player 1's turn
                f.drawBoard(theBoard)
                move = f.getPlayerMove(theBoard)
                f.makeMove(theBoard, playerLetter, move)

                if f.isWinner(theBoard, playerLetter):
                    f.drawBoard(theBoard)
                    print('Player 1 has won the game!')
                    gameIsPlaying = False
                else:
                    if f.isBoardFull(theBoard):
                        f.drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'Player 2'

            else:
                # Player 2's turn
                f.drawBoard(theBoard)
                move = f.getPlayer2Move(theBoard)
                f.makeMove(theBoard, player2Letter, move)

                if f.isWinner(theBoard, player2Letter):
                    f.drawBoard(theBoard)
                    print('Player 2 has won the game!')
                    gameIsPlaying = False
                else:
                    if f.isBoardFull(theBoard):
                        f.drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'Player 1'
    
    # Ask player if they want to play again. The function already has a while loop to ensure the user gives a valid entry. If the response is not true, the game loop breaks and the program ends
    if f.reuse():
      continue
    else:
      break
