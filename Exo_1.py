def call(fonction, *args, **kwargs) : 
    return fonction(*args, **kwargs)


def hello(): 
    print('hello')  
call(hello) 

def add(a,b) : 
    return a + b

print(call(add, 2, 9))   

def sub(a,b)  :
    return a - b 

def compute(a, b, op = add) :  #Ici on crée un paramètre optionnel op en lui donnant une valeur (par défaut) 
    if op == add : 
        return add(a,b)
    if op == sub : 
        return sub(a,b)

print(compute(12,3, op=sub))
print(call(compute,1222,33))