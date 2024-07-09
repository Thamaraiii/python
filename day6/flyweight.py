#class
class  character:
    def __init__(self,char):
        self.char=char

    def display(self,font,size,color):
        print (f"Displaying '{self.char}' with font {font}, size{size}, color: {color}")
#factorycls

class characterfactory:
    def __init__(self):
        self.characters={}

    def getcharacter(self,char):
        if char not in self.characters:
            self.characters[char]=character(char)
        return self.characters[char]
#usage
factory=characterfactory()

#req char from factory
char_a1=factory.getcharacter('a')
char_a2=factory.getcharacter('a')
char_T=factory.getcharacter('t')

#display char

char_a1.display("Arial",11,"black")
char_a2.display("times new roman",10,"teal")
char_T.display("Arial",12,"green")

print(char_a1 is char_a2)