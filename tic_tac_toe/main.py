import display_board # display the board
import marker_choice # returns a tuple ('X','O')
import place_marker # place marker 'X' or 'O' on the board
import position_choice # where to place marker on the board (position: 1-9)
import check_for_victory # returns True if either player wins
import check_for_available_space # contains 2 functions:
									# 1. check_for_available_spaces
									# returns True if there is no more available space on the board
									# 2. check_for_available_space
									# returns True if chosen position on the board is available												    	
def tic_tac_toe():
	while True:
		board = [' '] * 10
		player_marker1 = marker_choice.marker_choice()[0] # returns 'X'
		player_marker2 = marker_choice.marker_choice()[1] # returs 'O'
		ask = '#'
		game_on = False
		turn_player_1 = True

		while ask == '#':
			ask = input('Are you ready to play? (Y/N) ') # ask player to play the game

			if ask[0].lower() not in ['y','n']:
				print('I do not undertand! Try again!')
				ask = '#'
			elif ask[0].lower() == 'n':
				break
			elif ask[0].lower() == 'y':
				game_on = True

		while game_on == True: # player wants to play

			display_board.display_board(board) # display the board

			if turn_player_1 == True: # player 1 turn
				position = position_choice.position_choice(board) # returns position from 1 to 9
				place_marker.place_marker(board,position,player_marker1) # place marker on the board
				print('\n')
				display_board.display_board(board) # display the board

				if check_for_victory.check_for_victory(board,player_marker1) == True: # check if player one won the game
					print('Congradulations Player One! You have won the game!')
					break # stop the game if we have a winner

				if check_for_available_space.check_for_available_spaces(board) == False: # check for free space
					print('It is a tie!') # if there is no more available space, then it is a tie
					break # stop the game if we have a tie
				
				turn_player_2 = True # if no winners, and no tie, then switch to player 2

			if turn_player_2 == True: # player 2 turn
				position = position_choice.position_choice(board) # returns position from 1 to 9
				place_marker.place_marker(board,position,player_marker2) # place marker on the board

				if check_for_victory.check_for_victory(board,player_marker2) == True: # check if player two won the game
					print('Congradulations Player Two! You have won the game!')
					break # stop the game if we have a winner

				if check_for_available_space.check_for_available_spaces(board) == False: # check for free space
					print('It is a tie!') # if there is no more available space, then it is a tie
					break # stop the game if we have a tie

				turn_player_1 == True # if no winners, and no tie, then switch to player 1

		if game_on == False: # not ready to play
			break


if __name__=='__main__':
	tic_tac_toe()