import random
import time
from show_dice import show_dice

def time_roll_dice(rolls):
	if rolls >= 10:
		# Python time sleep function is used to add delay in the execution of a program
		time.sleep(0.3) # 0.3 == 300ms
	elif rolls >= 6 and rolls < 10:
		time.sleep(0.5)
	elif rolls >= 3 and rolls < 6:
		time.sleep(0.7)
	elif rolls >= 1 and rolls < 3:
		time.sleep(0.9)

def roll_dice():
	# generate how many times the dice will be rolled
	rolls = random.randint(15,20)
	# we keep track of previous and current roll so that current roll 
	# would not be the same as the previous one
	previous_roll = 0
	current_roll = 0
	while rolls > 1:
			# show_dice is a dictionary: where keys are the numbers from 1 to 6
			# and values are the visual represantations of the dice
			current_roll = show_dice[random.randint(1,6)]
			while current_roll == previous_roll:
				current_roll = show_dice[random.randint(1,6)]
			print(current_roll)
			time_roll_dice(rolls)
			rolls -= 1
			previous_roll = current_roll

if __name__=='__main__':
	roll_dice()