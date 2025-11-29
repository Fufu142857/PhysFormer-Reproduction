import os
import scipy.io
import cv2
import numpy as np
import torch
from facenet_pytorch import MTCNN
from tqdm import tqdm
import datetime

# 不通用的记得改掉，比如路径之类的，来个注释

# 输出路径       
OUTPUT_DIR = './processed_faces' 
# 目标尺寸
TARGET_SIZE = (128, 128)       
# 批次处理
BATCH_SIZE = 512
# 日志文件名
LOG_FILE = 'process_log.txt'

# 打印时写入文件
def log(msg):
    print(msg)
    time_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"[{time_str}] {msg}\n")

def process(MAT_FILE):
    device = torch.device('cuda:0')
    # 调用 MTCNN 模型
    # 只要最大的脸，最小人脸尺寸 15x15，不要后处理
    mtcnn = MTCNN(keep_all=False, select_largest=True, min_face_size=15, 
                  margin=0, device=device, post_process=False)
    # 读取输入
    if not os.path.exists(MAT_FILE):
        log(f"找不到 {MAT_FILE}，请检查路径。")
        return
    mat = scipy.io.loadmat(MAT_FILE)
    log(f"正在读取 {MAT_FILE} ...")
    # 获取 `key` 为 'video' 的变量
    if 'video' not in mat:
        log(f"找不到 'video' 变量，请检查 {MAT_FILE} 文件内容。")
        return
    video_data = mat['video']
    total_frames = video_data.shape[0]
    # 准备输出
    file_name = os.path.splitext(os.path.basename(MAT_FILE))[0]
    subject_name = file_name.split('_')[0]
    save_folder = os.path.join(OUTPUT_DIR, subject_name, file_name)
    os.makedirs(save_folder, exist_ok=True)

    if video_data.dtype != np.uint8:
        video_data = (video_data * 255).astype(np.uint8) if video_data.max() <= 1.5 else video_data.astype(np.uint8)
    # 循环处理每512帧
    for i in tqdm(range(0, total_frames, BATCH_SIZE), desc="处理进度"):
        # 确定结束位置
        batch_end = min(i + BATCH_SIZE, total_frames)
        # 切片出当前批次的帧
        batch_frames = video_data[i : batch_end]

        # 人脸检测
        # 调用 detect 返回框框 [x1, y1, x2, y2] 和 置信度
        try:
            batch_boxes, batch_probs = mtcnn.detect(batch_frames)
        except RuntimeError:
            # 时间过长或显存不足时捕获错误
            batch_boxes = None
        
        final_img = None
        # 处理每一张图
        for j, frame in enumerate(batch_frames):
            current_index = i + j
            img_rgb = frame
            boxes = batch_boxes[j] if batch_boxes is not None else None
            # 处理检测结果
            last_valid_face = final_img        
            final_img = None
            if boxes is not None and len(boxes.shape) > 0:
                box = boxes[0] if boxes.ndim > 1 else boxes
                x1, y1, x2, y2 = [int(b) for b in box]
                # 边界检查 (防止坐标变成负数或超出图片)
                h_raw, w_raw, _ = img_rgb.shape
                x1 = max(0, x1); y1 = max(0, y1)
                x2 = min(w_raw, x2); y2 = min(h_raw, y2)
                # 裁剪
                face_crop = img_rgb[y1:y2, x1:x2]
                # 调整尺寸 到 128x128
                if face_crop.size > 0:
                    final_img = cv2.resize(face_crop, TARGET_SIZE,interpolation=cv2.INTER_CUBIC)
            if final_img is None:
                log(f"第 {i+j+1} 帧未检测到人脸，复制前一帧。")
                if last_valid_face is not None:
                    final_img = last_valid_face
                else:
                    log(f"第 {i+j+1} 帧未检测到人脸，且前一帧也无效，使用原图缩放。")
                    final_img = cv2.resize(img_rgb, TARGET_SIZE, interpolation=cv2.INTER_CUBIC)
            # 调整图片格式
            save_img_bgr = cv2.cvtColor(final_img, cv2.COLOR_RGB2BGR)
            # 调整文件名（五位数右对齐）
            filename = f"image_{current_index+1:05d}.png"
            # 及时保存图片
            cv2.imwrite(os.path.join(save_folder, filename), save_img_bgr, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
    log(f"\n成功转换{MAT_FILE}\n\n")

if __name__ == '__main__':
    # 输入路径
    for i in range(1, 34):
        MAT_DIR = 'subject{:d}'.format(i)
        for j in range(0, 20):
            MAT_FILE = MAT_DIR + '\p{:d}_{:d}.mat'.format(i,j)
            process(MAT_FILE)
    log(f"所有文件处理完成，结果保存在: {OUTPUT_DIR}\n")