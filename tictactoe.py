import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'    

def player_input():
    marker= False
    while marker!=True:
        p1=input('choose X or O')
        p1=p1.upper()
        if p1.upper()=="X" or p1.upper()=="O":
            marker=True
    if p1.upper()=="X" :
        p2="O"
    else:
        p2="X"
    return (p1,p2) 
    
def display_board(board):
    print(board[7]+"|"+board[8]+"|"+board[9])
    print(board[4]+"|"+board[5]+"|"+board[6])
    print(board[1]+"|"+board[2]+"|"+board[3]) 

    

def place_marker(board,marker,position):
    board[position]=marker

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
    return position

def replay():
    ch=input('Do you want to play again? Enter Yes or No: ')
    if ch=='Yes':
        return True
    else:
        return False

while True:
    the_board=[' '] * 10
    print('Tic tac toe')
    p1_marker,p2_marker=player_input()
    ch= input("enter True if you want to play or false")
    turn=choose_first()
    print(turn + "will go first")

    while ch:
        if turn=="Player 1":
            display_board(the_board)
            position= player_choice(the_board)
            place_marker(the_board,p1_marker,position)
            if win_check(the_board,p1_marker):
                display_board(the_board)
                print("you've won")
                ch=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("draw")
                    break
                else:
                    turn="Player 2"
        else:
            display_board(the_board)
            position= player_choice(the_board)
            place_marker(the_board,p2_marker,position)
            
            if win_check(the_board,p2_marker):
                display_board(the_board)
                print("you've won")
                ch=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("draw")
                    break
                else:
                    turn="Player 1"
        
    if not replay():
        break


   
