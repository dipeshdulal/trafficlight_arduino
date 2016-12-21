# check for commit
import serial
import time
import cv2

def writeToArduino(str):
	try:
		arduino = serial.Serial("/dev/ttyACM0", 9600)
		time.sleep(1)
		arduino.setDTR()
		time.sleep(1)
		arduino.write(str.encode())
	except:
		print("Change the permissions")
	

def carDetector(image, car_cascade, windowName):

	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	cars = car_cascade.detectMultiScale(gray, 1.1, 1)

	a = len(cars)

	for (x,y,w,h) in cars:
	    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
	          
	cv2.imshow(windowName,image)	    
	return a

	
	
	