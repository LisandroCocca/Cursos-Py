# -*- coding: utf-8 -*-
from IPython.display import clear_output
import random

# Welcome!
print('Welcome to Tic Tac Toe!')

## Definition of functions
def display_board(board):
    
    print('           ')

    print('   |   |   ')
    print(f' {board[7]} | {board[8]} | {board[9]}  ')
    print('   |   |   ')
    
    print('------------')
    
    print('   |   |   ')
    print(f' {board[4]} | {board[5]} | {board[6]}  ')
    print('   |   |   ')
    
    print('------------')

    print('   |   |   ')
    print(f' {board[1]} | {board[2]} | {board[3]}  ')
    print('   |   |   ')
    
    print('           ')

    
# First player selection
def choose_first():
    erste = str(random.randint(1,2))
    print(f"The player No.{erste} goes first")
    return erste


# First player chooses mark
def player_input(nr):
    
    choice = 'wrong'
    
    while choice not in ['X','O']:
        
        choice = input(f"Player {nr}: Would you like to pick X or O? ")
        
        if choice not in ['X','O']:
            print("Sorry man, you're retarded. I said X or O")
            
    return choice
 
           
# Check if board is full
def full_board_check(board):

    for pos in range(1,9):
        if board[pos] == ' ':
            return False

    return True


# Asking for position
def space_check(board, position):
    return board[position] == ' '


# Player position selection
def player_choice(board,marker):
    
    choice = "Wrong"
    correct_v = ['0','1','2','3','4','5','6','7','8','9']
    
    # Validating Input
    while choice not in correct_v :
        
        choice = input (f"Player {marker}: Please select the desired position (1-9): ")
        
        if choice not in correct_v:
            print("You are really retarded bro! NUMBERS FROM 1 to 9")
        elif  space_check(board,int(choice)):
            return int(choice)
        else:
            print("Sorry my friend, space is not empty!")
            choice = "Wrong"


# Replace mark in board
def place_marker(board, marker, position):
    
    board[position] = marker


# Check if someone has won
def win_check(board, mark):
    
    win_conditions = [ [1,2,3], [4,5,6], [7,8,9] , [1,4,7] , [2,5,8] , [3,6,9] , [1,5,9] , [3,5,7]]
    
    for win_c in win_conditions:
        if board[win_c[0]] == mark and board[win_c[1]] == mark and board[win_c[2]] == mark:
            print (f"Congratulations, Player {mark} has won!")
            return True
     
# Replaying or not
def replay():
    
    answer = 'Wrong'
    
    while answer not in ['Y','N']:
        
        answer = input ("Would you like to play again loser? (Y-N): ")
        
        if answer not in ['Y','N']:
            print ("At this point, you are full retarded -.-")
    
    return answer == 'Y'
       

# Game Initialization
while True:
    ## Set the game up here
    clear_output()
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    board_full = False

    # Print empty board
    display_board(board)

    # Select First player
    clear_output()
    starting_player = choose_first()

    # Mark assignment for first player
    marker = player_input(starting_player)

    while not board_full:
    
        # Check if board is full
        board_full = full_board_check(board)
        
        # Player Turn ---> Ask for position
        position = player_choice(board,marker)
    
        # Replace mark on position
        place_marker(board, marker,position)
        display_board(board)
        
        # Check if someone won
        if win_check(board,marker):
            break
    
        # Change marker
        if marker == 'X':
            marker = 'O'
        elif marker == 'O':
            marker = 'X'
    
    # While ended due to full stacking
    if board_full:
        print ("Board is full, nobody win, both losers :P")
       
    # Replay?
    if not replay():
        break
    X
print("Thank you for playing with us machine!")

        
    