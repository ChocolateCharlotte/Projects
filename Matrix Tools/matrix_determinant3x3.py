from matrix_cofactors import matrix_cofactors_3x3

def matrix_determinant_3x3 ( matrix ):
    a00 = matrix[ 0 ][ 0 ]
    a01 = matrix[ 0 ][ 1 ]
    a02 = matrix[ 0 ][ 2 ]

    cofactors_matrix = matrix_cofactors_3x3( matrix )

    cofactor_a00 = cofactors_matrix[0][0]
    cofactor_a01 = cofactors_matrix[0][1]
    cofactor_a02 = cofactors_matrix[0][2]

    determinant = a00 * cofactor_a00 + a01 * cofactor_a01 + a02 * cofactor_a02

    return determinant