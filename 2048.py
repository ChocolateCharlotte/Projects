import random
import copy
import os

MATRIX_COLUMNS_TOTAL = MATRIX_ROWS_TOTAL = 4

TOP_BOTTOM = [ "+-----", "+" ]
ROW = """
+-----+-----+-----+-----+
|     |     |     |     |
|nnnnn|nnnnn|nnnnn|nnnnn|
|     |     |     |     |
"""

def initialize_matrix():
    matrix = [  [ "" for column_index in range( MATRIX_COLUMNS_TOTAL ) ] for row_index in range( MATRIX_ROWS_TOTAL ) ]
    
    for random_element_index in range( 0, 2 ):
    
        random_row = random.randrange( 0, MATRIX_ROWS_TOTAL )
        random_column = random.randrange( 0, MATRIX_COLUMNS_TOTAL )
        
        random_value = 2 ** ( random.randint(1,2) )
        
        matrix[ random_row ][ random_column ] = random_value
        
    return matrix
    
def print_matrix( matrix ):
    print( matrix )

    for row_index in range( 0, MATRIX_ROWS_TOTAL ):
    
        editted_ROW = ROW
        stripped_ROW = editted_ROW.strip()
        
        for column_index in range( 0, MATRIX_COLUMNS_TOTAL ):
        
            element = matrix[ row_index ][ column_index ]
            element_length = len( str( element ) )
            
            if element_length == 1:
                padded_element = "  {}  ".format( str(element) )
                
            elif element_length == 2:
                padded_element = " {}  ".format( str(element) )
                
            elif element_length == 3:
                padded_element = " {} ".format( str(element) )
                
            elif element_length == 4:
                padded_element = " {}".format( str(element) )
            else:
                padded_element = "     "
            
            
            number_in_ROW = stripped_ROW.replace( "nnnnn" , padded_element, 1 )
            stripped_ROW = number_in_ROW
            
        print( stripped_ROW , end = "" )
        print()

    # print bottom
    print( TOP_BOTTOM[0] * MATRIX_COLUMNS_TOTAL + TOP_BOTTOM[1] )

def get_row_first_filled_space( matrix, element_row_number, element_column_number, direction ):

    entire_row = matrix[element_row_number]

    if direction == "RIGHT":
        for column_index in range( MATRIX_COLUMNS_TOTAL ):
            if column_index > element_column_number:
                element = entire_row[ column_index ]

                if element != "":
                    return column_index
                else:
                    return None

    elif direction == "LEFT":
        for column_index in range( MATRIX_COLUMNS_TOTAL ):
            if column_index < element_column_number:
                element = entire_row[ column_index ]

                if element != "":
                    return column_index
                else:
                    return None


def update_matrix( matrix, direction ):
    copy_matrix_2 = copy.deepcopy(matrix)

    if direction == "RIGHT":

        for row_index in range( MATRIX_ROWS_TOTAL ):

            copy_matrix = copy.deepcopy( matrix )

            for column_index in range( MATRIX_COLUMNS_TOTAL - 1, -1, -1 ):

                element = copy_matrix[ row_index ][ column_index ]

                if element != "":
                    if row_index == MATRIX_ROWS_TOTAL - 1:
                        continue

                    first_filled_space_column_index = get_row_first_filled_space( copy_matrix, row_index, column_index, "RIGHT" )

                    if first_filled_space_column_index is not None:
                        first_empty_space_column_index = first_empty_space_column_index - 1
                        first_filled_element = copy_matrix[ row_index ][ first_filled_space_column_index ]

                        if element == first_filled_element:
                            copy_matrix[row_index][first_filled_space_column_index] = 2 * element
                            copy_matrix[row_index][column_index] = ""

                        else:
                            copy_matrix[row_index][first_empty_space_column_index] = element
                            copy_matrix[row_index][column_index] = ""

                    else:
                        first_empty_space_column_index = MATRIX_COLUMNS_TOTAL - 1

                        copy_matrix[row_index][first_empty_space_column_index] = element
                        copy_matrix[row_index][column_index] = ""

            copy_matrix_2[ row_index ] = copy_matrix[ row_index ]

        return copy_matrix_2







def main():
    playing_field = initialize_matrix()
    print_matrix( playing_field )

    while True:
        user_direction = input("W/A/S/D...")

        if user_direction == "D":
            matrix = update_matrix( playing_field, "RIGHT" )

            os.system( "cls" )
            print_matrix( matrix )

    
    
if __name__ == "__main__":
    main()
    
    
        
        
    
    