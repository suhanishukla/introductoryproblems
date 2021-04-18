
def FindMissingNum(list1): 
    total_list1 = sum(list1)            #find the sum of all the elements of list1 

    x = len(list1) + 1
    missingnumsum = (x * (x+1))/2       #sum of list with missing number 

    n = missingnumsum - total_list1     #finding the missing number
    
    print(n)

#testing function
list1 = [15, 14, 13, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
FindMissingNum(list1)