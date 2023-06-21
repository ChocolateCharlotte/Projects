def get_column( matrix, columnIndex ):
	column = []
	
	rowTotal = len( matrix )
	
	for rowIndex in range( rowTotal ):
		column_element = matrix[ rowIndex ][ columnIndex ]
		column.append( column_element )
		
	return column

def transpose( givenMatrix ):
    transposed_matrix = []

    rowTotal = len( givenMatrix )
    columnTotal = len( givenMatrix[0] )

    for columnIndex in range( columnTotal ):
        column = get_column( givenMatrix, columnIndex )
        transposed_matrix.append( column )
		
    return transposed_matrix
    
def test():
    myMatrix = [ [1,2,3], [4,5,6], [7,8,9] ]
    transposed_matrix = transpose( myMatrix )
    print( transposed_matrix )
    
  
if __name__ == "__main__":
    test()
