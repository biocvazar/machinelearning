__author__ = 'Bio'


import numpy as np
import cv2
import argparse
import imutils

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
# 	help="path to the input image")
# args = vars(ap.parse_args())

# load the image, convert it to grayscale, blur it slightly,
# and threshold it
image = cv2.imread('Human_eye_with_blood_vessels.jpg')
image = cv2.resize(image,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]


# find contours in the thresholded image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
# loop over the contours
for c in cnts:
    # compute the center of the contour
    M = cv2.moments(c)

    if M["m00"]:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        continue
    print(M["m"
            "00"])
    # draw the contour and center of the shape on the image
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)
    cv2.putText(image, "center", (cX - 20, cY - 20),
    	cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # show the image
cv2.imshow("Image", image)
cv2.waitKey(0)