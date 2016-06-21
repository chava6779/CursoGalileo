import mraa
import time
import pyupm_i2clcd as lcd 

myLcd = lcd.Jhd1313m1(0,0x3E, 0x62)
myLcd.setCursor(0,0)
myLcd.setColor(0,0,255)
myLcd.write('VOLTAJE : ')

try:
        pinsensor = mraa.Aio(0)
        pinsensor.setBit(12)
        while True:
                valorsensor = pinsensor.read()
		myLcd.setCursor(1,0)
                myLcd.write("%.6f"%(valorsensor /819.0))
                time.sleep(1)
except:
	myLcd.setCursor(1,0)
        myLcd.write( "SEGURO QUE TIENES UN VOLTAJE?")






