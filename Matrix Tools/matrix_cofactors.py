from matrix_minors import matrix_minors_3x3

def matrix_cofactors_3x3( matrix ):
    matrix_minors = matrix_minors_3x3( matrix )

    rowTotal = len( matrix_minors )
    columnTotal = len( matrix_minors[0] )

    cofactor_matrix = []

    for rowIndex in range( 0, rowTotal ):
        for columnIndex in range( 0, columnTotal ):
            corrected_rowIndex = rowIndex + 1
            correct_columnIndex = columnIndex + 1

            minor_matrix_element = matrix_minors[ rowIndex ][ columnIndex ]

            cofactor = (-1)**( corrected_rowIndex + correct_columnIndex ) * minor_matrix_element

            try:
                cofactor_matrix[ rowIndex ].append( cofactor )
            except IndexError:
                cofactor_matrix.append( [cofactor] )

    return cofactor_matrix

def test():
    myMatrix =  [[12, 22, 23], [54, 25, 16], [17, 58, 29]]
    print( matrix_cofactors_3x3(myMatrix) )

if __name__ == "__main__":
    test()




