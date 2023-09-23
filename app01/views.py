from django.shortcuts import render, HttpResponse
from selenium import webdriver
import json
import sys
sys.path.append("..")  # 添加项目根目录到系统路径
from random_coordinates import get_random_coordinates  # 导入 get_random_coordinates 函数

def index(request):
    return render(request, "user_list.html")

def get_coordinates(request):
    x, y = get_random_coordinates()  # 调用 get_random_coordinates 函数获取随机 x 和 y 坐标

    # 将数据转换为JSON格式并返回

    response_data = {'x': x, 'y': y}
    return HttpResponse(json.dumps(response_data), content_type="application/json")

# 【**重要**】，连接py和html的地方。