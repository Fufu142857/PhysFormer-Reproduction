# 工作记录

> 30 min 一记，极限专注时间

1. 理解 3.1 Stem
2. 完全理解 Stem
3. 了解 Transformer(https://jalammar.github.io/illustrated-transformer/)
4. 修硬盘（啊啊啊花了两个小时，My heart broken，我再也不跨系统工作了
5. 继续了解 Transformer
6. 我来不及理解了，先清洗数据
7. 理解 `Loadtemporal_data.py`

## 清洗数据

> 我分配到的是 mini_MMPD 的数据集内复现工作。

+ 我拿到的：`.mat` $\to$ `.png`

## 数据预处理

+ 理解模型需要的 `Input` 特征

  + 只有人脸的图片，于是我们……
    + 
  + 名称要求：
  + `VIPL_train_list` 要求：
  + `VIPL_root_list` 要求：

+ **改路径：**训练模型需要的输入路径入口

  ```python
  # train_Physformer_160_VIPL.py
  VIPL_train(VIPL_train_list, VIPL_root_list, transform=transforms.Compose([Normaliztion(),RandomHorizontalFlip(), ToTensor()]))
  ```

  ```python
  # Loadtemporal_data.py
  def __init__(self, info_list, root_dir, transform = None):
  ```

  