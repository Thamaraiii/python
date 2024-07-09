class eurodevice:
    def plug(self):
        return"euro plug"
class usadapter:
    def __init__(self,device):
        self.device=device

    def plug(self):
        return f"us socket with {self.device.plug()} adapteed"
    
euro_device=eurodevice()
adapter=usadapter(euro_device)
print(adapter.plug())