#Scratch_n_sketch scripting
board = scratch_n_sketch()
#auto find and connect board
board.connect()
#set background color
board.backGroundColor(255, 255, 255)
#set textbackcolor
board.textBackColor(255, 255, 255)
#set pen color
board.penColor(0, 0, 0)
#rotate display at 0
board.rotateDisplay(board.rotate_0)
#draw text at pos 40, 130
board.drawText("Scratch n Sketch", 40, 130)
#blink for 100 times
for blink in range(1001):
    #set red led on
    board.ledWrite(Red, On)
    #wait 50ms
    wait(50)
    #set red led off
    board.ledWrite(Red, Off)
    #waut 50ms
    wait(50)
    #draw number of blinks at pos 100, 170
    board.drawText(blink, 100, 170)
#disconnect
board.disconnect()
