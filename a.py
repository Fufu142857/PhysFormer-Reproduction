import os

# 你的数据集路径
dataset_path = r"D:\mini_MMPD"
expected_count = 20
total_subjects = 33
error_found = False

print(f"正在检查: {dataset_path} ...\n")

for i in range(1, total_subjects + 1):
    sub_name = f"subject{i}"
    sub_path = os.path.join(dataset_path, sub_name)
    
    # 1. 检查文件夹是否存在
    if not os.path.exists(sub_path):
        print(f"❌ 缺失文件夹: {sub_name}")
        error_found = True
        continue
    
    # 2. 计算该文件夹下的 .mat 文件数量
    mat_files = [f for f in os.listdir(sub_path) if f.endswith('.mat')]
    count = len(mat_files)
    
    # 3. 如果数量不对，打印报错
    if count != expected_count:
        print(f"⚠️  {sub_name}: 发现 {count} 个文件 (应为 {expected_count} 个)")
        error_found = True

if not error_found:
    print(f"✅ 完美！所有 {total_subjects} 个文件夹都包含 {expected_count} 个 .mat 文件。")
else:
    print("\n检查结束，请处理上述缺失或错误。")