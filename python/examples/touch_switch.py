#Scratch_n_sketch scripting

board = scratch_n_sketch()
board.connect()
board.backGroundColor(0, 0, 0)
board.textBackColor(50, 50, 50)
board.penColor(50, 50, 50)
board.setFont(board.comic_sans) 
board.rotateDisplay(board.rotate_0)
board.fillRoundRectangle(10, 250, 115, 300);
board.fillRoundRectangle(120, 250, 230, 300);
board.penColor(255, 0, 0)
board.drawText('On',  50 , 270)
board.penColor(0, 255, 0)
board.drawText('Off', 150 , 270)
board.penColor(255, 255, 0)
board.textBackColor(0, 0, 0)
xpos = 0
ypos = 0
board.setFont(board.font_small)
while True:
    board.getSensorData()
    xpos = board.touchX
    ypos = board.touchY
    board.drawText('x : {0}  y : {1}'.format(xpos, ypos), 50, 120)
    if (xpos>153 and xpos<482) and (ypos>766 and ypos<910):
        board.ledWrite(Green, On)
    if (xpos>527 and xpos<865) and (ypos>766 and ypos<910):
        board.ledWrite(Green, Off)
    wait(50)
#disconnect board
board.disconnect()