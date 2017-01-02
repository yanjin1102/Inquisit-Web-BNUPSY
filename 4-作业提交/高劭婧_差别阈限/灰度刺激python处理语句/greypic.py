# 这个python文件的功能是生成不同灰度的图片刺激

from PIL import Image
from numpy import *

work_dir = "C:/Users/dell/Desktop/高劭婧_差别阈限/pictures/"

im = array(Image.open(work_dir+'doge.jpg').convert('L'))

print(im)

im3 = (50/255) * im + 150 # 将图像像素值变换到50...200 区间

for i in range(30,180,10):
    image=(i/255)*im+100
    pic_image=Image.fromarray(uint8(image))
    pic_image.save(work_dir + "grey" + str(i) + ".bmp")


