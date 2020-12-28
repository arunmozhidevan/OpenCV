import cv2

# Read the image
img = cv2.imread('Resources/aceCard.jpg')

# flip an image
imgInvert = cv2.flip(img, 0)

# show the image
cv2.imshow("Original Output", img)
cv2.imshow("Flipped Output", imgInvert)
cv2.waitKey(0)
