#调用所需要的模块库
from PIL import Image
from numpy import *
#设置当前工作路径
work_dir = "E:/picturemaker/"

#读取图片，灰度化，并转为数组
im = array ( Image.open(work_dir+"blank.bmp").convert('L'))
for i in range (0, 50, 10):
    im2= im2= (215/255) * im + i
    j=40-i
    out_im2 = Image.fromarray(uint8(im2))
    out_im3 = out_im2.resize((700, 500))
    out_im3.save (work_dir+"pic/"+str(j)+".bmp")
    out_im3.show()


