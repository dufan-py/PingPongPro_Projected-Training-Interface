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

    point, corner = axis_change_coordinates()  # 调用 get_random_coordinates 函数获取随机 x 和 y 坐标

    # 将数据转换为JSON格式并返回

    response_data = {'x': point[0], 'y': point[1],
                     'cor1x': corner[2][0], 'cor1y': corner[2][1], 'cor2x': corner[3][0], 'cor2y': corner[3][1],
                     'cor3x': corner[0][0], 'cor3y': corner[0][1], 'cor4x': corner[1][0], 'cor4y': corner[1][1]}
    for key in response_data:
        if isinstance(response_data[key], np.float32):
            response_data[key] = float(response_data[key])

    return HttpResponse(json.dumps(response_data), content_type="application/json")

