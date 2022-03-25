#Links de referencia
# RoseBrock, A. (2014) OpenCV and Python Color Detection. Recuperado el 24/03/22 de: https://pyimagesearch.com/2014/08/04/opencv-python-color-detection/
# OpenCV. (s.f.) Changing Colorspaces. Recuperado el 24/03/22 de: https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html
# OpenCV. (s.f.) Adding a trackbar to our applications. Recuperado el 24/03/22 de: https://docs.opencv.org/3.4/da/d6a/tutorial_trackbar.html
# Canu, S. (s.f.) Detecting Colors. OpenCV with Python. Recuperado el 24/03/22 de: https://pysource.com/2019/02/15/detecting-colors-hsv-color-space-opencv-with-python/

#Import Libraries
import numpy as np
import cv2

def empty (evt):
    pass

#Set Camera
cap = cv2.VideoCapture(0)
#Define trackbars with ranges
cv2.namedWindow("trackbars",)
cv2.resizeWindow("trackbars", 640,420)
cv2.createTrackbar("Matiz Min", "trackbars", 0, 179, empty)
cv2.createTrackbar("Matiz Max", "trackbars", 19, 179, empty)
cv2.createTrackbar("Sat Min", "trackbars", 110, 255, empty)
cv2.createTrackbar("Sat Max", "trackbars", 240, 179, empty)
cv2.createTrackbar("Valor Min", "trackbars", 153, 255, empty)
cv2.createTrackbar("Valor Max", "trackbars", 255, 255, empty)
cap.set(3,640 )
cap.set(4, 480)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Matiz Min", "trackbars")
    h_max = cv2.getTrackbarPos("Matiz Max", "trackbars")
    s_min = cv2.getTrackbarPos("Sat Min", "trackbars")
    s_max = cv2.getTrackbarPos("Sat Max", "trackbars")
    v_min = cv2.getTrackbarPos("Valor Min", "trackbars")
    v_max = cv2.getTrackbarPos("Valor Max", "trackbars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower= np.array([h_min, s_min, v_min])
    upper= np.array([h_max, s_max, v_max])
    mask = cv2.inRange(hsv, lower, upper )
    img_result = cv2.bitwise_and(frame,frame,mask = mask)
    
    #Set filters and show them in different windows
    cv2.imshow('frame',frame)
    cv2.imshow("mask", mask)
    cv2.imshow('HSV',hsv)
    cv2.imshow('gray',gray)
    cv2.imshow('result',img_result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
