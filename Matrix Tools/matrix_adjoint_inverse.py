from matrix_cofactors import matrix_cofactors_3x3
from matrix_determinant3x3 import matrix_determinant_3x3
from matrix_transpose import transpose
from copy import deepcopy

def adjoint_3x3( matrix ):
    cofactor_matrix = matrix_cofactors_3x3( matrix )
    adjoint = transpose( cofactor_matrix )

    return adjoint

def inverse_3x3( matrix ):
    adjoint = adjoint_3x3( matrix )
    determinant = matrix_determinant_3x3( matrix )

    rowTotal = len( adjoint )
    columnTotal = len( adjoint[0] )

    inverse = deepcopy( adjoint )

    for rowIndex in range( 0, rowTotal ):
        for columnIndex in range( 0, columnTotal ):
            element = adjoint[ rowIndex ][ columnIndex ]

            inverse[ rowIndex ][ columnIndex ] = element/determinant

    return inverse



def test():
    myMatrix = [[12, 22, 23], [54, 25, 16], [17, 58, 29]]
    print( adjoint_3x3( myMatrix ), inverse_3x3(myMatrix) )

if __name__ == "__main__":
    test()