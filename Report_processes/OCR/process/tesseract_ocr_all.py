import pytesseract
import os
import sys
from pathlib import Path
import argparse
from PIL import Image
from ocrUtils import OcrUtils

# Install Tesseract Engine before running the program
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# COMMAND - value default
input_img = r'..\data\data\simple\simple_0.png'
output_result = r'..\data\process\simple_text.txt'

image_folders = [
    (r'D:\Workspace\University\Report_DATN\Report_processes\OCR\data\simple',
    [
        r'simple_0.png',
        r'simple_1.png',
        r'simple_2.png',
        r'simple_3.png',
        r'simple_4.png',
        # r'simple_5.png', # Chinese
        # r'simple_6.jpg',
    ], r'simple_tesseract_result.txt'),
    
    (r'D:\Workspace\University\Report_DATN\Report_processes\OCR\data\intermediate', 
    [
        r'intermediate_0.png',
        r'intermediate_1.png',
        r'intermediate_2.png',
        r'intermediate_3.png',
        r'intermediate_4.png',
        # r'intermediate_5.png',  # Chinese
    ], r'intermediate_tesseract_result.txt'),
    
    (r'D:\Workspace\University\Report_DATN\Report_processes\OCR\data\complex', 
    [
        r'complex_0.png',
        r'complex_1.png',
        r'complex_2.jpg',
        r'complex_3.jpg',
        r'complex_4.jpg',
        r'complex_5.jpg',
        r'complex_6.jpg',
        # r'complex_7.jpeg', # Chinese
    ], r'complex_tesseract_result.txt'),
]

def main():
    for folder in image_folders:
        folder_prefix = folder[0]
        images = folder[1]
        output_result = os.path.join(folder_prefix, folder[2])

        for input_img in images:
            # Read image by pillow
            img = Image.open(os.path.join(folder_prefix, input_img))
            # Extract text from image
            extracted_text = pytesseract.image_to_string(img, lang ='vie')
            # Export Result
            OcrUtils.exportResult(input_img= input_img, output_result= output_result, text= extracted_text)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)