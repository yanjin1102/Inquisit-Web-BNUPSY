# -* - coding: UTF-8 -* -

'''
这个部分我们要开始生成我们的刺激材料啦，让照片转起来，每15度转一下，然后我们裁剪出我们想要的内容，进行保存

很简单吧！

直接看代码！

'''


# 导入所需模块库

from PIL import Image

# 设置一个我们当前的工作路径

work_dir = "E:/PictureMaker/"

# 导入我们刚才裁剪过的照片！

blank_image = Image.open(work_dir+"picmodual.bmp")

# 让照片放大一下，回复刚才的尺寸

blank_image = blank_image.resize((1000, 1000))

# 生成一张跟原始照片镜像的照片

mirror_blank_image = blank_image.transpose(Image.FLIP_LEFT_RIGHT)

# 好啦，现在我们设置一个for循环，每15度操作一下，转一下，切一下，存一下，以特定的文件名进行保存！

for i in range(0, 360, 15):
    image = blank_image.rotate(i, expand=0)
    out = image.crop(box=(200, 200, 800, 800))
    out.save(work_dir + "NPic/" + "N" + str(i) + ".bmp")
    mirror_image = mirror_blank_image.rotate(i, expand=0)
    mirror_out = mirror_image.crop(box=(200, 200, 800, 800))
    mirror_out.save(work_dir + "MPic/" + "M" + str(i) + ".bmp")

# 好啦，打完收工！

'''
有了这等神器，以后图片刺激材料的制作和生成，吃喝不愁啊！

还有进阶的版本，我们还可以用python处理动图，处理声音和视频

可以把彩色照片转成黑白的，可以调节照片的锐化，高斯模糊，图片融合等

小白们，还买什么PhotoShop，直接上代码！

'''






