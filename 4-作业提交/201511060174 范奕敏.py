from PIL import Image
from pylab import *
im=array(Image.open("picture.jpg").convert('L'))
image=(195/255)*im
out=Image.fromarray(uint8(image))
out.save("C:\\Users\Mya\Desktop\\University\实心\实验\inquisit\\3rd 11.25\pic\\"+"N"+str(4)+".bmp")