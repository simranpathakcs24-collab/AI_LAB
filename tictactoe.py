import random
import time

def printboard(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]} |")
    #print("--- | --- | --- |")
    print(f"{board[3]} | {board[4]} | {board[5]} |")
    #print("--- | --- | --- |")
    print(f"{board[6]} | {board[7]} | {board[8]} |")
    print("\n")

def checkwin(board, player):
    win=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for condition in win:
        if board[condition[0]]== board[condition[1]]==board[condition[2]] ==player:
            return True
    return False

def checkdraw(board):
    return all(space in ['X' , 'O'] for space in board)

def getemptyspaces(board):
    return [i for i,space in enumerate(board) if space not in ['X' , 'O']]

def tictactoe():
    board = [str(i) for i in range (1,10)]
    print ("welcome , game starts")
    printboard(board)
    humanmarker=""
    while humanmarker not in ['X', 'O']:
        humanmarker=input("do you want to be player x or player o").strip().upper()
    aimarker='O' if humanmarker == 'X' else 'X'
    currentplayer='X'
    while True:
        if currentplayer==humanmarker:
            choice =int(input("your turn, enter the position where you want to place(1-9)")) -1
            if choice<0 and choice> 8:
                print("invalid")
                continue
            if board[choice] in ['X', 'O']:
                print("al;ready occupied")
                continue
            board[choice]=humanmarker
            printboard(board)
        else:
            print("systems turn")
            time.sleep(1)
            emptyspaces=getemptyspaces(board)
            aichoice=random.choice(emptyspaces)
            board[aichoice]=aimarker
            printboard(board)
        if checkwin(board,currentplayer):
            if currentplayer ==humanmarker:
                print("you won")
                break
            else:
                print("system won")
                break
        if checkdraw(board):
            print("tie")
            break
       
        currentplayer=aimarker if currentplayer==humanmarker else humanmarker

tictactoe()
            
