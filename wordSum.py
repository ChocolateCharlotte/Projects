def wordSum(word):
    sum = 0 
    
    for ch in word:
        sum = sum + ord(ch) - 96
        
    return sum
    

with open("enable1.txt", "rt") as f:
    fDict = {}
    
    for line in f:
        word = line.strip()
        wS = wordSum(word)
        
        if wS in fDict:
            fDict[wS] += 1
        else:
            fDict[wS] = 1
            
    max = 0
    maxK = None
    
    for k, v in fDict.items():
        if v > max:
            max = v
            maxK = k
        
    
    print( max, maxK )