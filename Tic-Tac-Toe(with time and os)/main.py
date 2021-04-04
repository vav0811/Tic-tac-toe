from random import randrange
import os
import time

def DisplayBoard(board):
    # the function accepts one parameter containing the board's current status
    # and prints it out to the console

    

    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[0][0], "  |  ", board[0][1], "  |  ", board[0][2], "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[1][0], "  |  ", board[1][1], "  |  ", board[1][2], "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", board[2][0], "  |  ", board[2][1], "  |  ", board[2][2], "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

def EnterMove(board):

    # the function accepts the board current status, asks the user about their move,
    # checks the input and updates the board according to the user's decision

    while True:
        move=int(input("Enter a number corresponding to the square you want to select(i.e 1-9): "))
        if (move<1 or move>9):
            print("\n************************ Please enter a number between 1 and 9 only************************ \n")
            continue
        elif (move not in board[0] and move not in board[1] and move not in board[2]):
            print("\n************************ Spot already occupied select another option ************************\n")
            continue

        for row in range(3):
            for col in range(3):
                if board[row][col]==move:
                    board[row][col] = 'O'
        break


def MakeListOfFreeFields(board):

    # the function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers


    global free
    free=[]
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X' or board[row][col] == 'O':
                pass
            else:
                free.append(([row],[col]))
    print(free)


def VictoryFor(board, sign):

    # the function analyzes the board status in order to check if
    # the player using 'O's or 'X's has won the game

    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        return True
    elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        return True
    elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        return True
    elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        return True
    elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        return True
    elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        return True
    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True


def DrawMove(board):

    # the function draws the computer's move and updates the board

    while True:
        row = randrange(3)
        col = randrange(3)
        if ([row],[col]) not in free:
            continue
        else:
            board[row][col]='X'
            return

board=[[1,2,3],[4,'X',6],[7,8,9]]
totalmoves=1
player='O'
comp='X'

print("!!!!!!!!!!!!!!!!!!!!!!!!!!!   WELCOME TO TIC-TAC-TOE   !!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
print("\n\n\n               YOUR SYMBOL IS 'O' \n")
DisplayBoard(board)
while totalmoves<9:
    EnterMove(board)
    totalmoves+=1
    os.system("cls")
    DisplayBoard(board)
    if VictoryFor(board,player) == True:
        os.system("cls")
        print("You are the winner!!!")
        DisplayBoard(board)
        time.sleep(10)
        break
    else:
        os.system("cls")
        print("The current status of board after Your turn and list of free space are:\n")
        DisplayBoard(board)
        print("\nFree spaces:")
        MakeListOfFreeFields(board)

    print("\n************ Computer's turn *************")
    DrawMove(board)
    totalmoves+=1
    os.system("cls")
    DisplayBoard(board)
    if VictoryFor(board,comp) == True:
        os.system("cls")
        print("Computer is the winner!!! \n YOU LOSE")
        DisplayBoard(board)
        time.sleep(10)
        break
    else:
        os.system("cls")
        print("The current status of board after Computer's turn and list of free space are:\n")
        DisplayBoard(board)
        print("\nFree spaces:")
        MakeListOfFreeFields(board)
        print()

else:
    print("Its a tie!!")
    time.sleep(10)
    DisplayBoard(board)
print("Thank you for playing")
