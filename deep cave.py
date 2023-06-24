import random
import time

while True:
	start_position = random.randint(18, 22)
	gap = random.randint(8, 12)
	
	total_length = 50
	
	end_position = total_length - start_position - gap
	
	print( "#" * start_position + " " * gap + "#" * end_position )
	
	time.sleep( 1 )
	
	