
evens = []
odds = []

def beautification(n): 
    if n <= 3:
        print("NO SOLUTION")
    else: 
        for i in range(1, n+1): 

            if i % 2 == 0: 
                evens.append(i)
            else: 
                odds.append(i)
        
        beautifulperm = evens + odds
        print(beautifulperm)

beautification(6)
    

    
        