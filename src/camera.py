import numpy as np
import cv2

def empty (evt):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow("trackbars",)
cv2.resizeWindow("trackbars", 640,420)
cv2.createTrackbar("hue min", "trackbars", 0, 179, empty)
cv2.createTrackbar("hue max", "trackbars", 19, 179, empty)
cv2.createTrackbar("sat min", "trackbars", 110, 255, empty)
cv2.createTrackbar("sat max", "trackbars", 240, 179, empty)
cv2.createTrackbar("value min", "trackbars", 153, 255, empty)
cv2.createTrackbar("value max", "trackbars", 255, 255, empty)
cap.set(3,640 )
cap.set(4, 480)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
 
    cv2.imshow('frame',frame)
    cv2.imshow('HSV',hsv)
    cv2.imshow('gray',gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
