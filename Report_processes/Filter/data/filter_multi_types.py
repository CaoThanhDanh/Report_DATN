import os
import sys
import PIL.Image
import pilgram

from enum import Enum
from utils import Utils

class FilterType(Enum):
    _1977 = 1
    aden = 2
    brannan = 3
    brooklyn = 4
    clarendon = 5
    earlybird = 6
    gingham = 7
    hudson = 8
    inkwell = 9
    kelvin = 10
    lark = 11
    lofi = 12
    maven = 13
    mayfair = 14
    moon = 15
    nashville = 16
    perpetua = 17
    reyes = 18
    rise = 19
    slumber = 20
    stinson = 21
    toaster = 22
    valencia = 23
    walden = 24
    willow = 25
    xpro2 = 26
  
def FilterImage(filterType: FilterType, src, dest):
    img = PIL.Image.open(src)

    if filterType == FilterType._1977:
        pilgram._1977(img).save(dest)
    elif filterType == FilterType.aden:
        pilgram.aden(img).save(dest)
    elif filterType == FilterType.brannan:
        pilgram.brannan(img).save(dest)
    elif filterType == FilterType.brooklyn:
        pilgram.brooklyn(img).save(dest)
    elif filterType == FilterType.clarendon:
        pilgram.clarendon(img).save(dest)
    elif filterType == FilterType.earlybird:
        pilgram.earlybird(img).save(dest)
    elif filterType == FilterType.gingham:
        pilgram.gingham(img).save(dest)
    elif filterType == FilterType.hudson:
        pilgram.hudson(img).save(dest)
    elif filterType == FilterType.inkwell:
        pilgram.inkwell(img).save(dest)
    elif filterType == FilterType.kelvin:
        pilgram.kelvin(img).save(dest)
    elif filterType == FilterType.lark:
        pilgram.lark(img).save(dest)
    elif filterType == FilterType.lofi:
        pilgram.lofi(img).save(dest)
    elif filterType == FilterType.maven:
        pilgram.maven(img).save(dest)
    elif filterType == FilterType.mayfair:
        pilgram.mayfair(img).save(dest)
    elif filterType == FilterType.moon:
        pilgram.moon(img).save(dest)
    elif filterType == FilterType.nashville:
        pilgram.nashville(img).save(dest)
    elif filterType == FilterType.perpetua:
        pilgram.perpetua(img).save(dest)
    elif filterType == FilterType.reyes:
        pilgram.reyes(img).save(dest)
    elif filterType == FilterType.rise:
        pilgram.rise(img).save(dest)
    elif filterType == FilterType.slumber:
        pilgram.slumber(img).save(dest)
    elif filterType == FilterType.stinson:
        pilgram.stinson(img).save(dest)
    elif filterType == FilterType.toaster:
        pilgram.toaster(img).save(dest)
    elif filterType == FilterType.valencia:
        pilgram.valencia(img).save(dest)
    elif filterType == FilterType.walden:
        pilgram.walden(img).save(dest)
    elif filterType == FilterType.willow:
        pilgram.willow(img).save(dest)
    elif filterType == FilterType.xpro2:
        pilgram.xpro2(img).save(dest)

images = [
    (r'assets\sample_bmp.bmp', r'outputs\sample_bmp_filtered.bmp'),
    (r'assets\sample_gif.gif', r'outputs\sample_gif_filtered.gif'),
    (r'assets\sample_jpeg.jpg', r'outputs\sample_jpeg_filtered.jpg'),
    (r'assets\sample_png.png', r'outputs\sample_png_filtered.png'),
    # (r'assets\sample_svg.svg', r'outputs\sample_svg_filtered.svg'),
    (r'assets\sample_tiff.tif', r'outputs\sample_tiff_filtered.tif'),
    (r'assets\sample_webp.webp', r'outputs\sample_webp_filtered.webp'),
]


def main():
    for img in images:
        FilterImage(filterType= FilterType.kelvin, src= img[0], dest= img[1])
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