#realimage

class realimage:
    def __init__(self,filename):
        self.filename=filename
        self.loadimagefromdisk()

    def loadimagefromdisk(self):
        print(f"Loading {self.filename} from the disk")

    def display(self):
        print (f"Displaying{self.filename}")

#proxyimage
class proxyimage:
    def __init__(self,filename):
        self.filename=filename
        self.realimage=None

    def display(self):
        if self.realimage is None:
            self.realimage=realimage(self.filename)
            self.realimage.display()

#client
def main():
    image=proxyimage("cat.png")
    image.display()
    image.display()

if __name__=="__main__":
    main()