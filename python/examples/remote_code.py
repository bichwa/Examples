#Scratch_n_sketch scripting

board = scratch_n_sketch()
board.connect()
board.backGroundColor(0, 0, 0)
board.textBackColor(0, 0, 0)
board.penColor(0, 255, 255)
board.rotateDisplay(board.rotate_0)
#loop checking sensor data
while True:
    #get sensor data
    board.getSensorData()
    #get remote code
    rc = board.remoteCode
    if not rc == '0':
        board.drawText(join('Code : ', rc), 50, 150)
    #wait for 100ms
    wait(100)
#disconnect board
board.disconnect()