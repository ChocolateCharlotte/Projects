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
    coefficient_matrix = [ [2, 3, 1], [5, 5, 5], [10, 9, 4] ]
    constant_matrix = [ [4], [20], [100] ]

    print( solve3x3(  coefficient_matrix, constant_matrix  ) )

if __name__ == "__main__":
    test()

