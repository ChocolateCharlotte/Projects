def bubbleSort( number_array ):
	
	array_length = len( number_array )
	
	while True:
		swapped_flag = False
		
		for array_index in range( 1, array_length ):
			element_1 = number_array[ array_index ]
			element_2 = number_array[ array_index - 1 ]
			
			if element_1 < element_2:
				number_array[ array_index - 1 ], number_array[ array_index ] = element_1, element_2
				swapped_flag = True
			
		if swapped_flag == False:
			break
			
	return number_array
	
if __name__ == "__main__":
	print( bubbleSort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4] )
	print( bubbleSort([2, 2, 2, 2]) == [2, 2, 2, 2] )