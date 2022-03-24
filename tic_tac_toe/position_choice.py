import check_for_available_space

def position_choice(board):

	while True:
		try:
			position = int(input('Please choose your next position (1-9): '))
		except ValueError:
			print('Please provide a number from 1-9')
		else:
			if position not in [1,2,3,4,5,6,7,8,9]:
				print('Please choose the number between 1-9')
			elif check_for_available_space.check_for_available_space(board,position) != True:
				print('This position is taken, choose another one!')
			else:
				return position
				
			
