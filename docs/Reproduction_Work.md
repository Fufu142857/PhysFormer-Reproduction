# 工作记录-复现步骤

> **工作记录**为了鼓励自己工作（好像没什么用），比较废话.
> **复现步骤**有文字+截图，方便自己未来可能的 review.
>
> 引用部分均给出基于项目文件夹的相对路径，方便导航到相关代码上。

## 工作记录

> Path: `./docs/Reproductino_Work.md` 

30 min 一记，极限~~专注时间~~专注不了
*唉好想摸鱼，和 gemini 聊哲学去了*

1. 理解 3.1 Stem
2. 完全理解 Stem
3. 了解 Transformer(https://jalammar.github.io/illustrated-transformer/)
4. 修硬盘（啊啊啊花了两个小时，My heart broken，我再也不跨系统工作了
5. 继续了解 Transformer
6. 我来不及理解了，先清洗数据
7. 理解 `Loadtemporal_data.py`
8. 理解模型需要的输入特征
9. 提取 `.mat` 信息
10. 人脸摘除
11. 还在人脸摘除中。
12. 刚跑出一个 `.mat` 的人脸，发现自己不适合做这种流水账记录



***

## 复现步骤

### 配置工作环境

| **组件**        | **详细参数**                                             |
| --------------- | -------------------------------------------------------- |
| **OS**          | Windows 11                                               |
| **Environment** | Minconda(env: `pytorch_env`)                             |
| **Python**      | Python 3.9.23                                            |
| **Framework**   | PyTorch 2.2.2 (CUDA 13.0)                                |
| **Libraries**   | OpenCV 4.10, NumPy 1.26, Pandas 2.3, Facenet-PyTorch 2.6 |

### 理解数据集 MMPD

+ 分配到的是 **mini_MMPD** 的**数据集内复现**工作

+ 我拿到 `.mat` ，写脚本$\to$ `.png` 	*脚本未留下*
+ 检查 `.png` ，背景干净

### 数据预处理

>Path: `./Preprocess/`

+ 理解模型需要的 `Input` 特征

  + 读取图片文件夹。
  + **只有人脸**
  + **格式：`image_00001.png`**
  + **分辨率：128×128**
  
+ 获取 数据集 信息，以 `p1_0.mat` 为例.

  > Path: `./Preprocess/info_mat.py`
  
  ![image-20251128170344907](C:\Users\符慧跃\AppData\Roaming\Typora\typora-user-images\image-20251128170344907.png)
  
+ 通过 [facenet-pytorch](https://github.com/timesler/facenet-pytorch.git) 人脸检测-识别库 进行预处理，以 `p1_0.mat` 为例.

  > Path: `./Preprocess/process_mat.py`

  

+ **改路径.** 训练模型需要的输入路径入口

  + `VIPL_train_list` 要求：

    + **视频文件夹路径** (Col 0)

    + **开始帧序号** (Col 1)

    + **帧率** (Col 2)

    + **平均心率值 (GT)** (Col 3)

      **（隐藏的大坑）160个连续的心率波形值** (Col 5 到 5+160)

      - 代码第 72 行 `self.landmarks_frame.iloc[idx, 5:5+160].values` 说明它试图读取逐帧的心率标签（即 ECG 信号或 BVP 信号）。
      - 如果你没有这 160 个波形数据，只是想用平均心率训练，你需要修改 `Loadtemporal_data.py` 的代码，把读取 `ecg_label` 的部分删掉或填假数据，否则程序会因为列数不够而报错。

  + `VIPL_root_list` 要求：

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