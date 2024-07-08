#fibonacci
def fibo(limit):
    a,b=0,1
    while a<limit:
        yield a
        a,b=b,a+b
x=fibo(6)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))


def abc():
    for i in range(15):
        if(i%2==0):
            yield i
for i in abc():
    print(i)