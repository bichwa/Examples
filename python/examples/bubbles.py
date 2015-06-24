"""
* scratch_n_ sketch
*
* simple demo scripting in python language
*
"""
#init
mbd = scratch_n_sketch()
#connect board
mbd.connect()
#start
print('scratch_n_sketch')
print('Bubbles demo')
#set background color
mbd.backGroundColor(255, 255, 255)
#rotate the displays
mbd.rotateDisplay(mbd.rotate_270)
#delay
wait(1)
#show 50 times
for i in range(0, 50):
    #set the number of circles randomly
    num = randomNumber(5, 30)
    #draw circles
    for x in range(0, num):
        #set random pen color
        mbd.penColor(randomNumber(0, 255), 
                        randomNumber(0, 255), 
                        randomNumber(0, 255)) 
        #draw a circle at random pos and radius
        mbd.fillCircle(randomNumber(20, 300), 
                           randomNumber(20, 200),
                           randomNumber(5, 20))
        #animate with a delay
        mbd.ledWrite(Blue, On)
        wait(25)
        mbd.ledWrite(Blue, Off)
        wait(25)
    #clear everything
    mbd.backGroundColor(255, 255, 255)
    wait(1)
#disconnect board """
mbd.disconnect()
