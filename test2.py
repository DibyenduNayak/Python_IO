filename=input("enter the filename here :")

lines=[]

print("Enter any content and press \" exit\" to write")

while True:
    line=input()
    if line== 'exit':
        break
    else:
        lines.append(line)
        print(lines)
# open
file=open(filename,"w")

# write
file.writelines(lines)
file.close()