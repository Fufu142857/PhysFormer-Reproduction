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

+ #### 理解模型需要的 `Input` 特征

  + 读取图片文件夹。
  + **只有人脸**
  + **格式：`image_00001.png`**
  + **分辨率：128×128**
  
+ #### 获取 数据集 信息，以 `p1_0.mat` 为例

  > Path: `./Preprocess/info_mat.py`
  
  ![image-20251128170344907](C:\Users\符慧跃\AppData\Roaming\Typora\typora-user-images\image-20251128170344907.png)
  
+ #### 通过 [facenet-pytorch](https://github.com/timesler/facenet-pytorch.git) 人脸检测-识别库 进行预处理

  > Path: `./Preprocess/process_mat.py`

  + 以 `p1_0.mat` 为例
    <img src="C:\Users\符慧跃\AppData\Roaming\Typora\typora-user-images\image-20251128205635322.png" alt="image-20251128205635322" style="zoom:80%;" />

    很顺利，打开文件夹检查图片，图片很完美（参数、人脸）.

  + ##### 通过修改脚本，批量处理 $33 \times 20$ 个图片序列(`.mat`)，得到 `p1-0` 到 `p33-19` 个文件夹

    

+ #### 部分帧人脸识别失败，需要人为裁剪并处理

+ #### **改路径** 

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