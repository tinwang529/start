from ultralytics import YOLO
import numpy as np
import cv2

# 加载模型
model = YOLO("yolo11n.pt")

# 生成一张 640x640 的随机图片（模拟真实图片）
dummy_img = np.random.randint(0, 255, (640, 640, 3), dtype=np.uint8)

# 预测
results = model(dummy_img)

# 显示检测结果数量
print(f"✅ 检测完成！共检测到 {len(results[0].boxes)} 个物体")

# 如果你还想看到图片，可以保存
results[0].save("result_dummy.jpg")
print("✅ 结果已保存为 result_dummy.jpg")