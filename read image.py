import cv2

# Read the image
img = cv2.imread("Resources/kona-iron-man-video.jpg")

# Display the resulting frame
cv2.imshow('output', img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()