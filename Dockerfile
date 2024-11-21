FROM nvcr.io/nvidia/pytorch:24.06-py3

WORKDIR /app

RUN curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o ~/miniconda.sh \
    && sh ~/miniconda.sh -b -p /opt/conda \
    && rm ~/miniconda.sh

ENV PATH /opt/conda/bin:$PATH
COPY pyproject.toml pyproject.toml
COPY diffusion diffusion
COPY configs configs
COPY sana sana
COPY app app

COPY environment_setup.sh environment_setup.sh
RUN ./environment_setup.sh sana

# COPY server.py server.py
CMD ["conda", "run", "-n", "sana", "--no-capture-output", "python", "-u", "-W", "ignore", "app/app_sana.py", "--config=configs/sana_config/1024ms/Sana_1600M_img1024.yaml", "--model_path=hf://Sana_1600M_1024px/checkpoints/Sana_1600M_1024px.pth",]
