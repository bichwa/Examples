#Scratch_n_sketch scripting

#init
mbd = scratch_n_sketch()
#connect board
mbd.connect()
#rotate display
mbd.rotateDisplay(mbd.rotate_270)
#wait for 1ms
wait(1)
#console
console('Draw calendar demo')
"""
show calendar
date (1 - 28/30/31) ,
day of week (1 - 7) [sun = 1, sat=7],
month(1-12), 
redraw(1/0)
"""
mbd.showCalendar(30, 4, 1, 0);
#disconnect board
mbd.disconnect()