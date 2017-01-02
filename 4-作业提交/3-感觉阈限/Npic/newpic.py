# !/usr/bin/evn python
# _*_ encoding:utf-8_*_
# -*- coding: utf-8 -*-

'this is a test module'

__author__ = 'Hang Zhang'

from PIL import Image
from pylab import *

#设置当前工作路径
work_dir = "D:/schoolwork/Python/161130/"

#读取图片,灰度化，并转为数组
im = array(Image.open("a01.jpg").convert('L'))

#设置循环生成灰度图片
for i in range(0, 255, 16):
    image = (i/255)*im
    out = Image.fromarray(uint8(image))
    out.save(work_dir+"N"+str(i)+".bmp")

