"""
https://gist.github.com/Vusys/659670770734d2117b58b29ddb32bd51
"""

def read_N_lines( file_handle, n ):
	n_lines = []

	for line_read_count in range( 0, n ):
		n_lines.append( file_handle.readline().replace( "\n", "" ) )

	return n_lines
def get_character(character): # pass character argument as string
	search_string = "// {}".format( character )
	
	with open("segments.txt", "rt") as segments_file:
		for line in segments_file:
			if line.strip() == search_string: # remove trailing \n
				segment_array = read_N_lines( segments_file, 3 )
				segments_file.close() # close file to move file pointer back to the beginning for the next read

				return segment_array	
				
def convert_character_to_7_segments(character_to_convert, number_of_characters):
		if character_to_convert.isdigit():
			number_of_padding_zeros = number_of_characters - len(character_to_convert)
			padded_number = "0" * number_of_padding_zeros + character_to_convert
		
			character_segments_array = [ get_character( digit ) for digit in padded_number ]
		else:
			character_segments_array = [ get_character( character ) for character in character_to_convert ]

		return character_segments_array

def print_characters(characters_string, number_of_characters):
	segment_array = convert_character_to_7_segments( characters_string, number_of_characters )

	for segment_row_number in range( 0, 3 ):
		for number_segmented in segment_array:
			print( number_segmented[ segment_row_number ] , end = "\t" ) # print the i-th rows of each character
			
		print() # go to next line
		
def main():
	number = int(input("Enter your number:"))
	number_of_digits = int(input("Enter number of digits:"))

	print_characters( str(number), number_of_digits )


if __name__ == "__main__":
	main()
		
				