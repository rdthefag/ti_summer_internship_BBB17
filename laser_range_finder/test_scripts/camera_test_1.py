#!/bin/usr/env python2.7

def caminit(cap):
    print(cap.get(3)) # Width of pic
    print(cap.get(4)) # Height of pic


import cv2

print(cv2.__version__)

cap = cv2.VideoCapture(1)
caminit(cap)
print("Press any key to skip")
while (True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if  cv2.waitKey(1) != -1:
        break

cap.release()
cv2.destroyAllWindows()
