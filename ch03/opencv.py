import cv2 as cv
import numpy as np

videoCapture = cv.VideoCapture(0)

while True:
    ret, frame = videoCapture.read()
    if not ret: break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (15,15), 0)

    circles = cv.HoughCircles(blur, cv.HOUGH_GRADIENT, 2, 100, param1=100, param2=100, minRadius=35, maxRadius=500)

    if circles is not None:
        print(circles)

videoCapture.release()
