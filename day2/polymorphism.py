class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Drive!!")
class boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Sail")
class plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Fly")
car1=car("ford","bmw")
boat1=boat("abc","tvs")
plane1=plane("air","airliness")

for x in (car1,boat1,plane1):
    x.move()
    print(x.brand)
    print(x.model)