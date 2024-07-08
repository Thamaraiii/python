#component base coffee interface
class coffee:
    def cost(self):
        pass
    def description(self):
        pass
#basic coffee class
class simplecofee(coffee):
    def cost(self):
        return 6
    def description(self):
        return "simple description"
#abstract decorator class
class coffeedecor(coffee):
    def __init__(self,decor_coffee):
        self.decor_coffee=decor_coffee
    def cost(Self):
        return Self.decor_coffee.cost()
    def description(self):
        return self.decor_coffee.description()
    
#concrete decorator
#milk deccorator
class milk(coffeedecor):
    def __init__(self, decor_coffee):
        super().__init__(decor_coffee)
    def cost(Self):
        return Self.decor_coffee.cost()+ 4
    def description(self):
        return self.decor_coffee.description()+",with milk"
#hazel decorator
class hazel(coffeedecor):
    def __init__(self, decor_coffee):
        super().__init__(decor_coffee)
    def cost(Self):
        return Self.decor_coffee.cost() + 10
    def description(self):
        return self.decor_coffee.description()+",with hazel"

#clientcode creating and using decoratedd coffees

if __name__ =="__main__":
    simple_coffee=simplecofee()
    print(f"cost: {simple_coffee.cost}")
    print(f"description: {simple_coffee.description}")

    milk_coffee=milk(simple_coffee)
    print(f"cost: {milk_coffee.cost}")
    print(f"description: {milk_coffee.description}")

    hazel_coffee=hazel(simple_coffee) 
    print(f"cost: {hazel.cost}")
    print(f"description: {hazel.description}")  