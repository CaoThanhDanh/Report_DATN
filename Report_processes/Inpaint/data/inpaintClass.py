from enum import Enum
from typing import List
import numpy as np
import cv2 as cv

# Constants
RED = (0, 0, 255)
GREEN = (0, 255, 0)

class Mode(Enum):
    RECTANGLE = 1
    ELIP = 2
    POLYGON = 3

class Point:
    '''
    Define:
    Point with x and y coordinates on an image. Using for draw mask for Inpaint

    Args:
    - x (int): The x of the vertical axis.
    - y (int): The y of the horizontal axis.
    '''
    def __init__(self, x: int = 0, y: int = 0):
        self.x = int(x)
        self.y = int(y)

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
    
    def __floordiv__(self, num: int):
        x = self.x//num
        y = self.y//num
        return Point(x,y)
    
    def tuple(self): return (self.x, self.y)

class Shape:
    def __init__(self, mode: Mode, param: List[Point]):
        self.mode = mode
        self.param = param

    def exportPointsForPolygon(self) -> np.ndarray:
        points = np.array([[point.x, point.y] for point in self.param])
        return points.reshape((-1, 1, 2))

class Mask:
    def __init__(self, shapes: List[Shape] = []):
        self.shapes = shapes

    def drawMask(self, inputImage: cv.Mat) -> cv.Mat:
        mask = np.zeros((inputImage.shape[0], inputImage.shape[1]), dtype=int)

        for shape in self.shapes:
            
            mode = shape.mode
            if mode == Mode.RECTANGLE:
                topLeft, bottomRight = shape.param

                if isinstance(topLeft, Point) and isinstance(bottomRight, Point):
                    cv.rectangle(mask, topLeft.tuple(), bottomRight.tuple(), 255, -1)

            elif mode == Mode.ELIP:
                topLeft, bottomRight = shape.param
                
                if isinstance(topLeft, Point) and isinstance(bottomRight, Point):
                    center = (topLeft + bottomRight)//2
                    axesLength = ((bottomRight.x - topLeft.x)//2,(bottomRight.y - topLeft.y)//2)
                    mask = cv.ellipse(mask, center.tuple(), axesLength, 0, 0, 360, 255, -1)

            elif mode == Mode.POLYGON:
                points = shape.exportPointsForPolygon()
                isClosed = False
                thickness = 10
                mask = cv.polylines(mask, [points], isClosed, 255, thickness)

        return mask