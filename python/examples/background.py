"""
*Scratch_n_sketch scripting
* Background demo
"""

#init
mbd = scratch_n_sketch()
#connect board
mbd.connect()
#start
#initialize
for i in  range(0, 20):
    mbd.backGroundColor(randomNumber(0, 255),
                        randomNumber(0, 255),
                        randomNumber(0, 255))
    wait(1000)
mbd.disconnect()

        
        
