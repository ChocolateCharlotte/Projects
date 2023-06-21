

def matrix_determinant_2x2( matrix ):
    top_left_element = matrix[0][0]
    top_right_element = matrix[0][1]
    bottom_left_element = matrix[1][0]
    bottom_right_element = matrix[1][1]
    
    return top_left_element * bottom_right_element - top_right_element * bottom_left_element

