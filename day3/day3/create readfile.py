f=open("file.txt","w")
T=["hello this is Thamarai\n","how are you\n"]
f.writelines(T)
f.close()
f=open("file.txt","r+")
print(f.read())
print(f.readline())