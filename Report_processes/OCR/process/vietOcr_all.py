import os
import sys
from pathlib import Path
import argparse

# DIR OF INPAINT ANYTHING
LOCAL_ROOT_DIR = r'D:\Workspace\University\Report_DATN\Report_processes\OCR\resources\vietocr'

# COMMAND - value default
image_path = r'D:\Workspace\University\Report_DATN\Report_processes\OCR\data\simple\simple_0.png'
output_result = r'D:\Workspace\University\Report_DATN\Report_processes\OCR\process\simple_text.txt'

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
    ], r'simple_vietOcr_result.txt'),
    
    (r'D:\Workspace\University\Report_DATN\Report_processes\OCR\data\intermediate', 
    [
        r'intermediate_0.png',
        r'intermediate_1.png',
        r'intermediate_2.png',
        r'intermediate_3.png',
        r'intermediate_4.png',
        # r'intermediate_5.png',  # Chinese
    ], r'intermediate_vietOcr_result.txt'),
    
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
    ], r'complex_vietOcr_result.txt'),
]

SEPARATOR = ' && '
COMMAND_ACTIVATE_ENV = 'conda activate vietOcr'

def main():
    for folder in image_folders:
        folder_prefix = folder[0]
        images = folder[1]
        output_result = os.path.join(folder_prefix, folder[2])

        for input_img in images:
            ocr_command = ['python vietOcr_cmd.py',
                            f'--input_img {os.path.join(folder_prefix, input_img)}', 
                            f'--output_result {output_result}', 
                            ]

            commands = [
                COMMAND_ACTIVATE_ENV,
                ' '.join(ocr_command),
            ]

            # currentDirectory = os.getcwd()

            # RUN
            os.chdir(LOCAL_ROOT_DIR)

            returncode = os.system(SEPARATOR.join(commands))
            # print("`vietOcr` ran with exit code %d" % returncode)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)