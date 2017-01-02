#调用所需要的模块库
from PIL import Image

from numpy import *
#设置当前工作路径
work_dir = "E:/picturemaker/"

#读取图片，灰度化，并转为数组
im = array ( Image.open(work_dir+"blank.bmp").convert('L'))
for i in range (0, 5, 1):
    j = i * 1
    im2= im + j
    out_im2 = Image.fromarray(im2)
    out_im3 = out_im2.resize((700, 500))
    out_im3.save (work_dir+"pic/"+str(j)+".bmp")

#im2= im + 0.2
#out_im2= Image.fromarray(im2)
#out_im2.save(work_dir+"0.2.bmp")
#out_im2.show()


