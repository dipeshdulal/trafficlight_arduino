from traffic_light import defaultToggle
from datetime import datetime
import time
import random

date = datetime.now()
previousTime = date.second

while True:
	date = datetime.now()
	vehicle1 = open("1.txt", "r")
	vehicle2 = open("2.txt", "r")
	vehicle3 = open("3.txt", "r")
	currentTime = date.second
	deltaTime = currentTime - previousTime
	if (deltaTime >= 2):

		car1 = int(vehicle1.read())
		car2 = int(vehicle2.read())
		car3 = int(vehicle3.read())

		# car1 = 1
		# car2 = 4
		# car3 = 4


		time.sleep(1)
		print(car1, car2, car3)
		
		if ((car1 > car2) and (car1 > car3)):
			defaultToggle(True, 3, 2)
		elif ((car2 > car1) and (car2 > car3)):
			defaultToggle(True, 2, 2)
		elif ((car3 > car1) and (car3 > car2)):
			defaultToggle(True, 1, 2)
		else:
			defaultToggle(True, random.randrange(1,3), 2)

		print("Changed")	
		time.sleep(1)
		previousTime = datetime.now().second
		vehicle1.close()
		vehicle2.close()
		vehicle3.close()