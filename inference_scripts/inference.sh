yaml=/data/shanglinyuan/Mini-Sana/configs/sana_config/512ms/Sana_200M_img512.yaml
pth=/data/shanglinyuan/Mini-Sana/output/debug/checkpoints/epoch_1_step_626.pth
prompt=/data/shanglinyuan/Mini-Sana/test_prompt.txt

python scripts/inference.py\
    --config=$yaml\
    --model_path=$pth\
    --txt_file=$prompt\
    --step=20