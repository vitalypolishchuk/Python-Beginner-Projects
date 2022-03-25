import back_end
import time

def tic_tac_toe():
	while True:
		game_on = True
		back = back_end.Back_End()
		letter = 'X'
		player_or_computer = back.play_with()

		while game_on == True:
			if letter == 'X':
				back.print_board()

				if player_or_computer == 'Player' or player_or_computer == 'First':
					back.player_input(letter)
				elif player_or_computer == 'Second':
					print('Computer is choosing next move...')
					time.sleep(0.8)
					back.computer_move(letter)

				if back.winner_check(letter) == True:
					back.print_board()
					print('Player {} won the game!'.format(letter))
					break
				if len(back.available_spaces()) > 0:
					letter = 'O'
				else:
					back.print_board()
					print('It is a tie!')
					break

			if letter == 'O':
				back.print_board()

				if player_or_computer == 'Player' or player_or_computer == 'Second':
					back.player_input(letter) # input
				elif player_or_computer == 'First':
					print('Computer is choosing next move...')
					time.sleep(0.8)
					back.computer_move(letter)

				if back.winner_check(letter) == True:
					back.print_board()
					print('Player {} won the game!'.format(letter))
					break
				if len(back.available_spaces()) > 0:
					letter = 'X'
				else:
					back.print_board()
					break

		ask = input('Would you like to play again? (Y/N): ').lower()
		if ask[0] == 'y':
			game_on = True
		else:
			break

if __name__=='__main__':
	tic_tac_toe()