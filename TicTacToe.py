#TicTacToe.
import sys

theBoard = {'1': '1', '2': '2', '3': '3',
            '4': '4', '5' : '5', '6': '6',
            '7': '7', '8' : '8', '9': '9'}

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


def checkWin(board,turn):
    if ( theBoard['1'] == theBoard['2'] == theBoard['3'] or 
         theBoard['4'] == theBoard['5'] == theBoard['6'] or 
         theBoard['7'] == theBoard['8'] == theBoard['9'] or 
         theBoard['1'] == theBoard['4'] == theBoard['7'] or 
         theBoard['3'] == theBoard['6'] == theBoard['9'] or 
         theBoard['2'] == theBoard['5'] == theBoard['8'] or 
         theBoard['1'] == theBoard['5'] == theBoard['9'] or 
         theBoard['3'] == theBoard['5'] == theBoard['7']) :
             print(turn + ' WINS!!')
             sys.exit()
         
printBoard(theBoard)
turn = 'X'
for i in range(9):    
    print('It is your turn to play ' + turn)
    move = input()
    theBoard[move] = turn    
    printBoard(theBoard)
    checkWin(theBoard,turn)
    if( turn == 'X'):
        turn = 'O'
    else:
        turn = 'X'
print('ITS A DRAW!!!')

