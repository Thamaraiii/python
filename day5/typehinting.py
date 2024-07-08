def add2nos(num1:int,num2:int)->int:
    sum=num1+num2
    print("sum:",sum)
add2nos(10,30)

#eg2
class car:
    def __init__(self,brand:str,model:str):
        self.brand=brand
        self.model=model
    def move(self)->None:
        print("Drive!!")
class boat:
    def __init__(self,brand:str,model:str):
        self.brand=brand
        self.model=model
    def move(self)->None:
        print("Sail")
class plane:
    def __init__(self,brand:str,model:str):
        self.brand=brand
        self.model=model
    def move(self)->None:
        print("Fly")
car1=car("ford","bmw")
boat1=boat("abc","tvs")
plane1=plane("air","airliness")

for x in (car1,boat1,plane1):
    x.move()
    print(x.brand)
    print(x.model)