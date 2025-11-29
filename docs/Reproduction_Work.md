# 复现步骤

> 引用部分均给出基于项目文件夹的相对路径，方便导航到相关代码上。

### 配置工作环境

| **组件**        | **详细参数**                                                 |
| --------------- | ------------------------------------------------------------ |
| **OS**          | Windows 11                                                   |
| **Environment** | Minconda (env: `pytorch_env`)                                |
| **Python**      | 3.9.23                                                       |
| **Framework**   | PyTorch 2.5.1 (CUDA 12.1)                                    |
| **Libraries**   | OpenCV 4.10.0, NumPy 2.0.2, Pandas 2.3.2, Facenet-PyTorch 2.6.0 |

### 理解数据集 MMPD

+ 分配到的是 **mini_MMPD** 的**数据集内复现**工作

+ 我拿到 `.mat` ，写脚本$\to$ `.png` 	*脚本未留下*
+ 检查 `.png` ，背景干净

### 数据预处理

>Path: `./Preprocess/`

#### 

### **改路径** 

+ `VIPL_train_list` 要求：

  + **视频文件夹路径** (Col 0)

  + **开始帧序号** (Col 1)

  + **帧率** (Col 2)

  + **平均心率值 (GT)** (Col 3)

    **（隐藏的大坑）160个连续的心率波形值** (Col 5 到 5+160)

    - 代码第 72 行 `self.landmarks_frame.iloc[idx, 5:5+160].values` 说明它试图读取逐帧的心率标签（即 ECG 信号或 BVP 信号）。
    - 如果你没有这 160 个波形数据，只是想用平均心率训练，你需要修改 `Loadtemporal_data.py` 的代码，把读取 `ecg_label` 的部分删掉或填假数据，否则程序会因为列数不够而报错。

+ `VIPL_root_list` 要求

```python
# train_Physformer_160_VIPL.py
VIPL_train(VIPL_train_list, VIPL_root_list, transform=transforms.Compose([Normaliztion(),RandomHorizontalFlip(), ToTensor()]))
```

```python
# Loadtemporal_data.py
def __init__(self, info_list, root_dir, transform = None):
```


### 训练前准备

> Path: 

+ 调整参数
+ 五折交叉