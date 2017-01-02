from PIL import Image
from matplotlib import pylab
from pylab import *
for i in range(1,9):
    pic=str(i)+'.jpg'
    img = array(Image.open(pic))
    im = Image.fromarray(uint8(img)).resize((200,282))
    im.save(str(i)+'.jpg')
    if i<5:
        print(' /'+str(i)+'='+'"'+pic+'"')
    else:
        print(' /'+str(i-4)+'='+'"'+pic+'"')
