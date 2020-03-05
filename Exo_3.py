def binrep(n) : 
    while n > 0 : 
        bit = n% 2 
        n //=2 
        yield bit
        
b = binrep(12)
for i in b : 
    print(i)



while True : 
    try : 
        print(next(b))
    except StopIteration :
        break


class NaturalIterator : 
    def __init__(self, n ):
        self.__generator = binrep(n)
    def __next__(self):
        return next(self.__generator)
    def __iter__(self) : 
        return self
class Natural : 
    def __init__(self, n ): 
        self.__n = n
    def __iter__(self):
        return NaturalIterator(self.__n)
    
N= Natural(10)
for i in N : 
    for j in N : 
        print(i,j)