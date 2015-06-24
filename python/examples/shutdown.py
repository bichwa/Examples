#Scratch_n_sketch scripting

mbd = scratch_n_sketch()
mbd.connect()
wait(1)
mbd.powerControl(mbd.power_on);
wait(3000)
mbd.backGroundColor(255, 255, 255)
mbd.textBackColor(255, 255, 255)
mbd.penColor(255, 0, 0)
mbd.setFont(mbd.font_small)
mbd.rotateDisplay(mbd.rotate_0)
wait(5)
mbd.drawText('Shutting down in 10 seconds', 20, 50)

for i in range(10):
    mbd.drawText(i, 110, 80)
    wait(1000)
mbd.ledWrite(All, Off)
mbd.powerControl(mbd.power_off);
mbd.disconnect()

