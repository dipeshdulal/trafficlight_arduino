import numpy as np
import cv2
# from matplotlib import pyplot as plt

#load the color image in grayscale
# img = cv2.imread('prac.jpg', 0);

# displays the image in the window
# as many windows can be created but with different names
# cv2.imshow('PRACHANDA', img);

# it is the keyboard binding function 
# if 0 is passed it waits indefinitely for key strokes
# cv2.waitKey(0);

# to write the image
# cv2.imwrite('pracGray.jpg', img);

# cv2.destroyAllWindows();

# now the program to load the image in grayscale
# saves it if we press 's' and exit 

img = cv2.imread('prac.jpg', 0);

cv2.imshow('prachanda', img);

# for 64 bit machines
k = cv2.waitKey(0) & 0xFF;

if k == 27:
	cv2.destroyAllWindows();
elif k == ord('s'):
	cv2.imwrite('pracGGG.jpg', img);
	cv2.destroyAllWindows();


# cv2.destroyAllWindows();

# img = cv2.imgread('prac.jpg', 0);
# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic');
# plt.xticks([]), plt.yticks([]);
# plt.show();