"""
* Scratch_n_sketch scripting
* Sketch demo
"""

#init
mbd = scratch_n_sketch()
#connect
mbd.connect()
#start
console('Date and Time Demo')
#initialize
mbd.backGroundColor(255, 255, 255)
mbd.textBackColor(255, 255, 255)
mbd.setFont(mbd.comic_sans)
mbd.rotateDisplay(mbd.rotate_0)
#rotate by 90 deg
wait(5)
#draw date
mbd.penColor(255, 0, 0)
cr = time.strftime('%b-%d-%Y', time.localtime())
mbd.drawText(cr.upper(), 40, 100)
#time color
mbd.penColor(0, 0, 255)
#show time forever
while(1):
    #draw time
    cr = time.strftime('%H:%M:%S', time.localtime())
    mbd.drawText(cr, 70, 140)
    #delay for 1000ms/1 second
    wait(1000)
#disconnect port 
mbd.disconnect()