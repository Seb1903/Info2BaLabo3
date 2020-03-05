import time
def delay(t=1) : 
    def decorator(f) :
        def wrapper(*args, **kwargs) : 
            time.sleep(t)
            return f(*args, **kwargs)
        return wrapper
    return decorator

@delay(4)
def printnum(i) : 
    print(i)
i = 2
while i >= 0 :
    printnum(i)
    i -= 1 
print('Kabooooom ')
