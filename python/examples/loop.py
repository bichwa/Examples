#Scratch_n_sketch scripting

#init
mbd = scratch_n_sketch()
#connect board
mbd.connect()
#start
mbd.backGroundColor(0, 0, 0)
mbd.textBackColor(0, 0, 0)
mbd.penColor(0, 255, 255)
mbd.setFont(mbd.font_big)
mbd.rotateDisplay(mbd.rotate_0)
#draw some text
mbd.drawText('Scratch n sketch demo', 20, 50)
wait(5)
#loop 0-100
for x in range(0, 101):
    #draw loop numbers
    mbd.drawText(join('Please wait : ', 
                join(x, '%')), 20, 80)
    #delay a bit
    wait(20)
#script done
for i in range(0, 3):
    mbd.drawText('Done', 20, 110)
#disconnect port
mbd.disconnect()
