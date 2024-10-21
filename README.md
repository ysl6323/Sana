<p align="center" style="border-radius: 10px">
  <img src="https://raw.githubusercontent.com/lawrence-cj/Sana/refs/heads/page/asset/sana.jpg" width="30%" alt="logo"/>
</p>

# ⚡️Sana: Efficient High-Resolution Image Synthesis with Linear Diffusion Transformer
[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg)](CODE_LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/release/python-3100/)

[//]: # ([![Model License]&#40;https://img.shields.io/badge/MODEL%20License-CC%20By%20NC%204.0-red.svg&#41;]&#40;MODEL_LICENSE&#41;)

[Sana arxiv](https://arxiv.org/abs/2410.10629) / [Sana Demo](https://sana-gen.mit.edu)

<p align="center" border-raduis="10px">
  <img src="asset/Sana.jpg" width="90%" alt="teaser_page1"/>
</p>


## 💡 Introduction
We introduce Sana, a text-to-image framework that can efficiently generate images up to 4096 × 4096 resolution. 
Sana can synthesize high-resolution, high-quality images with strong text-image alignment at a remarkably fast speed, deployable on laptop GPU. 
Core designs include:

(1) [DC-AE](https://hanlab.mit.edu/projects/dc-ae): unlike traditional AEs, which compress images only 8×, we trained an AE that can compress images 32×, effectively reducing the number of latent tokens. \
(2) Linear DiT: we replace all vanilla attention in DiT with linear attention, which is more efficient at high resolutions without sacrificing quality. \
(3) Decoder-only text encoder: we replaced T5 with modern decoder-only small LLM as the text encoder and designed complex human instruction with in-context learning to enhance the image-text alignment. \
(4) Efficient training and sampling: we propose **Flow-DPM-Solver** to reduce sampling steps, with efficient caption labeling and selection to accelerate convergence.

As a result, Sana-0.6B is very competitive with modern giant diffusion model (e.g. Flux-12B), being 20 times smaller and 100+ times faster in measured throughput. Moreover, Sana-0.6B can be deployed on a 16GB laptop GPU, taking less than 1 second to generate a 1024 × 1024 resolution image. Sana enables content creation at low cost.

## 🔥🔥 News
-  Sana code is coming soon
- (🔥 New) [DC-AE Code](https://github.com/mit-han-lab/efficientvit/blob/master/applications/dc_ae/README.md) and [weights]() are released!
- [2024/10] [Paper](https://arxiv.org/abs/2410.10629) is on Arxiv!


## Contents

- [TODO](#to-do-list)
- [Citation](#bibtex)

## 💪To-Do List

We will try our best to release

- \[ \] Training code
- \[ \] Inference code
- \[ \] Model zoo
- \[ \] Diffusers
- \[ \] ComfyUI

# 🤗Acknowledgements

- Thanks to [PixArt-α](https://github.com/PixArt-alpha/PixArt-alpha), [PixArt-Σ](https://github.com/PixArt-alpha/PixArt-sigma) and [Efficient-ViT](https://github.com/mit-han-lab/efficientvit) for their wonderful work and codebase!

[//]: # (- Thanks to [Diffusers]&#40;https://github.com/huggingface/diffusers&#41; for their wonderful technical support and awesome collaboration!)
[//]: # (- Thanks to [Hugging Face]&#40;https://github.com/huggingface&#41; for sponsoring the nicely demo!)

# 📖BibTeX

```
@misc{xie2024sana,
      title={Sana: Efficient High-Resolution Image Synthesis with Linear Diffusion Transformer},
      author={Enze Xie and Junsong Chen and Junyu Chen and Han Cai and Haotian Tang and Yujun Lin and Zhekai Zhang and Muyang Li and Ligeng Zhu and Yao Lu and Song Han},
      year={2024},
      eprint={2410.10629},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2410.10629},
    }
```

[//]: # (## Star History)

[//]: # ([![Star History Chart]&#40;https://api.star-history.com/svg?repos=NVlabs/Sana&type=Date&#41;]&#40;https://star-history.com/#NVlabs/Sana&Date&#41;)
