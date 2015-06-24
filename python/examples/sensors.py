#Scratch_n_sketch scripting

board = scratch_n_sketch()
board.connect()
board.backGroundColor(0, 0, 0)
board.textBackColor(0, 0, 0)
board.penColor(0, 255, 255)
board.setFont(board.font_small)
board.rotateDisplay(board.rotate_0)
board.drawText('Luminance', 20, 30);
board.drawText('Touch', 95, 100);
board.drawText('Remote', 85, 170);
board.drawText('Encoder', 150, 30);
board.drawText('Button 1', 20, 230);
board.drawText('Button 2', 150, 230);
#loop checking sensor data
while True:
    #get sensor data
    board.getSensorData()
    board.drawText(board.lightSensor, 35, 50)
    board.drawText('x : {0}  y : {1}'.format(board.touchX, board.touchY), 55, 120)
    board.drawText(board.remoteCode, 95, 190)
    board.drawText(board.angleSensor, 155, 50)
    board.drawToggleIcon(45, 250, board.SwitchOne)
    board.drawToggleIcon(175, 250, board.SwitchTwo)
    #wait for 100ms
    wait(100)
#disconnect board
board.disconnect()