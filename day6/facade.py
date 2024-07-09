#subsystem cls
class CPU:
    def freeze(self):
        print("CPU Freezing")
    def jump(self,position):
        print("cpu jumping to position {position}")
    def execute(self):
        print("cpu executing")

class memory:
     def load(self,position,data):
         print(f"loading data {data} into {position}")

class harddrive:
    def read(self,lba,size):
        return f"data from {lba} with size {size}"
    
#facade cls

class computer:
    def __init__(self):
        self.cpu=CPU()
        self.memory=memory()
        self.harddrive=harddrive()

    def start(self):
        self.cpu.freeze()
        self.memory.load(0,self.harddrive.read(0,1024))
        self.cpu.jump(0)
        self.cpu.execute()

Computer=computer()
Computer.start()