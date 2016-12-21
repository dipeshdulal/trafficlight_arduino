from traffic_light import defaultToggle
from datetime import datetime
import time


date = datetime.now()
previousTime = date.second

while True:
	date = datetime.now()
	vehicle1 = open("1.txt", "r")
	vehicle2 = open("2.txt", "r")
	currentTime = date.second
	deltaTime = currentTime - previousTime
	if (deltaTime >= 5):
		car1 = vehicle1.read()
		car2 = vehicle2.read()
		print(car1, car2)
		if (int(car1) < 2) & (int(car2) < 5):
			defaultToggle(True)
			time.sleep(1)
			defaultToggle(True, 2)
			time.sleep(1)
			defaultToggle(True, 3)
			time.sleep(1)	
		
		



		previousTime = datetime.now().second
		vehicle1.close()
		vehicle2.close()