import copy

class Tacos:         #prototype
    def __init__(self,name):
        self.name=name

    def clone(self):
        return copy.deepcopy(self)
    
class Tacobell:         #factory
    def __init__(self,prototype):
        self.prototype=prototype

    def makeclone(Self):
        return Self.prototype.clone()
    
#usage
originalTaco=Tacos("crispypotato")
store=Tacobell(originalTaco)

cloneTaco=store.makeclone()

print(f"original Taco : {originalTaco}")
print(f"clonetaco : {cloneTaco}")
