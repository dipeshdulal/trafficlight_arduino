# to turn on and off the traffic lights
from arduino_vehicle import writeToArduino
import time

# default toggle should be called in a loop
# for the traffic light to function
def defaultToggle(is_default, str = 1, sleepTime = 60):
	'To default toggle the lights'
	if not(is_default):
		return
	else:
		if str == 4:
			writeToArduino("aBcdEfgHijkl")
			time.sleep(1)
			writeToArduino("abCdeFghIJkl")
		elif str == 3:
			writeToArduino("aBcdEfgHijkl")
			time.sleep(1)
			writeToArduino("abCdeFGhijkL")
		elif str == 2:
			writeToArduino("aBcdEfgHijkl")
			time.sleep(1)
			writeToArduino("abCDefghIjkL")
		elif str == 1:
			writeToArduino("aBcdEfgHijkl")
			time.sleep(1)
			writeToArduino("AbcdeFghIjkL")
		time.sleep(sleepTime)
# writeToArduino("ABCDefghijkl")

i = 1;
while True:
	defaultToggle(True, i, 10)
	i = i + 1
	if i == 3:
		i = 1