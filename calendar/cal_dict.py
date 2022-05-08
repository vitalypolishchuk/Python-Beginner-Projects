import datetime
import calendar

def cal_dict(month_inp,year_inp):
    month_input, year_input = month_inp, year_inp # type(month) == int; type(year) == int
    date = datetime.datetime(year_input,month_input,1)
    first_day, total_days = calendar.monthrange(date.year, date.month) # monthrange returns tuple(weekday of the first day, total number of days in the month)

    month_dict = {}
    if first_day != 6:
        num_of_days_from_pr_month = first_day + 1
        if date.month > 1:
            prev_month = date.replace(day = 1, month=month_input-1)
        else:
            prev_month = date.replace(day = 1, month=12, year=year_input-1)
        first_day_prev, total_days_prev = calendar.monthrange(prev_month.year, prev_month.month)
        for i in range((total_days_prev - num_of_days_from_pr_month) + 1, total_days_prev + 1):
            prev_month = prev_month.replace(day = i)
            day_name = calendar.day_name[prev_month.weekday()]
            month_dict[f'{i} '] = day_name
    
    for i in range(1, total_days + 1):
        date = date.replace(day = i)
        day_name = calendar.day_name[date.weekday()]
        month_dict[i] = day_name

    date = datetime.datetime(year_input,month_input,total_days)
    if date.weekday() != 6:
        num_of_days_from_next_month = 6 - date.weekday()
        if date.month < 12:
            next_month = date.replace(day = 1, month = month_input + 1)
        else:
            next_month = date.replace(day = 1, month=1, year=year_input + 1)
        first_day_next, total_days_next = calendar.monthrange(next_month.year, next_month.month)
        for i in range(1, num_of_days_from_next_month + 1):
            next_month = next_month.replace(day = i)
            day_name = calendar.day_name[next_month.weekday()]
            month_dict[f'{i}  '] = day_name
    return month_dict