lam=lambda:print("hello")
lam()

lamname=lambda name:print("hello",name)
lamname("Thamarai")

def func(n):
    return lambda a:a*n
double=func(2)
print(double(11))

max=lambda a,b :a if(a>b)else b
print(max(19,200))

ages=[1,29,30,49,43,28,17,13,17]
adults=list(filter(lambda age: age>18,ages))
print(adults)



