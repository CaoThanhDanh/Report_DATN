import numpy as np
import cv2

inputImages = [
    (r'..\data\shape\simple\simple_0.jpg', r'..\data\shape\simple_masks\simple_0.jpg', r'..\data\shape\simple_inpainted\simple_0.jpg'),
    (r'..\data\shape\simple\simple_1.jpg', r'..\data\shape\simple_masks\simple_1.jpg', r'..\data\shape\simple_inpainted\simple_1.jpg'),
    (r'..\data\shape\simple\simple_2.jpg', r'..\data\shape\simple_masks\simple_2.jpg', r'..\data\shape\simple_inpainted\simple_2.jpg'),
    (r'..\data\shape\simple\simple_3.jpg', r'..\data\shape\simple_masks\simple_3.jpg', r'..\data\shape\simple_inpainted\simple_3.jpg'),
    (r'..\data\shape\simple\simple_4.jpg', r'..\data\shape\simple_masks\simple_4.jpg', r'..\data\shape\simple_inpainted\simple_4.jpg'),
    (r'..\data\shape\simple\simple_5.jpg', r'..\data\shape\simple_masks\simple_5.jpg', r'..\data\shape\simple_inpainted\simple_5.jpg'),
    (r'..\data\shape\intermediate\intermediate_0.jpg', r'..\data\shape\intermediate_masks\intermediate_0.jpg', r'..\data\shape\intermediate_inpainted\intermediate_0.jpg'),
    (r'..\data\shape\intermediate\intermediate_1.jpg', r'..\data\shape\intermediate_masks\intermediate_1.jpg', r'..\data\shape\intermediate_inpainted\intermediate_1.jpg'),
    (r'..\data\shape\intermediate\intermediate_2.jpg', r'..\data\shape\intermediate_masks\intermediate_2.jpg', r'..\data\shape\intermediate_inpainted\intermediate_2.jpg'),
    (r'..\data\shape\intermediate\intermediate_3.jpg', r'..\data\shape\intermediate_masks\intermediate_3.jpg', r'..\data\shape\intermediate_inpainted\intermediate_3.jpg'),
    (r'..\data\shape\intermediate\intermediate_4.jpg', r'..\data\shape\intermediate_masks\intermediate_4.jpg', r'..\data\shape\intermediate_inpainted\intermediate_4.jpg'),
    (r'..\data\shape\intermediate\intermediate_5.jpg', r'..\data\shape\intermediate_masks\intermediate_5.jpg', r'..\data\shape\intermediate_inpainted\intermediate_5.jpg'),
    (r'..\data\shape\intermediate\intermediate_6.jpg', r'..\data\shape\intermediate_masks\intermediate_6.jpg', r'..\data\shape\intermediate_inpainted\intermediate_6.jpg'),
    (r'..\data\shape\intermediate\intermediate_7.jpg', r'..\data\shape\intermediate_masks\intermediate_7.jpg', r'..\data\shape\intermediate_inpainted\intermediate_7.jpg'),
    (r'..\data\shape\intermediate\intermediate_8.jpg', r'..\data\shape\intermediate_masks\intermediate_8.jpg', r'..\data\shape\intermediate_inpainted\intermediate_8.jpg'),
    (r'..\data\shape\complex\complex_0.jpg', r'..\data\shape\complex_masks\complex_0.jpg', r'..\data\shape\complex_inpainted\complex_0.jpg'),
    (r'..\data\shape\complex\complex_1.jpg', r'..\data\shape\complex_masks\complex_1.jpg', r'..\data\shape\complex_inpainted\complex_1.jpg'),
    (r'..\data\shape\complex\complex_2.jpg', r'..\data\shape\complex_masks\complex_2.jpg', r'..\data\shape\complex_inpainted\complex_2.jpg'),
    (r'..\data\shape\complex\complex_3.jpg', r'..\data\shape\complex_masks\complex_3.jpg', r'..\data\shape\complex_inpainted\complex_3.jpg'),
    (r'..\data\shape\complex\complex_4.jpg', r'..\data\shape\complex_masks\complex_4.jpg', r'..\data\shape\complex_inpainted\complex_4.jpg'),
    (r'..\data\shape\complex\complex_5.jpg', r'..\data\shape\complex_masks\complex_5.jpg', r'..\data\shape\complex_inpainted\complex_5.jpg'),
    (r'..\data\shape\complex\complex_6.jpg', r'..\data\shape\complex_masks\complex_6.jpg', r'..\data\shape\complex_inpainted\complex_6.jpg'),
]

for image in inputImages:
    inputPath = image[0]
    maskPath = image[1]
    outputPath = image[2]

    # Open the image.
    img = cv2.imread(inputPath)

    # Load the mask.
    mask_show = cv2.imread(maskPath)
    mask = cv2.cvtColor(mask_show, cv2.COLOR_BGR2GRAY)
    
    # Inpaint.
    dst = cv2.inpaint(img, mask, 5, cv2.INPAINT_NS)

    # Write the output.
    cv2.imwrite(outputPath, dst)
