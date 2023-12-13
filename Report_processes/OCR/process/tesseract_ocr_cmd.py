import pytesseract
import os
import sys
from pathlib import Path
import argparse
from PIL import Image
from ocrUtils import OcrUtils
from utils import Utils

# Install Tesseract Engine before running the program
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# COMMAND - value default
image_path = r'D:\Workspace\University\Report_DATN\Report_processes\OCR\data\simple\simple_0.png'
output_result = r'D:\Workspace\University\Report_DATN\Report_processes\OCR\process\simple_text.txt'

def setup_args(parser):
    parser.add_argument(
        "--input_img", type=str, required=True,
        help="Path to a single input img",
    )

    parser.add_argument(
        "--output_result", type=str, required=True,
        help="Output path for a result.",
    )

def main():
    parser = argparse.ArgumentParser()
    setup_args(parser)
    args = parser.parse_args(sys.argv[1:])

    # python tesseract_ocr_cmd.py
    # --input_img
    # D:\Workspace\University\Report_DATN\Report_processes\OCR\data\simple\simple_0.png 
    # --output_result
    # D:\Workspace\University\Report_DATN\Report_processes\OCR\process\simple_tesseract_text.txt  
    input_img = args.input_img
    output_result = args.output_result

    # print(pytesseract.get_languages(config=''))

    # Read image by pillow
    img = Image.open(input_img)

    # Extract text from image
    extracted_text = pytesseract.image_to_string(img, lang ='vie')

    # # Show result
    # print(extracted_text)

    # Export Result
    OcrUtils.exportResult(input_img= input_img, output_result= output_result, text= extracted_text)
    Utils.reportTime()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)