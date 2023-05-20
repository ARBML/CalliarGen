# CalliarGen

**Word-To-Image: Morphing Arabic Text to a Visual Representation**

[![Huggingface Space](https://img.shields.io/badge/🤗-Demo%20-yellow.svg)]([https://huggingface.co/spaces/SemanticTypography/Word-As-Image](https://huggingface.co/spaces/bkhmsi/Word-To-Image))
[![Colab Notebook](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1wobOAsnLpkIzaRxG5yac8NcV7iCrlycP)
[![GitHub](https://img.shields.io/badge/💻-GitHub%20-black.svg)](https://github.com/BKHMSI/Word-To-Image)

**Multilingual OpenCLIP** <br>
[![Multilingual OpenCLIP](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1zlGkbQh7ny9LKrMLNXtA6VDB151zxl_0?usp=sharing)


## Dataset

**Preprocessing:**

- Extract the caption from the images' names.
- Remove the numbers in the caption using [Maha library](https://github.com/TRoboto/Maha).
- Write the "file_name" and "text" in jsonl file as recommended from HF.
- Upload the dataset to HF dataset hub.

References: 

- Uploading the dataset to HF hub, [here](https://huggingface.co/docs/datasets/upload_dataset#upload-with-python).
- Dataset in HF hub, [here](https://huggingface.co/datasets/arbml/Calliar_dataset).

## Model training:

- Creating venv using venv in python.
- Install the diffusers using these instructions: [https://github.com/huggingface/diffusers/tree/main/examples/text_to_image#installing-the-dependencies](https://github.com/huggingface/diffusers/tree/main/examples/text_to_image#installing-the-dependencies).

- Run the training using the command line: 

```bash
export MODEL_NAME="CompVis/stable-diffusion-v1-4"
export dataset_name="lambdalabs/pokemon-blip-captions"

accelerate launch --mixed_precision="fp16"  train_text_to_image.py \
  --pretrained_model_name_or_path=$MODEL_NAME \
  --dataset_name=$dataset_name \
  --use_ema \
  --resolution=512 --center_crop --random_flip \
  --train_batch_size=1 \
  --gradient_accumulation_steps=4 \
  --gradient_checkpointing \
  --max_train_steps=15000 \
  --learning_rate=1e-05 \
  --max_grad_norm=1 \
  --lr_scheduler="constant" --lr_warmup_steps=0 \
  --output_dir="calliar_1" 
  ```
  
  - References:
  - The model and the latest checkpoint, [here](https://huggingface.co/arbml/CalliarGen).
