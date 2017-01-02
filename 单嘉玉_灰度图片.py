from PIL import Image
from numpy import *
work_dir = "C:/Users/DELL/Desktop/程序/Python/尝试程序/shiyan/"

image = array (Image.open(work_dir + "pic.jpg").convert('L'))

for i in range (0 , 5 , 1):
    image2 = image + i
    out_image2 = Image.fromarray(image2)
    out_image3 = out_image2.resize((700,500))
    out_image3.save(work_dir+"pic"+(str(i))+".jpg")

