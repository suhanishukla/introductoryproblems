def longestrepetition(DNA):
    occurences = 1
    final = 0 
    
    for i in range(0, len(DNA) - 1): 
        if DNA[i] == DNA[i+1]: 
            occurences = occurences + 1
            final = max(final, occurences)
        else: 
            occurences = 1

    print(final)

        
DNA = "ATTCGGGGGA"
longestrepetition(DNA)
    