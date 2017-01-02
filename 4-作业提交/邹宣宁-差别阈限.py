from PIL import Image
im = Image.open('1.jpg').convert('L')
# im.save('graypic1.jpg')
from PIL import ImageDraw
draw = ImageDraw.Draw(im)
for x in range(1, 16):
    for i in range(0, list(im.size)[0]):
            for j in range(0, list(im.size)[1]):
                    color = im.getpixel((i, j))
                    # 改变灰度值
                    color = color + x
                    point = [i, j]
                    draw.point(point, color)
    # im.show('pic1.jpg')
    im.save('pic'+str(x)+'.jpg')