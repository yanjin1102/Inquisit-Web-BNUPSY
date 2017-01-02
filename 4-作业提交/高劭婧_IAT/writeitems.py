#这个python文件的功能是输出inquisit格式的item

import os

work_dir = "C:/Users/dell/Desktop/高劭婧_IAT/pictures/"

os.getcwd()

os.chdir(work_dir)
picturename = os.listdir(work_dir+"white\\")

print("<item black>")
for i in range(0, len(picturename)):
    j = i+1
    print('    '+'/'+str(j)+' = ' + '"' +'pictures/'+'white/'+ picturename[i] + '"')
print("</item>")
print("\n")
