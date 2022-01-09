'''
Name: Rayyan Aamir
Date: November 4, 2021
Program: Tic-Tac-Toe (modified for 1 or 2 players)
'''

# Modules
import functions

# Program begins
print('Welcome to Tic-Tac-Toe!')

while True:
    functions.playerOrAI()
    if functions.opponent == 'AI':
        # Reset the board.
        theBoard = [' '] * 10
        playerLetter, computerLetter = functions.inputPlayerLetter()
        turn = functions.whoGoesFirst()
        print('The ' + turn + ' will go first.')
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'player':
                # Player's turn
                functions.drawBoard(theBoard)
                move = functions.getPlayerMove(theBoard)
                functions.makeMove(theBoard, playerLetter, move)

                if functions.isWinner(theBoard, playerLetter):
                    functions.drawBoard(theBoard)
                    print('Hooray! You have won the game!')
                    gameIsPlaying = False
                else:
                    if functions.isBoardFull(theBoard):
                        functions.drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'computer'

            else:
                # Computer's turn
                move = functions.getComputerMove(theBoard, computerLetter)
                functions.makeMove(theBoard, computerLetter, move)

                if functions.isWinner(theBoard, computerLetter):
                    functions.drawBoard(theBoard)
                    print('The computer has beaten you! You lose.')
                    gameIsPlaying = False
                else:
                    if functions.isBoardFull(theBoard):
                        functions.drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player'
    # If user selects 2-player option, run this code
    elif functions.opponent == 'Player 2':
        # Reset the board.
        theBoard = [' '] * 10
        playerLetter, player2Letter = functions.inputPlayerLetter()
        turn = functions.whoGoesFirst()
        print('' + turn + ' will go first.')
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'Player 1':
                # Player 1's turn
                functions.drawBoard(theBoard)
                move = functions.getPlayerMove(theBoard)
                functions.makeMove(theBoard, playerLetter, move)

                if functions.isWinner(theBoard, playerLetter):
                    functions.drawBoard(theBoard)
                    print('Player 1 has won the game!')
                    gameIsPlaying = False
                else:
                    if functions.isBoardFull(theBoard):
                        functions.drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'Player 2'

            else:
                # Player 2's turn
                functions.drawBoard(theBoard)
                move = functions.getPlayer2Move(theBoard)
                functions.makeMove(theBoard, player2Letter, move)

                if functions.isWinner(theBoard, player2Letter):
                    functions.drawBoard(theBoard)
                    print('Player 2 has won the game!')
                    gameIsPlaying = False
                else:
                    if functions.isBoardFull(theBoard):
                        functions.drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'Player 1'
    
    # Ask player if they want to play again. The function already has a while loop to ensure the user gives a valid entry. If the response is not true, the game loop breaks and the program ends
    if functions.playAgain() != True:
      break
    else:
      # If user says yes to playing again
      continue