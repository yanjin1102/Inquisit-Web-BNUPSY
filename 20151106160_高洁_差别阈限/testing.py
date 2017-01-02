from PIL import Image
from pylab import *
import os
os.makedirs('TPic')
os.makedirs('OPic')
for i in range(0, 16):
 im = Image.open('pic'+ str(i)+'.jpg')
 img = Image.fromarray(uint8(im))
 img.save('Opic/' + 'Opic' + str(i+1) + '.jpg')
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
 #im.show(im)
 img = Image.fromarray(uint8(im))
 img.save('Tpic/'+ 'Tpic'+ str(i+1) + '.jpg')


OPicNames = os.listdir("OPic/")

TPicNames = os.listdir("TPic/")

# 打印出我们所需要的格式

print("<item OPics>")
for i in range(0, 16):
    print('    '+'/'+str(i)+' = ' + '"' + "OPic/" + OPicNames[i] + '"')
print("</item>")
print("\n")

print("<item TPics>")
for i in range(0, 16):
    print('    '+'/'+str(i)+' = ' + '"' + "TPic/" + TPicNames[i] + '"')
print("</item>")