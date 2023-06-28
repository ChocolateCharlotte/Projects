
"""
Ship placement -> matrix, 4 oreintations, check for space and other ships
attack -> declare element, check for all spaces
tracking -> matrix
display -> matrix
storing ships -> matrix
"""

from collections import defaultdict
import copy

SHIP_DICT = { "Carrier":5, "Battleship":4, "Destroyer":3, "Submarine":3, "Patrol Boat":2 }
SHIP_CHARACTERS = { "Carrier": "C", "Battleship": "B", "Destroyer": "D", "Submarine": "S", "Patrol Boat": "P" }
SHIP_COLUMNS = "ABCDEFGHIJ"
SHIP_ROWS_NUMBER = 10

ORIENTATIONS_LIST = [ "TOP", "BOTTOM", "LEFT", "RIGHT" ]

def print_dict( dictionary ):

    for key, value in dictionary.items():
        print( key, value )
        
        
def traslate_playboard_positions( position ):

    position_alphabet = position[0]
    position_row_index = position[1]
    
    alphabet_number = ord( position_alphabet ) - 96
    
    matrix_column_index = alphabet_number - 1
    matrix_row_index = position_row_index - 1
    
    return matrix_row_index, matrix_column_index
    
    
    
def generate_empty_user_ship_matrix():
    user_ship_matrix = []
    
    for row_index in range( SHIP_ROWS_NUMBER ):
        for column_index in range( len( SHIP_COLUMNS ) ):
            
            try:
                user_ship_matrix[ row_index ][ column_index ] = " "
            except IndexError:
                user_ship_matrix.append( [ " " ] )
                
    return user_ship_matrix
    
    
def check_for_orientation_collisions( orientation_dict, ship_matrix ):

    copy_orientation_dict = orientation_dict.copy()
    
    for orientation, coordinate_list in copy_orientation_dict.items():
    
        for row_index, column_index in coordinate_list:
            matrix_element = ship_matrix[ row_index ][ column_index ]
            
            if matrix_element != " ":
                copy_orientation_dict.pop( orientation )
                
    return copy_orientation_dict


def get_orientations( ship_length, ship_position, ship_matrix ):

    translated_position = translated_position( ship_position )
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
        orientation_flags[ "LEFT" ] = [ ( translated_position_row_index, translated_position_column_index - count ) for count in range( 0, ship_length ) ]
        
    elif translated_position_column_index =< maximum_right_index:
        orientation_flags[ "RIGHT" ] = [ ( translated_position_row_index, translated_position_column_index + count ) for count in range( 0, ship_length ) ] 
        
    elif translated_position_row_index >= minimum_top_index:
        orientation_flags[ "TOP" ] = [ ( translated_position_row_index - count, translated_position_column_index ) for count in range( 0, ship_length ) ]
        
    elif translated_position_row_index =< maximum_bottom_index:
        orientation_flags[ "BOTTOM" ] = [ ( translated_position_row_index + count, translated_position_column_index ) for count in range( 0, ship_length ) ] 
        
        
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

    for row_index in range( SHIP_ROWS_NUMBER ):
    
        for column_index in range( len( SHIP_COLUMNS ) ):
        
            element = user_ship_matrix[ row_index ][ column_index ]
            print(element, end = "" )
            
        print()
    
    
    
def place_ships():

    user_ship_matrix = generate_empty_user_ship_matrix()
    user_ship_dict = SHIP_DICT.copy()
    
    loop_flag = True
    
    while loop_flag:
    
        display_user_ship_matrix( user_ship_matrix )
    
        number_of_ships_available = sum( user_ship_dict.values() )
        if number_of_ships_available == 0:
            loop_flag = False
            break
            
            
        print( "Available choices" )
        print_dict( user_ship_dict )
        
        
        ship_type = input( "Please enter ship type:" )
        if ship_type not in SHIP_DICT:
            continue
        elif user_ship_dict[ ship_type ] == 0:
            continue
            
            
        ship_position = input( "Please enter ship position:" )
        ship_position_column_alphabet = ship_position[0]
        ship_position_row_index = ship_position[1]
        if (ship_position_column_alphabet not in SHIP_COLUMNS) or (ship_position_row_index not in range( 1, 10 + 1 ):
            continue
            
            
        ship_length = user_ship_dict[ ship_type ]
        ship_character = SHIP_CHARACTERS[ ship_type ]
        
        orientation_dict = get_orientations( ship_length, ship_position, user_ship_matrix )
        display_orientations( orientation_dict )

        user_orientation = input("Choose an orientation (Top/Bottom/Left/Right)":)
        
        if user_orientation not in orientation_dict:
            continue
                        
            
        confirmation_flag = input( "Confirm placement? (True/False)" )
        
        if confirmation_flag == True:
            user_ship_dict[ ship_type ] -= 1
            
            choosen_orientation_coordinate_list = orientation_dict[ user_orientation ]
            
            for row_index, column_index in choosen_orientation_coordinate_list:
                user_ship_matrix[ row_index ][ column_index ] = ship_character
            
            
        
def main():
    place_ships()
    
if __name__ == "__main__":
    main()
        
        
    
    