
"""
Ship placement -> matrix, 4 oreintations, check for space and other ships
attack -> declare element, check for all spaces
tracking -> matrix
display -> matrix
storing ships -> matrix
"""

"""
change alphabets to numbers and add translation
add quantity
"""

import copy
import os

SHIP_SIZE_DICT = {"Carrier":5, "Battleship":4, "Destroyer":3, "Submarine":3, "Patrol Boat":2}
SHIP_COUNT_DICT = {"Carrier":1, "Battleship":1, "Destroyer":1, "Submarine":1, "Patrol Boat":1}
SHIP_CHARACTERS = { "Carrier": "C", "Battleship": "B", "Destroyer": "D", "Submarine": "S", "Patrol Boat": "P" }
SHIP_COLUMNS = "ABCDEFGHIJ"
SHIP_ROWS_NUMBER = 10

ORIENTATIONS_LIST = [ "TOP", "BOTTOM", "LEFT", "RIGHT" ]

def clear_screen():
    os.system( "cls" )

def print_dict( dictionary ):

    for key, value in dictionary.items():
        print( key, value )
        
        
def translate_playboard_positions( position_string ):

    position_alphabet = position_string[0]
    position_row_index = int( position_string[1:] )
    
    alphabet_number_index = SHIP_COLUMNS.find( position_alphabet )
    
    matrix_column_index =  alphabet_number_index
    matrix_row_index = position_row_index - 1
    
    return matrix_row_index, matrix_column_index
    
    
    
def generate_empty_user_ship_matrix():
    user_ship_matrix = []
    
    for row_index in range( SHIP_ROWS_NUMBER ):
        for column_index in range( len( SHIP_COLUMNS ) ):
            
            try:
                user_ship_matrix[ row_index ].append( " " )
            except IndexError:
                user_ship_matrix.append( [ " " ] )
                
    return user_ship_matrix
    
    
def check_for_orientation_collisions( orientation_dict, ship_matrix ):

    copy_orientation_dict = orientation_dict.copy()
    
    for orientation, coordinate_list in copy_orientation_dict.copy().items():
    
        for row_index, column_index in coordinate_list:
            matrix_element = ship_matrix[ row_index ][ column_index ]
            
            if matrix_element != " ":
                copy_orientation_dict.pop( orientation )
                break
                
    return copy_orientation_dict


def get_orientations( ship_length, ship_position, user_ship_matrix ):

    translated_position = translate_playboard_positions( ship_position )
    translated_position_row_index = translated_position[0]
    translated_position_column_index = translated_position[1]
    
    last_row_index = SHIP_ROWS_NUMBER - 1
    last_column_index = len( SHIP_COLUMNS ) - 1
    
    minimum_left_index = ( ship_length - 1 )
    maximum_right_index = last_column_index - ( ship_length - 1 )
    minimum_top_index = ( ship_length - 1 )
    maximum_bottom_index = last_row_index - ( ship_length - 1 )
    
    orientation_dict = {}
    
    if translated_position_column_index >= minimum_left_index:
        orientation_dict[ "LEFT" ] = [ ( translated_position_row_index, translated_position_column_index - count ) for count in range( 0, ship_length ) ]
        
    if translated_position_column_index <= maximum_right_index:
        orientation_dict[ "RIGHT" ] = [ ( translated_position_row_index, translated_position_column_index + count ) for count in range( 0, ship_length ) ]
        
    if translated_position_row_index >= minimum_top_index:
        orientation_dict[ "TOP" ] = [ ( translated_position_row_index - count, translated_position_column_index ) for count in range( 0, ship_length ) ]
        
    if translated_position_row_index <= maximum_bottom_index:
        orientation_dict[ "BOTTOM" ] = [ ( translated_position_row_index + count, translated_position_column_index ) for count in range( 0, ship_length ) ]
        
        
    collision_filter_orientation_dict = check_for_orientation_collisions( orientation_dict, user_ship_matrix )
        
        
    return collision_filter_orientation_dict
    
    
    
def display_orientations( orientation_dict, user_ship_matrix, ship_type ):

    user_ship_matrix_copy = copy.deepcopy( user_ship_matrix )

    ship_character = SHIP_CHARACTERS[ ship_type ]


    for orientation, coordinate_list in orientation_dict.items():
        for row_index, column_index in coordinate_list:
            user_ship_matrix_copy[ row_index ][ column_index ] = ship_character
            
            
    display_user_ship_matrix( user_ship_matrix_copy )


def display_user_ship_matrix( user_ship_matrix ):

    print( "  " + SHIP_COLUMNS ) # Two-space column to account for two-digit "10" at the end

    for row_index in range( SHIP_ROWS_NUMBER ):
        num_of_spaces = 2 - len( str( row_index + 1 ) )

        print( row_index + 1, end = " " * ( num_of_spaces ) ) # When 10 is printed, it shifts the entire row by 1 unit
    
        for column_index in range( len( SHIP_COLUMNS ) ):
        
            element = user_ship_matrix[ row_index ][ column_index ]
            print(element, end = "" ) #make sure to not print a new line
            
        print() # go to next line


    print() # print blank line after the entire grid is printed
    
def place_ships():

    user_ship_matrix = generate_empty_user_ship_matrix()
    user_ship_count_dict = SHIP_COUNT_DICT.copy()
    
    loop_flag = True
    
    while loop_flag:

        clear_screen()
        display_user_ship_matrix( user_ship_matrix )
    
        number_of_ships_available = sum( user_ship_count_dict.values() )
        if number_of_ships_available == 0:
            loop_flag = False
            break
            
            
        print( "Available choices" )
        print_dict( user_ship_count_dict )
        
        
        ship_type = input( "Please enter ship type:" ).title()

        if ship_type not in SHIP_SIZE_DICT:
            continue
        elif user_ship_count_dict[ ship_type ] == 0:
            continue
            
            
        ship_position_string = input( "Please enter ship position:" )
        ship_position_column_alphabet = ship_position_string[0].upper()
        ship_position_row_index = int( ship_position_string[1:] )
        if (ship_position_column_alphabet not in SHIP_COLUMNS) or (ship_position_row_index not in range( 1, 10 + 1 ) ):
            continue
            
            
        ship_length = SHIP_SIZE_DICT[ ship_type ]
        ship_character = SHIP_CHARACTERS[ ship_type ]
        
        orientation_dict = get_orientations( ship_length, ship_position_string, user_ship_matrix )
        display_orientations( orientation_dict, user_ship_matrix, ship_type )

        if orientation_dict == {}:
            continue

        user_orientation = input("Choose an orientation (Top/Bottom/Left/Right):").upper()
        
        if user_orientation not in orientation_dict:
            continue

        specific_orientation_dict = { user_orientation.upper() : orientation_dict[ user_orientation.upper() ] }
        display_orientations( specific_orientation_dict, user_ship_matrix, ship_type )
        confirmation_flag = input( "Confirm placement? (yes/no)" ).lower()
        
        if confirmation_flag == "yes":
            user_ship_count_dict[ ship_type ] -= 1
            
            chosen_orientation_coordinate_list = orientation_dict[ user_orientation ]
            
            for row_index, column_index in chosen_orientation_coordinate_list:
                user_ship_matrix[ row_index ][ column_index ] = ship_character
            
            
        
def main():
    place_ships()


if __name__ == "__main__":
    main()
        
        
    
    