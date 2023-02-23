from diffusers import StableDiffusionPipeline
import torch 

model_path = "/home/lenovo/Desktop/stable_diffusion/diffusers/examples/text_to_image/calliar_1"
pipe = StableDiffusionPipeline.from_pretrained(model_path, torch_dtype=torch.float16)
pipe.to("cuda")

image = pipe(prompt="الحمدلله").images[0]
image.save("الحمدلله.png")