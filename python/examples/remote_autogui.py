#Scratch_n_sketch scripting
import pyautogui
pyautogui.FAILSAFE = false

board = scratch_n_sketch()
board.connect()
board.backGroundColor(0, 0, 0)
board.textBackColor(0, 0, 0)
board.setFont(board.font_small)
board.rotateDisplay(board.rotate_0)
board.penColor(255, 255, 0)
board.drawText('REMOTE CONTROL', 50, 140)
rc1 = 0
rc2 = 0
while True:
    board.getSensorData()
    rc1 = board.remoteCode
    if not (rc1==rc2):
        #volume up
        if rc1 == '6C90':
            pyautogui.press('volumeup')
            board.ledWrite(Red, On)
        #volume down
        elif rc1 == 'CC30':
            pyautogui.press('volumedown')
            board.ledWrite(Green, On)
        #backspace
        elif rc1 == '9C60':
            pyautogui.press('space')
            board.ledWrite(Blue, On)
        #right
        elif rc1 == 'AC50':
            pyautogui.press('right')
            board.ledWrite(Green, On)
        #left
        elif rc1 == '8C70':
            pyautogui.press('left')
            board.ledWrite(Green, On)
        #copy rc2 to rc1
        rc2 = rc1
    wait(50)
    board.ledWrite(All, Off)
    wait(50)
    #disconnect board
board.disconnect()