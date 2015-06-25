from board import *
#Scratch_n_sketch scripting

board = scratch_n_sketch()

board.connect()

for i in range(101):
    board.doutWrite(board.Do1, On)
    wait(50)
    board.doutWrite(board.Do1, Off)
    wait(50)
    
board.disconnect()