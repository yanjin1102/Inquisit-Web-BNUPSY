from PIL import Image
from matplotlib import pylab
from pylab import *
import os
im = Image.open('image00.jpg').convert('L')
img = array(im)
img = 0.5*img + 30

for i in range(1,17):
    img = img + 3
    image = Image.fromarray(uint8(img)).resize((400,300))
    image.save('image'+str(i-8)+'.jpg')

PicName = os.listdir()
print("<item grey>")
j = 0
for i in range(0, len(PicName)-1):
    if (i>8)or(i<7):
        j = j+1
        print('  ' + '/' + str(j) + ' = ' + '"' + PicName[i] + '"')
print("</item>")
print("\n")
