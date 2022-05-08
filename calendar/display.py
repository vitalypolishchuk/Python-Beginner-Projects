from cal_dict import cal_dict
from user_input import user_input
import datetime

def display():
    string_calendar = ''
    month, year = user_input()
    calendar_dictionary = cal_dict(month, year)
    date = datetime.datetime(year,month,1)

    weekSeparator = ('+----------' * 7) + '+\n'
    blankRow = ('|          ' * 7) + '|\n'

    string_calendar += ' ' * 34 + date.strftime('%B') + ' ' + date.strftime('%Y') + '\n'
    string_calendar += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'


    for i in range(0, len(calendar_dictionary) - 1, 7):
        for j in range(i, i+7):
            string_calendar += f'|{list(calendar_dictionary)[j]:<10}'
        string_calendar += '\n'
        string_calendar += blankRow * 3
        string_calendar += weekSeparator

    print(string_calendar)
    

if __name__=='__main__':
    print(display())