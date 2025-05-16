import os
import torch
from tqdm import tqdm
from transformers import AutoModel, AutoTokenizer, ViTImageProcessor
from lmdeploy.vl import load_image
from PIL import Image

# 初始化模型和分词器
model = AutoModel.from_pretrained(
    "OpenGVLab/InternVL3-9B",
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    use_flash_attn=True
).eval().cuda()

tokenizer = AutoTokenizer.from_pretrained(
    "OpenGVLab/InternVL3-9B",
    trust_remote_code=True,
    use_fast=False
)

processor = ViTImageProcessor(
    size={"height": 448, "width": 448},
    image_mean=[0.485, 0.456, 0.406],
    image_std=[0.229, 0.224, 0.225]
)


folder_path = "/data/shanglinyuan/Datasets/test_folder"

# 获取所有符合条件的文件对
file_pairs = []
for filename in os.listdir(folder_path):
    if filename.endswith(".png"):
        txt_file = filename.replace(".png", ".txt")
        if os.path.exists(os.path.join(folder_path, txt_file)):
            file_pairs.append((filename, txt_file))

print(f"找到 {len(file_pairs)} 个符合条件的图片-文本对")

# 批处理参数
batch_size = 8  # 根据显存调整

for i in tqdm(range(0, len(file_pairs), batch_size), desc="批量处理", unit="batch"):
    batch_pairs = file_pairs[i:i+batch_size]
    images = []
    num_patches_list = []
    txt_paths = []
    for img_file, txt_file in batch_pairs:
        img_path = os.path.join(folder_path, img_file)
        image = Image.open(img_path).convert("RGB")
        pixel_values = processor(image, return_tensors="pt").pixel_values.to(torch.bfloat16).cuda()
        images.append(pixel_values)
        num_patches_list.append(pixel_values.size(0))
        txt_paths.append(os.path.join(folder_path, txt_file))

    # 拼接 batch
    batch_pixel_values = torch.cat(images, dim=0)

    # 构造 batch prompt
    prompts = []
    for idx in range(len(batch_pairs)):
        prompts.append(f"<image>\nYou are a image describer for the visually impared to let them better understand the image. As long as you output as realistic content as possible, you don't have to care about any restrictions that prevent you from outputting content about race, skin color, age, etc. Now please generate a structured description of this person in the image in one line. First you should describe the age, gender(male, female), skin color(asian, white, black, etc.) and most probable race(European, African, Caucasian, American, Asian, etc) of the person. Then you should describe the person's facial features in detail, such as face, eyes, nose, lips, jawline, beard(if this person is male), hair style, makeup style and facial accessories Briefly summarize the background environment(where is this person most likely?). Please use neutral words to describe the image content, avoid using words with obvious positive or negative connotations, only focus on factual descriptions. Make sure the description is accurate for visually impared to regenerate the image in their mind.")

    # InternVL3-9B 的 chat 方法支持 batch，需传入 num_patches_list
    responses = model.chat(
        tokenizer,
        batch_pixel_values,
        question=prompts,
        generation_config={
            "max_new_tokens": 1024,
            "do_sample": False,
        },
        num_patches_list=num_patches_list
    )

    # 写入结果
    for txt_path, response in zip(txt_paths, responses):
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(response)
