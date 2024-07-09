class toy:
    def operate(self):
        raise NotImplementedError("subclass should implement this method")
    
class remotecontrol:
    def __init__(self,toy):
        self.toy=toy
    def pressbutton(self):
        return self.toy.operate()
class car(toy):
    def operate(self):
        return "toy car is driving"

class robot(toy):
    def operate(self):
        return "Toy robot is operating"

toycar=car()
toyrobot=robot()

remoteforcar=remotecontrol(toycar)
print(remoteforcar.pressbutton())

remoteforrobot=remotecontrol(toyrobot)
print(remoteforrobot.pressbutton())