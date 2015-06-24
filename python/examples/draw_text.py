"""
* scratch_n_ sketch
*
* simple demo scripting in python language
*
"""
from board import *

#init
mbd = scratch_n_sketch()
#connect board
mbd.connect()
#start
print('Draw Text demo')
#clear screen
#myBoard.clearScreen()
mbd.backGroundColor(20, 20, 20)
mbd.textBackColor(20, 20, 20)
mbd.setFont(mbd.font_big);
mbd.rotateDisplay(mbd.rotate_270)
#delay a bit
wait(1)
#draw rectangle
mbd.penColor(0, 255, 255);
mbd.drawRectangle(40, 70, 255, 160)
wait(1);
#write text 1 
mbd.penColor(150, 150, 150)
mbd.drawText('* Scratch-N-Sketch Demo', 50, 80)
#delay
wait(1)
#print text 2
mbd.penColor(255, 55, 240)
mbd.drawText('* Please wait ....', 50, 110)
#delay
wait(1)
#print number 0 to 100
for x in range(0,101):
    #print new number
    mbd.drawText(join(x, ' %') , 210, 115)
    #generate a random colour
    """myBoard.penColor(randomNumber(0, 255),
                     randomNumber(0, 255), 
                     randomNumber(0, 255))"""
    #a 200 ms short delay
    wait(20)
#print text 3
wait(1)
mbd.penColor(255, 255, 0)
for i in range(1,3):
    mbd.drawText('* Done . Bye!', 50, 140)
#disconnect board """
mbd.disconnect()
