import string
import random

def random_string_generator( length_of_string, number_of_strings ):
	character_string = string.ascii_lowercase + string.ascii_uppercase + string.punctuation
	character_list = list( character_string )
	
	random_string_list = []
	
	while len(random_string_list) <= number_of_strings:
		random_string = random.sample( character_list, k = length_of_string )
		
		if random_string not in random_string_list:
			random_string_list.append( "".join(random_string) )
			
	return random_string_list
	
if __name__ == "__main__":
	print( random_string_generator( 10, 5 ) )