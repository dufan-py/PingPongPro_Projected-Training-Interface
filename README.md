# PingPongPro_Projected-Training-Interface
基于Django的乒乓球训练系统的投影交互界面

简介：本工程为乒乓球训练系统的投影界面部分：绘制乒乓球台框架和乒乓球的位置，投影于乒乓球台面上，实现可视化与人机交互。

具体实现：在Linux操作系统下，根据硬件采集的球台大小和乒乓球实时位置，将乒乓球坐标经过OpenCV的透射变换，确保其不受投影而导致的画面倾斜的影响，通过Django构架将后端计算所得的5个坐标传至前端文件，在前端文件中根据坐标绘制乒乓球台框架和乒乓球的位置，并全屏显示。
![e191650243cde80a9ae6a70a6ecfd5b](https://github.com/dufan-py/PingPongPro_Projected-Training-Interface/assets/53752434/5307b23a-9890-4c20-a67b-11e45dbdbc06)

UPDATE:


23/9/24：实现显示任意四边形球台（投影变换）   

    Ⅰ 后端-py：使用cv2投射变换函数，初步测试通过，待实测

    Ⅱ 前端-html：通过django的view和urls连接前后端(即html和py)，在html文件使用py传的参数绘制任意四边形和乒乓球






23/10/10：在Ubuntu系统中实现该项目

    Ⅰ 在Ubuntu中使用anaconda新建python虚拟环境，用vscode打开工程文件，并在vscode中配置django环境


23/10/17：添加球台十二等分线

  
23/10/24: 

    Ⅰ 提高页面和乒乓球刷新率，测试CPU占用

    Ⅱ 实现球台中心位置在页面上的可任意设定

23/11/08: 

    Ⅰ 实现在球台上保留球的轨迹和落点

    Ⅱ 测试在Ubuntu中页面高刷新率的CPU占用
    
截至11.08页面如图：
<img width="1358" alt="f8d6fbd52aded33f5607e7fc66a0fc8" src="https://github.com/dufan-py/PingPongPro_Projected-Training-Interface/assets/53752434/8eed7a16-4697-4bcd-9e64-dda5d6f3795c">


23/11/14：

    Ⅰ 引入新线程points_test.py用以测试，在主线程中调用以模拟后端乒乓球轨迹坐标的传输




