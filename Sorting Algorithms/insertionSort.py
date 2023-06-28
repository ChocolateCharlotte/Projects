def insertionSort( number_array ):
	array_length = len( number_array )
	
	for element_index in range( 1, array_length ):
		current_element = number_array[ element_index ]
		
		last_comparision_index = element_index
		current_less_than_comparision_flag = True
		
		for comparision_index in range( element_index - 1, -1, -1 ):
			comparision_element = number_array[ comparision_index ]
			
			if current_element > comparision_element:
				current_less_than_comparision_flag = False
				
				number_array.remove( current_element )
				number_array.insert( last_comparision_index, current_element )
				
				break
				
			last_comparision_index = comparision_index
			
		if current_less_than_comparision_flag == True:
			number_array.remove( current_element )
			number_array.insert( 0, current_element  )

	return number_array
		
if __name__ == "__main__":
	print( insertionSort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4] )
	print( insertionSort([2, 2, 2, 2]) == [2, 2, 2, 2] )