#Permutations
#A permutation of numbers 1,2,...,n is called beautiful if there are no adjacent elements with a difference of 1. 
#Given n, print a possible beautiful permutation or NO SOLUTIONS if one does not exist. 
#put all even numbers in ascending order in front of odds in ascending order, does not work for 1,2,and 3

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

#testcode
beautification(6) 
