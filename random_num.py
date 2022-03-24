import random # generate a secret number

def generate_num():
	ask = 0

	while ask < 1:
		ask = int(input('Please enter a number from 1 to 100: '))

		if ask < 1:
			print('Cannot be less than 1!')
		else:
			return ask

def comp_guess(ask):
	num = 0
	low = 0
	high = 100
	index_count = 0

	while num != ask and low != high:
		num = random.randint(low,high)
		index_count += 1

		if num < ask:
			low = num+1
			print(f'Generating number {num}. Too Low! Setting boundaries from {low} to {high}')

		if num > ask:
			high = num-1
			print(f'Generating number {num}. Too High! Setting boundaries from {low} to {high}')

	print(f'Your number is {num}! I guessed at the {index_count} attempt!')

if __name__=='__main__':
	comp_guess(generate_num())
