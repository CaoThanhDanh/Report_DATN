import os
import sys
from pathlib import Path
import argparse


        
# DIR OF INPAINT ANYTHING
LOCAL_ROOT_DIR = r'D:\Workspace\University\LVTN\PythonCode\Inpaint_Anything\Inpaint-Anything'

# # COMMAND - value default
# input_path = r'D:\Workspace\University\LVTN\PythonCode\run_shell\assets\airport_0.jpg'
# coordinate = (964, 761)
# output_dir = r'D:\Workspace\University\LVTN\PythonCode\run_shell\outputs'

# def setup_args(parser):
#     parser.add_argument(
#         "--input_img", type=str, required=True,
#         help="Path to a single input img",
#     )

#     parser.add_argument(
#         "--point_coords", type=float, nargs='+', required=True,
#         help="The coordinate of the point prompt, [coord_W coord_H].",
#     )

#     parser.add_argument(
#         "--output_dir", type=str, required=True,
#         help="Output path to the directory with results.",
#     )
    

SEPARATOR = ' && '
COMMAND_ACTIVATE_ENV = 'conda activate inpaint'

# # python inpaint.py --input_img D:\Workspace\University\LVTN\PythonCode\run_shell\assets\airport_0.jpg --point_coords 964 761 --output_dir D:\Workspace\University\LVTN\PythonCode\run_shell\outputs
def main():
    # parser = argparse.ArgumentParser()
    # setup_args(parser)
    # args = parser.parse_args(sys.argv[1:])

    # input_path = args.input_img
    # coordinate = tuple(args.point_coords)
    # output_dir = args.output_dir

    point_result_file = r'D:\Workspace\University\Report_DATN\Report_processes\Inpaint\data\point\point_result.txt'
    dir_prefix = r'D:\Workspace\University\Report_DATN\Report_processes\Inpaint\data'

    with open(point_result_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            input_path, output_dir, point = line.split('|')

            point = point[1:-1].split(',')
            coordinate = (int(point[0]), int(point[1]))

            remove_command = ['python remove_anything.py',
                            f'--input_img {os.path.join(dir_prefix, input_path)}',
                            '--coords_type key_in',
                            f'--point_coords {coordinate[0]} {coordinate[1]}',
                            '--point_labels 1' ,
                            '--dilate_kernel_size 15' ,
                            f'--output_dir {os.path.join(dir_prefix, output_dir)}' ,
                            '--sam_model_type "vit_h"' ,
                            '--sam_ckpt ./pretrained_models/sam_vit_h_4b8939.pth' ,
                            '--lama_config ./lama/configs/prediction/default.yaml' ,
                            '--lama_ckpt ./pretrained_models/big-lama']

            commands = [
                COMMAND_ACTIVATE_ENV,
                ' '.join(remove_command),
            ]

            # currentDirectory = os.getcwd()

            # RUN
            os.chdir(LOCAL_ROOT_DIR)

            returncode = os.system(SEPARATOR.join(commands))
            print("`remove_anything` ran with exit code %d" % returncode)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)