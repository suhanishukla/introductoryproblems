DNA = input()

occurrences = 1          
final = 0                 
if len(DNA) == 1: 
    final = 1
for i in range(0, len(DNA) - 1):        
    if DNA[i] == DNA[i+1]:            
        occurrences = occurrences + 1
        final = max(final, occurrences)
    else: 
        occurrences = 1
        final = max(final, occurrences)
print(final)