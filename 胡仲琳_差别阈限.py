from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
# 定义生成路径
work_dir = "D:/inquisit/11.25experiment/"
# 根据不同RGB生成不同灰度的图片（利用循环）
# 针对RGB15-90的图片
for i in range(15,105,15):
    blank_image = Image.new("RGB", size=(200, 400), color=(i, i, i))
    txt = "KiCo"
    font = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", size=50)
    draw = ImageDraw.Draw(blank_image, mode="RGB")
    draw.text((50, 200), txt, fill=(255, 255, 255), font=font)
# 保存图片
    blank_image.save(work_dir + "RGB0"+str(i)+".bmp", "bmp")

#针对RGB105-255
for i in range(105,255,15):
    blank_image = Image.new("RGB", size=(200, 400), color=(i, i, i))
    txt = "KiCo"
    font = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", size=50)
    draw = ImageDraw.Draw(blank_image, mode="RGB")
    draw.text((50, 200), txt, fill=(255, 255, 255), font=font)
# 保存图片
    blank_image.save(work_dir + "RGB"+str(i)+".bmp", "bmp")
