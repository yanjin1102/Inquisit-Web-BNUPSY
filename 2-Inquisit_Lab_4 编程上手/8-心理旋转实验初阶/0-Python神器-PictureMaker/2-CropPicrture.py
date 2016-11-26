# -* - coding: UTF-8 -* -

'''

这段代码就是来处理R跑偏的问题的，我们要根据R的中心在哪儿来定义裁剪的范围，裁剪一下照片！

'''


# 导入所需模块库


from PIL import Image

# 设置一个我们当前的工作路径

work_dir = "E:/PictureMaker/"

# 添加图片对象

blank_image = Image.open(work_dir+"blank_image.bmp")

# 拿起剪刀，告诉计算机，剪切那个部位！

out = blank_image.crop(box=(55, 113, 855, 913))

# 搞定，保存图片到内存！

out.save(work_dir+"picmodual.bmp")






