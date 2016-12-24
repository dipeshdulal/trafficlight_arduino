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
	if (deltaTime >= 2):

		car1 = int(vehicle1.read())
		car2 = int(vehicle2.read())
		car3 = int(vehicle3.read())

		# car1 = 1
		# car2 = 4
		# car3 = 4


		time.sleep(1)
		print(car1, car2, car3)
		
		# 1
		if ((car1 < 1) and (car2 < 1) and (car3 < 1)):
			defaultToggle(True, 3, 2)
		# 2
		elif ((car1 >= 1) and (car2 < 1) and (car3 < 1)):
			defaultToggle(True, 3, 2)
		# 3
		elif ((car1 < 1) and (car2 >= 1) and (car3 < 1)):
			defaultToggle(True, 2, 2)
		# 4
		elif ((car1 < 1) and (car2 < 1) and (car3 >= 1)):
			defaultToggle(True, 1, 2)
		# 5
		elif ((car1 >= 1) and (car2 >= 1) and (car3 < 1)):
			defaultToggle(True, 3, 2)
		# 6
		elif ((car1 >= 1) and (car2 < 1) and (car3 >= 1)):
			defaultToggle(True, 3, 2)
		# 7
		elif ((car1 < 1) and (car2 >= 1) and (car3 >= 1)):
			defaultToggle(True, 1, 2)
		# 8
		elif ((car1 >= 1) and (car2 >= 1) and (car3 >= 1)):
			defaultToggle(True, 3, 2)
		else:
			defaultToggle(True, 2, 2)

		print("Changed")	
		time.sleep(1)
		previousTime = datetime.now().second
		vehicle1.close()
		vehicle2.close()
		vehicle3.close()