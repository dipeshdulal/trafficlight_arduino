# -*- coding: utf-8 -*-

import cv2
print(cv2.__version__)

def carDetector(image, cascade_src):

	car_cascade = cv2.CascadeClassifier(cascade_src)

	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	cars = car_cascade.detectMultiScale(gray, 1.1, 1)
	z = len(cars)

	for (x,y,w,h) in cars:
	    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)      

	return z

