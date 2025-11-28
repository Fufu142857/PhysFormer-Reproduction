# PhysNet

### 专业名词

- “Spatio-Temporal Networks” ([Yu 等, 2019](zotero://select/library/items/M2LH9M7H)) ([snapshot](zotero://open-pdf/library/items/JDIPGVXJ?sel=%23abs%20%3E%20h1)) 时空网络。
  
- “pulse peaks” ([Yu 等, 2019](zotero://select/library/items/M2LH9M7H)) ([snapshot](zotero://open-pdf/library/items/JDIPGVXJ?sel=blockquote)) 脉冲峰值。
  
- “ground truth pulse curves” ([Yu 等, 2019](zotero://select/library/items/M2LH9M7H)) ([snapshot](zotero://open-pdf/library/items/JDIPGVXJ?sel=blockquote)) 真值脉冲曲线。
  
- “the constraint of trend-consistency with ground truth pulse curves” ([Yu 等, 2019](zotero://select/library/items/M2LH9M7H)) ([snapshot](zotero://open-pdf/library/items/JDIPGVXJ?sel=blockquote)) 与真值脉冲曲线的趋势一致性约束。（是和这条曲线趋势一致这样的约束吗？）
  
- “benchmark datasets” ([Yu 等, 2019](zotero://select/library/items/M2LH9M7H)) ([snapshot](zotero://open-pdf/library/items/JDIPGVXJ?sel=blockquote)) 基准数据集。
  
- “remote photoplethysmography (rPPG)” ([Yu 等, 2019](zotero://select/library/items/M2LH9M7H)) ([snapshot](zotero://open-pdf/library/items/JDIPGVXJ?sel=blockquote)) 远程光电容积描记法( rPPG )。
  
- “the Electrocardiography (ECG) and Photoplethysmograph (PPG)” ([Yu 等, 2019, p. 1](zotero://select/library/items/M2LH9M7H)) ([pdf](zotero://open-pdf/library/items/GZ6YD62T?page=1)) 心电图( Ecg )和光电容积描记仪( PPG )。
  
- “end-to-end framework” ([Yu 等, 2019, p. 10](zotero://select/library/items/M2LH9M7H)) ([pdf](zotero://open-pdf/library/items/GZ6YD62T?page=10)) 端到端框架。
  
- “PhysNet” ([Yu 等, 2019, p. 10](zotero://select/library/items/M2LH9M7H)) ([pdf](zotero://open-pdf/library/items/GZ6YD62T?page=10)) 物理网络。
  
- “accurate time location of each individual pulse peak” ([Yu 等, 2019, p. 10](zotero://select/library/items/M2LH9M7H)) ([pdf](zotero://open-pdf/library/items/GZ6YD62T?page=10)) 对每个单独的脉冲峰值进行准确的时间定位。 **这是方法中的具体一个细节吗**
  
- “regions of interest (ROI)” ([Yu 等, 2019, p. 2](zotero://select/library/items/M2LH9M7H)) ([pdf](zotero://open-pdf/library/items/GZ6YD62T?page=2)) ( ROI )。
  
- “low frequency (LF), high frequency (HF), and their ratio LF/HF” ([Yu 等, 2019, p. 3](zotero://select/library/items/M2LH9M7H)) ([pdf](zotero://open-pdf/library/items/GZ6YD62T?page=3)) 低频( LF )、高频( HF )及其比值LF / HF。“the respiratory frequency (RF)” ([Yu 等, 2019, p. 3](zotero://select/library/items/M2LH9M7H)) ([pdf](zotero://open-pdf/library/items/GZ6YD62T?page=3)) 呼吸频率( RF )。
  
- “3D convolutional neural networks (3DCNN)” ([Yu 等, 2019, p. 3](zotero://select/library/items/M2LH9M7H)) ([pdf](zotero://open-pdf/library/items/GZ6YD62T?page=3)) 3D卷积神经网络( 3DCNN )。
  
- “recurrent neural network (RNN)” ([Yu 等, 2019, p. 3](zotero://select/library/items/M2LH9M7H)) ([pdf](zotero://open-pdf/library/items/GZ6YD62T?page=3)) 循环神经网络( RNN )。
  

## 需要收集的数据

- HR是 heart rate，找 Average 的
  
- “atrial fibrillation (AF)” ([Yu 等, 2019](zotero://select/library/items/M2LH9M7H)) ([snapshot](zotero://open-pdf/library/items/JDIPGVXJ?sel=blockquote)) 心房颤动( AF )。
  
- “heart rate variability (HRV)” ([Yu 等, 2019, p. 1](zotero://select/library/items/M2LH9M7H)) ([pdf](zotero://open-pdf/library/items/GZ6YD62T?page=1)) 心率变异性( HRV )。
  
- “Emotion Recogniton” ([Yu 等, 2019, p. 2](zotero://select/library/items/M2LH9M7H)) ([pdf](zotero://open-pdf/library/items/GZ6YD62T?page=2)) 情感识别。
  
- “Peak Detection” ([Yu 等, 2019, p. 2](zotero://select/library/items/M2LH9M7H)) ([pdf](zotero://open-pdf/library/items/GZ6YD62T?page=2)) 峰值检测。
  
- “inter-beat-interval (IBI)” ([Yu 等, 2019, p. 1](zotero://select/library/items/M2LH9M7H)) ([pdf](zotero://open-pdf/library/items/GZ6YD62T?page=1)) 拍间间隔( inter-beat- interval，IBI )。


## Introduction

- Figure 1 shows **frames and steps.**
  
- **所以主要是 spatio-temporal networks 的贡献**

## Related Work

> 领域内相关工作

- rPPG 的测量方法
  
- HRV 的测量方法
  
- 时空网络
  
    - 两种主流框架
      
        - 3DCNN：3D卷积神经网络
          
        - RNN：循环神经网络
          

## 理论推导

> spatio-temporal modeling and loss functions 时空建模方法和损失函数

### PhysNet

> Merge two steps into one step, architecture of it shown in Figure below.
> 
> 这篇文章提出的**核心的时空模型**，就是基于 3DCNN or RNN（两种主流框架）的 PhysNet。
- Two steps
  
    - | **步骤**         | **目标**                                                     |
      | ---------------- | ------------------------------------------------------------ |
      | **第一次投影**   | 离开**RGB空间**，进入一个对**肤色和生理信号更敏感**的空间。  |
      | **第二次再投影** | 在新空间里，找到一个**最佳方向**，将**生理信号**与**光照/运动噪声**分离开。 |



***

# 25-11-24 New-Note

## n.

+ **HR** heart rate 心率
+ **RF** respiration frequency 呼吸频率
+ **HRV** heart rate variability 心率变异性
+ 

## Reproduction Steps

+ 其实已经有过一步真正的裁剪（Preprocessing），用 MTCNN 人脸检测算法把人脸抠出来了。这个……视频变成一张张连续图片了没？
  ohno我要用的数据集并没有变

+ ### Input Video

+ ### Stem ($E_{stem}$)

  + **目标：**
  + **做法：**

  > 因为后续没有谈到stem，所以现在我们集中讨论stem这个问题。
  >
  > **新问题**
  >
  > 1. + **特征空间，高维特征，D=96 种抽象特征，transformer才能懂**
  >
  >      代码里是 `dim: int = 768`
  >      （每一副都在做什么，为什么一定是96，需要为了时间而变小或者为了需要的信息而变大吗。）
  >
  >    + Transformer 的核心计算复杂度（Attention 机制）通常与**Token 数量的平方**成正比 $O(N^2)$ 。Transformer 的核心是让**每一个 Token** 去和 **每一个 Token**“打招呼”（计算相关性）。
  >      + 这是 Transformer (Vaswani et al. 2017) 的基础常识(需要补习)，论文直接引用了相关工作
  >
  > 2. 我需要特别详细地理解卷积是如何实现我们的操作的了，我现在正在对照Physformer.py 里的代码一个个看
  >
  >    ```python
  >    # Stem 涉及到的所有代码
  >            self.Stem0 = nn.Sequential(
  >                nn.Conv3d(3, dim//4, [1, 5, 5], stride=1, padding=[0,2,2]),
  >                nn.BatchNorm3d(dim//4),
  >                nn.ReLU(inplace=True),
  >                nn.MaxPool3d((1, 2, 2), stride=(1, 2, 2)),
  >            )
  >                        
  >            self.Stem1 = nn.Sequential(
  >                nn.Conv3d(dim//4, dim//2, [3, 3, 3], stride=1, padding=1),
  >                nn.BatchNorm3d(dim//2),
  >                nn.ReLU(inplace=True),
  >                nn.MaxPool3d((1, 2, 2), stride=(1, 2, 2)),
  >            )
  >            self.Stem2 = nn.Sequential(
  >                nn.Conv3d(dim//2, dim, [3, 3, 3], stride=1, padding=1),
  >                nn.BatchNorm3d(dim),
  >                nn.ReLU(inplace=True),
  >                nn.MaxPool3d((1, 2, 2), stride=(1, 2, 2)),
  >            )
  >    # 这个代码是在实现这个模型的，然后除了ST_TDC以外代码都没导入，所以我下面不了解的东西实际上都是传统库里的，但我学不扎实所以没有理解。不理解是什么也不理解具体的函数代码长什么样有什么用。
  >    # .Sequential and .Conv3d 是什么？
  >    # BatchNorm3d是什么
  >    ```
  >
  >    + 卷积核大小的体现与意义，归一化的体现，激活函数，最大池化
  >      + 归一化
  >        $$y = \frac{x - \mu}{\sqrt{\sigma^2 + \epsilon}} \cdot \gamma + \beta$$
  >        拉回 $N(0,1)$ 分布 ，学习参数 $\gamma, \beta$在哪里设置？

***

普通的transformer和TD transformer区别？
