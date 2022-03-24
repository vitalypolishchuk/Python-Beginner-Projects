def check_for_victory(board,marker):
	if (board[1] == board[2] == board[3] == marker or # top row
	board[4] == board[5] == board[6] == marker or # middle row
	board[7] == board[8] == board[9] == marker or # bottom row
	board[1] == board[4] == board[7] == marker or # left column
	board[2] == board[5] == board[8] == marker or # middle column
	board[3] == board[6] == board[9] == marker or # right column
	board[1] == board[5] == board[9] == marker or # diagonal
	board[3] == board[5] == board[7] == marker): # diagonal
		return True