#这个python文件的功能是输出inquisit格式的item

import os

work_dir = "C:/Users/dell/Desktop/高劭婧_差别阈限/"

os.getcwd()

os.chdir(work_dir)
picturename = os.listdir(work_dir+"pictures\\")

print("<item pic>")
for i in range(0, len(picturename)):
    j = i+1
    print('    '+'/'+str(j)+' = ' + '"' +'pictures/'+ picturename[i] + '"')
print("</item>")
print("\n")
