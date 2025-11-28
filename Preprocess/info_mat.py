import scipy.io as sio

# 1. 加载文件
data = sio.loadmat('D:\mini_MMPD\subject1\p1_0.mat')

# 2. 打印所有的 Key 
print("所有的Key:", data.keys())
print()

# 3. 打印所有对应信息
for key in data.keys():
    # 跳过 header
    if key.startswith('__'): continue
    # 打印 值
    val = data[key]
    if hasattr(val, 'shape'):
        print(f"{key}:形状{val.shape}, 类型{val.dtype}")
    else:
        print(f"{key}:内容{val}")
    print()
