import cv2
import numpy as np

video=cv2.VideoCapture("opencv-assets-main/green.mp4")
# video=cv2.VideoCapture(0)
# print (video.read())
background=0
for i in range(60):
    ret,background=video.read()
while video.isOpened():
    ret,image=video.read()
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    lower_green=np.array([104,153,70])
    upper_green=np.array([30,30,0])
    mask1=cv2.inRange(hsv,lower_green,upper_green)
    lower_green=np.array([50,100,100])
    upper_green=np.array([70,255,255])
    mask2=cv2.inRange(hsv,lower_green,upper_green)
    mask3=cv2.bitwise_not(mask2)
    result1=cv2.bitwise_and(background,background,mask=mask2)
    result2=cv2.bitwise_and(image,image,mask=mask3)
    final_output=cv2.addWeighted(result1,1,result2,1,0)
    cv2.imshow('Output',final_output)
    k=cv2.waitKey(10)
    if k==27:
        break