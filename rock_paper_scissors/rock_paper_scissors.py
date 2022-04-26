import random

def user_input():

	x = ''

	# user input
	while x == '':
		x = input('Enter: (R) for rock, (P) for paper, (S) for scissors: ')

		if x[0].lower() not in ['r','p','s']: 
			print('Wrong Input!')
			x = ''

		else:
			return x[0].lower()

def comp_gen(user_choice):
	rock_paper_scissors = ['r','p','s']
	comp_choice = random.choice(rock_paper_scissors)
	try_again = '#'

	print(f'User choice: {user_choice}, Computer choice: {comp_choice}')

	# user wins
	if user_choice == 'r' and comp_choice == 's':
		print('User: Rock | Computer: Scissors.  USER WINS!')

	elif user_choice == 'p' and comp_choice == 'r':
		print('User: Paper | Computer: Rock.  USER WINS!')

	elif user_choice == 's' and comp_choice == 'p':
		print('User: Scissors | Computer: Paper.  USER WINS!')

	# user loses
	if user_choice == 'r' and comp_choice == 'p':
		print('User: Rock | Computer: Paper.  COMPUTER WINS!')

	elif user_choice == 'p' and comp_choice == 's':
		print('User: Paper | Computer: Scissors.  COMPUTER WINS!')

	elif user_choice == 's' and comp_choice == 'r':
		print('User: Scissors | Computer: Rock.  COMPUTER WINS!')

	# tie
	elif user_choice == comp_choice:
		print("It is a Tie! Try again!")
		comp_gen(user_input())

	while try_again[0].lower() not in ['y','n']:
		try_again = input('Would you like to try again? (Y/N) ')

		if try_again[0].lower() not in ['y','n']:
			print('Wrong Input!')

		elif try_again[0].lower() == 'y':
			comp_gen(user_input())

if __name__=='__main__':
	comp_gen(user_input())