# Kết hợp mouse event và 3 shape tiến hành thực hiện tạo mask, bằng cách duyệt qua tất cả các ảnh

from enum import Enum
import math
from typing import List
import numpy as np
import cv2 as cv
from inpaintClass import *

# Holder
isDrawing = False
mode = Mode.RECTANGLE
startPoint = Point()
listPoints = []
inpaintMask = Mask()

# Callback Mouse Event
def MouseEventHandler(event,x,y,flags,param):
    global startPoint, listPoints, isDrawing, mode, inpaintMask

    if event == cv.EVENT_LBUTTONDOWN:
        isDrawing = True
        startPoint = Point(x, y)
        listPoints = []
    
    elif event == cv.EVENT_MOUSEMOVE:
        if isDrawing and mode == Mode.POLYGON:
            # draw polygon
            cv.circle(img, (x, y), 5, RED, -1) 
            listPoints.append(Point(x, y))

    elif event == cv.EVENT_LBUTTONUP:
        isDrawing = False
        if mode == Mode.RECTANGLE:
            # draw rectangle
            topLeft = startPoint
            bottomRight = Point(x, y)

            print(f"Rect: topLeft = {topLeft}, bottomRight = {bottomRight}")

            cv.rectangle(img, topLeft.tuple(), bottomRight.tuple(), RED, -1)
            inpaintMask.shapes.append(Shape(mode= mode, param=[topLeft, bottomRight]))

        elif mode == Mode.ELIP:
            # draw elip
            topLeft = startPoint
            bottomRight = Point(x, y)

            print(f"Elip: topLeft = {topLeft}, bottomRight = {bottomRight}")
            center = (topLeft + bottomRight)//2
            axesLength = ((bottomRight.x - topLeft.x)//2,(bottomRight.y - topLeft.y)//2)

            cv.ellipse(img, center.tuple(), axesLength, 0, 0, 360, RED, -1)
            inpaintMask.shapes.append(Shape(mode= mode, param=[topLeft, bottomRight]))

        elif mode == Mode.POLYGON:
            inpaintMask.shapes.append(Shape(mode= mode, param= listPoints))

inputPath = r'shape\simple\simple_0.jpg'

images = [
    # r'shape\simple\simple_0.jpg',
    # r'shape\simple\simple_1.jpg',
    # r'shape\simple\simple_2.jpg',
    r'shape\simple\simple_3.jpg',
    # r'shape\simple\simple_4.jpg',
    # r'shape\simple\simple_5.jpg',
    # r'shape\simple\simple_6.jpg',
]

currentIndex = 0
img = cv.imread(images[currentIndex])

cv.namedWindow('image')
cv.setMouseCallback('image',MouseEventHandler)

# Interact with images
while(1):
    cv.imshow('image',img)
    key = cv.waitKey(1) & 0xFF
    if key == ord('n'):
        # export mask
        mask = inpaintMask.drawMask(img)
        cv.imwrite(f"shape\simple_masks\simple_3.jpg", mask)

        # restart image
        inpaintMask.shapes = []
        currentIndex += 1
        if currentIndex == len(images):
            break
        img = cv.imread(images[currentIndex])
        
    elif key == ord('q'):
        break
    elif key == ord('r'):
        mode = Mode.RECTANGLE
    
    elif key == ord('e'):
        mode = Mode.ELIP
    
    elif key == ord('p'):
        mode = Mode.POLYGON

cv.destroyAllWindows()