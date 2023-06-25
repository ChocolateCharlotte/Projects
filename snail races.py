import random
import os
import time

SNAIL_AVATAR = "@v"
FIELD_LENGTH = 40

def snail_tiles_covered( snail_speed, time_elapsed ):
    tiles = snail_speed * time_elapsed
    return tiles
    
    
def print_snail_tiles( snail_name, tiles ):

    if tiles <= FIELD_LENGTH:
        print( " " * tiles + snail_name )
        print( "." * tiles + SNAIL_AVATAR )
    else:
        print( " " * FIELD_LENGTH + snail_name )
        print( "." * FIELD_LENGTH + SNAIL_AVATAR )
    
def main():
    
    snail_dict = {}
    
    number_of_snails = int( input( "Number of snails:") )
    
    for snail_index in range( 0, number_of_snails ):
        snail_name = input( "Enter the name of snail {}:".format( snail_index ) )
        
        snail_speed_random = random.randint(1, 3)
        snail_dict[ snail_name ] = snail_speed_random
        
    least_speed = min( snail_dict.values() )
    
    time_elapsed = 0
    max_time = FIELD_LENGTH/least_speed
    
    while time_elapsed < max_time:
        os.system("cls")
        
        whitespace = FIELD_LENGTH 
        print( "START" + " " * (FIELD_LENGTH - 5 + 1) + "END" )
        print( "|" + " " * (FIELD_LENGTH - 2) +  "|" )
        
        for snail_name, snail_speed in snail_dict.items():
            tiles_covered = snail_tiles_covered( snail_speed, time_elapsed )
            print_snail_tiles( snail_name, tiles_covered )
            
        time.sleep( 1 )
        time_elapsed += 1
            
           
if __name__ == "__main__":
    main()