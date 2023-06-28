def selectionSort( number_array ):
	array_length = len( number_array )
	
	for index in range( array_length ):
		array_slice = number_array[ index: ]
		min_slice_element = min( array_slice )
		number_array.remove( min_slice_element )
		number_array.insert( index, min_slice_element )
		
	return number_array
	
if __name__ == "__main__":
	print( selectionSort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4] )
	print( selectionSort([2, 2, 2, 2]) == [2, 2, 2, 2] )