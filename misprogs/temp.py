
import signal
import sys
import time
import pyupm_grove as grove
import pyupm_i2clcd as lcd

def interruptHandler(signal, frame):
        sys.exit(0)
if __name__ == '__main__':
        signal.signal(signal.SIGINT, interruptHandler)
        myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
        sensortemp = grove.GroveTemp(0)
        colorR = 255;
        colorG = 0;
        colorB = 0;
        myLcd.setColor(colorR,colorG,colorB)

