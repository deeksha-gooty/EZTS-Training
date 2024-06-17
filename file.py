import os
with open("file.txt","w") as f:
    f.write("Hello World")

with open("file.txt","a") as f:
    f.write("\nContent is written to the file.")

with open("file.txt","r") as f:
    data=f.read()
    print(data)

with open("file.txt","w") as f:
    f.write("My name is Deeksha.\nI am currently in bellary.\nI am in super coding batch.")
f.close()

with open("file.txt","r") as f:
    data=f.read()
    print(data)

with open("file.txt","w") as f:
    data=data.replace("bellary","BITM")
    f.write(data)
f.close()

with open("file.txt","rb") as f:
    print(f.tell())
    f.seek(-35,2)
    print(f.read().decode('utf-8'))
    print(f.tell())
    f.close()


with open("file.txt","r+b") as f:
    print(f.tell())
    f.seek(-35,2)
    f.write(b"#")  #f.write(s.encode())
    #print(f.read().decode('utf-8'))
    print(f.tell())
f.close()

with open("file.txt","r") as f:
    d=f.readlines()
    c=1
    data=[]
    for i in d:
        k=i[4:].split(" ")
        print(k)
        data.append(k)
    print(data)
f.close()