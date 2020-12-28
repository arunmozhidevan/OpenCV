import cv2
import numpy as np

# Read the image
img = cv2.imread('Resources/Hearts-5c195fc746e0fb000103d252.jpg')

width, height = 250, 350

# pixel point locations of four corners of the card, point denoted as [y,x]
pts1 = np.float32([[987, 231], [1276, 320], [864, 639], [1154, 726]])
# setting size of the new image
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

# Perspective Transformation
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgWarp = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("output",imgWarp)
cv2.waitKey(0)


