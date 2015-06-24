"""
*Scratch_n_sketch scripting
* Matrix demo
"""
#init
mbd = scratch_n_sketch()
#connect board
mbd.connect()
#start
console('Random Rectangles demo')
#initialize colors
mbd.backGroundColor(255, 255, 255)
#rotate 90 degrees
mbd.rotateDisplay(mbd.rotate_90)
#delay for 5ms
wait(5)
#variables
y = 0
x = 0
#loop drawing random rectangles
for i in range(0, 50):
    for j in range(0, 20):
        #random pen color
        mbd.penColor(randomNumber(0, 255),
                    randomNumber(0, 255),
                    randomNumber(0, 255))
        #draw fill round rectangle of random size
        mbd.drawRoundRectangle(x, y, 
                         (x+randomNumber(5, 41)),
                         (y+randomNumber(5, 41)))
        #set a random position
        x = randomNumber(20, 301)
        y = randomNumber(20, 221)
        #animate drawing with a 100 ms delay
        wait(100)
    #set background color to white
    mbd.backGroundColor(255, 255, 255)
    wait(5)
#disconnect from port
mbd.disconnect()

        
        
