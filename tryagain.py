from PIL import Image

from pylab import *
import os

# 获取当前工作的目录，并将目录设置为需要使用的目录

work_dir = "D:/python/homework1/"
os.makedirs('changingpic')
for i in range(1,17,1):
    im = Image.open('image1.jpg')
    pix = im.load()
    width = im.size[0]
    height = im.size[1]
    for x in range(width):
        for y in range(height):
            r, g, b = pix[x, y]
            r = r + 10*i
            g = g + 10*i
            b = b + 10*i
            pix[x, y] = r, g, b
    im2 = Image.fromarray(uint8(im))
    im2.save('changingpic/' + 'changepic' + str(i) + ".bmp")
