# to get the webcam feed
import numpy as np
import cv2

def getImage(cap):
	# 0 with video name
	# cap = cv2.VideoCapture(camNo)
	# Capture frame-by-frame
	ret, frame = cap.read()
	return frame

# def showImage(image):
	