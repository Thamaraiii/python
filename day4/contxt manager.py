class contextmanager():
    def __init__(self):
        print("init method called")
    
    def __enter__(self):
        print("enter method called")
        return self
    
    def __exit__(self,exec_type,exec_value,exec_traceback):
        print("exit method called")

with contextmanager() as manager:
    print("with statement block")