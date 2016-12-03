__author__ = 'Bio'

import cv2
import numpy as np

big_radius = 0
flag = True

def get_coordinate(event, x, y, flags, param):
    global flag, big_radius, sx, sy, im2
    if event == cv2.EVENT_LBUTTONDOWN and flag:
        print("i`m here 2")
        big_radius = points_length((x,y), (sx, sy))
        cv2.circle(im2, (sx, sy), big_radius, color=(255,0,255))
        flag = False
        cv2.imshow("Keypoints", im2)

        circle_mask = np.zeros((height,width,3), np.uint8)
        cv2.circle(circle_mask, (sx, sy), big_radius, color=(255,255,255), thickness=cv2.FILLED)
        cv2.circle(circle_mask, (sx, sy), radius, color=(0, 0, 0), thickness=cv2.FILLED)
        image_bitwise = np.zeros((height,width,3), np.uint8)
        cv2.bitwise_and(im2, circle_mask, image_bitwise)
        cv2.imshow("bitwise", image_bitwise)
        cv2.imwrite("bitwise.png", image_bitwise)

def points_length(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return int(((x2-x1)**2 + (y2-y1)**2)**0.5)

# Read image
im =  cv2.imread("eye2.jpg", cv2.IMREAD_GRAYSCALE)
im2 = cv2.imread("eye2.jpg")
im = cv2.resize(im, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
im2 = cv2.resize(im2, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
height, width = im.shape[:2]

# Set up the detector with default parameters.
params = cv2.SimpleBlobDetector_Params()
# Setup SimpleBlobDetector parameters.
# Change thresholds
params.minThreshold = 0
params.maxThreshold = 50

# Filter by Area.
params.filterByArea = 0
params.minArea = height/2

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.4

# Filter by Convexity
params.filterByConvexity = 1
params.minConvexity = 0.1
params.maxConvexity = 1

# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.5
detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs.
keypoints = detector.detect(im)

# Draw detected blobs as red circles.
#im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


cv2.namedWindow('Keypoints')
cv2.setMouseCallback('Keypoints',get_coordinate)

sx, sy, radius = int(keypoints[0].pt[0]), int(keypoints[0].pt[1]), int(keypoints[0].size/2)
c = cv2.circle(im2, (sx, sy), radius, color=(255,0,255))
cv2.rectangle(im2, (sx - 2, sy - 2), (sx + 2, sy + 2), (0, 128, 255), -1)
# Show keypoints



cv2.imshow("Keypoints", im2)
cv2.waitKey(0)
