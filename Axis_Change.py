import cv2
import numpy as np
import random

def get_random_coordinates():
    x = random.randint(-460, 460)  # 您可以自定义范围
    y = random.randint(-250, 250)  # 您可以自定义范围
    return x, y

def get_coordinates():

    # 定义原始的矩形Q和任意四边形W的坐标
    halfWidth = 2740 / 2 / 2/1.5
    halfHeight = 1525 / 2 / 2/1.5

    Q = np.float32([
        [-halfWidth, -halfHeight],
        [halfWidth, -halfHeight],
        [halfWidth, halfHeight],
        [-halfWidth, halfHeight]
    ])

#  ！！！改四角坐标的地方！！！
    W = np.float32([
        [-halfWidth, -halfHeight],
        [halfWidth , -halfHeight],
        [halfWidth/2, halfHeight],
        [-halfWidth/2, halfHeight]
    ])
#  ！！！改四角坐标的地方！！！

    K = get_random_coordinates()

    # 使用cv2.getPerspectiveTransform计算透视变换矩阵
    M = cv2.getPerspectiveTransform(Q, W)


    # 对乒乓球的坐标K进行透视变换，得到L
    K_ = np.array([[K[0], K[1]]], dtype=np.float32)
    L = cv2.perspectiveTransform(K_.reshape(-1, 1, 2), M)
    point = [0,0]
    point[0] = L[0][0][0]
    point[1] = L[0][0][1]


    W_ = []

    # 通过循环将W的内容复制到W_中
    for x in range(W.shape[0]):
        row = []
        for y in range(W.shape[1]):
            row.append(W[x, y])
        W_.append(row)


    return point, W_


