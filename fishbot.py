import pyautogui as p
from time import sleep, time
import numpy as np
import PIL
import PIL.ImageGrab
import cv2 as cv

sleep(3)
for k in range(3):
    sleep(1)
    x1, y1 = p.locateCenterOnScreen('examples/hook.png', confidence=0.95)

    #проверка функции выше!
    #ty = PIL.ImageGrab.grab(bbox=(x1-10,y1-10,x1+10,y1+10))
    #ty.save('chek/hook'+str(k)+'.png')
    
    p.click(x1, y1, duration = 1)
    sleep(2)
    im = PIL.ImageGrab.grab(bbox=(0,160,1073,550))
    im.save('examples/screennew.png')
    new = cv.imread('examples/screennew.png', 0)
    new = cv.medianBlur(new,5)
    th3 = cv.adaptiveThreshold(new,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv.THRESH_BINARY,221,20)
    mas = np.asarray(th3)
    qw = False
    for y,i in enumerate(mas):
        for x,j in enumerate(i):
            if j != 255:
                qw =True
                xx, yy = x , y +160
                break
        if qw == True:
            break    
    im = PIL.ImageGrab.grab(bbox=(xx,yy-10,xx+20,yy+10))

    #проверка поиска попловка
    #im.save('chek/bobber'+str(k)+'.png')
    
    I = np.asarray(im)
    for y, i in enumerate(I):
        for x, j in enumerate(i):
            I[y][x] = j[1]
    for i in range(30):
        sleep(0.3)
        im = PIL.ImageGrab.grab(bbox=(xx,yy-10,xx+20,yy+10))
        i = np.asarray(im)
        for y, u in enumerate(i):
            for x, j in enumerate(u):
                i[y][x] = j[1]
        res = np.mean(i)-np.mean(I) 
        I = i
        if abs(np.mean(res))>4:
            p.rightClick(xx,yy)
            break
    sleep(3)