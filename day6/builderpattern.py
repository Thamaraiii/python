class sandwich:          #product
    def __init__(self):
        self.bread=None
        self.filling=None
        self.topping=None
    
    def __str__(self):
        return f"sandwich with {self.bread} bread , {self.filling} filling and {self.topping} topping"
    
class sandwichbuilder:           #abstractbuilder
    def add_bread(self,bread):
        raise NotImplementedError
    def add_filling(self,filling):
        raise NotImplementedError
    def add_topping(self,topping):
        raise NotImplementedError
    def get_sandwich(self):
        raise NotImplementedError
    
class Mysandwichbuilder(sandwichbuilder):         #concretebuilder
    def __init__(self):
        self.sandwich = sandwich()
    def add_bread(self, bread):
        self.sandwich.bread=bread
    def add_filling(self, filling):
        self.sandwich.filling=filling
    def add_topping(self, topping):
        self.sandwich.topping=topping

    def get_sandwich(self):
        return self.sandwich
    
class sandwichdirector:           #director
    def __init__(self,builder):
        self.builder=builder
    
    def make_sandwich(self):
        self.builder.add_bread("whole wheat")
        self.builder.add_filling("veggie")
        self.builder.add_topping("tomato")

builder=Mysandwichbuilder()         #usage
director=sandwichdirector(builder)
director.make_sandwich()

sandwich=builder.get_sandwich()
print(sandwich)
        
        