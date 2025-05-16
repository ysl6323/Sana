#/bin/bash
set -e

work_dir=output/debug
np=1


if [[ $1 == *.yaml ]]; then
    config=$1
    shift
else
    config="/data/shanglinyuan/Sana/configs/sana_config/512ms/Sana_200M_img512.yaml"
    echo "Only support .yaml files, but get $1. Set to --config_path=$config"
fi

TRITON_PRINT_AUTOTUNING=1 HF_ENDPOINT=https://hf-mirror.com CUDA_VISIBLE_DEVICES=3 \
    torchrun --nproc_per_node=$np --master_port=15432 \
        train_scripts/train.py \
        --config_path=$config \
        --work_dir=$work_dir \
        --name=tmp \
        --resume_from=latest \
        --report_to=tensorboard \
        --debug=false \
        "$@"
