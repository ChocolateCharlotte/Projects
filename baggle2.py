import random

def generate():
	return str(random.randint(100, 1000))

def check(guess, correct):
	flag = False

	for i in range( 0, len(correct) ):

			if guess[i] == correct[i]:
				print(guess[i], "Fermi", end = " " )
				flag = True

			elif guess[i] in correct:
				print(guess[i], "Pico", end = " ")
				flag = True

			else:
				print(guess[i], "None", end = " ")

	return flag

def main():
	correct = generate()

	
	for i in range( 1, 10 ):
		guess = input( "\n Guess number {}:".format( i ) )
			
		if guess == correct:
			print("Correct Guess")
			break 

		elif check(guess, correct):
			pass
		else:
			print("Bagel")
			
main()
				
					

					