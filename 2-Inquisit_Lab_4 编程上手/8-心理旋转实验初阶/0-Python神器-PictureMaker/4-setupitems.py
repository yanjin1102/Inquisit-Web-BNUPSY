# -* - coding: UTF-8 -* -

# 导入需要使用的模块

import os

# 获取当前工作的目录，并将目录设置为需要使用的目录

work_dir = "E:\\PictureMaker\\"

os.getcwd()

os.chdir(work_dir)

# 遍历两个需要扫描的文件夹，并将文件名导入到列表当中

NPicNames = os.listdir(work_dir+"NPic\\")

MPicNames = os.listdir(work_dir+"MPic\\")

# 打印出我们所需要的格式

print("<item NR>")
for i in range(0, len(NPicNames)):
    j = i+1
    print('    '+'/'+str(j)+' = ' + '"' + NPicNames[i] + '"')
print("</item>")
print("\n")

print("<item MR>")
for i in range(0, len(MPicNames)):
    j = i+1
    print('    '+'/'+str(j)+' = ' + '"' + MPicNames[i] + '"')
print("</item>")