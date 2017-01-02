from PIL import Image
from numpy import array
work_dir = "D:/game/"
image_file = Image.open(work_dir+"wall.jpg") # open colour image
image_file = image_file.convert('1') # convert image to black and white
image_file.save(work_dir+"wallg.jpg")
im = array(Image.open(work_dir+"wallg.jpg"))
im2= Image.fromarray(im*0.5)
im2 = im2.convert("RGB")
im2.save(work_dir+"gray1.jpg")
im2= Image.fromarray(im*0.75)
im2 = im2.convert("RGB")
im2.save(work_dir+"gray2.jpg")
im2= Image.fromarray(im*0.875)
im2 = im2.convert("RGB")
im2.save(work_dir+"gray3.jpg")
im2= Image.fromarray(im*0.9375)
im2 = im2.convert("RGB")
im2.save(work_dir+"gray4.jpg")
im2= Image.fromarray(im*0.96875)
im2 = im2.convert("RGB")
im2.save(work_dir+"gray5.jpg")
im2= Image.fromarray(im*0.984375)
im2 = im2.convert("RGB")
im2.save(work_dir+"gray6.jpg")