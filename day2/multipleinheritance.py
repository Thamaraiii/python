class mammal:
    def mammalchar(self):
        print("mammals give direct birth")
class wingedanimal:
    def wingedanichar(self):
        print("winged animals can fly")
class bat(mammal,wingedanimal):
    pass
batty=bat()
batty.mammalchar()
batty.wingedanichar()