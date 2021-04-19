n = int(input())
list1 = [int(i) for i in input().split()]

total_list1 = sum(list1)            
missingnumsum = (n * (n+1))//2      
m = missingnumsum - total_list1     
print(m)
