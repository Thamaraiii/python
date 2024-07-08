class vehicle():
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def info(self):
        pass
    
class car(vehicle):
    def info(self):
        return f"the car's brand is {self.brand},and in {self.color}colour"

class truck(vehicle):
    def info(self):
        return f"the truck's brand is {self.brand},and in {self.color}colour"
 
class bike(vehicle):
    def info(self):
        return f"the bike's brand is {self.brand},and in {self.color}colour"

class vehiclefactory:
    @staticmethod
    def createvehicle(vehicletype,brand,color):
        if vehicletype=="car":
            return car(brand,color)
        elif vehicletype=="truck":
            return truck(brand,color)
        elif vehicletype=="bike":
            return bike(brand,color)
        else:
            raise ValueError(f"{vehicletype}vehicle not found")
        
if __name__=="__main__":
    factory=vehiclefactory()

    car=factory.createvehicle("car","maruthisuzuki","grey")
    truck=factory.createvehicle("truck","ford","yellow")
    bike=factory.createvehicle("bike","honda","black")

    print(car.info())
    print(truck.info())
    print(bike.info())