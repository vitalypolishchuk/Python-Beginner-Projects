import re

def user_input():
    while True:
        try:
            print("Enter the year and the month for the calendar separating with ','. For example: 8, 2020")
            inp = input('> ')
            month, year = re.split(r',\s*',inp)
        except ValueError:
            print("Wrong Input! Make sure you provided 2 values separating them with ','")
        else:
            if int(month) > 12 or int(month) < 1 or int(year) < 1975:
                print('Please choose vaid month from 1 to 12, and year from 1975')
            else:
                return int(month), int(year)