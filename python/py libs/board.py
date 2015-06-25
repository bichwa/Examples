"""
*
* scratch_n_sketch
*
* (c) 2015 wwww.warefab.com
*
"""

import threading
import serial
import sys
import os
import time, datetime
from random import randint
from enum import Enum

import commands
from list_ports import *

#leds
Red = 'r'
Green = 'g'
Blue = 'b'
All = 'a'

On = 255
Off = 0

#utils 
#generate random number
def randomNumber(start, end):
    return randint(start, end)
#end

#join two objects
def join(token1, token2):
    return '{0}{1}'.format(token1, token2)
#end

#delay milliseconds
def wait(millis):
    time.sleep((millis/1000))
#end

#write message to console
def console(message):
	print(message)
	sys.stdout.flush()
#end
#region fonts
class Fonts:
    calibri         = 'c'
    calibri_light   = 'i'
    digital         = 'd'
    ocr_extended    = 'o'
    font_big        = 'f'
    font_small      = 'g'
    comic_sans      = 's'
#end


#region fonts
class Control:
    rotate_0    = 'p'
    rotate_90   = 'i'
    rotate_180  = 'q'
    rotate_270  = 'n'
    clear_display = 'c'
    power_off = 'f'
    power_on = 'o'
    Do1 = 'h'
    Do2 = 'l'
#end

#sensor info
    """
class SensorInfo:
    angleSensor = 0
    lightSensor = 0
    A1 = 0
    A2 = 0
    SwitchOne = 0
    SwitchTwo = 0
    Do2 = 0
    Do1 = 0
    remoteCode = 0"""
#end
    
class BoardNotFound(Exception): pass

#end utils
false = 0
true = 1
#board class
class scratch_n_sketch(Fonts, Control):
    angleSensor = 0
    lightSensor = 0
    A1 = 0
    A2 = 0
    SwitchOne = 0
    SwitchTwo = 0
    Di2 = 0
    Di1 = 0
    remoteCode = 0
    touchX = 0
    touchY = 0
    
    #initialize
    def __init__(self):
        self.errorMsg = 'none'
        #self.ser = serial.Serial(port, 230400, timeout=1)
        #self.ser.close()
    #end
    
    def connect(self, port = 'p'):
        try:
            if len(port) > 1:
                self.ser = serial.Serial(port, 230400, timeout=1)
                self.ser.close()
            else:
                ports = serial_ports()
                if len(ports) > 0:   
                    cpt = find_port(ports)
                    if ('COM' or 'dev') in cpt:
                        console('Board connected successfully!') # : ' + cpt)
                        self.ser = serial.Serial(cpt, 230400, timeout=1)
                        self.ser.close();
                else:
                    raise BoardNotFound#Exception('Board not found')
        except:
            console('cant find board! please reconnect it.')
            os._exit(0)
            
    #send helper
    def sendHelper(self, out):
        try:
            if not self.ser.isOpen():
                    self.ser.open()
            #self.ser.flushOutput()
            self.ser.write(('<' + out + '>').encode())
            self.ser.flush()
        except:
            os._exit(0)
    #end

    #populate sensor info
    def __populateSensorData(self, data):
        if data[0] == 'a' and len(data) == 12:
            self.angleSensor = int(data[1])
            self.lightSensor = int(data[2])
            self.A1 = int(data[3])
            self.A2 = int(data[4])
            self.SwitchOne = int(data[5])
            self.SwitchTwo = int(data[6])
            self.Di2 = int(data[7])
            self.Di1 = int(data[11])
            self.remoteCode = data[8]
            self.touchX = int(data[9])
            self.touchY = int(data[10])
    #end
            
    #get sensor data
    def getSensorData(self):
        try:
            if not self.ser.isOpen():
                    self.ser.open()
            self.ser.write(b'<0xE0>')
            self.ser.flush()
            sensors = (str(self.ser.readline(), 'utf8')).split(',')
            """while (not (len(sensors) == 10)) and blocking == True:
                self.ser.write(b'<0xE0>')
                sensors = (str(self.ser.readline(), 'utf8')).split(',')
            """
            self.__populateSensorData(sensors)
        except:
            console('Failed to retrieve sensor info')
            pass
            
    #clear screen
    def clearScreen(self):
        data = '{0}|{1}'.format(commands.ctl, 'c')
        self.sendHelper(data)
        #self.errorMsg = 'Failed to clear screen'
    #end

    #clear screen
    def doutWrite(self, l, x):
        data = '{0}|{1}|{2}'.format(commands.dout, l, x)
        self.sendHelper(data)
    #end

    #change background color
    def backGroundColor(self, r, g, b):
        data = '{0}|{1}|{2}|{3}'.format(commands.fsc, r, g, b)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to set background color'
    #end

    #change pen color
    def penColor(self, r, g, b):
        data = '{0}|{1}|{2}|{3}'.format(commands.pen, r, g, b)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to set pen color'
    #end

    #change text back color
    def textBackColor(self, r, g, b):
        data = '{0}|{1}|{2}|{3}'.format(commands.tbc, r, g, b)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to set text back color'
    #end

    #draw text
    def drawText(self, text, xpos, ypos):
        data = '{0}|{1}|{2}|{3}'.format(commands.txt, text, 
                                        xpos, ypos)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #erase text from specified position
    def eraseText(self, num, xpos, ypos):
        data = '{0}|{1}|{2}|{3}'.format(commands.ers, num, 
                                        xpos, ypos)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #draw filled rectangle
    def drawLine(self, x1, y1, x2, y2):
        data = '{0}|{1}|{2}|{3}|{4}'.format(commands.drl, x1, y1, x2, y2)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end
        
    #draw filled rectangle
    def fillRectangle(self, x1, y1, x2, y2):
        data = '{0}|{1}|{2}|{3}|{4}'.format(commands.frt, x1, y1, x2, y2)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #draw empty rectangle
    def drawRectangle(self, x1, y1, x2, y2):
        data = '{0}|{1}|{2}|{3}|{4}'.format(commands.drt, x1, y1, x2, y2)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #draw empty round rectangle
    def fillRoundRectangle(self, x1, y1, x2, y2):
        data = '{0}|{1}|{2}|{3}|{4}'.format(commands.frr, x1, y1, x2, y2)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #draw filled round rectangle
    def drawRoundRectangle(self, x1, y1, x2, y2):
        data = '{0}|{1}|{2}|{3}|{4}'.format(commands.drr, x1, y1, x2, y2)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #draw filled circle
    def fillCircle(self, x, y, r):
        data = '{0}|{1}|{2}|{3}'.format(commands.fcr, x, y, r)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #draw empty circle
    def drawCircle(self, x, y, r):
        data = '{0}|{1}|{2}|{3}'.format(commands.dcr, x, y, r)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #draw filled ellipse
    def fillEllipse(self, x, y, w, h):
        data = '{0}|{1}|{2}|{3}|{4}'.format(commands.fep, x, y, w, h)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #draw empty ellipse
    def drawEllipse(self, x, y, w, h):
        data = '{0}|{1}|{2}|{3}|{4}'.format(commands.dep, x, y, w, h)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #draw battery level icon
    def drawBatteryIcon(self, x, y, l):
        data = '{0}|{1}|{2}|{3}'.format(commands.bli, x, y, l)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #draw progress bar icon
    def drawProgressIcon(self, x, y, l):
        data = '{0}|{1}|{2}|{3}'.format(commands.pgi, x, y, l)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #draw toggle icon
    def drawToggleIcon(self, x, y, st):
        data = '{0}|{1}|{2}|{3}'.format(commands.tgi, x, y, st)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #show calendar icon
    def showCalendar(self, dt, wk, mth, rh):
        data = '{0}|{1}|{2}|{3}|{4}'.format(commands.cal, dt,
                                        wk, mth, rh)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #set font
    def setFont(self, x):
        data = '{0}|{1}'.format(commands.fnt, x)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #rotate display
    def rotateDisplay(self, x):
        data = '{0}|{1}'.format(commands.ctl, x)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #rotate display
    def powerControl(self, x):
        data = '{0}|{1}'.format(commands.ctl, x)
        self.sendHelper(data)
        #self.errorMsg = 'Failed to draw text'
    #end

    #rotate display
    def ledWrite(self, l, x):
        data = '{0}|{1}|{2}'.format(commands.led, l, x)
        self.sendHelper(data)
        wait(1)
        #self.errorMsg = 'Failed to draw text'
    #end
        
    #disconnect board
    def disconnect(self):
        try:
            if self.ser.isOpen():
                self.ser.close()
        except:
            console('Failed to disconnect board')
            os._exit(0)
    #end
#end board class    
        
        
    
