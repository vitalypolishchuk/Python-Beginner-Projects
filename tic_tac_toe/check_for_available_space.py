def check_for_available_spaces(board):
	for place in board[1:]:
		if place == ' ':
			return True
	return False

def check_for_available_space(board,position):
	return board[position] == ' '