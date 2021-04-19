#Two Sets (casework took forever)
#Divide the numbers 1,2,...,n into two sets of equal sum. Only input is n. 
#Print YES if possible, NO if not. If YES, print subsets and number of elements in each subset. 
#Only possible if n(n+1)/2 is divisible by 2, meaning that n = 0 mod 4 or n = 3 mod 4.
#case n = 0 mod 4: split list in half, take all even indices of first half and odd of second half to create set 1, odd indices of first half and even of second for set 2
#case n = 3 mod 4: n = 4m - 1, and take m, 2m, and 3m out of list. Split remaining list in half and do same as other case. Add m and 2m to first set, and 3m to second. 

def oddindices(list1):               #function to create list of odd indices of list
    newlist = []
    for index in range(1, len(list1), 2): 
        newlist.append(list1[index])
    return newlist
    
def evenindices(list2):              #function to create list of even indices
    newerlist = []
    for index in range(0, len(list2), 2):
        newerlist.append(list2[index])
    return newerlist

def equalsets(n): 
    seq = list(range(1, n + 1))

    if n % 4 == 1 or n % 4 == 2: 
        print ("NO")
    else: 
        print ("YES")

        if n % 4 == 0:
            length = len(seq)                    #splitting the list in half
            middle_index = length//2
            alphafirsthalf = seq[:middle_index]
            alphasechalf = seq[middle_index:]
            
            #set 1
            evena_firsthalf = evenindices(alphafirsthalf)
            odda_sechalf = oddindices(alphasechalf)
            set1 = evena_firsthalf + odda_sechalf
            
            #set 2
            odda_firsthalf = oddindices(alphafirsthalf)
            evena_sechalf = evenindices(alphasechalf)
            set2 = odda_firsthalf + evena_sechalf
            #print the final sets
            print(len(set1))
            print(set1)
            print(len(set2))
            print(set2)

        else:                                   #if n mod 4 = 3
            m = n//4 + 1
            multiples1 = [m, m*2]
            multiples2 = [m*3]
            #remove m, 2m, and 3m from seq
            del seq[m-1:n:m]
            #split seq in half
            length = len(seq)
            middle_index = length//2
            betafirsthalf = seq[:middle_index]
            betasechalf = seq[middle_index:]
            
            #set 1
            evenb_firsthalf = evenindices(betafirsthalf)
            oddb_sechalf = oddindices(betasechalf)
            set1final = evenb_firsthalf + oddb_sechalf + multiples1
            
            #set 2
            oddb_firsthalf = oddindices(betafirsthalf)
            evenb_sechalf = evenindices(betasechalf)
            set2final = oddb_firsthalf + evenb_sechalf + multiples2
            
            #print the final sets
            print(len(set1final))
            print(set1final)
            print(len(set2final))
            print(set2final)

#testingcode
equalsets(15)
#equalsets(8)
