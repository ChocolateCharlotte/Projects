def get_columns( matrix, column_index ):
	rowTotal = len( matrix )
	column = []
	
	for rowIndex in range( rowTotal ):
		column_element = matrix[ rowIndex ][ column_index ]
		
		column.append( column_element )
		
	return column
	
def multiply( matrix1, matrix2 ):
	multiplication_matrix = []

	rowTotal_matrix1 = len( matrix1 )
	columnTotal_matrix2 = len( matrix2[0] )

	for rowIndex in range( rowTotal_matrix1 ):
		for columnIndex in range( columnTotal_matrix2 ):
			column_and_row_length = len( matrix2 )
			
			sum = 0 
			
			for element_index in range( column_and_row_length ):
				row_element_matrix1 = matrix1[ rowIndex ][ element_index ]
				column_element_matrix2 = matrix2[ element_index ][ columnIndex ]
				
				elemental_product = row_element_matrix1 * column_element_matrix2
				
				sum += elemental_product
				
			try:
				multiplication_matrix[ rowIndex ].append( sum )
			except IndexError:
				multiplication_matrix.append( [ sum ] )

	return multiplication_matrix
	
def test():
	given_matrix1 = [ [1,2,3], [4,5,6], [7,8,9] ] # a1 x b1
	given_matrix2 = [ [10,11,12], [13,14,15], [16,17,18] ] # a2 x b2

	multiplied_matrix = multiply( given_matrix1, given_matrix2 )
	print( multiplied_matrix )

if __name__ == "__main__":
	test()