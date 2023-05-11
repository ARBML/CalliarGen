# https://stackoverflow.com/questions/65494932/imagedraw-adapt-font-size-dynamically-to-text-length
from PIL import Image, ImageDraw, ImageFont
import random
import numpy as np
from numpy.random import choice
import json 
from random import shuffle

def get_samples(max_words= 1000, seed = 4):
    with open('words_freq.txt', 'r') as f:
        data = json.load(f)
    words = list(data.keys())
    freqs = list(data.values())
    total = sum(freqs)
    random.seed(seed)
    np.random.seed(seed)
    freqs = [freq / total for freq in freqs]
    samples= choice(words, p = freqs, size =max_words,  replace = False)
    shuffle(samples)
    train_size = int(0.8 * max_words)
    test_eval_size  = (max_words - train_size)//2
    train_samples = samples[:train_size]
    valid_samples = samples[-2*test_eval_size:-test_eval_size]
    test_samples =  samples[-test_eval_size:]
    return train_samples, valid_samples, test_samples

def get_font(draw, text, font_name, width = 64, height = 64, min_size = 10,  max_size = 100, n_attempts = 10):
    # default values at start
    font_size = None   # for font size
    font = None        # for object truetype with correct font size
    box = None         # for version 8.0.0
    w, h = width, height
    x, y = 0, 0
        
    for i in range(n_attempts - 1):
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
        else:
            max_size = max_size - 10
    else:
        return None,w,h,x,y
    return font, w, h, x, y