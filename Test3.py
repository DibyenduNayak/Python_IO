from os import write

from test import filename

filename=input("enter the file name ")

lines=[]
print("eneter the text here and \"exit\" anytime to write :")

while True:
    line=input()
    if line== 'exit':
        break
    else:
        lines.append(line)
        print(lines)

# open
file=open(filename,"w")
#wwrite
file.writelines(lines)
file.close()






