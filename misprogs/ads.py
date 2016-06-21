import mraa
import time

try:
	pinsensor = mraa.Aio(0)
	pinsensor.setBit(12)
	while True:
		valorsensor = pinsensor.read()
		print "%.6f"%(valorsensor /819.0)
		time.sleep(1)
except:
	print "SEGURO QUE TIENES UN VOLTAJE?"
		
