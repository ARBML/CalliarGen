#%%
from huggingface_hub import notebook_login
notebook_login()


#%%
import os 
##%
# %%

#%%
os.getcwd()

#%%
output_path = "/home/lenovo/Desktop/stable_diffusion/diffusers/examples/text_to_image"
os.chdir(output_path)
#%%
os.getcwd()

#%%

output_path = "/home/lenovo/Desktop/stable_diffusion/diffusers/examples/text_to_image/calliar_1"

uploaded_files_folders = ["feature_extractor", "safety_checker", "scheduler", "text_encoder", "tokenizer", "unet", "vae", "model_index.json", "checkpoint-15000"]
#os.chdir(output_path)

#%%
os.listdir(output_path)

#%%
for file_folder in os.listdir(output_path):
    print(file_folder)
    if file_folder in uploaded_files_folders:
        if os.path.isfile(os.path.join(output_path, file_folder)):
            print("Hello")

            api.upload_file(
                path_or_fileobj=os.path.join(output_path, file_folder),
                path_in_repo=file_folder,
                repo_id="arbml/CalliarGen",
                repo_type="model",
            )      
        elif os.path.isdir(os.path.join(output_path, file_folder)):

            from huggingface_hub import HfApi
            api = HfApi()
            api.upload_folder(
                folder_path=os.path.join(output_path, file_folder),
                path_in_repo=file_folder,
                repo_id="arbml/CalliarGen",
                repo_type="model",
                ignore_patterns="**/logs/*.txt",
            )
