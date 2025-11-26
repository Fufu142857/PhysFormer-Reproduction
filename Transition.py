import scipy.io as sio
import numpy as np
import cv2
import os

# 读取一个文件试试，比如 p1_0.mat
mat_path = 'p1_0.mat' 
# 配置路径
output_dir = '../MMPD_data/p1_0'    # 图片要存到哪里
os.makedirs(output_dir, exist_ok=True)

# 1. 读取数据
data = sio.loadmat(mat_path)
video_data = data['video']  # Shape: (1800, 80, 60, 3)

# 2. 检查维度顺序
# 有时候 mat 里是 (H, W, C, T)，有时候是 (T, H, W, C)
# 你的输出说是 (1800, ...)，说明第一维是帧数，这很好！
frames_total = video_data.shape[0]

print(f"开始转换 {frames_total} 帧图片...")

for i in range(frames_total):
    # 取出第 i 帧
    frame = video_data[i] # 形状应该是 (80, 60, 3)

    if frame.max() <= 1.01:
        frame = frame * 255.0
        
    frame = np.clip(frame, 0, 255).astype(np.uint8)
    
    # 【重要】颜色转换：Matlab通常存RGB，但OpenCV用BGR
    # frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    # 【核心步骤】暴力拉伸到 128x128 (PhysFormer的要求)
    frame = cv2.resize(frame, (128, 128))
    
    # 命名：image_00001.png (注意：VIPL代码通常从1开始计数)
    filename = f"image_{i+1:05d}.png"
    save_path = os.path.join(output_dir, filename)
    
    cv2.imwrite(save_path, frame)

print("转换完成！去文件夹里看看吧！")
