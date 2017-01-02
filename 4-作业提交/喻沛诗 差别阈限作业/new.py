from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


txt = "R"
font = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", size=400)

for i in range(1, 31, 3):
    blank_image = Image.new("RGB", size=(1000, 1000), color=(100, 100, 100))
    draw = ImageDraw.Draw(blank_image, mode="RGB")
    draw.text((300, 300), txt, fill=(201-i, 201-i, 201-i), font=font)
    blank_image.save("pic_new" + str(i) + ".bmp", "bmp")
