import os
import scipy.io
import cv2
import numpy as np
import torch
from facenet_pytorch import MTCNN
from tqdm import tqdm

# ================= 配置区域 =================
MAT_FILE = 'p1_0.mat'          # 你的 .mat 文件名
OUTPUT_DIR = 'processed_faces' # 输出文件夹
TARGET_SIZE = (128, 128)       # 想要输出的大小
CONFIDENCE = 0.9               # 置信度 (越确信是脸才截取)
# ===========================================

def process():
    # 1. 检查设备 (有显卡用显卡，没显卡用CPU)
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    print(f"正在使用设备: {device}")

    # 2. 初始化 MTCNN
    # min_face_size=20: 因为你的原图只有60x80，必须把最小检测尺寸调小，否则检测不到
    # margin=0: 紧贴着脸剪裁
    mtcnn = MTCNN(keep_all=False, select_largest=True, min_face_size=15, 
                  margin=0, device=device, post_process=False)

    # 3. 读取 .mat
    if not os.path.exists(MAT_FILE):
        print("找不到 .mat 文件！")
        return

    print(f"正在读取 {MAT_FILE} ...")
    mat = scipy.io.loadmat(MAT_FILE)
    
    # 获取视频数据
    if 'video' not in mat:
        print("错误：.mat 里没有 'video' 这个变量")
        return
    
    video_data = mat['video'] # 形状 (1800, 80, 60, 3)
    total_frames = video_data.shape[0]
    
    # 准备输出目录
    save_folder = os.path.join(OUTPUT_DIR, os.path.splitext(MAT_FILE)[0])
    os.makedirs(save_folder, exist_ok=True)
    
    print(f"数据加载成功: {video_data.shape}。开始处理...")

    # 4. 循环处理每一帧
    for i in tqdm(range(total_frames), desc="处理进度"):
        # 获取图像并确保是 uint8 格式
        frame = video_data[i]
        if frame.dtype != np.uint8:
            frame = (frame * 255).astype(np.uint8) if frame.max() <= 1.5 else frame.astype(np.uint8)

        # MTCNN 内部需要 RGB，但 OpenCV 保存需要 BGR
        # 如果你的 .mat 原生是 RGB (通常是)，则不需要动，直接送入 mtcnn
        # 如果 .mat 原生是 BGR (比较少见)，则需要转换
        # 这里假设 .mat 是 RGB
        img_rgb = frame 
        
        # --- 核心步骤：人脸检测 ---
        try:
            # detect 返回框框 [x1, y1, x2, y2]
            boxes, probs = mtcnn.detect(img_rgb)
        except RuntimeError:
            # 捕获类似刚才那样的崩溃
            boxes = None

        final_img = None
        
        # 如果检测到了人脸
        if boxes is not None and len(boxes) > 0:
            # 取置信度最高的一个
            box = boxes[0]
            x1, y1, x2, y2 = [int(b) for b in box]

            # 边界检查 (防止坐标变成负数或超出图片)
            h_raw, w_raw, _ = img_rgb.shape
            x1 = max(0, x1); y1 = max(0, y1)
            x2 = min(w_raw, x2); y2 = min(h_raw, y2)

            # 裁剪
            face_crop = img_rgb[y1:y2, x1:x2]
            
            # 如果裁剪有效，Resize 到 128x128
            if face_crop.size > 0:
                final_img = cv2.resize(face_crop, TARGET_SIZE, interpolation=cv2.INTER_CUBIC)

        # --- 兜底策略 ---
        # 如果这一帧没检测到脸（你的图太小了，很有可能发生），
        # 为了不让数据断层，我们直接把原图 Resize 后保存
        if final_img is None:
            final_img = cv2.resize(img_rgb, TARGET_SIZE, interpolation=cv2.INTER_CUBIC)

        # --- 保存 ---
        # 保存前要把 RGB 转回 BGR，因为 cv2.imwrite 默认是 BGR
        save_img_bgr = cv2.cvtColor(final_img, cv2.COLOR_RGB2BGR)
        
        filename = f"image_{i+1:05d}.png" # 5位数，右对齐
        cv2.imwrite(os.path.join(save_folder, filename), save_img_bgr)

    print(f"\n大功告成！所有图片保存在: {save_folder}")

if __name__ == '__main__':
    process()