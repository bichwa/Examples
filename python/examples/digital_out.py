#Scratch_n_sketch scripting

board = scratch_n_sketch()
#connect board
board.connect()
#loop 10 times
for i in range(101):
    #digital out 1 to on
    board.doutWrite(board.Do1, On)
    #wait 50ms
    wait(50)
    #digital out 2 to off
    board.doutWrite(board.Do1, Off)
    #wait 50ms
    wait(50)
#disconnect board   
board.disconnect()