from inpaintClass import *
import math
import os

def main():
    rootDirectory = os.getcwd()

    inputFolders = [
        r'shape\simple',
        r'shape\intermediate',
        r'shape\complex',
    ]

    outputFolder = [folder + "_masks" for folder in inputFolders]

    for i, folder in enumerate(inputFolders):
        currentIndex = 0
        if not os.path.exists(folder):
            print(f"Folder is not exit: {folder}")
            exit()

        if not os.path.exists(outputFolder):
            os.mkdir(outputFolder)
        os.chdir(folder)

        files = [item for item in os.listdir() if os.path.isfile(item)]

        if len(files) == 0:
            continue

        for file in files:
            

    # inputFolder = r'data\shape\simple'
    # outputFolder = inputFolder + '_masks'
    
    # if not os.path.exists(outputFolder):
    #     os.mkdir(outputFolder)

    # # Thực hiện ở 1 folder
    # os.chdir(inputFolder)

    # files = [f for f in os.listdir() if os.path.isfile(f)]
    
    # for file in files:

    #     # Xử lý ra được mask
    #     mask = np.zeros(shape= (100,100))

    #     fileName, extension = os.path.splitext(file)
    #     cv.imwrite(f"{fileName}_mask{extension}", mask)

    #     os.chdir(currentDic)

if __name__ == "__main__":
    main()