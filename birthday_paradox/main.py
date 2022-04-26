# In probability theory, the birthday problem asks for the probability that, 
# in a set of n randomly chosen people, at least two will share a birthday.
# In a room of just 23 people there’s a 50-50 chance of at least two people having the same birthday. 
# In a room of 75 there’s a 99.9% chance of at least two people matching.

import datetime
import random
from collections import Counter

def generate_birthdays(numOfBirthdays):
	# select a year for birthdays
	year = datetime.date(2001,1,1)
	birthdays = []
	for i in range(numOfBirthdays):
		# randomly generate days of birthdays from 0 to 364
		randomDay = datetime.timedelta(days=random.randint(0,364))
		birthday = year + randomDay
		birthdays.append(birthday)
	return birthdays

def check_same_day(numOfBirthdays):
	birthdays = generate_birthdays(numOfBirthdays)
	# A Counter is a dict subclass for counting hashable objects. 
	# It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values. 
	for key,value in Counter(birthdays).items():
		if value > 1:
			return True
	return False	

def simulation(numOfBirthdays=75,numOfSimulations=1000):
	num_of_birthdays_same_day_all_simulations = 0
	for i in range(numOfSimulations):
		if check_same_day(numOfBirthdays) == True: # at least two birthdays on the same day
			num_of_birthdays_same_day_all_simulations += 1
	percent = num_of_birthdays_same_day_all_simulations / numOfSimulations * 100
	return f'{numOfSimulations} simulations with {numOfBirthdays} birthdays showed {percent:.1f} percent chance of having 2+ birthday at the same day'

if __name__=='__main__':
	# simulation(number of birthdays,number of simulations)
	print(simulation())