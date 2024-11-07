from math import inf
from random import choice

# INITIALIZING THE BOARD WITH ALL ZEORS.........
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

# FOR PRINTING THE BOARD..........
def Gameboard(board):
    chars = {1: 'X', -1: 'O', 0: ' '}
    for i in range(len(board)):
        print('-----' * len(board))
        for j in range(len(board[i])):
            ch = chars[board[i][j]]
            print('|',ch,'|', end='')
        print()
    print('-----' * len(board))

# TO CLEAR THE ENTIRE BOARD...........
def Clear_The_Board(board):
    for x, row in enumerate(board):
        for y, col in enumerate(row):
            board[x][y] = 0

# TO CHECK THE WETHER THE PLAYER IS WINNER OR NOT IF HE IS IN GIVEN CONDITIONS OR NOT.......
def winner(board, player):
    check = [[board[0][0], board[0][1], board[0][2]],
                     [board[1][0], board[1][1], board[1][2]],
                     [board[2][0], board[2][1], board[2][2]],
                     [board[0][0], board[1][0], board[2][0]],
                     [board[0][1], board[1][1], board[2][1]],
                     [board[0][2], board[1][2], board[2][2]],
                     [board[0][0], board[1][1], board[2][2]],
                     [board[0][2], board[1][1], board[2][0]]]
    if [player, player, player] in check:
        return True
    return False

# RETURNING WIN OR LOOSE REGARDING PLAYER THAT U CHOOSE...........
def won(board):
    return winner(board, 1) or winner(board, -1)

# PRINTING THE RESULT OF THE PLAYER WETHER HE WON OR LOST..........
def printResult(board):
    if winner(board, 1):
        print('X has won...! ' + '\n')
    elif winner(board, -1):
        print('O has won...! ' + '\n')
    else:
        print('Draw...!!' + '\n')

def blanks(board):
    blank = []
    for x, row in enumerate(board):
        for y, col in enumerate(row):
            if board[x][y] == 0:
                blank.append([x, y])
    return blank

# RETUNRS THE VALUE IF THE BOARD IS FULL...........
def full(board):
    if len(blanks(board)) == 0:
        return True
    return False

def Move(board, x, y, player):
    board[x][y] = player

# FUNCTION TO MAKE MOVES........
def playerMove(board, player):
    c = True

    # ASSINGING MOVES TO THE INDISES OF THE BOARD THE WE HAVE CREATED...
    moves = {1: [0, 0], 2: [0, 1], 3: [0, 2],
             4: [1, 0], 5: [1, 1], 6: [1, 2],
             7: [2, 0], 8: [2, 1], 9: [2, 2]}

    # EXCEPTION HANDILING FOR INVALID MOVES..........
    while c:
        try:
            move = int(input('Enter a number between 1-9: '))
            if move < 1 or move > 9:
                print('Invalid Move! Try again!')
            elif not (moves[move] in blanks(board)):
                print('Invalid Move! Try again!')
            else:
                # MOVES[1] IMPLIES THE KEY VALUE AND THE OTHER [] REPRESENT THE INDEX VALUE OF THE VALUES THAT IT CONTAIN...
                Move(board, moves[move][0], moves[move][1], player)
                Gameboard(board)
                c = False
            
        except(KeyError, ValueError):
            print('Enter a number!')
            
# RETRUNING THE VALUE TO PRINT THE FINAL RESULT....
def getScore(board):
    if winner(board, 1):
        return 1
    elif winner(board, -1):
        return -1
    else:
        return 0

# CODE FOR ALPHA-BETA PRUNING........
def Alpha_Beta(board, depth, alpha, beta, player):
    row = -1
    col = -1
    if depth == 0 or won(board):
        return [row, col, getScore(board)]

    else:
        for cell in blanks(board):
            Move(board, cell[0], cell[1], player)
            score = Alpha_Beta(board, depth - 1, alpha, beta, -player)
            if player == 1:
                # X is always the max player
                if score[2] > alpha:
                    alpha = score[2]
                    row = cell[0]
                    col = cell[1]
            else:
                if score[2] < beta:
                    beta = score[2]
                    row = cell[0]
                    col = cell[1]

            Move(board, cell[0], cell[1], 0)

            if alpha >= beta:
                break

        if player == 1:
            return [row, col, alpha]

        else:
            return [row, col, beta]

# TAKING MOVES FOR THE 'O' PLAYER....
def O_Chance(board):

    if len(blanks(board)) == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
        Move(board, x, y, -1)
        Gameboard(board)

    else:
        result = Alpha_Beta(board, len(blanks(board)), -inf, inf, -1)
        Move(board, result[0], result[1], -1)
        Gameboard(board)

# TAKING MOVES FOR THE 'X' PLAYER.....
def X_Chance(board):
    if len(blanks(board)) == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
        Move(board, x, y, 1)
        Gameboard(board)

    else:
        result = Alpha_Beta(board, len(blanks(board)), -inf, inf, 1)
        Move(board, result[0], result[1], 1)
        Gameboard(board)

# BASED ON THE ABOVE CHOICE WILL INITIATE THE MOVE OF THE PARTICULAR PLAYER IN THE BOARD....
def Make_A_Move(board, player, mode):
    if mode == 1:
        if player == 1:
            playerMove(board, player)
        else:
            O_Chance(board)
    elif mode == 2:
        if player == 1:
            playerMove(board, player)
        else:
            playerMove(board, player)

# MAIN FUNCTOINS CALLING FUNCTION......
def Start_Game():
    while True:
        try:
            mode = int(input('1. To play with computer \n2. To play with human\nEnter your choice: '))
            order = int(input('Enter to play 1st or 2nd: '))

            if not (order == 1 or order == 2):
                print('Please pick 1 or 2')
            else:
                break
        except(KeyError, ValueError):
            print('Enter a number')

    Clear_The_Board(board)
    if order == 2:
        currentPlayer = -1
    else:
        currentPlayer = 1

    # THIS LOOP CONTINUES UNTILL THE BOARD IS FULL OR ANY OF THE PLAYER IS WON....
    while not (full(board) or won(board)):
        Make_A_Move(board, currentPlayer, mode)
        # TOGGLES BETWEEN THE PLAYER-1 AND PLAYER-2 THE MULTIPLICATION MAKE SURE ABT IT....
        currentPlayer *= -1

    printResult(board)

print("TIC-TAC-TOE using ALPHA-BETA Pruning")
print("_____________________________________")
Start_Game()

