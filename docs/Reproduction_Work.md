# Explanation Tree

> 显示新增代码、修改代码.



# 复现步骤

> 引用部分均给出基于项目文件夹的相对路径，方便导航到相关代码上。
> **注意：**不是实际跑代码时的路径。

### 配置工作环境

| **组件**        | **详细参数**                                                 |
| --------------- | ------------------------------------------------------------ |
| **OS**          | Windows 11                                                   |
| **Environment** | Minconda (env: `pytorch_env`)                                |
| **Python**      | 3.9.23                                                       |
| **Framework**   | PyTorch 2.5.1 (CUDA 12.1)                                    |
| **Libraries**   | OpenCV 4.10.0, NumPy 2.0.2, Pandas 2.3.2, Facenet-PyTorch 2.6.0 |

### 数据预处理

> Path: `.\Preprocess\MMPD_MMPD_MMPD_PHYSFORMER_BASIC.yaml`

+ 理解 `rPPG-Toolbox` 关于 `MMPD` 数据集的预处理代码
+ 分析 `.yaml` 结构
+ 写关于 `7-2-1` **MMPD** 的 `.yaml` 配置 处理数据

+ 开始处理数据：`python main.py --config_file ./configs/train_configs/MMPD_MMPD_MMPD_PHYSFORMER_BASIC.yaml`