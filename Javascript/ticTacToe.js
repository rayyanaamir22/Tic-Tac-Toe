// Javascript src

const title = "TIC-TAC-TOE";

// Display board whenever necessary
function drawBoard(board) {
    console.log(board[1] + '|' + board[2] + '|' + board[3]);
    console.log('-+-+-');
    console.log(board[4] + '|' + board[5] + '|' + board[6]);
    console.log('-+-+-');
    console.log(board[7] + '|' + board[8] + '|' + board[9]);
}

function isSpaceFree(board, move) {
    if (board[move-1] == ' ') { // -1 for indexing
        return true;
    } 
    return false;
}

// Determine if opponent is another player or AI
function getNumPlayers() {
    while (true) {
        n = readInt('Enter number of players (1 or 2): ');
        if (n==1 || n==2) {
            return n;
        } else {
            console.log("Invalid input.");
        }
    }
}

// Choose letters
function getPlayerLetters() {
    while (true) {
        var letter = readLine("PLAYER 1--Do you want to be X or O? Enter: ");
        if (letter in ['X', 'O']) {
            if (letter == 'X') {
                return 'X', 'O';
            } else {
                return 'O', 'X';
            }
        } else {
            console.log("Invalid input");
        }
    }
}

function whoGoesFirst(player1Name, player2Name) { // Unfinished--need a random method
    var r = (Math.floor(Math.random()));
    if (r==1) {
        return player1Name;
    } else {
        return player2Name;
    }
}

function getPlayerMove(playerName) {
    while (true) {
        var move = readInt(playerName + "--Enter move (1-9): ")
        if (1<=move<=9) {
            if (board[move-1] == ' ') { // -1 for indexing of board
                return move; // Player chose an empty space on the board
            } else {
                console.log("Choose an empty space!"); // Not empty
            }
        } else {
            console.log("That space doesn't exist!");
        }
    }
}

function getComputerMove(board, letter) {
    // Record player1's letter to check if they're winning
    if (letter == 'X') {
        playerLetter = 'O';
    } else {
        playerLetter = 'X';
    }

    // First, check if computer can win with the next move
    for (i=0; i<9; i++) {
        boardCopy = board; // Make sure it isn't address ref
        if (isSpaceFree(board, i)) {
            makeMove(board, letter, i);
            if (isWinner(board, letter)) {
                //delete BoardCopy;
                return i;
            }
        }
    }

    // Second, check if player can win with the next move so computer can block them
    for (i=0; i<9; i++) {
        boardCopy = board;
        if (isSpaceFree(board, i)) {
            makeMove(board, playerLetter);
            if (isWinner(board, playerLetter)) {
                //delete boardCopy;
                return i;
            }
        }
    }

    // Take a corner if available
    for (i=0; i<9; i+=2) { // spaces 1, 3, 7, 9
        if (isSpaceFree(board, i) && (i!=4)) { // Skip 5
            return i;
        }
    }

    // Take the middle if available
    if (isSpaceFree(4)) {
        return i;
    }

    // Take whatever space remains
    for (i=1; i<9; i+=2) { // Only 2, 4, 6, 8 remain
        if (isSpaceFree(board, i)) {
            return i;
        }
    }
}

function makeMove(board, letter, move) {
    board[move] = letter;
}

function isWinner(board, letter) { // Check if a letter has won
    // Straight wins
    for (i=0; i<3; i++) {
        if ((board[i][0] == board[i][1] == board[i][2] == letter) || (board[0][i] == board[1][i] == board[2][i] == letter)) {
            return true;
        }
    } 

    // Diagonal wins
    if ((board[0][0] == board[1][1] == board[2][2] == letter) || (board[0][2] == board[1][1] == board[2][0] == letter)) {
        return true;
    }

    return false;
}

function boardIsFull(board) {
    for (i=0; i<9; i++) {
        if (board[i] == ' ') {
            return false; // If a single space is open
        }
    }
    return true;
}

function reuse(thisCode) {
    while (true) {
        re = readLine("Do you want to reuse " + thisCode + "? (yes or no)");
        if (re[0].toUpperCase() == 'Y') {
            return true;
        } else if (re[0].toUpperCase() == 'N') {
            return false;
        }
    }
}

function main() {
    while (true) { // Main menu loop
        console.log(title, "\n");

        // Define player names
        const playerName = 'Player1';
        if (getNumPlayers() == 1) {
            opponentName = 'AI';
        } else {
            opponentName = 'Player2';
        }

        // Initialize innermost (with param (!gameIsDone)) loop
        gameIsDone = false;

        while (true) { // Game start loop
            var theBoard = [' '] * 9; // Define empty board

            // Define player symbols
            var playerLetter, opponentLetter;
            playerLetter, opponentLetter = getPlayerLetters(); 

            // Randomly choose who goes first
            turn = whoGoesFirst(playerName, opponentName);

            while (!gameIsDone) {
                if (turn == playerName) { // Player turn
                    drawBoard(theBoard);
                    move = getPlayerMove(playerName);
                    makeMove(theBoard, playerLetter, move);
                    
                    gameIsDone = true; // less declarations in the conditions below

                    // Check followup game status
                    if (isWinner(theBoard, playerLetter)) {
                        drawBoard(theBoard);
                        console.log("\nPlayer 1 wins!\n");
                    } else if (boardIsFull(theBoard)) {
                        drawBoard(theBoard);
                        console.log("\nGame is a draw!\n");
                    } else {
                        turn = opponentName;
                        gameIsDone = false;
                    }
            
                } else { // Opponent turn
                    drawBoard(theBoard);

                    // Depends who opponent is
                    if (opponentName == 'Player2') {
                        move = getPlayerMove(playerName);
                    } else {
                        move = getComputerMove(theBoard, opponentLetter);
                    }

                    makeMove(theBoard, opponentLetter, move);

                    // Check followup game status
                    if (isWinner(theBoard, playerLetter)) {
                        drawBoard(theBoard);
                        console.log("\n" + opponentName + " wins!\n");
                    } else if (boardIsFull(theBoard)) {
                        drawBoard(theBoard);
                        console.log("\nGame is a draw!\n");
                    } else {
                        turn = playerName;
                        gameIsDone = false;
                    }
                }
            }

            // Reuse the game 
            if (reuse(title)) { 
                continue;
            } else {
                break; // Exit game loop
            }
        }
        
        // Main menu
        if (reuse("the program")) {
            continue;
        } else {
            break; // Exit main menu loop--Terminate
        }
    }
}

main();