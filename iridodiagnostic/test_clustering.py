__author__ = 'Bio'
import numpy as np
import cv2

img = cv2.imread("bitwise.png")
# img = cv2.resize(img,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
Z = img.reshape((-1,3))

# convert to np.float32
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 8
ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))





cv2.imshow('res2',res2)

average_color_per_row = np.average(res2, axis=0)
black = np.array([(0, 0, 0)])
average_color_per_row = np.setdiff1d(average_color_per_row, black)
average_color = np.average(average_color_per_row, axis=0)
average_color = np.setdiff1d(average_color, black)
print(average_color)
# average_color_img = np.array([[average_color]*100]*100, np.uint8)
# cv2.imshow('color', average_color_img)


img_hsv=cv2.cvtColor(res2, cv2.COLOR_BGR2HSV)
params = cv2.SimpleBlobDetector_Params()
# Setup SimpleBlobDetector parameters.
# Change thresholds
params.minThreshold = 100
params.maxThreshold = 255

# Filter by Circularity
params.filterByCircularity = 1
params.minCircularity = 0.1

# Filter by Convexity
params.filterByConvexity = 1
params.minConvexity = 0


# Filter by Inertia
params.filterByInertia = 1
params.minInertiaRatio = 0.5

# params.filterByColor = 1
# params.blobColor = average_color[0]
detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs.
keypoints = detector.detect(cv2.cvtColor(res2, cv2.COLOR_BGRA2GRAY))
im_with_keypoints = cv2.drawKeypoints(res2, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow("Keypoints", im_with_keypoints)


lower_clr = np.array([average_color[0]-10,100,100])
upper_clr = np.array([average_color[0]+10,255,255])
mask = cv2.inRange(img_hsv, lower_clr, upper_clr)
print(mask)
# mask = mask0 + mask1
# set my output img to zero everywhere except my mask
output_img = res2.copy()
output_img[np.where(mask==0)] = 255

cv2.imshow('without',output_img)

cv2.waitKey(0)
cv2.destroyAllWindows()