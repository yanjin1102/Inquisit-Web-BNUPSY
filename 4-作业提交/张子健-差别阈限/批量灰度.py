from PIL import Image
import os
from PIL import ImageDraw
workdir ="E:/python/PyCharm Community Edition 2016.3/file/"
os.chdir(workdir)
im = Image.open(workdir+'test.jpg').convert('L')
# im.save('graypic1.jpg')
draw = ImageDraw.Draw(im)
for x in range(1, 11):
    for i in range(0, list(im.size)[0]):
            for j in range(0, list(im.size)[1]):
                    color = im.getpixel((i, j))
                    color = color + x
                    point = [i, j]
                    draw.point(point, color)
    # im.show('pic1.jpg')
    im.save('p'+str(x-1)+'.jpg')
    PicNames = os.listdir(workdir + "p/")


    print("<item grey>")
    for i in range(0, len(PicNames)):
        j = i + 1
        print('    ' + '/' + str(j) + ' = ' + '"' + PicNames[i] + '"')
    print("</item>")
    print("\n")
# thanks to 程凯琳