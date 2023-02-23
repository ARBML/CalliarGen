import os 
from maha.cleaners.functions import remove_numbers
import json

data = {}

for i, file in enumerate(os.listdir("images")):

    caption = remove_numbers(os.path.basename(file).split('.')[0])
  
    data = {"file_name": file, "text": caption}

    with open('metadata.json', 'a',encoding="utf8") as f:
        json.dump(data , f)
        f.write('\n')