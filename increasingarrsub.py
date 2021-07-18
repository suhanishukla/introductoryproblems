n = int(input())
array = [int(i) for i in input().split()]
 
moves = 0                 
for i in range(1,n): 
    if array[i] < array[i-1]: 
        x = array[i-1] - array[i]
        moves = moves + x
        array[i] = array[i-1]
 
print(moves)
