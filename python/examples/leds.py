#Scratch_n_sketch scripting

mbd = scratch_n_sketch()
mbd.connect()

while True:
    mbd.ledWrite(Green, On)
    mbd.ledWrite(Blue, Off)
    mbd.ledWrite(Red, Off)
    wait(1000)
    
    mbd.ledWrite(Green, Off)
    mbd.ledWrite(Blue, On)
    mbd.ledWrite(Red, On)
    wait(100)

mbd.disconnect()