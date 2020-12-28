import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

# draw line
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 0, 255), 2)
cv2.line(img, (0, img.shape[0]), (img.shape[1], 0), (0, 0, 255), 2)

# draw circle
cv2.circle(img, (img.shape[1] // 2, img.shape[0] // 2), 100, (0, 255, 0), cv2.FILLED)

# draw rectangle
cv2.rectangle(img, (img.shape[1] // 2 - 150, img.shape[0] // 2 - 150),
              (img.shape[1] // 2 + 150, img.shape[0] // 2 + 150), (0, 255, 255), 2)
# put a text
cv2.putText(img, 'Awesome', org=(img.shape[1] // 2 - 75, img.shape[0] // 2 + 5), fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=2, color=(0, 0, 255))

# show the image
cv2.imshow("Output", img)
cv2.waitKey(0)
