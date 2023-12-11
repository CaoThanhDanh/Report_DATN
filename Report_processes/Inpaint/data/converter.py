from PIL import Image
import os

# From webp, png to jpg


### Single image

# inputPath = r'shape\intermediate\intermediate_2.png'
# outputPath = r'shape\intermediate\intermediate_2.jpg'

# im = Image.open(inputPath).convert("RGB")
# im.save(outputPath, "jpeg")

### Batch images
INPUT_DIRECTORY = r'D:\Workspace\University\Report_DATN\Report_processes\Inpaint\data\shape\complex'
OUTPUT_DIRECTORY = r'D:\Workspace\University\Report_DATN\Report_processes\Inpaint\data\shape\complex'
OUTPUT_EXTENSION = '.jpg'

INPUT_IMAGES = [
    'complex_3.png',
    # 'simple_5.png',
    # 'simple_1.png',
    # 'simple_2.png',
    # 'simple_3.png',
    # 'simple_4.png',
]

for image in INPUT_IMAGES:
    (fileName, extension) = os.path.splitext(image)

    im = Image.open(os.path.join(INPUT_DIRECTORY, image)).convert("RGB")
    outputPath = os.path.join(OUTPUT_DIRECTORY, fileName + OUTPUT_EXTENSION)
    im.save(outputPath)
