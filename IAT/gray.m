clc;clear
Path1='D:\2016\bin\IAT\picture\b1.jpg'%存放彩色照片的路径%
Path2='D:\2016\bin\IAT\picture\b2.jpg'
Path3='D:\2016\bin\IAT\picture\b3.jpg'
Path4='D:\2016\bin\IAT\picture\b4.jpg'
Path5='D:\2016\bin\IAT\picture\w1.jpg'
Path6='D:\2016\bin\IAT\picture\w2.jpg'
Path7='D:\2016\bin\IAT\picture\w3.jpg'
Path8='D:\2016\bin\IAT\picture\w4.jpg'
origin1=imread(Path1)%读取这些彩色照片%
origin2=imread(Path2)
origin3=imread(Path3)
origin4=imread(Path4)
origin5=imread(Path5)
origin6=imread(Path6)
origin7=imread(Path7)
origin8=imread(Path8)
grey1 = rgb2gray(origin1)%转成灰度图片%
grey2 = rgb2gray(origin2)
grey3 = rgb2gray(origin3)
grey4 = rgb2gray(origin4)
grey5 = rgb2gray(origin5)
grey6 = rgb2gray(origin6)
grey7 = rgb2gray(origin7)
grey8 = rgb2gray(origin8)

imwrite(grey1,'D:\2016\bin\IAT\greypicture\gb1.jpg')%把灰度图片转入新文件夹%
imwrite(grey2,'D:\2016\bin\IAT\greypicture\gb2.jpg')
imwrite(grey3,'D:\2016\bin\IAT\greypicture\gb3.jpg')
imwrite(grey4,'D:\2016\bin\IAT\greypicture\gb4.jpg')
imwrite(grey5,'D:\2016\bin\IAT\greypicture\gw1.jpg')
imwrite(grey6,'D:\2016\bin\IAT\greypicture\gw2.jpg')
imwrite(grey7,'D:\2016\bin\IAT\greypicture\gw3.jpg')
imwrite(grey8,'D:\2016\bin\IAT\greypicture\gw4.jpg')


