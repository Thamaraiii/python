#try and except
try:
    print(x)
except:
    print('An error as occured')

#multiple exception statements

try:
    print(1/0)
except ZeroDivisionError:
    print('cannot divide a value with zero')
except:
    print("something else went wrong")

#try except else
try:
    result=1/10
except ZeroDivisionError:
    print("there is a error")
else:
    print(f'your answer is{result}')

#index error
x=[1,4,78,54]
def findNthvalue(x,n):
    try:
        result=x[n]
    except IndexError:
        print("the value is exceeded")
    else:
        print(f'the value is {result}')
findNthvalue(x,5)
findNthvalue(x,1)

#finally
def divide(x,y):
    try:
        result=x/y
    except ZeroDivisionError:
        print("change Y")
    except:
        print("something is wrong")
    else:
        print(f"your answer is {result}")
    finally:
        print("successfully completed")
divide(3,9)