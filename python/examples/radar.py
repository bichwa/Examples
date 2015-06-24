"""
*Scratch_n_sketch scripting
* Matrix demo
"""

#init
mbd = scratch_n_sketch()
#connect
mbd.connect()
#start
console('Radar scanning demo')
#initialize
mbd.backGroundColor(255, 255, 255)
mbd.textBackColor(255, 255, 255)
mbd.setFont(mbd.ocr_extended)
#rotate by 90 deg
wait(5)
mbd.rotateDisplay(mbd.rotate_0)
#variables
rad = 5
#start loop
for x in range(0, 10):
    #select a random pen color
    mbd.penColor(20, 20, 20)
    mbd.drawText('Scanning .... ', 60, 10)
    for y in range(0, 6):
        mbd.drawCircle(120, 150, rad)
        rad += 16
        wait(100)
    mbd.penColor(255, 255, 255)
    mbd.fillRectangle(20, 40, 230, 300)
    wait(50)
    rad = 5
#disconnect port 
mbd.disconnect()

        
        
