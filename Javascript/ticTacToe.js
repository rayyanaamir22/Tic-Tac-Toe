// Javascript src

const title = "TIC TAC TOE";

// Display board whenever necessary
function drawBoard(board) {
    console.log(board[1] + '|' + board[2] + '|' + board[3]);
    console.log('-+-+-');
    console.log(board[4] + '|' + board[5] + '|' + board[6]);
    console.log('-+-+-');
    console.log(board[7] + '|' + board[8] + '|' + board[9]);
}

// Determine if opponent is another player or AI
function numPlayers() {
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
    return player1Name;
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

function main() {
    while (true) {
        console.log(title, "\n");
        var board = [' '] * 10;

        // Define player names
        const playerName = 'Player1';
        var opponent;
        if (numPlayers() == 1) {
            opponentName = 'AI';
        } else {
            opponentName = 'Player2';
        }

        // Define player symbols
        var playerLetter, opponentLetter;
        playerLetter, opponentLetter = getPlayerLetters(); 

        // Randomly choose who goes first
        first = whoGoesFirst();
        

        
    }
}

main();