# to turn on and off the traffic lights
from arduino_vehicle import writeToArduino
import time

# default toggle should be called in a loop
# for the traffic light to function
def defaultToggle(is_default, str = "t1"):
	'To default toggle the lights'
	if not(is_default):
		return
	else:
		if str == "t3":
			writeToArduino("aBcdEfgHijkl")
			time.sleep(1)
			writeToArduino("abCdeFGhijkl")
		elif str == "t2":
			writeToArduino("aBcdEfgHijkl")
			time.sleep(1)
			writeToArduino("abCDefghIjkl")
		elif str == "t1":
			writeToArduino("aBcdEfgHijkl")
			time.sleep(1)
			writeToArduino("AbcdeFghIjkl")
		time.sleep(60)
