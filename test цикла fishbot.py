import pyautogui as p
from time import sleep, time
import numpy as np
import PIL
import PIL.ImageGrab
import cv2 as cv
im = PIL.ImageGrab.grab(bbox=(0,160,1073,550))
im.save('screennew.png')
new = cv.imread('screennew.png', 0)
new = cv.medianBlur(new,5)
th3 = cv.adaptiveThreshold(new,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                           cv.THRESH_BINARY,221,20)
mas = np.asarray(th3)
qw = False
for x,i in enumerate(mas):
    for y,j in enumerate(i):
        if j != 255:
            qw =True
            print(x,y)
            break
    if qw == True:
        break