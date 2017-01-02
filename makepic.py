 from PIL import Image

 from PIL import ImageDraw

 # 设置一个我们当前的工作路径，便于后面引用

 work_dir = "C:/Users/haus-pc/Desktop/python"

 im = Image.open(work_dir+'pic00.jpg').convert('L')

for i in range(0, 255, 16):
    image = (i / 255) * im
    out = Image.fromarray(uint8(image))
    out.save(work_dir + "pic" + str(i) + ".bmp")