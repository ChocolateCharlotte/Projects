def collatz_sequence_generator( start_number ):
    if start_number == 1:
        return
    elif start_number % 2 == 0:
        new_number = start_number / 2
        print( new_number )

        collatz_sequence_generator( new_number )
    else:
        new_number = 3 * start_number + 1
        print( new_number )

        collatz_sequence_generator( new_number )

if __name__ == "__main__":
    user_number = int( input("Enter a starting number:") )
    collatz_sequence_generator( user_number )
