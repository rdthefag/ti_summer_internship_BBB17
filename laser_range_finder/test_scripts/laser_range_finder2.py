#!/bin/py
import cv2
from numpy import*

loop=1

cv2.namedWindow('preview')
vc=cv2.VideoCapture(0)
vc.set(cv2.cv.CV_CAP_PROP_FPS, 30)
if vc.isOpened():
	rval, frame=vc.read()

else:
	rval=False

if rval==1:
	while loop==1:
		cv2.imshow('preview',frame)
		rval,frame=vc.read()
		key=cv2.waitKey(20)
		if key==27:
			loop=0
		num=(frame[:,...,2]>240)
		xy_val = num.nonzero()
		y_val=median(xy_val[0])
		x_val=median(xy_val[1])
		dist=abs(x_val - 320)
		dist2=abs(y_val - 240)
		print "dist from center pixel is" + str((dist**2+dist2**2)**0.5)
		Q=(dist2)*(0.000945)-0.00154
		tan=abs(math.tan(Q))
		if tan>0:
			obj_dist=int(5.33/tan)
			print "\033[12:0H" + " the dot is " + str(obj_dist) + " cm away "
		else:
			print "red dot not visible"
elif rval==0:
	print "webcam error"
