# to get the webcam feed
import numpy as np
import cv2

def getImage():
	# 0 with video name
	cap = cv2.VideoCapture(0)

	# Capture frame-by-frame
	ret, frame = cap.read()

	# Our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	return gray
