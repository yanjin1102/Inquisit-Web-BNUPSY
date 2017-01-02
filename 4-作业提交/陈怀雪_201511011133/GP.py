from PIL import Image
from pylab import *
work_dir = "C:/Users/chenh/Desktop/GRAYP"

im = array(Image.open('C:/Users/chenh/Desktop/Foolcan/1.jpg').convert('L'))

for i in range(0, 255, 16):
    image = (i/255)*im
    out = Image.fromarray(uint8(image))
    out.save(work_dir+"N"+str(i)+".bmp")
