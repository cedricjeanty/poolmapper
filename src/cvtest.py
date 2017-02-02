# import the necessary packages
import sys
import numpy as np
import cv2
import pdb


def pixel_val(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		print (x, y)
 
# load the games image
# image = cv2.imread("games.jpg")
image = cv2.imread("pool4.jpeg")

# lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# l_channel,a_channel,b_channel = cv2.split(lab_image)
# pdb.set_trace()
cv2.namedWindow("image")
cv2.setMouseCallback("image", pixel_val)
cv2.imshow("image", hsv_image)
cv2.waitKey(0)
sys.exit()
 
# find the red color game in the image
upper = np.array([100,100,255]) 
lower = np.array([50,0,200]) 
mask = cv2.inRange(hsv_image, lower, upper)
cv2.imshow("mask", mask)
# cv2.waitKey(0)
# sys.exit()
# find contours in the masked image and keep the largest one
(_, cnts, _) = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
c = max(cnts, key=cv2.contourArea)
 
# approximate the contour
peri = cv2.arcLength(c, True)
approx = cv2.approxPolyDP(c, 0.05 * peri, True)
 
# draw a green bounding box surrounding the red game
cv2.drawContours(image, [approx], -1, (0, 255, 0), 4)
cv2.imshow("Image", image)
cv2.waitKey(0)

