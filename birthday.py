from collections import Counter
import random


n = int( input("How many people:") )
success = 0

for j in range(1, 10 + 1):
    print("Running simulations", (j - 1)*10000, "to", j * 10000 )
    
    for i in range(1, 10_000 + 1 ):
        
        bDayList = []
        
        for i in range(1, n + 1):
            bDayList.append( random.randint(1, 365) )
            
            
        myCounter = Counter(bDayList)
        
        if myCounter.most_common(1)[0][1] > 1:
            success += 1
            
    prob = success/( j * 10000 )
    print("Probability:", prob)
            
            
print("Final probability:", success/( 100_000  ) )
