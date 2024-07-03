class Bird:
    name=""

    def eat(self):
        print("I can eat")
class crow(Bird):
    def show(self):
        print("My name is:",self.name)
whitecrow=crow()
whitecrow.name="vellacrow"
whitecrow.eat()
whitecrow.show()
