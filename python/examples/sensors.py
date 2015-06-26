#Scratch_n_sketch scripting

board = scratch_n_sketch()
#auto find and connect board
board.connect()
#set colors,  backgroung, textbackcolor and pen
board.backGroundColor(0, 0, 0)
board.textBackColor(0, 0, 0)
board.penColor(0, 255, 255)
#font small
board.setFont(board.font_small)
#rotate display 0 degrees
board.rotateDisplay(board.rotate_0)
#headers
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
    #show light sensor
    board.drawText('{:04d}'.format(board.lightSensor), 35, 50)
    #show touch x and y pos
    board.drawText('x : {0:03d}  y : {1:03d}'.format(board.touchX, board.touchY), 55, 120)
    #show remote code
    board.drawText(board.remoteCode, 95, 190)
    #show angle sensor value
    board.drawText('{:04d}'.format(board.angleSensor), 155, 50)
    #show switch one status
    board.drawToggleIcon(45, 250, board.SwitchOne)
    #show switch two status
    board.drawToggleIcon(175, 250, board.SwitchTwo)
    #wait for 100ms
    wait(100)
#disconnect board
board.disconnect()