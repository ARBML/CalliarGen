from huggingface_hub import HfApi
api = HfApi()
api.upload_folder(
    folder_path="images",
    path_in_repo="images",
    repo_id="arbml/Calliar_dataset",
    repo_type="dataset",
)