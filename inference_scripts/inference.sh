yaml=/data/shanglinyuan/Sana/configs/sana_config/512ms/Sana_200M_img512.yaml
pth=/data/shanglinyuan/pretrained_weights/Sana-200M-vanilla-82Kdata/checkpoints/epoch_71_step_60000.pth
prompt=/data/shanglinyuan/Sana/test_prompt.txt

python scripts/inference.py\
    --config=$yaml\
    --model_path=$pth\
    --txt_file=$prompt\
    --step=20\
    # --model.image_size=256