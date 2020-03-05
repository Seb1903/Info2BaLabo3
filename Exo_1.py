def call(fonction) : 
    return fonction()


def hello(): 
    print('hello')  
call(hello) 

def add(a,b) : 
    return a + b

print(call(add, 2, 9))   