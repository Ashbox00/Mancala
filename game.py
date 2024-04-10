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


def draw_board():
    print(f'|{board[0][0]}|{board[0][1]}|{board[0][2]}|{board[0][3]}|{board[0][4]}|{board[0][5]}|')
    print(f'|{board[1][0]}|{board[1][1]}|{board[1][2]}|{board[1][3]}|{board[1][4]}|{board[1][5]}|')



draw_board()
move_piece(0,0)
draw_board()
#check_board_empty()