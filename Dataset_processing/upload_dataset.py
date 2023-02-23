from datasets import load_dataset


dataset = load_dataset("images")
dataset.push_to_hub("arbml/Calliar_dataset")