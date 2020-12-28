import cv2

# 0 for web camera
vid = cv2.VideoCapture(0)
# setting width
vid.set(3, 640)
# setting height
vid.set(4, 480)
# setting brightness
vid.set(10, 100)

while True:
    # read the video
    _, img = vid.read()
    # show the image frame by frame
    cv2.imshow("Output", img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
