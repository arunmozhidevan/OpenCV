import cv2

# Read the image
img = cv2.imread('Resources/kona-iron-man-video.jpg')
# print image pixel
print(img.shape)

# resize the image
imgResize = cv2.resize(img, (500, 300))
# print resized image pixel
print(imgResize.shape)

# crop the image
imgCropped = img[200:800, 200:1400]
print(imgCropped.shape)

# show the image
cv2.imshow("Original output", img)
cv2.imshow("Resized output", imgResize)
cv2.imshow("Cropped output", imgCropped)
cv2.waitKey(0)
