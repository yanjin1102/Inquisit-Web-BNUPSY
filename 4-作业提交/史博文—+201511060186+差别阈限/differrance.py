from PIL import Image
im = Image.open('c.jpg').convert('L')
from PIL import ImageDraw
draw = ImageDraw.Draw(im)
for x in range(1, 16):
    for i in range(0, list(im.size)[0]):
            for j in range(0, list(im.size)[1]):
                    color = im.getpixel((i, j))
                    color = color + x
                    point = [i, j]
                    draw.point(point, color)
    im.save('pic'+str(x)+'.jpg')