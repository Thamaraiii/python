class square:
    side=""

    def calculatearea(self):
        print("Area of square:",self.side*self.side)
floor=square() 
floor.side=90
floor.calculatearea()
