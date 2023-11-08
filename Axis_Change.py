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
    # halfWidth = 900
    # halfHeight = 600
    Q = np.float32([
        [-halfWidth, -halfHeight],
        [halfWidth, -halfHeight],
        [halfWidth, halfHeight],
        [-halfWidth, halfHeight]
    ])

# 改四角坐标的地方----------------------------
    W = np.float32([
        [-halfWidth, -halfHeight],
        [halfWidth , -halfHeight],
        [halfWidth/1.5, halfHeight/1.3],
        [-halfWidth/2, halfHeight]
    ])
# 改四角坐标的地方-----------------------------





    # 使用cv2.getPerspectiveTransform计算透视变换矩阵
    M = cv2.getPerspectiveTransform(Q, W)

    k =[[0,0]]
    point=[]
    LandPoint=[]
    k[0] = get_random_coordinates()

    for i in range(0, 9):
        k.append( [k[i][0]+15,k[i][1]+15] )

# TODO：把k中坐标变成后端提供的轨迹坐标
# TODO：把j中坐标变成后端提供的落点坐标
    j = []
    j.append([-100, -30])
    for i in range(0,9):
        j.append( [j[i][0]+30,j[i][1]] )

    for i in range(0,10):
        k_ = np.array([[k[i][0], k[i][1]]], dtype=np.float32) #转变成NumPy数组加快计算
        L = cv2.perspectiveTransform(k_.reshape(-1, 1, 2), M) #透视变换
        point.append([L[0][0][0], L[0][0][1]])
    for i in range(0,10):
        j_ = np.array([[j[i][0], j[i][1]]], dtype=np.float32)
        L = cv2.perspectiveTransform(j_.reshape(-1, 1, 2), M)
        LandPoint.append([L[0][0][0], L[0][0][1]])

    # 对乒乓球的坐标K进行透视变换，得到L
    # K_ = np.array([[K[0], K[1]]], dtype=np.float32)  #NumPy数组
    # L = cv2.perspectiveTransform(K_.reshape(-1, 1, 2), M)
    # point = [0,0]
    # point[0] = L[0][0][0]
    # point[1] = L[0][0][1]



# 计算12个等分点的坐标--------------------------------
    division_points = []  #二维列表

    # 在宽度上的10个点
    for i in range(1, 6):
        x = -halfWidth + (2*halfWidth/6) * i
        division_points.append([x, halfHeight])
        division_points.append([x, -halfHeight])

    # 在高度上的2个点
    division_points.append([-halfWidth, 0])
    division_points.append([halfWidth, 0])

    # 对这12个点进行透视变换
    division_points_ = np.array(division_points, dtype=np.float32)
    transformed_points = cv2.perspectiveTransform(division_points_.reshape(-1, 1, 2), M).reshape(-1, 2).tolist()


    P = []
    # 格式化transformed_points的内容并存储在P中
    for i in range(0, 12):

        P.append(transformed_points[i])   #!在改P的结构
#--------------------------------------------------



    W_ = []

    # 通过循环将W的内容复制到W_中
    for x in range(W.shape[0]):
        row = []
        for y in range(W.shape[1]):
            row.append(W[x, y])
        W_.append(row)




# 原点变换------------------------------------
    origin_ = np.array([0,0], dtype=np.float32)
    origin__ = cv2.perspectiveTransform(origin_.reshape(-1, 1, 2), M)
    origin=[0,0]
    origin[0] = origin__[0][0][0]
    origin[1] = origin__[0][0][1]
#--------------------------------------------

    return point, LandPoint, W_ ,P , origin


