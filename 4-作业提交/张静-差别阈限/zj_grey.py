from PIL import Image
from pylab import *
work_dir = "E:/eprime/1125class/pycharm/pic/"
#转换成矩阵
im = array(Image.open("E:/eprime/1125class/pycharm/pic/old.jpg").convert('L'))
#生成灰度图
im1 = Image.fromarray(uint8(im))
im1.save(work_dir+"grey.jpg")
#生成不同灰度差异的图
for i in range(0, 255, 32):
    image = (i/255)*im
    out = Image.fromarray(uint8(image))
    ii = 8-i/32
    out.save(work_dir+str(ii)+".jpg")