import os
from glob import glob 
fonts = glob("fonts/**.ttf")
font_names = open("fonts/font_names.txt", 'r').read().splitlines()
print(font_names)
font_colors = ["black"]
font_colors_ar = ["اسود"]
import json
with open('words_freq.txt', 'r') as f:
    data = json.load(f)
print(len(data))
words = list(data.keys())
freqs = list(data.values())
total = sum(freqs)
freqs = [freq / total for freq in freqs]
from numpy.random import choice
from random import shuffle
def get_samples(max_words= 1000):
    samples= choice(words, p = freqs, size =max_words,  replace = False)
    shuffle(samples)
    train_size = int(0.8 * max_words)
    test_eval_size  = (max_words - train_size)//2
    train_samples = samples[:train_size]
    valid_samples = samples[-2*test_eval_size:-test_eval_size]
    test_samples =  samples[-test_eval_size:]
    return train_samples, valid_samples, test_samples

font_names_en = ['diwani decorated', 'diwani diacritized', 'diwani long', 'diwani standard',
                'kufi standard', 'kufi curved suqare', 'farisi standard', 'morrocan andulus',
                'rukaa bold', 'rukaa standard', 'rukaa fast', 'thuluth diwani', 'thuluth standard'
                ,'square standard', 'free bold', 'free standard', 'free long', 'mobili', 'managa'
                , 'aljazeera']

for i in range(20):
    print(font_names[i], font_names_en[i])

max_words = 10
train_samples, valid_samples, test_samples = get_samples(max_words = max_words)
dataset = {'train': train_samples, 'valid': valid_samples, 'test': test_samples}
from PIL import Image
from PIL import ImageDraw
import matplotlib.pyplot as plt
from PIL import ImageFont
import random
import numpy as np
from tqdm.auto import tqdm
# Open an Image

# !rm -r data_10k_mulfont_64x64_en

W, H = (128, 128)
features = []
i = 0
path_to_data = f"data_10k_mulfont_{W}x{H}_en"
os.mkdir(path_to_data)
os.mkdir(f"{path_to_data}/valid")
os.mkdir(f"{path_to_data}/train")
os.mkdir(f"{path_to_data}/test")

import random 
from utils_datasets import get_font
capts = {}
pbar = tqdm(total=max_words*20)
for split in dataset:
    for _, word in enumerate(dataset[split]):
        for _, font_type in enumerate(fonts):
            w, h = (W, H)
            #choose background and resize
            bg = np.random.choice(glob('fonts-bgs/**.jpg'))
            img = Image.open(bg)
            img = img.resize((W, H))
            #choose a font color
            font_color = np.random.choice(font_colors)
            font_color_ar = font_colors_ar[font_colors.index(font_color)]
            #get font description
            ft_idx = int(font_type[6:-4]) - 1
            font_name = font_names[ft_idx]
            #draw the font on the canvas given a premissable font size
            n_attempts = 1
            #insert space
            if random.random() < 0.01 and len(word) > 2:
                rnd_idx = random.randint(1, len(word) - 1)
                word = word[:rnd_idx] + ' ' + word[rnd_idx:]

            draw = ImageDraw.Draw(img)
            font, w, h, x, y = get_font(draw, word, font_type, width=W, height=H)
            draw.text((x, y), word, (0, 0, 0), font)
            file_name = f"{word}_{i:05d}"
            img.save(f"{path_to_data}/{split}/{file_name}.png")
            capts[file_name] = font_names_en[ft_idx]
            open(f"{path_to_data}/{split}/{file_name}.txt", 'w').write(word)
            i += 1
            pbar.update(1) 

for split in dataset:
    print(split, len(dataset[split]))

capts[list(capts.keys())[0]]

print(path_to_data)

with open(f"{path_to_data}/capts.json", "w") as fp:
    json.dump(capts,fp) 

base_path = f"{path_to_data}/train"
for i, img_name in enumerate(os.listdir(base_path)):
    key, _ = img_name.split('.')    
    if img_name.endswith(".png"):
        txt = open(f"{base_path}/{img_name[:-4]}.txt", "r").read()
        capt = capts.get(key)
        print(txt)
        print(capt)
        im = Image.open(f"{base_path}/{img_name}")
        plt.imshow(im)
        plt.show()
        if i > 100:
            break

base_path = "../first_batch"
for i, img_name in enumerate(os.listdir(base_path)):
    key, _ = img_name.split('.')    
    if img_name.endswith(".png"):
        txt = open(f"{base_path}/{img_name[:-4]}.txt", "r").read()
        capt = open(f"{base_path}/{img_name[:-4]}_capt.txt", "r").read()
        print(txt)
        print(capt)
        im = Image.open(f"{base_path}/{img_name}")
        plt.imshow(im)
        plt.show()
        if i > 50:
            break

font_type

# +
from PIL import Image, ImageDraw, ImageFont

def get_font(draw, text, font_name, width = 64, height = 64, min_size = 10,  max_size = 100):
    # default values at start
    font_size = None   # for font size
    font = None        # for object truetype with correct font size
    box = None         # for version 8.0.0
    w, h = width, height
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
