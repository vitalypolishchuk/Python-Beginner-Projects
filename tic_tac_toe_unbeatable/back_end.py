import random
import math

class Back_End:

	def __init__(self):
		self.board = ['#','1','2','3','4','5','6','7','8','9']
		self.save_board = ['#','1','2','3','4','5','6','7','8','9']
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

	def player_input(self,letter):
		position = False
		while not position:
			try:
				position = int(input('Please choose your next move (1-9): '))
			except ValueError:
				print('Wrong Input! Please try again!')
			else:
				if position not in self.available_spaces():
					print('Current position is taken! Choose another one!')
					position = False
				else:
					self.board[position] = letter

	def computer_move(self,letter):
		if len(self.available_spaces()) > 7:
			square = random.choice(self.available_spaces())
			self.board[square] = letter
		else:
			# get the square based off the minimax algorithm
			square = self.minimax(letter,letter)['position']
			self.board[square] = letter

	def minimax(self,player,letter):
		max_player = letter # yourself
		other_player = 'O' if player == 'X' else 'X' # the other player

		# check if the previous move is a winner
		if self.current_winner == other_player:
			return {'position': None,'score': 1 * (len(self.available_spaces())+1) if other_player == max_player else -1 * (len(self.available_spaces())+1)}
		elif len(self.available_spaces()) == 0: # not empty squares
			return {'position': None,'score': 0}

		if player == max_player:
			best = {'position': None, 'score': -math.inf}  # each score should maximize
		else:
			best = {'position': None, 'score': math.inf}  # each score should minimize

		for possible_move in self.available_spaces():
			# MAKE MOVE
			self.board[possible_move] = player
			if self.winner_check(player) == True:
				self.current_winner = player

			sim_score = self.minimax(other_player,letter)

			# UNDO MOVE
			self.board[possible_move] = self.save_board[possible_move]
			self.current_winner = None
			sim_score['position'] = possible_move

			if player == max_player:
				if sim_score['score'] > best['score']:
					best = sim_score
			else:
				if sim_score['score'] < best['score']:
					best = sim_score

		return best

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