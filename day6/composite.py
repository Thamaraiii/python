#base component
class Filesystemitem:
    def showdetails(self):
        raise NotImplementedError("subclass should implement this method")
    
    def getsize(self):
        raise NotImplementedError("subclass should implement this method")
    
#leafcls FILE

class file(Filesystemitem):
    def __init__(self,name,size):
        self.name=name
        self.size=size

    def showdetails(self):
        return f'file: {self.name}'
    def getsize(self):
        return self.size
    
#compositecls directory

class directory(Filesystemitem):
    def __init__(self,name):
        self.name=name
        self.items=[]

    def additem(self,item):
        self.items.append(item)

    def showdetails(self):
        details=[item.showdetails() for item in self.items]
        return f"Directory: {self.name}"
    def getsize(self):
         totalsize=sum(items.getsize() for items in self.items)
         return totalsize
    
#usaage
#createfile
file1=file("1.txt",100)
file2=file("2.txt",200)

#create directory

dir1=directory("dir1")
dir1.additem(file1)
dir1.additem(file2)

print(dir1.showdetails())
print(f"Totalsize: {dir1.getsize()} bytes")