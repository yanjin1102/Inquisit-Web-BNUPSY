print("<item test>")
for i in range(1,11):
    print("\t/"+str(i)+"=\""+str(i)+".jpg\"")
print("</item>\n")
for i in range(1,5):
    print("<picture origin"+str(i)+">")
    print("\t/items=(\"0.jpg\")")
    print("\t/position=(5%,5%)")
    print("</picture>\n")