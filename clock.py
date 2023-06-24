import os
import time
import datetime
import seven_segment_display

def clear_screen():
    os.system( "cls" )

def print_time():
    while True:
        clear_screen()

        current_time = datetime.datetime.now()

        time_parsing_string = "%H:%M:%S"
        parsed_time = current_time.strftime( time_parsing_string )

        seven_segment_display.print_characters( parsed_time, len(parsed_time) )

        time.sleep( 0.8 )


if __name__ == "__main__":
    print_time()