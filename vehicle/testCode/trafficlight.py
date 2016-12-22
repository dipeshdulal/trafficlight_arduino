from traffic_light import defaultToggle
from datetime import datetime
import time


date = datetime.now()
previousTime = date.second

while True:
	date = datetime.now()
	vehicle1 = open("1.txt", "r")
	vehicle2 = open("2.txt", "r")
	vehicle3 = open("3.txt", "r")
	currentTime = date.second
	deltaTime = currentTime - previousTime
	if (deltaTime >= 5):

		car1 = int(vehicle1.read())
		car2 = int(vehicle2.read())
		car3 = int(vehicle3.read())
		
		# 1
		if ((car1 < 2) and (car2 < 2) and (car3 < 2)):
			defaultToggle(True, 3, 2)
		# 2
		if ((car1 > 2) and (car2 < 2) and (car3 < 2)):
			defaultToggle(True, 3, 2)
		# 3
		if ((car1 < 2) and (car2 > 2) and (car3 < 2)):
			defaultToggle(True, 2, 2)
		# 4
		if ((car1 < 2) and (car2 < 2) and (car3 > 2)):
			defaultToggle(True, 1, 2)
		# 5
		if ((car1 > 2) and (car2 > 2) and (car3 < 2)):
			defaultToggle(True, 3, 2)
		# 6
		if ((car1 > 2) and (car2 < 2) and (car3 > 2)):
			defaultToggle(True, 3, 2)
		# 7
		if ((car1 < 2) and (car2 > 2) and (car3 > 2)):
			defaultToggle(True, 1, 2)
		# 8
		if ((car1 > 2) and (car2 > 2) and (car3 > 2)):
			defaultToggle(True, 3, 2)

		time.sleep(10)
		previousTime = datetime.now().second
		vehicle1.close()
		vehicle2.close()