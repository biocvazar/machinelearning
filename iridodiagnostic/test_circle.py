__author__ = 'Bio'
import cv2
import numpy as np

image = cv2.imread('Human_eye_with_blood_vessels.jpg')
image = cv2.resize(image,None,fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
height, width = image.shape[:2]
# detect circles in the image
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=50, minDist=1, minRadius=height//20, maxRadius=height//2)

# ensure at least some circles were found
if circles is not None:
    # convert the (x, y) coordinates and radius of the circles to integers
    circles = np.round(circles[0, :]).astype("int")

    # loop over the (x, y) coordinates and radius of the circles
    for (x, y, r) in circles:
        # draw the circle in the output image, then draw a rectangle
        # corresponding to the center of the circle
        cv2.circle(output, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

    # show the output image
cv2.imshow("img",output)
cv2.waitKey(0)