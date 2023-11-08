from django.shortcuts import render, HttpResponse
from selenium import webdriver
import json
import sys

import numpy as np
from Axis_Change import get_coordinates as axis_change_coordinates


sys.path.append("..")  # 添加项目根目录到系统路径
from random_coordinates import get_random_coordinates  # 导入 get_random_coordinates 函数

def index(request):
    return render(request, "user_list.html")

def get_coordinates(request):

    point, LandPiont, corner, P, origin = axis_change_coordinates()  # 调用 Axis_Change  获取变换后的 x 和 y 坐标

    # 将数据转换为JSON格式并返回
    # 当前端通过 AJAX 请求后端以获取数据时，常用的数据交换格式是 JSON。
    # JSON存储方式类似字典，但其是跨语言的数据格式
    response_data = { 'x0':origin[0], 'y0':origin[1],
                     'cor1x': corner[2][0], 'cor1y': corner[2][1], 'cor2x': corner[3][0], 'cor2y': corner[3][1],
                     'cor3x': corner[0][0], 'cor3y': corner[0][1], 'cor4x': corner[1][0], 'cor4y': corner[1][1]}
    for i in range(len(P)): #12个等分点
        response_data[f'P{i}x'] = P[i][0]
        response_data[f'P{i}y'] = P[i][1]

    for i in range(len(point)): #乒乓球轨迹坐标
        response_data[f'point{i}x'] = point[i][0]
        response_data[f'point{i}y'] = point[i][1]
    for i in range(len(LandPiont)):
        response_data[f'LandPoint{i}x'] = LandPiont[i][0]
        response_data[f'LandPoint{i}y'] = LandPiont[i][1]

    # 将数据中的 np.float32 类型转换为 float 类型，进而转为 JSON 格式
    for key in response_data:
        if isinstance(response_data[key], np.float32):
            response_data[key] = float(response_data[key])

    return HttpResponse(json.dumps(response_data), content_type="application/json")

