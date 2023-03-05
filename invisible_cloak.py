import cv2
import time
import numpy as np

fourcc = cv2.VideoWriter_fourcc(*"xvid")
outputfile = cv2.VideoWriter("output.avi")

capture = cv2.VideoCapture(0)
time.sleep(2)
background = 0

for i in range(60):
    ret,background = capture.read()

background = np.flip(background,axis = 1)

while(capture.isopen()):
    ret,image = capture.read()
    if not ret:
        break

    image = np.flip(image,axis = 1)

    hsv = cv2.cvtcolor(image,cv2.COLOR_BGR2HSV)
    lowerred = np.array([0,120,50])
    upperred = np.array([0,100,150])
    mask1 = cv2.inrange(hsv,lowerred,upperred)

    lowerred = np.array([120,120,70])
    upperred = np.array([180,255.255])
    mask2 = cv2.inrange(hsv,lowerred,upperred)

    mask = mask1 + mask2

    mask_1 = cv2.morphologyEx(mask_1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8)) 
    mask_1 = cv2.morphologyEx(mask_1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))

    mask2 = cv2.bitwise_not(mask1)

capture.realase()
cv2.destroyallwindows()