#Scratch_n_sketch scripting

board = scratch_n_sketch()
board.connect()
board.backGroundColor(0, 0, 0)
board.textBackColor(0, 0, 0)
board.setFont(board.font_big)
board.rotateDisplay(board.rotate_0)
board.penColor(255, 255, 0)
board.drawText('Temp sensor : TMP36', 40, 50)
voltage = 0
celcius = 0
farenheit = 0
board.setFont(board.calibri)
while True:
    board.getSensorData()
    #convert ADC output to millivolts
    voltage = ((board.A1*5)/1024)*1000
    board.drawText('{0}{1:.2f}'.format('V  : ', voltage), 20, 100)
    #get temp in celcius
    celcius = (abs(voltage-500))/10
    board.drawText('{0}{1:.2f}'.format('oC : ', celcius), 20, 140)
    #farenheit
    farenheit = (celcius*9.0/5.0)+32
    board.drawText('{0}{1:.2f}'.format('F  : ', farenheit), 20, 180)
    #wait for 250 ms
    wait(250)
    #disconnect board
board.disconnect()