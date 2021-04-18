def increasearray(array): 
    moves = 0
    n = len(array)
    for i in range(n-1): 
        if array[i] > array[i+1]: 
            x = array[i] - array [i+1]
            moves = moves + x
        else: 
            x = 0
    print(moves)

array = [3, 2, 5, 1, 7]
increasearray(array)