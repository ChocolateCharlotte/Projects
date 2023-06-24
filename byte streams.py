import random
import time

def generate_byte_streams( length_of_byte_stream, number_of_streams ):
    byte_streams_list = []
    
    for byte_stream_count in range( 0, number_of_streams ):
    
        flag = random.randrange(1, 5)
                
        if flag == 1:
    
            byte_stream_whitespace_leading  = " " * random.randint(1, 3)
            byte_stream_whitespace_trailing = " " * random.randint(0, 3)
            
            byte_stream_digit_length = length_of_byte_stream - len( byte_stream_whitespace_leading,) - len( byte_stream_whitespace_trailing )
            # byte_stream_digit_length = random.randrange(1, max_byte_stream_digit_length )
            
            # byte_stream_whitespace_trailing_length = length_of_byte_stream - len( byte_stream_whitespace_leading ) - byte_stream_digit_length 
            # byte_stream_whitespace_trailing = " " * byte_stream_whitespace_trailing_length
            
            byte_stream_digits = ""
            
            for byte_stream_digit_count in range( byte_stream_digit_length ):
                bit = str( random.randint(0, 1) )
                
                byte_stream_digits += bit
                
            byte_stream = byte_stream_whitespace_leading + byte_stream_digits + byte_stream_whitespace_trailing
            
            byte_streams_list.append( byte_stream )
            
        else:
            byte_streams_list.append( " " * length_of_byte_stream )
        
    return byte_streams_list
        

def print_byte_streams( byte_streams_list ):
    
    byte_stream_length = len( byte_streams_list[0] )
    
    for byte_stream_character_index in range( 0, byte_stream_length ):
        for byte_stream in byte_streams_list:
            print( byte_stream[ byte_stream_character_index ], end = "" )
        time.sleep(0.5)
                
        print()
        
if __name__ == "__main__":
    while True:
        byte_streams_list = generate_byte_streams( 10, 190 )
        print_byte_streams( byte_streams_list )
        