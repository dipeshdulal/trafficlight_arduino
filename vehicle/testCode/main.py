# the main file that combines all the functions together
import cv2
import time
from webcam_feed import getImage
from arduino_vehicle import carDetector

# webcam = [cv2.VideoCapture(1), 
# 		  cv2.VideoCapture(2), 
# 		  # cv2.VideoCapture(2), 
# 		  # cv2.VideoCapture(4)
# 		  ]

# webcam0 = cv2.VideoCapture(3)
webcam1 = cv2.VideoCapture(1)
webcam2 = cv2.VideoCapture(2)
# webcam3 = cv2.VideoCapture(3)

webcam1.set(3,320)
webcam1.set(4,240)
webcam2.set(3,320)
webcam2.set(4,240)
# webcam3.set(3,300)
# webcam3.set(4,300)

cascade_src = "./cars.xml"
car_cascade = cv2.CascadeClassifier(cascade_src)
car1 = 0
car2 = 0
# car3 = 0

vehicle3 = open("3.txt", "w")

while True:
	image1 = getImage(webcam1)
	image2 = getImage(webcam2)
	image3 = getImage(webcam3)

	for a in range(1,4):
		if a == 1:
			vehicle1 = open("1.txt", "w")
			car1 = carDetector(image1, car_cascade, "1")
			vehicle1.write(str(car1))
			vehicle1.close()
		elif a == 2:
			vehicle2 = open("2.txt", "w")
			car2 = carDetector(image2, car_cascade, "2")
			vehicle2.write(str(car2))
			vehicle2.close()
		elif a == 3:
			vehicle3 = open("3.txt", "w")
			car3 = carDetector(image3, car_cascade, "3")
			vehicle3.write(str(car3))
			vehicle3.close()

	if cv2.waitKey(33) & 0xff == 27:
		break	


	print(car1, car2)


cv2.destroyAllWindow()
