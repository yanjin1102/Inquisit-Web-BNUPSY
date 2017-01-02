from PIL import Image
from pylab import *
pil_im = Image.open('life.bmp').convert('L')
im = array(pil_im)

for i in range(0, 255, 15):
    image = (i/255)*im
    out = Image.fromarray(uint8(image))
    out.save(str(int(i/15)) + ".bmp")