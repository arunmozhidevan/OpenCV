import cv2
import numpy as np

# Read the image
img = cv2.imread('Resources/kona-iron-man-video.jpg')
kernel = np.array((5, 5), np.uint8)

# RGB to grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# apply Gaussian Blur
imgBlur = cv2.GaussianBlur(imgGray, (51, 51), 0)  # ksize should be in odd numbers (3,3) or (5,5) and so on
# Canny edge detector
imgCanny = cv2.Canny(imgGray, 150, 80)
# increase the white region
imgDilate = cv2.dilate(imgCanny, kernel, iterations=3)
# decrease the white region
imgErode = cv2.erode(imgDilate, kernel, iterations=2)

cv2.imshow("Original output", img)
cv2.imshow("Canny output", imgCanny)
cv2.imshow("Blur output", imgBlur)
cv2.imshow("Gray output", imgGray)
cv2.imshow("Dilate output", imgDilate)
cv2.imshow("Erode output", stackImages)
cv2.waitKey(0)
