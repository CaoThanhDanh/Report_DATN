import numpy as np
import cv2 as cv
from inpaintClass import *

# COMMAND
# input_path = r'D:\Workspace\University\Report_DATN\Report_processes\Inpaint\data\point\simple\simple_0.jpg'

images = [
    # (r'point\simple\simple_0.jpg', r'point\simple_points\simple_0.jpg', r'point\simple_inpainted'),
    # (r'point\simple\simple_1.jpg', r'point\simple_points\simple_1.jpg', r'point\simple_inpainted'),
    # (r'point\simple\simple_2.jpg', r'point\simple_points\simple_2.jpg', r'point\simple_inpainted'),
    # (r'point\simple\simple_3.jpg', r'point\simple_points\simple_3.jpg', r'point\simple_inpainted'),
    # (r'point\simple\simple_4.jpg', r'point\simple_points\simple_4.jpg', r'point\simple_inpainted'),
    # (r'point\simple\simple_5.jpg', r'point\simple_points\simple_5.jpg', r'point\simple_inpainted'),
    # (r'point\intermediate\intermediate_0.jpg', r'point\intermediate_points\intermediate_0.jpg', r'point\intermediate_inpainted'),
    # (r'point\intermediate\intermediate_1.jpg', r'point\intermediate_points\intermediate_1.jpg', r'point\intermediate_inpainted'),
    # (r'point\intermediate\intermediate_2.jpg', r'point\intermediate_points\intermediate_2.jpg', r'point\intermediate_inpainted'),
    # (r'point\intermediate\intermediate_3.jpg', r'point\intermediate_points\intermediate_3.jpg', r'point\intermediate_inpainted'),
    # (r'point\intermediate\intermediate_4.jpg', r'point\intermediate_points\intermediate_4.jpg', r'point\intermediate_inpainted'),
    # (r'point\intermediate\intermediate_5.jpg', r'point\intermediate_points\intermediate_5.jpg', r'point\intermediate_inpainted'),
    # (r'point\intermediate\intermediate_6.jpg', r'point\intermediate_points\intermediate_6.jpg', r'point\intermediate_inpainted'),
    # (r'point\intermediate\intermediate_7.jpg', r'point\intermediate_points\intermediate_7.jpg', r'point\intermediate_inpainted'),
    # (r'point\intermediate\intermediate_8.jpg', r'point\intermediate_points\intermediate_8.jpg', r'point\intermediate_inpainted'),
    # (r'point\complex\complex_0.jpg', r'point\complex_points\complex_0.jpg', r'point\complex_inpainted'),
    # (r'point\complex\complex_1.jpg', r'point\complex_points\complex_1.jpg', r'point\complex_inpainted'),
    # (r'point\complex\complex_2.jpg', r'point\complex_points\complex_2.jpg', r'point\complex_inpainted'),
    (r'point\complex\complex_3.jpg', r'point\complex_points\complex_3.jpg', r'point\complex_inpainted'),
    # (r'point\complex\complex_4.jpg', r'point\complex_points\complex_4.jpg', r'point\complex_inpainted'),
    # (r'point\complex\complex_5.jpg', r'point\complex_points\complex_5.jpg', r'point\complex_inpainted'),
    # (r'point\complex\complex_6.jpg', r'point\complex_points\complex_6.jpg', r'point\complex_inpainted'),
]

# mouse callback function
ix,iy = -1,-1

# Holder

points = {}

listPoints = []

def draw_circle(event,x,y,flags,param):
    global ix,iy
    if event == cv.EVENT_LBUTTONDOWN:
        # draw point on the image
        cv.circle(img, (x, y), 10, GREEN, -1)

        listPoints.append((x, y))
        print(f'(x, y)= ({x}, {y})')

currentIndex = 0
img = cv.imread(images[0][0])
cv.namedWindow('Select coordinates inpainted object')
cv.setMouseCallback('Select coordinates inpainted object',draw_circle)

while(1):
    cv.imshow('Select coordinates inpainted object',img)
    key = cv.waitKey(1) & 0xFF
    if key == ord('n'):
        points.update({f'{images[currentIndex][0]}|{images[currentIndex][2]}': listPoints})
        # export point
        cv.imwrite(images[currentIndex][1], img)

        # restart image
        currentIndex += 1
        listPoints = []
        if currentIndex == len(images):
            break
        img = cv.imread(images[currentIndex][0])
        
    elif key == ord('q'):
        break

cv.destroyAllWindows()

with open('point\point_result_test.txt', 'w') as file:
    for key, value in points.items():
        file.write(f'{key}|{str(value)[1:-1]}\n')