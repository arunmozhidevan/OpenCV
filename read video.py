import cv2

vid = cv2.VideoCapture("Resources/samplevideo.mp4")
# setting width
vid.set(3, 640)
# setting height
vid.set(4, 480)
# setting brightness
vid.set(10, 100)

while True:
    # Capture frame-by-frame
    _, img = vid.read()
    # Display the resulting frame
    cv2.imshow("Output", img)
    if cv2.waitKey(3) & 0xff == ord('q'):
        break

# When everything done, release the capture
vid.release()
cv2.destroyAllWindows()
