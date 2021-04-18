#Repetitions
#Given a DNA sequence: string consisting of A, G, C, T. Find the longest substring in sequence consisting of one character. 
#Find longest repetition of a letter. 
#Print one integer: the length of the longest repetition. 

def longestrepetition(DNA):
    occurrences = 1           #occurrences of a character
    final = 0                 #final answer
    
    for i in range(0, len(DNA) - 1):        
        if DNA[i] == DNA[i+1]:            #Does this character match the one directly after it? (index + 1)
            occurrences = occurrences + 1
            final = max(final, occurrences)
        else: 
            occurrences = 1

    print(final)
    
#testing code
DNA = "ATTCGGGGGA"
longestrepetition(DNA)
    
