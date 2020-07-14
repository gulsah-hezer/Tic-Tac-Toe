
#STEP 1: Write a function that can print out a board. Set up your board as a list where each index 1-9 with a number on a number pad.
#So you get a 3 by 3 board representation.

#STEP 2: Write a function that can take in a player input and assign their marker  as 'X' or 'O'.Think about using while loops to continually ask
#until you get a correct answer.

#STEP 3: Write a function that takes in the board list object  a marker ('X' or 'O') and desired position (number 1-9) and assign it to board.

#STEP 4: Write a function that takes in a board and a mark ('X or 'O') and then checks to see if that mark has won.

#STEP 5: Write a function that uses the random module to randomly decide which player goes first.You may want to lookup random.randint().Return a string of 
#which player went first.

#STEP 6: Write a function that returns a boolean indicating whether a space on the board is freely available.

#Long Story Short: Visual representation --> User Input --> Function --> Updates --> New Visual.

#-----------------------------------------------------------------------------------------------------------------------------------------

def display_board(board):
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

# In here we set our board and we also give value for each empty area.We call it as a list.This board list fill all empty spaces.
# For ex. one list example is in below.
 test_board = ['#','X','O','X','O','X','O','X','O','X'] 
#--> this is the list.
display_board(test_board)
#-----------------------------------------------------------------------------------------------------------------------------------------

def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
 
#if we want to test this function, first we can write player_input() function and we see Do you want to be X or O? this question and we 
# answer as for ex. 'X' then we get ('X', 'O') as a result.
#----------------------------------------------------------------------------------------------------------------------------------------

# until we came to the here, we form one board and we numbered it with list properties, and also we get desired choice from client.Okay,
# now we can place it to desired place.

def place_marker(board, marker, position):
    board[position] = marker
    
# we create a function that takes position value and marker value and it puts it to correct place.that's it.
place_marker(test_board,'$',8)
display_board(test_board)
#we can test like this.
#----------------------------------------------------------------------------------------------------------------------------------------

# we placed our values to our desired board index.So, now we can decide that person win or lose.Let's start.

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
 
# in here we determine our own rules.that's it.That means that right, left, diagonal etc. satisfy our condition to be correct.
# if we fill empty spaces, then we can control we win or lose.
win_check(test_board,'X')
#we can test it like this. The important thing in here is to have test_board as tiem passes by.
#----------------------------------------------------------------------------------------------------------------------------------------

# actually we create board and input marker and win lost situation and it seems like it finished, but unfortunately no.
#in here we decide which people start first.

import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1
#----------------------------------------------------------------------------------------------------------------------------------------

#in here we want to get information if board index space is full or empty.

def space_check(board, position):
    
    return board[position] == ' '
  
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
 
#----------------------------------------------------------------------------------------------------------------------------------------

#we decide position choice in here.

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

#---------------------------------------------------------------------------------------------------------------------------------------

def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
#---------------------------------------------------------------------------------------------------------------------------------------

# this is the hardest part because in here we combine all of it.we use all functions that we created before and use while loops and ,
#then we can run the game.


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
        
#----------------------------------------------------------------------------------------------------------------------------------------

                                             #THE HAPPY END 

















