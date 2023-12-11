import numpy as np
import cv2 as cv

# COMMAND
input_path = r'D:\Workspace\University\Report_DATN\Report_processes\Inpaint\data\point\simple\simple_0.jpg'

img = cv.imread(input_path)
# mouse callback function
ix,iy = -1,-1

def draw_circle(event,x,y,flags,param):
    global ix,iy
    if event == cv.EVENT_LBUTTONDOWN:
        print(f'Coordinates - EVENT_LBUTTONDOWN: (x, y)= ({x}, {y})')

cv.namedWindow('Select coordinates inpainted object')
cv.setMouseCallback('Select coordinates inpainted object',draw_circle)

while(1):
    cv.imshow('Select coordinates inpainted object',img)
    key = cv.waitKey(1) & 0xFF
    if key == ord('n'):
        # # export mask
        # mask = inpaintMask.drawMask(img)
        # cv.imwrite(f"shape\complex_masks\complex_{currentIndex}.jpg", mask)

        # # restart image
        # inpaintMask.shapes = []
        # currentIndex += 1
        # if currentIndex == len(images):
        #     break
        # img = cv.imread(images[currentIndex])\
        pass
        
    elif key == ord('q'):
        break

cv.destroyAllWindows()