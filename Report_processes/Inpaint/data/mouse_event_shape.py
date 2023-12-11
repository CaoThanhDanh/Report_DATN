import numpy as np
import cv2 as cv
# mouse callback function

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

img = cv.imread('assets\cat_damaged.png')

def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode,overlay,imgnew
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img,(ix,iy),(x,y),(0,0,255),-1)
        else:
            cv.circle(img,(x,y),5,(0,0,255),-1)


cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)

while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode

    if (cv.waitKey(25) & 0xFF) == ord('q'):
        break

cv.destroyAllWindows