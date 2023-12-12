import os
import sys
from pathlib import Path
import argparse

# DIR OF INPAINT ANYTHING
LOCAL_ROOT_DIR = r'D:\Workspace\University\Report_DATN\Report_processes\Filter'

# COMMAND - value default
filter = '_1977'
input_img = r'D:\Workspace\University\Report_DATN\Report_processes\Filter\data\assets\mountain.jpg'
output_img = r'D:\Workspace\University\Report_DATN\Report_processes\Filter\data\outputs\mountain_1977.jpg'

def setup_args(parser):
    parser.add_argument(
        "--filter", type=str, required=True,
        help="Type of filter applied to the image",
    )

    parser.add_argument(
        "--input_img", type=str, required=True,
        help="Path to a single input img",
    )

    parser.add_argument(
        "--output_img", type=str, required=True,
        help="Output path for a result.",
    )

SEPARATOR = ' && '
COMMAND_ACTIVATE_ENV = 'conda activate filter'

# python filterEnv.py --filter _1977 --input_img data\assets\mountain.jpg --output_img data\outputs\mountain_1977.jpg
# python filterEnv.py --filter aden --input_img D:\Workspace\University\Report_DATN\Report_processes\Filter\data\assets\mountain.jpg --output_img D:\Workspace\University\Report_DATN\Report_processes\Filter\outputstest\mountain_aden.jpg
def main():
    parser = argparse.ArgumentParser()
    setup_args(parser)
    args = parser.parse_args(sys.argv[1:])

    filter = args.filter
    input_img = args.input_img
    output_img = args.output_img

    remove_command = ['python filters.py',
                    f'{filter}',
                    f'{input_img}',
                    f'{output_img}',
                    ]

    commands = [
        COMMAND_ACTIVATE_ENV,
        ' '.join(remove_command),
    ]

    # currentDirectory = os.getcwd()

    # RUN
    os.chdir(LOCAL_ROOT_DIR)

    returncode = os.system(SEPARATOR.join(commands))
    print("`filter Env` ran with exit code %d" % returncode)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)