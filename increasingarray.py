#Increasing Array
#Given an array of n integers. Modify array so that it is increasing, meaning each number is >= the one before. 
#A move is increasing a number by 1. Print minimum number of moves. 

def increasearray(array): 
    moves = 0               #move is increasing number by 1
    n = len(array)          #array of n integers
    
    for i in range(n-1): 
        if array[i] > array[i+1]: 
            x = array[i] - array [i+1]
            moves = moves + x
        else: 
            x = 0
    print(moves)

#testingcode
array = [3, 2, 5, 1, 7]
increasearray(array)
