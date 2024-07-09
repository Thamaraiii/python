from abc import ABC,abstractmethod

class Icecreamfactory(ABC): #abstract
    @abstractmethod
    def makecone(self):
        pass
    @abstractmethod
    def makecup(self):
        pass
    @abstractmethod
    def makesundae(self):
        pass

class Fruiticecreamfactory(Icecreamfactory):  #concrete factories
    def makecone(self):
        return "strawberry cone"
    def makecup(self):
        return "banana cup"
    def makesundae(self):
        return "litchi sundae"

class Chocoicecreamfactory(Icecreamfactory):
    def makecone(self):
        return "millkchoco cone"
    def makecup(self):
        return "darkchoco cup"
    def makesundae(self):
        return "chocochip sundae"
    
def ordericecream(factory):         #clientcode
    print(factory.makecone())
    print(factory.makecup())
    print(factory.makesundae())

print("Fruit icecream Factory Order: ")
ordericecream(Fruiticecreamfactory())

print("Choco icream Factory Order: ")
ordericecream(Chocoicecreamfactory())
