import cv2

# Create the haar cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Read the image
img = cv2.imread('Resources/face.jpg')

# Convert into grayscale image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# Detect faces in the image
faces = face_cascade.detectMultiScale(imgGray, 1.3, 5)

# Draw rectangle on the face
for (x, y, w, h) in faces:
    img1 = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# show the image
cv2.imshow('single person', img1)
cv2.waitKey(0)
