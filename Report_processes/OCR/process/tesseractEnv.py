import os
import sys
from pathlib import Path
import argparse

# DIR OF INPAINT ANYTHING
LOCAL_ROOT_DIR = r'D:\Workspace\University\Report_DATN\Report_processes\OCR\process'

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

SEPARATOR = ' && '
COMMAND_ACTIVATE_ENV = 'conda activate tesseract_ocr'

# python tesseractEnv.py
# --input_img
# D:\Workspace\University\Report_DATN\Report_processes\OCR\data\simple\simple_0.png 
# --output_result
# D:\Workspace\University\Report_DATN\Report_processes\OCR\process\simple_text.txt 
def main():
    parser = argparse.ArgumentParser()
    setup_args(parser)
    args = parser.parse_args(sys.argv[1:])

    input_img = args.input_img
    output_result = args.output_result

    ocr_command = ['python tesseract_ocr_cmd.py',
                    f'--input_img {input_img}', 
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
    print("`Tesseract Env` ran with exit code %d" % returncode)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)