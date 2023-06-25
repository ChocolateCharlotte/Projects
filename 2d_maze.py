import os

def read_maze( filename ):

    maze_matrix = []
    row_index = 0
    startCoords = ()
    endCoords = ()
    
    with open( filename, "rt" ) as maze_file:
    
        for line in maze_file:
            column_index = 0

            for character in line.strip():
            
                try:
                    maze_matrix[ row_index ].append( character )
                except IndexError:
                    maze_matrix.append( [ character ] )
                    
                    
                if character.lower() == "e":
                    endCoords = ( row_index, column_index )

                if character.lower() == "s":
                    startCoords = ( row_index, column_index )

                column_index += 1
            row_index += 1
                
                
    return maze_matrix, startCoords, endCoords
    
def print_maze( maze_matrix ):

    for row_index in range( len( maze_matrix ) ):
        for column_index in range( len( maze_matrix[0] ) ):
        
            element = maze_matrix[ row_index ][ column_index ]
            print( element , end = "" )
            
        print()
        
def clear_screen():
    os.system( "cls" )
    
    
def move_character( matrix, current_position_tuple, direction ):
    current_row_index = current_position_tuple[0]
    current_column_index = current_position_tuple[1]

    if direction.lower() == "n":
        new_position_column_index = current_column_index
        new_position_row_index = current_row_index - 1
        
    elif direction.lower() == "s":
        new_position_column_index = current_column_index 
        new_position_row_index = current_row_index + 1
        
    elif direction.lower() == "e":
        new_position_column_index = current_column_index + 1
        new_position_row_index = current_row_index 
        
    elif direction.lower() == "w":
        new_position_column_index = current_column_index - 1
        new_position_row_index = current_row_index
        
        
    if matrix[ new_position_row_index ][ new_position_column_index ] != "#":
           matrix[ new_position_row_index ][ new_position_column_index ] = "S"
           matrix[ current_row_index ][ current_column_index ] = " "
           
    return matrix

def get_current_coords( maze_matrix ):
    for row_index in range( len( maze_matrix ) ):
        for column_index in range( len( maze_matrix[0] ) ):
            element = maze_matrix[ row_index ][ column_index ]

            if element.lower() == "s":
                return (row_index, column_index)
    
def main():
    maze_name = input("Enter maze file name:")
    
    read_maze_tuple = read_maze( maze_name )
    maze_matrix, startCoords, endCoords = read_maze_tuple[0], read_maze_tuple[1], read_maze_tuple[2]
    currentCoords = startCoords
    
    print_maze( maze_matrix )
    
    while True:
        clear_screen()
        print_maze( maze_matrix )

        direction = input( "N/S/E/W:" )
        
        if direction.lower() not in ( "n", "s", "e", "w" ):
            continue
        
        maze_matrix = move_character( maze_matrix, currentCoords, direction )
        currentCoords = get_current_coords( maze_matrix )
        
        
if __name__ == "__main__":
    main()
    
    