# -* - coding: UTF-8 -* -

# 这个python文件的目的是生成一张图片，要求黑底白字，呈现一个R，作为我们制作刺激材料的原始材料！
# Python很好用哦，加油学习吧！

# 导入所需模块库

from PIL import Image

from PIL import ImageDraw

from PIL import ImageFont

# 设置一个我们当前的工作路径，便于后面引用

work_dir = "E:/PictureMaker/"  # 可以替换成你任意想存在文件的位置，比如就放在GitHub文件夹里，用起来特别方便

'''

看好啦，我们现在要用编程的方法画画啦！

首先我们生成一个黑色的画布，大小为1000*1000像素。

然后生成一个文字“R”

之后定义文字需要用的字体和大小

再之后把这个文字防止到我们定义好的位置，计算机是根据左上角定位滴

好，现在已经画上去了，我们该保存图像了！

具体的代码请看！

'''

# 新建一个黑色背景的图片，图片大小设定为1000*1000像素，颜色设置为黑色

blank_image = Image.new("RGB", size=(1000, 1000), color=(0, 0, 0))


# 定义我们要添加的文字内容

txt = "R"

# 定义文字呈现的字体和大小

font = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", size=400)

# 定义一个方法，就是画的对象，我们要把这个字写到什么图片上

draw = ImageDraw.Draw(blank_image, mode="RGB")

# 看，我们开始画了啊！告诉计算机我们在什么位置画，画什么，用什么颜色，用什么字体！

draw.text((300, 300), txt, fill=(255, 255, 255), font=font)

# 好啦，现在把图片从内存保存到硬盘吧，注意我们要存放在什么文件夹中！

blank_image.save(work_dir + "blank_image.bmp", "bmp")

# 告诉计算机，我想看看我刚才画的那副画

blank_image.show()

'''

嗯，很不错；

我看到我画了一张画；

上面写了一个R；

但很不幸是跑偏哒；

为什么呢？

因为在字体库中，R的面积本身就不是左右对称的，右边会偏大！

怎么办呢？

哦，我可以裁剪一下；

请看下面的代码！

'''



