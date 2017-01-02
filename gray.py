# 导入所需模块库
import os

from PIL import Image

from PIL import ImageDraw


# 设置一个我们当前的工作路径，便于后面引用

work_dir = "E:/working/"

im = Image.open(work_dir+'0.jpg').convert('L')

draw = ImageDraw.Draw(im)
for x in range(1, 11):
    for i in range(0, list(im.size)[0]):
            for j in range(0, list(im.size)[1]):
                color = im.getpixel((i, j))
                color = color + x
                point = [i, j]
                draw.point(point, color)
    im.save(work_dir + "Picturemake\\"+'pic'+str(x-1)+'.jpg')
    PicNames = os.listdir(work_dir + "Picturemake\\")

# 打印出我们所需要的格式
    print("<item grey>")
    for i in range(0, len(PicNames)):
        j = i + 1
        print('    ' + '/' + str(j) + ' = ' + '"' + PicNames[i] + '"')
    print("</item>")
    print("\n")