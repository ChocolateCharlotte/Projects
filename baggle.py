import random

def generate():
	return str(random.randint(100, 1000))

def pico(guess, correct):
	flag = False
	
	for ch in guess:
		if ch in correct:
			flag = True
			return flag
					
def fermi(guess, correct):
	flag = False
	
	for i in range( 0, len(correct) ):
		if guess[i] == correct[i]:
			flag = True
			return flag
	
def main():
	correct = generate()
	print( correct )
	
	for i in range( 1, 10 ):
		guess = input( "Guess number {}:".format( i ) )
		
		if guess == correct:
			print("Correct Guess")
			break 
		
		elif fermi(guess, correct):
			print("Fermi")
		elif pico(guess, correct):
			print("Pico")
		else:
			print("Baggle")
			
			
			
		
			
main()
