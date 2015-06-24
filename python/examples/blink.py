#Scratch_n_sketch scripting
board = scratch_n_sketch()
#find and connect board
board.connect()
board.backGroundColor(255, 255, 255)
board.textBackColor(255, 255, 255)
board.penColor(0, 0, 0)
board.rotateDisplay(board.rotate_0)
board.drawText("Scratch n Sketch", 40, 130)
for blink in range(1001):
    board.ledWrite(Red, On)
    wait(50)
    board.ledWrite(Red, Off)
    wait(50)
    board.drawText(blink, 100, 170)
#disconnect
board.disconnect()
