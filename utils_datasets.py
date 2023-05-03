# https://stackoverflow.com/questions/65494932/imagedraw-adapt-font-size-dynamically-to-text-length
from PIL import Image, ImageDraw, ImageFont
import random
def get_font(draw, text, font_name, width = 64, height = 64, min_size = 10,  max_size = 100):
    # default values at start
    font_size = None   # for font size
    font = None        # for object truetype with correct font size
    box = None         # for version 8.0.0
    w, h = 64, 64
    x, y = 0, 0
        
    while 1:
        r_font_size = random.randint(min_size, max_size)
        # create new font
        font = ImageFont.truetype(font_name, r_font_size)
        # calculate bbox for version 8.0.0
        box = draw.textbbox((0, 0), text, font)  # need 8.0.0
        # `bbox` may have top/left margin so calculate real width/height
        w = box[2] - box[0]  # bottom-top
        h = box[3] - box[1]  # right-left
        # if too big then exit with previous values
        if w < width and h < height:
            x = (width - w)//2 - box[0]   # minus left margin
            y = (height - h)//2 - box[1]  # minus top margin
            break
    return font, w, h, x, y