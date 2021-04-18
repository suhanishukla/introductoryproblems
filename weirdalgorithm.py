#WeirdAlgorithm

def weirdalgorithm(n): 
    while n != 1: 
        print(n)
        if n % 2 == 0:              #if n is even divide by 2
            n = n // 2 
        else: 
            n = n * 3 + 1           #if n is odd then 3n+1
    print(n)
  
weirdalgorithm(3)
    

