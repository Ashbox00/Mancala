from player import Player

#bring in the player class and initialize them
Player1 = Player()
Player2 = Player()

#initialze the board at start of game
board = [[5,0,0,0,0,0],
         [0,0,0,0,0,0]]


def move_piece(y,x):
    marble_amount = int(board[y][x])
    board[y][x] = 0
    if y == 0:
        for amount in range(1,marble_amount):
            board[y][x+amount] += 1

            if x+amount >= len(board[0]):
                pass
                #figure out how to flip board when it goes over
            
        # alternative side of board version
    
# not working its going out of range (did -1 on ranges still not working as intended)
def check_board_empty():
    Empty:bool = False
    for i in range(len(board[0])):
        for j in range(len(board[1])):
            if board[i][j] > 0:
                Empty = True
                break
            else:
                pass

    if Empty == False:
        print("All Empty")
    else:
        print("Not empty")

#works fine 
def draw_board():
    print(f'Player 1 |{board[0][0]}|{board[0][1]}|{board[0][2]}|{board[0][3]}|{board[0][4]}|{board[0][5]}|  Player 2')
    print(f'   {Player1.pool}     |{board[1][0]}|{board[1][1]}|{board[1][2]}|{board[1][3]}|{board[1][4]}|{board[1][5]}|      {Player2.pool}')



draw_board()

#check_board_empty()