"""
00 01 02
10 11 12
20 21 22
"""

from matrix_determinant2x2 import matrix_determinant_2x2

def matrix_minors_3x3( matrix ):
    rowTotal = len( matrix )
    columnTotal = len( matrix[0] )

    all_row_indexs = list( range( 0, rowTotal ) )
    all_column_indexs = list( range( 0, columnTotal ) )
    minors_matrix = []

    for rowIndex in range( rowTotal ):
        for columnIndex in range( columnTotal ):
            element = matrix[ rowIndex ][ columnIndex ]

            excluded_row_index = rowIndex
            excluded_column_index = columnIndex

            included_elements_matrix = [ ]

            included_rows_list = [ row_index for row_index in all_row_indexs if row_index != excluded_row_index ]
            included_columns_list = [ column_index for column_index in all_column_indexs if column_index != excluded_column_index ]

            for included_row_list_index in range( len( included_rows_list ) ):
                for included_column_list_index in range( len( included_columns_list ) ):

                    included_row_index = included_rows_list[ included_row_list_index ]
                    included_column_index = included_columns_list[ included_column_list_index ]

                    included_element = matrix[ included_row_index ][ included_column_index ]

                    try:
                        included_elements_matrix[ included_row_list_index ].append( included_element )
                    except IndexError:
                        included_elements_matrix.append( [ included_element ] )

            minor = matrix_determinant_2x2( included_elements_matrix )

            try:
                minors_matrix[ rowIndex ].append( minor )
            except IndexError:
                minors_matrix.append( [ minor ] )

    return minors_matrix



def test():
    myMatrix =  [[12, 22, 23], [54, 25, 16], [17, 58, 29]]

    print( matrix_minors_3x3( myMatrix ) )

if __name__ == "__main__":
    test()
