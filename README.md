# Reproduction: PhysFormer on MMPD Dataset

This repository is an **unofficial reproduction** of the CVPR 2022 paper **PhysFormer** on the **MMPD dataset** (mini-MMPD).

The original code is forked from [ZitongYu/PhysFormer](https://github.com/ZitongYu/PhysFormer).

## 🚀 Project Goal
The primary goal of this project is to verify the performance of the PhysFormer model on the challenging MMPD dataset. I strictly follow the **evaluation protocols and preprocessing pipelines** proposed in the recent state-of-the-art work, **RhythmFormer**.

## 📄 My Reproduction Work

Detailed documentation of my reproduction process, experimental analysis, and code modifications explanation can be found here: 
👉 **[Reproduction_Work.md](./docs/Reproduction_Work.md)** 

> **Note1:** A **project file tree** highlighting the new and modified code files (vs. the original `PhysFormer`) is provided at the beginning of the document.
>
>  *Note2: Documentation is written in Chinese 🇨🇳*

## Acknowledgements

This reproduction involves three key components. I explicitly acknowledge and credit the following works for their contributions to the community:

### 1. Model Architecture (Original Work)
* **Source:** [PhysFormer: Facial Video-based Physiological Measurement with Temporal Difference Transformer](https://github.com/ZitongYu/PhysFormer)
* **Usage:** I use the original model provided by Yu et al.

### 2. Evaluation Protocol
* **Source:** [RhythmFormer: Extracting Patterned rPPG Signals based on Periodic Sparse Attention](https://arxiv.org/abs/2402.12788)
* **Usage:** I strictly follow the experimental setting described in the RhythmFormer paper:
    * **Dataset:** mini-MMPD.
    * **Data Split:** Sequential split with 7:1:2 ratio (Train:Val:Test).
    * **Preprocessing:** Facial region cropped and resized to 128x128 in the first frame, fixed for subsequent frames.

### 3. Data Preprocessing Tools
* **Source:** [rPPG-Toolbox](https://github.com/ubicomplab/rPPG-Toolbox)
* **Usage:** I utilize the robust data loading and preprocessing pipelines from rPPG-Toolbox to handle the MMPD dataset format and generate inputs compatible with PhysFormer.

## 📝 References

If you find this reproduction work record useful, please cite the original authors, the evaluation protocol provider, and the toolbox developers:

**1. PhysFormer:**

```
     @inproceedings{yu2021physformer,
        title={PhysFormer: Facial Video-based Physiological Measurement with Temporal Difference Transformer},
        author={Yu, Zitong and Shen, Yuming and Shi, Jingang and Zhao, Hengshuang and Torr, Philip and Zhao, Guoying},
        booktitle={CVPR},
        year={2022}
      }
      
      @article{yu2023physformer++,
       title={PhysFormer++: Facial Video-based Physiological Measurement with SlowFast Temporal Difference Transformer},
       author={Yu, Zitong and Shen, Yuming and Shi, Jingang and Zhao, Hengshuang and Cui, Yawen and Zhang, Jiehua and Torr, Philip and Zhao, Guoying},
       journal={International Journal of Computer Vision (IJCV)},
       pages={1--24},
       year={2023}
     }
```

**2. RhythmFormer:**

> *I followed the data split and preprocessing protocol defined in RhythmFormer.*

```
@article{zou2025rhythmformer,
    title = {RhythmFormer: Extracting patterned rPPG signals based on periodic sparse attention},
    journal = {Pattern Recognition},
    volume = {164},
    pages = {111511},
    year = {2025},
    issn = {0031-3203},
    doi = {https://doi.org/10.1016/j.patcog.2025.111511},
    url = {https://www.sciencedirect.com/science/article/pii/S0031320325001712},
    author = {Bochao Zou and Zizheng Guo and Jiansheng Chen and Junbao Zhuo and Weiran Huang and Huimin Ma},
    keywords = {Remote physiological measurement, Periodic sparse attention},
}
```

**3. rPPG-Toolbox:**

> *I used rPPG-Toolbox for data loading and processing.*

```
@article{liu2022rppg,
  title={rPPG-Toolbox: Deep Remote PPG Toolbox},
  author={Liu, Xin and Narayanswamy, Girish and Paruchuri, Akshay and Zhang, Xiaoyu and Tang, Jiankai and Zhang, Yuzhe and Wang, Yuntao and Sengupta, Soumyadip and Patel, Shwetak and McDuff, Daniel},
  journal={arXiv preprint arXiv:2210.00716},
  year={2022}
}
```

**4. Dataset (MMPD):**

```
@INPROCEEDINGS{10340857,
  author={Tang, Jiankai and Chen, Kequan and Wang, Yuntao and Shi, Yuanchun and Patel, Shwetak and McDuff, Daniel and Liu, Xin},
  booktitle={2023 45th Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC)}, 
  title={MMPD: Multi-Domain Mobile Video Physiology Dataset}, 
  year={2023},
  volume={},
  number={},
  pages={1-5},
  doi={10.1109/EMBC40787.2023.10340857}}
```
