import random

class Back_End:

	def __init__(self):
		self.board = ['#','1','2','3','4','5','6','7','8','9']
		self.current_winner = None

	def print_board(self):
			print(' | '.join(self.board[1:4]) + '\n'
				+ ' | '.join(self.board[4:7]) + '\n'
				+ ' | '.join(self.board[7:10]))

	def available_spaces(self):
		return [index+1 for index,element in enumerate(self.board[1:]) if element not in ['X','O']]

	def play_with(self):
		comp_or_player = '#'
		first_or_second = '#'
		while comp_or_player == '#':
			comp_or_player = input('Would you like to play with another player or computer? (P/C): ')
			if comp_or_player[0].lower() == 'p':
				return 'Player'
			elif comp_or_player[0].lower() == 'c':
				while first_or_second == '#':
					first_or_second = input('Would you like to go first? (Y/N): ')
					if first_or_second[0].lower() == 'y':
						return 'First'
					elif first_or_second[0].lower() == 'n':
						return 'Second'
					else:
						print("Wrong Input! Please enter 'Y' to go first or 'N' to go second: ")
						first_or_second = '#'
			else:
				print("Wrong Input! Please enter 'P' for player or 'C' for computer")
				comp_or_player = '#'

	def player_input(self,game,letter):
		position = False
		while not position:
			try:
				position = int(input('Please choose your next move (1-9): '))
			except ValueError:
				print('Wrong Input! Please try again!')
			else:
				if position not in game.available_spaces():
					print('Current position is taken! Choose another one!')
					position = False
				else:
					self.board[position] = letter

	def computer_move(self,game,letter):
		if len(game.available_spaces) > 7:
			number = random.choice(game.available_spaces())
			self.board[number] = letter
		else:
			# get the square based off the minimax algorithm
			square = game.minimax(game,letter)
		return square

	def minimax(self,state,letter):
		max_player = letter # yourself
		other_player = 'O' if letter == 'X' else 'X' # the other player

		# check if the previous move is a winner
		if state.current_winner == max_player:
			return {'position': None,
					'score': 1 * (len(available_spaces)+1) if other_player == max_player else 
						-1 * (len(available_spaces)+1)
					}
		elif available_spaces == []: # not empty squares
			return {position: None, 'score': 0}

	def winner_check(self,letter):
		if (self.board[1:4] == [letter]*3 or
			self.board[4:7] == [letter]*3 or
			self.board[7:10] == [letter]*3 or
			self.board[1:8:3] == [letter]*3 or
			self.board[2:9:3] == [letter]*3 or
			self.board[3:10:3] == [letter]*3 or
			self.board[1:10:4] == [letter]*3 or
			self.board[3:8:2] == [letter]*3):
			return True