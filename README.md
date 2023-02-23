# CalliarGen

**Multilingual OpenCLIP**: [![Multilingual OpenCLIP](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1zlGkbQh7ny9LKrMLNXtA6VDB151zxl_0?usp=sharing)


**Preprocessing:**

- Extract the caption from the images' names.
- Remove the numbers in the caption using [Maha library](https://github.com/TRoboto/Maha).
- Write the "file_name" and "text" in jsonl file as recommended from HF.
- Upload the dataset to HF dataset hub.


**Model training**:

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
  
