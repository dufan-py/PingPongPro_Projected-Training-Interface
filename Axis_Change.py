import cv2
import numpy as np


# 定义原始的矩形Q和任意四边形W的坐标
halfWidth = 550 * 1.8 / 2
halfHeight = 550 / 2

Q = np.float32([
    [-halfWidth, -halfHeight],
    [halfWidth, -halfHeight],
    [halfWidth, halfHeight],
    [-halfWidth, halfHeight]
])

W = np.float32([
    [-halfWidth, -halfHeight + 50],
    [halfWidth + 50, -halfHeight],
    [halfWidth, halfHeight],
    [-halfWidth, halfHeight - 50]
])



K = get_random_coordinates();

# Q和W是已经定义好的四边形的四个角的坐标
pts1 = np.float32(Q)  # Q的坐标，例如：[[0,0],[rectWidth,0],[rectWidth,rectHeight],[0,rectHeight]]
pts2 = np.float32(W)  # W的坐标，例如：[[0,50],[rectWidth+50,0],[rectWidth,rectHeight-50],[0,rectHeight]]

# 使用cv2.getPerspectiveTransform计算透视变换矩阵
M = cv2.getPerspectiveTransform(pts1, pts2)

# 对乒乓球的坐标K进行透视变换，得到L
K_ = np.array([[[K.x, K.y]]], dtype='float32')  # 假设K有x和y属性
L_ = cv2.perspectiveTransform(K_, M)

# L_中的值即为变换后的乒乓球坐标L
