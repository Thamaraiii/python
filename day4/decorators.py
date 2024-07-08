def pretty(func):
    def inner():
        print("beautiful")
        func()
    return inner
def ordinary():
    print("ordinary")
func=pretty(ordinary)
func()

#@symbol
def pretty(func):
    def inner():
      print("beauty")
      func()
    return inner
@pretty
def ordinary():
    print("ordinary")
ordinary()
#dec func with parameters

def division(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("cannot divide")
            return

        return func(a, b)
    return inner

@division
def divide(a, b):
    print(a/b)

divide(2,5)

divide(2,0)