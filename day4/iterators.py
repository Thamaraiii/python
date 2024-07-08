str="hello"
iterate=iter(str)
print(next(iterate))
print(next(iterate))

#example
class oddnos:
    def __init__(self,end_range):
        self.start=-1
        self.end=end_range
    def __iter__(self):
        return self
    def __next__(self):
        if self.start< self.end -1:
            self.start+=2
            return self.start
        else:
            raise StopIteration
count=oddnos(15)
while True:
    try:
        no=next(count)
        print(no)
    except StopIteration:
        break