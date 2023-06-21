"""
AX = B
X = A-1 B
"""

from matrix_adjoint_inverse import inverse_3x3
from matrix_mutiplication import multiply

def solve3x3( coefficient_matrix, constants_matrix ):
    coefficient_matrix_inverse = inverse_3x3( coefficient_matrix )
    solution_matrix = multiply( coefficient_matrix_inverse, constants_matrix )

    return solution_matrix

def test():
    coefficient_matrix = [ [3, 2, 3], [4, 5, 6], [7, 8, 9] ]
    constant_matrix = [ [10], [11], [12] ]

    print( solve3x3(  coefficient_matrix, constant_matrix  ) )

if __name__ == "__main__":
    test()

