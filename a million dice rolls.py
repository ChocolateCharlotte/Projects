from collections import defaultdict
import random

def roll_dices_sum( number_of_dices ):
    sum = 0
    for dice_roll in range( number_of_dices ):
        dice_outcome = random.randint(1, 6)
        sum += dice_outcome
        
    return sum

def main():

    number_of_dices = int( input("Enter number of dices:") )
    
    sum_counter = defaultdict( int )
                
    print( type(sum_counter) )
        
        
    for count in range( 1, 100_000 + 1):
        dice_sum = roll_dices_sum( number_of_dices )
        sum_counter[ dice_sum ] += 1
        
        if count % 10_000 == 0:
            print( str(count//10_00) + "% complete")

    for sum, frequency in sum_counter.items():
        print( "Probability of", sum, "is", frequency/100_0 )
      
main()