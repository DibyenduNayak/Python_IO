filename=input("enter the file name :")

lines=[]

print("enter the text here and \" exit\" amy time to write" )

while True:
    line=input()
    if line=='exit':
        break
    else:
        lines.append(line)
        print(lines)
# open
file=open(filename,"w")
file.writelines(lines)
file.close()
print("program running")
