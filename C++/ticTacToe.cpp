// Tic-Tac-Toe (Absolute failure of an attempt)

#include <iostream>
#include <stdlib.h>
#include <string>
using namespace std;

// Create the board
char board[3][3] = {{' ', ' ', ' '}, {' ', ' ', ' '}, {' ', ' ', ' '}};

// Variables
string title = "TIC TAC TOE";
int playerCount; 
int row, column;
char playerLetter, opponentLetter;
bool draw = false;

char letterSelect() {
    playerLetter = -1;
    while ((playerLetter != 'X') || (playerLetter != 'O')) {
        cout << "Enter player 1 letter (X or O):";
        cin >> playerLetter;

        if (playerLetter == 'X') { // Assign each player's letter
            return 'X', 'O';
        } else {
            return 'O', 'X';
        }
    }
}

char whoGoesFirst() {
    // Need a stochastic method
    if (true) {
        return 'X';
    } else {
        return 'O';
    }
}

// Display board function
void displayBoard() {
    cout << "PLAYER - 1 [X]t PLAYER - 2 [O]nn";
    cout << "tt     |     |     n";
    cout << "tt  "<<board[0][0]<<"  | "<<board[0][1]<<"  |  "<<board[0][2]<<" n";
    cout << "tt_____|_____|_____n";
    cout << "tt     |     |     n";
    cout << "tt  "<<board[1][0]<<"  | "<<board[1][1]<<"  |  "<<board[1][2]<<" n";
    cout << "tt_____|_____|_____n";
    cout << "tt     |     |     n";
    cout << "tt  "<<board[2][0]<<"  | "<<board[2][1]<<"  |  "<<board[2][2]<<" n";
    cout << "tt     |     |     n";
}

// Check if a given space is free and may be filled
bool isSpaceFree(char board, int *move) { // Pointer
    return (board[move-1] == ' ');
}

// Check if game over
bool gameIsDone() {
    for (int i=0; i<3; i++) { // Check for straight wins
        if ((board[i][0] == board[i][1] && board[i][0] == board[i][2]) || (board[0][i] == board[1][i] && board[0][i] == board[2][i])) {
            return false;
        }
    }

    // Check for diagonal wins
    if ((board[0][0] == board[1][1] && board[0][0] == board[2][2]) || (board[0][2] == board[1][1] && board[0][2] == board[2][0])) {
        return false;
    }
}

// Input and update board function
void playerTurn(char playerLetter, char board) { // Player will be 1 or 2
    int move; // User enters move
    while (true) {
        cout << "Enter move (1-9)";
        cin >> move; // int
        if (1<=move<=9) { // Move in [1, 9]
            if (isSpaceFree(board, &move)) { // Address reference
                break; 
            } else {
                cout << "Invalid input";
            }
        } else {
            cout << "Invalid input";
        }
    }

    switch (move) { // Assign row and column based on move
        case 1: row=0; column=0; break;
        case 2: row=0; column=1; break;
        case 3: row=0; column=2; break;
        case 4: row=1; column=0; break;
        case 5: row=1; column=1; break;
        case 6: row=1; column=2; break;
        case 7: row=2; column=0; break;
        case 8: row=2; column=1; break;
        case 9: row=2; column=2; break;
        }

    // Assign next turn 
    if ((playerLetter == 'X') && (board[&row][&column] != 'X') && (board[&row][&column] != 'O')) {
        board[&row][&column] = 'X';
        playerLetter = 'O';
    } else if ((playerLetter == 'O') && (board[&row][&column] != 'X') && (board[&row][&column] != 'O')) {
        board[&row][&column] = 'O';
        playerLetter = 'X';
    } else { // Error: Player chose a taken space
        cout << "Choose an empty space!";
        playerTurn(playerLetter, board); // Rerun without changing the letter
    }

    

    displayBoard();
}

bool reuse(string thisCode) { // Reuse function to run at end of each game
    cout << "Do you want to reuse " << thisCode << "? (yes or no)";
    string re;
    while (true) {
        cin >> re;
        if (re[0] == 'y' || re[0] == 'Y') {
            return true;
        } else if (re[0] == 'n' || re[0] == 'N') {
            return false;
        }
    }
}

int main() {
    while (true) {
        cout << title;

        // Players choose letters
        char player1Letter, player2Letter;
        player1Letter, player2Letter = letterSelect();

        // Randomly choose who goes first (unfinished)
        char first;
        first = whoGoesFirst();
        if ((first == player1Letter)) {
            playerTurn(player1Letter, board[3][3]);
        } 

        if (reuse(title)) { // This can be refactored, keeping it for understanding
            continue;
        } else {
            break; // Break from loop
        }
    }
    return 0; // Terminate
}