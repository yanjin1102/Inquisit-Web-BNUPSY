from PIL import Image
from pylab import *
work_dir="D:/孙洪力_差别阈限/"
image=Image.open(work_dir+"0.jpg").convert('L')
a=array(image)
for i in range(1,16):
    a1=a*(1-0.01*i)
    im1=Image.fromarray(a1).convert('L')
    im1.save(work_dir+str(i)+".jpg")