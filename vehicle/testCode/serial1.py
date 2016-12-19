import cv2
import time
from arduino_vehicle import writeToArduino
from webcam_feed import getImage
from arduino_vehicle import carDetector

# image = getImage()
image = cv2.imread("123.png")

x = carDetector(image, "cars.xml")

# here we should calculate the traffic density
# and change the lights based on the traffic density

print("Number of cars: ",x)

for x in range(0,20):
	writeToArduino("abCdefghijkL")
	time.sleep(1)
	writeToArduino("abcDefghijkL")
	time.sleep(1)
	writeToArduino("abcdefghIjkL")
	time.sleep(1)


