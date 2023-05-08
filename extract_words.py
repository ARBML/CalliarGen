#%%
## One word 
words_data = [] 
with open(file="data.txt", mode='r') as file:

    for line in file:
        print(line.split( )[0])
        words_data.append((line.split( )[0]))


unique_words_data = list(set(words_data))

#%%
from maha.cleaners.functions import keep
import os 
import json
# from collections import defaultdict
words = {}

for category in os.listdir('Sanad'):
    for text_file in os.listdir(os.path.join('Sanad', category)):
        with open(os.path.join('Sanad', category, text_file)) as file:
            text = file.read()
            cleaned_text = keep(text,arabic_letters=True)
            cleaned_text_list = cleaned_text.split( )
            sanad_words_data = list(set(cleaned_text_list))
            
            # print(sanad_words_data)
            for word in sanad_words_data:
                if word in words.keys():
                    words[word] += 1
                else:
                    words[word] = 1
            #print(words)
            #break


output = dict(sorted(words.items(), key=lambda x: x[1],reverse=True))
# json.dumps(words, ensure_ascii=False).encode('utf-8')

with open('output_text.txt', 'w', encoding='utf8') as json_file:
    json.dump(output, json_file, ensure_ascii=False, indent=2)
              
# for word in cleaned_text_list:
#     with open('result.txt', 'a') as file:
#         file.write(word+"\n")
                
                    #print(word+"\n")
# %%
!pip install ipywidgets

#%%
import os 
import json
# from collections import defaultdict
from maha.cleaners.functions import keep
import os 
import json
from maha.parsers.functions import parse
import re 
from tqdm.notebook import trange, tqdm

#%%

words = {}

for category in os.listdir('Sanad'):
    for text_file in tqdm(os.listdir(os.path.join('Sanad', category))):
        with open(os.path.join('Sanad', category, text_file)) as file:
            text = file.read()
            cleaned_text = keep(text,arabic_letters=True)
            
            # cleaned_text_list = cleaned_text.split( )

            cleaned_text_list = re.findall(r'\b\w+\b \b\w+\b', cleaned_text)
            # from maha.parsers.functions import parse
            # cleaned_text_list = parse(cleaned_text, custom_expressions=r'\b\w+\b \b\w+\b', include_space=True)


            sanad_words_data = list(set(cleaned_text_list))

            
            # print(sanad_words_data)
            for word in sanad_words_data:
                if word in words.keys():
                    words[word] += 1
                else:
                    words[word] = 1
            
            #print(words)
            #break

#%%

output = dict(sorted(words.items(), key=lambda x: x[1],reverse=True))
# json.dumps(words, ensure_ascii=False).encode('utf-8')

with open('output_text_2words.txt', 'w', encoding='utf8') as json_file:
    json.dump(output, json_file, ensure_ascii=False, indent=2)
              
# for word in cleaned_text_list:
#     with open('result.txt', 'a') as file:
#         file.write(word+"\n")
                
                    #print(word+"\n")
# %%
len(output)
# %%
